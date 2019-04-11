#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: api-testing
@file: utils.py
@time: 2019/1/6 上午11:26
'''

import logging
import os
import json
from functools import wraps
import shutil
import pymongo
import requests
from sshtunnel import SSHTunnelForwarder
from PIL import Image, ImageDraw, ImageFont


class Log(object):
    def __init__(self, level=logging.DEBUG):
        self.level = level
        logging.basicConfig(level=self.level)

    @staticmethod
    def getlog(name=None):
        return logging.getLogger(name)
    
    def logtestcase():
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                logging.info('call test: {}'.format(func.__name__))
                logging.info('case: {}'.format(kwargs['test_title']))
                return func(*args, **kwargs)
            return wrapper
        return decorator

class PathParser:

    def __init__(self, workspace_name='api-testing'):
        self.workspace_name = workspace_name

    @staticmethod
    def current_path():
        return os.getcwd()

    def get_workspace_root_path(self):
        present_work_dir = self.current_path()
        while True:
            if present_work_dir.endswith(self.workspace_name):
                break
            else:
                present_work_dir = os.path.dirname(present_work_dir)
        return present_work_dir

    @staticmethod
    def get_abs_path(path):
        return os.path.abspath(path)

    @staticmethod
    def path_join(path, *paths):
        return os.path.join(path, *paths)

    @staticmethod
    def make_dir(path):
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)

    @staticmethod
    def remove_dirs(*paths):
        for path in paths:
            if os.path.exists(path):
                shutil.rmtree(path)


class Requests:

    def req(self, method, url, **kwargs):
        try:
            logging.info('request args:{}'.format(kwargs))
            response = requests.request(method, url, **kwargs)
        except requests.exceptions.RequestException as e:
            logging.exception(e)
            assert False, 'request fail'
        try:
            response_json = json.loads(response.content)
            logging.info('response json:{}'.format(response_json))
            return response_json
        except json.decoder.JSONDecodeError as e:
            logging.exception(e)
            assert False, 'decode fail'