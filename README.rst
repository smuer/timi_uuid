timi_uuid
=======

timi_uuid is a lightweight Python library for sensibly dealing with UUID5 (or Time Random UUIDs as we like to sometimes call them). It allows you to create UUID str in a variety of different ways. Take a look at `the docs <https://github.com/lxl0928/timi_uuid/blob/master/README.md>`_ for the interface.


The Interface
-------------

.. automodule:: time_uuid

    .. autofunction:: get_id
    .. autofunction:: get_id_info

Recipes
-------

**Examples**

Timi-UUIDs single machine generate auto-incrementing uuid str..::

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


Who/What/When/Where
-------------------

Author: Timi long (`@timilong <http://blog.timilong.com>`_)

PyPi: `http://pypi.python.org/pypi/timi_uuid/ <http://pypi.python.org/pypi/timi-uuid/>`_

Docs: `http://packages.python.org/timi_uuid/ <https://github.com/lxl0928/timi_uuid/blob/master/README.md/>`_

License: MIT License

I am definitely open to contributions. Please feel free to submit your lock implementation.
