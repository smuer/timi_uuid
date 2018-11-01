.. timi-uuid documentation master file, created by
   sphinx-quickstart on Sun Nov 18 18:03:47 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to timi-uuid's documentation!
=====================================

timi_uuid is a lightweight Python library for sensibly dealing with random UUID5 str.

The Interface
-------------

.. automodule:: time_uuid

    .. autofunction:: get_id
    .. autofunction:: get_id_info

Recipes
-------

**Examples**

Single machine generate auto-incrementing uuid str.::

    >>> from timie_uuid import TimiUUID

    >>> obj = TimiUUID()

    >>> obj.get_id()
    '8c288f25-d690-4600-f911-e6011175d101'

    >>> timi_uuid.get_id_info(cnt_id="8c288f25-d690-4600-f911-e6011175d101")
    # {
    #     'timestamp': 1541058282.02128,
    #     'seq': 1,
    #     'pid': 5982,
    #     'mac': '46:00:f9:11:e6:01',
    #     'msg': 'Success.',
    #     'datetime': '2018-11-01 15:44:42.021280'
    # }


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

