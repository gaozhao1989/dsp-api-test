#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: api-testing
@file: conftest.py
@time: 2019/1/6 上午11:26
'''

import pytest
import pymongo
from sshtunnel import SSHTunnelForwarder
from utils import Log


MONGO_HOST = '182.140.144.180'
MONGO_DB = 'sndo'
MONGO_USER = 'staff'
MONGO_PASS = 'zxt@56$%998*'
BIND_HOST = '127.0.0.1'
BIND_PORT = 27018
server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=(BIND_HOST, BIND_PORT)
)


@pytest.fixture(scope='session', autouse=True)
def base():
    log = Log.getlog('Base')
    log.info('set up test')
    yield
    log.info('tear down test')


@pytest.fixture(scope="session")
def mongo_connection():
    server.start()
    client = pymongo.MongoClient(BIND_HOST, server.local_bind_port)
    return client


@pytest.fixture(scope="session")
def mongodb(mongo_connection):
    yield mongo_connection
    server.stop()
