timi_uuid
=======

timi_uuid is a lightweight Python library for sensibly dealing with UUID5 (or Time Random UUIDs as we like to sometimes call them). It allows you to create UUID str in a variety of different ways. Take a look at `the docs <https://github.com/lxl0928/timi_uuid/blob/master/README.md>`_ for the interface.


The Interface
-------------

.. automodule:: time_uuid

    .. autofunction:: get_uuid
    .. autofunction:: get_uuid_obj
    .. autofunction:: get_32uuid
    .. autofunction:: get_36uuid

Recipes
-------

**Examples**

Timi-UUIDs can get a random uuid5 str.::

    >>> import timi_uuid

    >>> timi_uuid.get_uuid()
    'af8d8fe4-35bb-5ac1-b63f-6f8e346ba2c8'

    >>> timi_uuid.get_36uuid()
    'ed35b50b-e149-5cd4-91d8-dadffce5198b'

    >>> timi_uuid.get_32uuid()
    '49d01ceffecb5844a9b11c3bf654f016'

    >>> timi_uuid.get_uuid_obj()
    UUID('fe556b46-3c17-5969-9740-d8f9d9e3e41c')


Who/What/When/Where
-------------------

Author: Timi long (`@timilong <http://blog.timilong.com>`_)

PyPi: `http://pypi.python.org/pypi/timi-uuid/ <http://pypi.python.org/pypi/timi-uuid/>`_

Docs: `http://packages.python.org/timi-uuid/ <https://github.com/lxl0928/timi_uuid/blob/master/README.md/>`_

License: MIT License

I am definitely open to contributions. Please feel free to submit your lock implementation.
