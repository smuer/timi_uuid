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
    
    .. autofunction:: get_uuid
    .. autofunction:: get_uuid_obj

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
>>>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

