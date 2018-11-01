# -*- coding: utf-8 -*-

#   __
#  /__)  _  _     _   _ _/   _
# / (   (- (/ (/ (- _)  /  _)
#          /

"""
Description: single machine generate auto-incrementing uuid str.

Examples:
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

"""


from .main_uuid import TimiUUID

from .__version__ import __version__, __title__, __description__, __url__, __author_email__
