import configparser
import datetime
import json
import logging
import os
import random
import string
import time

from functools import wraps

import pymongo
import requests
import shutil

from sshtunnel import SSHTunnelForwarder
from PIL import Image, ImageDraw


class Log(object):
    """Log utils for pytest.

    Func getlog used for get the specfic logger.
    Func logtestcase used as decorator for test cases.

    Attributes:
        level: Set the root logger level to the specified level. Default set to 'DEBUG'.
    """

    def __init__(self, level=logging.DEBUG):
        """Inits Log with logging level."""
        self.level = level
        logging.basicConfig(level=self.level)

    @staticmethod
    def getlog(name=None):
        """Get the specfic logger.

        Get the specfic logger with 'name'.

        Args:
            name: the specfic logger name. Default 'name' set with None.

        Returns:
            The specifc name logger.

        Example:
            log = Log.getlog('TsaTest')
        """
        return logging.getLogger(name)

    def logtestcase():
        """The decorator func for set log content of test cases.

        The decorator only use for test cases. By default, this decorator will
        auto generator 'INFO'(log level) log for test case. The log information
        contains: 1.the test case func name; 2. the title of the test case.

        Args:
            func: Test case func.
            Wrapper:
                *args: The non-keyworded argument passed by func.
                **kwargs: The keyword arguments passed by func.

        Returns:
            The decorator for func.

        Example:
            @Log.logtestcase()
            def test_case_example():
                ...
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # log the func name
                logging.info('call test: {}'.format(func.__name__))
                # log the test case title, must have a variable name as
                # 'test_title'
                logging.info('case: {}'.format(kwargs['test_title']))
                return func(*args, **kwargs)
            return wrapper
        return decorator


class PathParser:
    """Path utils for project.

    Func current_path used for get the current work path.
    Func get_abs_path used for get the absolute path for specfic path.
    Func path_join used for join two or more pathname components.
    Func make_dir used for make new directory.
    Func remove_dirs used for remove the specifc directories.
    """

    @staticmethod
    def current_path():
        """Get the current path.

        Returns:
            The path for current directory. example:
            '/Users/testuser/workspace/dsp-api-test'

        Example:
            PathParser.current_path()
        """
        return os.getcwd()

    @staticmethod
    def get_abs_path(path):
        """Get the specfic absolute path.

        Returns:
            The absolute path. example:
            '/Users/testuser/workspace/dsp-api-test'

        Args:
            path: The path for the specfic file or direcotry.

        Example:
            PathParser.get_abs_path(path)
        """
        return os.path.abspath(path)

    @staticmethod
    def path_join(path, *paths):
        """Join two or more pathname components, inserting '/' as needed.
        If any component is an absolute path, all previous path components
        will be discarded.  An empty last part will result in a path that
        ends with a separator.

        Returns:
            The full path after joined. example:
            '/Users/testuser/workspace/dsp-api-test'

        Args:
            path: The root path need to merge.
            *paths: one or more pathname to be joined.

        Example:
            PathParser.path_join('/Users/testuser/workspace', 'dsp-api-test')
        """
        return os.path.join(path, *paths)

    @staticmethod
    def make_dir(path):
        """Create new directory with the specfic path. If directory alread
        exists nothing will do nothing, otherwise will create new.

        Args:
            path: The directory need to be created.

        Example:
            PathParser.make_dir('/Users/testuser/workspace/dsp-api-test')
        """
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)

    @staticmethod
    def remove_dirs(*paths):
        """Delete directory with the specfic path if it exists.

        Args:
            *paths: The directories need to be deleted.

        Example:
            PathParser.remove_dirs('/Users/testuser/workspace/dsp-api-test')
        """
        for path in paths:
            if os.path.exists(path):
                shutil.rmtree(path)


class Requests:
    """Requests utils for http/https request action handle in test cases.

    Func req used for send http/https request.
    """

    def req(self, method, url, **kwargs):
        """Send the http/https request with library 'requests' and auto decode
        the response content in json format.

        Args:
            method: The request method.
            url: The request url.
            **kwargs: Support to other 'requests' keyword arguments.
                Argument list: params, data, json, headers, cookies, files,
                auth, timeout, allow_redirects, proxies, verify, stream, cert

        Returns:
            The json format response content will be returned if request progress
            success.

        Example:
            Requests.req('POST','http://www.example.com/the/url/need/to/send',json={'var1':'value1'})
        """
        try:
            logging.info('request url:{}'.format(url))
            # json args clean, remove the empty variables
            if 'json' in kwargs:
                kwargs['json'] = {k: v for k,
                                  v in kwargs['json'].items() if v is not ''}
            logging.info('request args:{}'.format(kwargs))
            response = requests.request(method, url, **kwargs)
        except requests.exceptions.RequestException as e:
            logging.exception(str(e))
            # fail the test cases if request fail
            assert False, 'request fail'
        try:
            # decode the response content and return
            response_json = json.loads(response.content)
            logging.info('response json:{}'.format(response_json))
            return response_json
        except json.decoder.JSONDecodeError as e:
            logging.exception(e)
            # fail the test cases if response content not as json format
            assert False, 'decode fail'


class ConfigParser:
    """ConfigParser utils get the project config from config.ini file

    Func get_admin_addr used for get the admin address.
    Func get_tsa_addr used for get the tsa address.
    Func get_wx_addr used for get the wx address.
    """

    def __init__(self):
        """Inits config file path and read it."""
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.getcwd(), 'config.ini'))

    def get_admin_addr(self):
        """Get the admin address."""
        return self.config['admin']['admin_addr']

    def get_tsa_addr(self):
        """Get the tsa address."""
        return self.config['tsa']['tsa_addr']

    def get_wx_addr(self):
        """Get the wx address."""
        return self.config['wx']['wx_addr']


class DataGenerator:
    """DataGenerator utils to generate the fake or random data
    for test case parameters.

    Func randint used for generate 5 digits.
    Func getdate used for get the current time and format as '%Y%m%d%H%M%S'.
    Func randchr used for generate mixed random characters by
    ascii letters and digits.
    Func drawimage used for generate new image.
    """

    @staticmethod
    def randint():
        """Generate 5 digits from 10000 to 99999.

        Returns:
            Return the generated digits.

        Example:
            DataGenerator.randint()
            # output: 56270
        """
        return random.randint(10000, 99999)

    @staticmethod
    def getdate():
        """Get the current time.

        Returns:
            Return the time as string format.

        Example:
            DataGenerator.getdate()
            # output: 20190421214855
        """
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    @staticmethod
    def randchr(char_len=16):
        """Generate mixed random characters by ascii letters and digits.
        Default set character length as 16.

        Args:
            char_len: The random cahracters length. if not specfic, default
            to 16.

        Returns:
            Return the generated characters.

        Example:
            DataGenerator.randchr()
            # output: 8lMyuzCfUYD7hKHv
        """
        return ''.join(
            random.sample(
                string.ascii_letters +
                string.digits,
                char_len))

    @staticmethod
    def drawimage():
        """Generate new image by library 'pillow' and mark the text
        'test image' on the image. The image saved path is in 'misc'
        folder.

        Returns:
            Return the image path after image saved.

        Example:
            DataGenerator.drawimage()
            # output: /Users/testuser/workspace/dsp-api-test/misc/image.png
        """
        # generate new image with random color
        img = Image.new('RGB', (400, 400), color=tuple(
            [random.randint(0, 256) for x in range(3)]))
        draw = ImageDraw.Draw(img)
        # mark the text on the image
        draw.text((20, 20), 'test image', fill=(255, 255, 0))
        pp = PathParser()
        path = pp.path_join(pp.current_path(), 'misc', 'image.png')
        img.save(path)
        return path


class AssertUtils:
    """AssertUtils utils to use the assert segment in test cases.

    Func assertgroup used for check the groups of assert segment if equal.
    Func assertnotfound used for check the assert if not found.
    """

    def assertgroup(self, groupa, groupb, lis2assert):
        """Check the data in two groups are equal. If the field not in groupa
        or not in groupb, the assertion will be skipped.

        Args:
            groupa: The first group need to be compared.
            groupb: The second group need to be compared.
            lis2assert: The field to checked in both two group.

        Example:
            AssertUtils.assertgroup(gpa, gpb, ['a','b','c'])
        """
        for item in lis2assert:
            if item in groupa and item in groupb:
                assert groupa[item] == groupb[item], '{}: "{}" and "{}" not equal'.format(
                    item, groupa[item], groupb[item])

    def assertnotfound(self, key, value):
        """Check the data if exists, valued or correct.

        Args:
            key: The data need to check.
            value: The key value.

        Example:
            AssertUtils.assertnotfound(key, value)
        """
        assert key, '{} {} not found'.format(key, value)
