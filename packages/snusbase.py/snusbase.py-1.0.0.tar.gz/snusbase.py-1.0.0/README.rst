snusbase.py
================

   an un-official async wrapper for the Snusbase API

Features
========

- none. just easier to use instead of ugly non-async examples

Install
=======

.. code:: sh

   # Linux/macOS
   python3 -m pip install -U snusbase.py

   # Windows
   py -3 -m pip install -U snusbase.py

To install the development version, do the following:

.. code:: sh

    $ pip install -U git+https://github.com/obstructive/snusbase.py

Optional Packages
-----------------

-  `aiodns <https://pypi.org/project/aiodns>`__,
   `brotlipy <https://pypi.org/project/brotlipy>`__,
   `cchardet <https://pypi.org/project/cchardet>`__ (for aiohttp
   speedup)

Quick Example
=============

.. code:: py

   from snusbase.py import SnusbaseApi
   from asyncio import get_event_loop

   client = SnusbaseApi("token")


   async def main():
       result = await client.search_by_username("example")
       print(result)


   loop = get_event_loop()
   loop.run_until_complete(main())

Links
=====
-  `Issues <https://github.com/obstructive/snusbase.py>`__
-  `Snusbase API <https://docs.snusbase.com/>`__
