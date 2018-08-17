# coding: utf-8

import os
import uuid
import time
import random


def get_uuid():
    """ Get random uuid5 str
    return: 'bc7d5c01-88d1-45dd-aaed-86abd18f27ca'
    """
    cnt_time = time.time()
    cnt_pid = os.getpid()
    cnt_random_num = random.randrange(1, int(cnt_time), 1)  # 从1开始到当前timestamp, 随机取一个整数
    cnt_uuid4 = uuid.uuid4()

    random_str = str(cnt_time) + str(cnt_pid) + str(cnt_random_num) + str(uuid.uuid4())
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, random_str))


def get_uuid_obj():
    """ Get random uuid5 str
    return: 'bc7d5c01-88d1-45dd-aaed-86abd18f27ca'
    """
    cnt_time = time.time()
    cnt_pid = os.getpid()
    cnt_random_num = random.randrange(1, int(cnt_time), 1)  # 从1开始到当前timestamp, 随机取一个整数
    cnt_uuid4 = uuid.uuid4()

    random_str = str(cnt_time) + str(cnt_pid) + str(cnt_random_num) + str(uuid.uuid4())
    return uuid.uuid5(uuid.NAMESPACE_DNS, random_str)

