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
import string
import logging
import os
import json
import configparser
import random
import datetime
import time
from functools import wraps
import shutil
import pymongo
import requests
from sshtunnel import SSHTunnelForwarder
from PIL import Image, ImageDraw


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
            logging.info('request url:{}'.format(url))
            # json args clean
            if 'json' in kwargs:
                kwargs['json'] = {k: v for k,
                              v in kwargs['json'].items() if v is not ''}
            logging.info('request args:{}'.format(kwargs))
            response = requests.request(method, url, **kwargs)
        except requests.exceptions.RequestException as e:
            logging.exception(str(e))
            assert False, 'request fail'
        try:
            response_json = json.loads(response.content)
            logging.info('response json:{}'.format(response_json))
            return response_json
        except json.decoder.JSONDecodeError as e:
            logging.exception(e)
            assert False, 'decode fail'


class ConfigParser:

    def __init__(self):
        self.config = configparser.ConfigParser()
        print(os.path.join(os.getcwd(), 'config.ini'))
        self.config.read(os.path.join(os.getcwd(), 'config.ini'))

    def get_admin_addr(self):
        return self.config['admin']['admin_addr']

    def get_tsa_addr(self):
        return self.config['tsa']['tsa_addr']

    def get_wx_addr(self):
        return self.config['wx']['wx_addr']


class DataGenerator:

    @staticmethod
    def randint():
        return random.randint(10000, 99999)

    @staticmethod
    def getdate():
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    @staticmethod
    def randchr(char_len=16):
        return ''.join(random.sample(string.ascii_letters + string.digits, char_len))
    
    @staticmethod
    def drawimage():
        img = Image.new('RGB',(400,400),color=tuple([random.randint(0,256) for x in range(3)]))
        draw = ImageDraw.Draw(img)
        draw.text((20,20),'test image',fill=(255,255,0))
        pp = PathParser()
        path = pp.path_join(pp.current_path(),'misc','image.png')
        img.save(path)
        return path

class AssertUtils:

    def assertgroup(self,groupa,groupb,lis2assert):
        for item in lis2assert:
            if item in groupa and item in groupb:
                assert groupa[item] == groupb[item],'{}: "{}" and "{}" not equal with _id {}'.format(item,groupa[item],groupb[item],groupa['_id'])
    
    def assertnotfound(self,key,value):
        assert key,'{} {} not found'.format(key, value)