# Tor Circuits Manager

This package provides a set of classes to construct circuit manager
that matches your taste.

Use it in conjunction with [mintc](https://github.com/amateur80lvl/mintc).

How to:

```python

    import asyncio
    from mintc import TorController
    from tcman import *

    class MyCircuitsManager(
        CircuitsManagerBase,
        RoundRobinManager,
        PromiscuousPathBuilder,
        Logger
    ):
        pass

    async def main():
        async with TorController('127.0.0.1:9051') as tc:
            await tc.authenticate('password')
            async with MyCircuitsManager(tc, num_hops=2, max_circuits=500) as tcm:
                await tcm.run()

    asyncio.run(main())
```

Mind exceptions and re-run when shit happens.

