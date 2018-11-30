# coding: utf-8

"""
Description:
    single machine generate auto-incrementing uuid str.

Warning:
    >>> a = "0xffffffffffff"

    >>> b = int(a, 16)
    >>> b
    281474976710655

    >>> c = b / 10.0 ** 5
    >>> c
    2814749767.10655

    >>> from datetime import datetime
    >>> datetime.fromtimestamp(c).strftime("%Y-%m-%d %H:%M:%S.%f")
    '2059-03-13 10:56:07.106550'

    >>>  # 目前12位16进制的字符存储时间戳，将在上面这个时间后12位16进制字符将无法存储当前时间戳。


Examples:
    >>> from timi_uuid import timi_uuid

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

"""


from .main_uuid import TimiUUID

from .__version__ import __version__, __title__, __description__, __url__, __author_email__

timi_uuid = TimiUUID()
