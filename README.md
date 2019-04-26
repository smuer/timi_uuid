# timi_uuid
Single machine generate auto-incrementing uuid str.

# install 
```
pip install timi-uuid
```

# examples

```
    >>> from timi_uuid import timi_uuid

    >>> 

    >>> timi_uuid.get_id()
    '8c288f25-d690-4600-f911-e6011175d101'

    >>> timi_uuid.get_id_info(cnt_id="8c288f25-d690-4600-f911-e6011175d101")
    {
        'timestamp': 1541058282.02128,
        'seq': 1,
        'pid': 5982,
        'mac': '46:00:f9:11:e6:01',
        'msg': 'Success.',
        'datetime': '2018-11-01 15:44:42.021280'
    }

    >>> timi_uuid.hex
    '8c8cca7e5fab8c859039ab0128640101'

    >>> timi_uuid.hex_to_id(hex_id="8c8cca7e5fab8c859039ab0128640101")
    '8c8cca7e-5fab-8c85-9039-ab0128640101'

```
