# coding: utf-8

import os
import uuid
import time
import random


def get_uuid():
    """ Get random uuid5 str
    return: <str 36 chars> 'bc7d5c01-88d1-45dd-aaed-86abd18f27ca'
    """
    cnt_time = time.time()
    cnt_pid = os.getpid()
    cnt_random_num = random.randrange(1, int(cnt_time), 1)  # 从1开始到当前timestamp, 随机取一个整数
    cnt_uuid4 = uuid.uuid4()

    random_str = str(cnt_time) + str(cnt_pid) + str(cnt_random_num) + str(uuid.uuid4())
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, random_str))


def get_32uuid():
    """ Get random uuid5 str with out '-'
    return: <str 32 chars> 'bc7d5c0188d145ddaaed86abd18f27ca'
    """
    _str = get_uuid()
    return "".join(_str.split("-"))


def get_36uuid():
    """ Get random uuid5 str
    return: <str 36 chars> 'bc7d5c01-88d1-45dd-aaed-86abd18f27ca'
    """
    _str = get_uuid()
    return _str


def get_uuid_obj():
    """ Get random uuid5 str
    return: <UUID object> UUID('6ab14380-7074-4e12-9b39-efec76fcddf7')
    """
    cnt_time = time.time()
    cnt_pid = os.getpid()
    cnt_random_num = random.randrange(1, int(cnt_time), 1)  # 从1开始到当前timestamp, 随机取一个整数
    cnt_uuid4 = uuid.uuid4()

    random_str = str(cnt_time) + str(cnt_pid) + str(cnt_random_num) + str(uuid.uuid4())
    return uuid.uuid5(uuid.NAMESPACE_DNS, random_str)

