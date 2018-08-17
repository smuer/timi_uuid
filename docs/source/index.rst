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
    'bc7d5c01-88d1-45dd-aaed-86abd18f27ca'

    >>> timi_uuid.get_uuid_obj()
    UUID('bc7d5c01-88d1-45dd-aaed-86abd18f27ca')

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

