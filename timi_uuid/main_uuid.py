# coding: utf-8

import os
import time
import uuid
from datetime import datetime


class TimiUUID(object):
    """ 单机实现自增UUID发号器的功能，能够集成timestamp, mac_addr, pid, seq_number等信息。使用方法如下:

    from timi_uuid import TimiUUID

    new_obj = TimiUUID()

    timi_uuid = new_obj.get_id()
    # '8c288f25-d690-4600-f911-e6011175d101'

    timi_uuid_info = new_obj.get_id_info('8c288f25-d690-4600-f911-e6011175d101')
    # {
    #     'timestamp': 1541058282.02128,
    #     'seq': 1,
    #     'pid': 5982,
    #     'mac': '46:00:f9:11:e6:01',
    #     'msg': 'Success.',
    #     'datetime': '2018-11-01 15:44:42.021280'
    # }

    """
    def __init__(self, _id=None):
        self.counter = 0
        self._id = _id
        self.unix_time = None
        self.mac_addr = None
        self.pid_hex = None
        self.sequence_num = None

    def __get_unix_now(self):
        """  Get time.time() hex str.
        example:
            cnt_timestamp: 1541056667.18915
            hex(154105666718915): '0x8c288585ccc3'

            return: <string length 12> '8c288585ccc3'
        """
        ms_now = int(time.time() * 10 ** 5)
        return hex(ms_now)[2:]

    def __get_mac_address(self):
        """ Get mac hex str.
        example:
            cnt_mac_address: '46:00:f9:11:e6:01'

            return: <string length 12> '4600f911e601'
        """
        str_hex_mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return str_hex_mac

    def __get_pid(self):
        """ Get pid hex str.
        example:
            cnt_pid+65535: 5613 + 65535 = 71148
            hex(71148): '0x115ec'

            return: <string length 5> '115ec'
        :return:
        """
        str_pid = os.getpid() + 65535
        str_hex_pid = hex(str_pid)[2:]
        return str_hex_pid

    def __get_sequence_number(self):
        """ Get sequence number hex str.
        example:
            counter: <int 1 ~ 1000> 1
            hex(counter+256): '0x101'

            return: <string length 3> '101'
        """
        if self.counter > 999:
            self.counter = 0
        else:
            self.counter += 1

        str_sequence_num = self.counter + 256
        str_hex_sequence_num = hex(str_sequence_num)[2:]
        return str_hex_sequence_num

    @staticmethod
    def __hex2int(_hex_str):
        """ hex str to int.

        :param _hex_str: '101'
        :return: <int> 257
        """
        return int("0x"+_hex_str, 16)

    def get_id(self):
        """ Get a TimiUUID str.

        :return: <string length 36> "8c288a6f-c52e-4600-f911-e60111658101"
        """
        self.unix_time = self.__get_unix_now()
        self.mac_addr = self.__get_mac_address()
        self.pid_hex = self.__get_pid()
        self.sequence_num = self.__get_sequence_number()

        # uuid format: 8 + 4 + 4 + 4 + 12
        _tmp_list = [self.unix_time[:8],
                    self.unix_time[8:],
                    self.mac_addr[:4],
                    self.mac_addr[4:8],
                    self.mac_addr[8:] + self.pid_hex + self.sequence_num]

        return "-".join(_tmp_list)

    def get_id_info(self, cnt_id=None):
        """ Get TimiUUID info.

        :param _id: <str> "8c288a6f-c52e-4600-f911-e60111658101"
        :return: <dict>
            {
                'timestamp': 1541057491.61262,
                'seq': 1,
                'pid': 5721,
                'mac': '46:00:f9:11:e6:01',
                'msg': 'Success.',
                'datetime': '2018-11-01 15:31:31.612620'
            }
        """
        self._id = cnt_id
        _res_info = dict(timestamp="", seq="", pid="", mac="", msg="", datetime="")
        _res_info['msg'] = "The _id format like: '8c26eb17-d7a0-4600-f911-e60128326101'"
        if not self._id:
            return _res_info

        if not isinstance(self._id, str):
            return _res_info

        if len(self._id) != 36:
            return _res_info

        tmp_list = self._id.split("-")
        if len(tmp_list) != 5:
            return _res_info

        if (len(tmp_list[0]) != 8 or len(tmp_list[1]) != 4 or len(tmp_list[2]) != 4
                or len(tmp_list[3]) != 4 or len(tmp_list[4]) != 12):
            return _res_info

        self.unix_time = tmp_list[0] + tmp_list[1]

        self.mac_addr = tmp_list[2] + tmp_list[3] + tmp_list[4][:4]

        self.pid_hex = tmp_list[4][4:9]

        self.sequence_num = tmp_list[4][9:]

        _timestamp = self.__hex2int(_hex_str=self.unix_time) / 10.0 ** 5
        _res_info['timestamp'] = _timestamp
        _res_info['datetime'] = datetime.fromtimestamp(_timestamp).strftime("%Y-%m-%d %H:%M:%S.%f")
        _res_info['mac'] = ":".join([self.mac_addr[e:e+2] for e in range(0, 11, 2)])
        _res_info['seq'] = self.__hex2int(_hex_str=self.sequence_num) - 256
        _res_info['pid'] = self.__hex2int(_hex_str=self.pid_hex) - 65535
        _res_info['msg'] = 'Success.'

        return _res_info
