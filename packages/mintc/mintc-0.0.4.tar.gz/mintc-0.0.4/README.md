# Minimalistic Tor Controller

Minimalistic asyncio-based Tor controller.

How to use:

```python

    from mintc import TorController

    tc = TorController('127.0.0.1:9051')
    try:
        await tc.start()
        await tc.authenticate('password')
        async for circuit in tc.get_circuits():
            print(circuit)
    finally:
        await tc.stop()
```

Or:

```python
    async with TorController('127.0.0.1:9051') as tc:
        await tc.authenticate('password')
        async for circuit in tc.get_circuits():
            print(circuit)
```

The format of control port argument passed to the constructor
is identical to `ControlPort` from `torrc`.

Only small subset of commands is implemented so far.

This controller neither does nor will implement auto reconnect.
It's the user's responsibility to catch any exceptions
and re-run the entire `async with TorController...` code block
or restart the controller with `tc.restart()` and start over again
from `tc.authenticate()`.

All response parsing is very minimalistic. E.g. date/time strings are not parsed.
