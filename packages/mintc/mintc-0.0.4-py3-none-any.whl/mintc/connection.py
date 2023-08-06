'''
Minimalistic asyncio-based Tor Controller

This module implements the basic communication with Tor control port.

:copyright: Copyright 2023 amateur80lvl
:license: LGPLv3, see LICENSE for details
'''

import asyncio
from dataclasses import dataclass
import re


@dataclass
class Request:
    '''
    Request object for use in queue.
    '''
    command: bytes
    completion: asyncio.Event
    reply: list | None = None


class TorConnection:
    '''
    This class implements the basic communication with Tor control port
    in terms of messages, replies, and asynchronous events.

    For synchronous communication with Tor controller use `send_request` method.

    To handle asynchronous events one should either override `handle_event`
    method in a subclass or assign custom handler using `set_handler` method.

    If this class is used outside `with` statement context,
    calling `start` and `stop` methods is a must:

        tc = TorConnection('9051')
        try:
            await tc.start()
            # do the job here
        finally:
            await tc.stop()

    If used along with `with` statement, 'start` and `stop` methods
    are called automagically:

        async with TorConnection('9051') as tc:
            # do the job here
            pass
    '''

    _default_port = 9051

    def __init__(self, control_port):
        self.control_port = control_port.strip()
        self._receiver_task = None
        self._event_task = None
        self._custom_event_handler = None
        self._reader, self._writer = None, None

        # a lock to serialze request transmission
        self._sender_lock = asyncio.Lock()

        # create queues
        self._request_queue = asyncio.Queue()
        self._event_queue = asyncio.Queue()


    async def start(self):
        '''
        Open connection and start background tasks.
        '''
        # connect to Tor control port
        if self.control_port.startswith('unix:'):
            socket_path = self.control_port[len('unix:'):]
            self._reader, self._writer = await asyncio.open_unix_connection(socket_path)
        else:
            host, port = self._parse_control_port()
            self._reader, self._writer = await asyncio.open_connection(host, port)

        # start background tasks
        self._receiver_task = asyncio.create_task(self._receiver())
        self._event_task = asyncio.create_task(self._process_events())


    def _parse_control_port(self):
        '''
        Parse self.control_port for tcp connection.
        '''
        # port only?
        if self.control_port.isdigit():
            return 'localhost', int(self.control_port)

        # IPv6 with port?
        matchobj = re.match(r'\[(.*)\]:(\d+)', self.control_port)
        if matchobj:
            addr, port = matchobj.groups()
            return addr, int(port)

        # IPv4/hostname without port?
        if ':' not in self.control_port:
            return self.control_port, self._default_port

        # IPv4/hostname with port?
        addr, port = self.control_port.rsplit(':', 1)
        if ':' in addr:
            # looks like IPv6 without port
            return self.control_port, self._default_port

        if not port.isdigit():
            # unknown mess, let getaddrinfo deal with it
            return self.control_port, self._default_port

        # looks like IPv4/hostname with port
        return addr, int(port)


    async def stop(self):
        '''
        Close connection and stop background tasks.
        This is an universal idempotent method used to force all tasks
        to stop by any task whichever detects stop condition first.
        '''
        # Close connection. This forces `self._reader.read` function
        # to return empty data, so the receiver task can gracefully
        # stop if it waits for data.
        if self._writer is not None:
            writer = self._writer
            self._writer = None
            writer.close()
            await writer.wait_closed()

        self._clear_request_queue()

        # put None values to queues to stop background tasks
        self._request_queue.put_nowait(None)
        self._event_queue.put_nowait(None)

        # wait for background tasks to complete
        current_task = asyncio.current_task()
        if self._receiver_task and self._receiver_task is not current_task:
            task = self._receiver_task
            self._receiver_task = None
            await task

        if self._event_task and self._event_task is not current_task:
            task = self._event_task
            self._event_task = None
            await task

        # finally clear queues
        self._clear_request_queue()
        while not self._event_queue.empty():
            self._event_queue.get_nowait()
            self._event_queue.task_done()


    def _clear_request_queue(self):
        '''
        Remove requests from queue and set completion events.
        '''
        while not self._request_queue.empty():
            request = self._request_queue.get_nowait()
            self._request_queue.task_done()
            if request is not None:
                request.completion.set()


    async def restart(self):
        '''
        Restart the controller.
        '''
        self.stop()
        self.start()

    async def __aenter__(self):
        '''
        Enter runtime context.
        '''
        await self.start()
        return self


    async def __aexit__(self, exc_type, exc_value, traceback):
        '''
        Exit runtime context.
        '''
        await self.stop()


    async def _receiver(self):
        '''
        Background task.
        Receive replies from Tor and assign them to pending requests.
        '''
        try:
            while True:
                try:
                    # receive reply
                    reply = await self._recv_reply()

                    if reply[0].startswith('6'):
                        # it's an event
                        self._event_queue.put_nowait(reply)
                        continue

                    # get pending request from queue,
                    request = await self._request_queue.get()
                    self._request_queue.task_done()
                    if request is None:
                        # stop signal
                        return

                    # set reply and signalize completion
                    request.reply = reply
                    request.completion.set()
                except ConnectionResetError:
                    # connection closed, force stop
                    await self.stop()
                    return
        except:
            # force stop in any unclear case
            await self.stop()
            raise


    async def _recv_reply(self):
        '''
        Receive reply lines.
        '''
        line = await self._read_line()
        status_code = line[:3]
        reply = []
        while True:
            reply.append(line)
            if line[3] == ' ':
                break
            if line[3] == '+':
                reply.extend(await self._read_multiline())

            line = await self._read_line()
            if line[:3] != status_code:
                raise Exception(f'Status code mismatch: {status_code} != {line}')

        return reply


    async def _read_line(self):
        '''
        Read line from socket.
        Raise ConnectionResetError exception if socket is closed.
        '''
        line = await self._reader.readline()
        if line == b'':
            # connection closed
            raise ConnectionResetError()
        # process line
        line = line.rstrip(b'\n').rstrip(b'\r').decode('ascii')
        self.logger.debug('<<< %s', line)
        return line


    async def _read_multiline(self):
        '''
        Read multiple lines till the line containing period only.
        '''
        multiline = []
        while True:
            line = await self._read_line()
            multiline.append(line)
            if line == '.':
                return multiline


    async def send_request(self, command):
        '''
        Send command and return reply.
        Returns None if controller is stopped.
        '''
        if self._writer is None:
            raise ConnectionResetError()

        # prepare request data to send
        if not isinstance(command, bytes):
            command = command.encode('ascii')

        self.logger.debug('>>> %s', command)

        command += b'\r\n'

        request = Request(
            command,
            asyncio.Event()
        )

        # Send request data.
        # Basically, this method can be called simultaneously
        # from multiple tasks, and this will result in pipelining.
        # Although Tor controller specification tells nothing
        # about pipelining, this seem to work.
        # And such a case is not as rare as it may seem.
        # If an event needs some interaction with Tor, this method
        # will be called from event handler task.
        async with self._sender_lock:
            try:
                self._writer.write(request.command)
                await self._writer.drain()
            except:
                # force stop in any unclear case
                await self.stop()
                raise

        # put request to the queue
        self._request_queue.put_nowait(request)

        # wait for response
        await request.completion.wait()
        # if receiver task is interrupted, then the event is set
        # but reply is left None
        if request.reply is None:
            raise ConnectionResetError()
        else:
            return request.reply


    async def _process_events(self):
        '''
        Background task to process queued events.
        '''
        while True:
            event = await self._event_queue.get()
            self._event_queue.task_done()
            if event is None:
                # stop signal
                return
            # handle event
            try:
                await self.handle_event(event)
            except:
                # force stop in any unclear case
                await self.stop()
                raise


    async def handle_event(self, event):
        '''
        Override and customize this method in a subclass as necessary
        or use set_handler to set custom handler.
        '''
        if self._custom_event_handler is None:
            self.logger.error('Unhandled event:\n %s', '\n'.join(event))
        else:
            await self._custom_event_handler(event)


    def set_event_handler(self, handler):
        '''
        Set event handler to be called from handle_event, as an alternative to subclassing.
        '''
        self._custom_event_handler = handler
