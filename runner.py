#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: api-testing
@file: runner.py
@time: 2019/1/6 下午1:53
'''

import os
import pytest
from utils import PathParser


class Runner(object):

    def __init__(self):
        self.path_parser = PathParser()
        self.tests_dir = self.path_parser.path_join(self.path_parser.get_workspace_root_path(), 'tests')
        self.report_dir = self.path_parser.path_join(self.path_parser.get_workspace_root_path(), 'report')
        self.html_report_dir = self.path_parser.path_join(self.report_dir, 'html')
        self.path_parser.remove_dirs(self.report_dir)

    def run_test(self):
        self.generate_results()
        self.generate_html_report()

    def generate_results(self):
        pytest.main([self.tests_dir, '--alluredir=' + self.report_dir])

    def generate_html_report(self):
        cmd = 'allure generate {} -o {}'.format(self.report_dir, self.html_report_dir)
        os.system(cmd)


def runner():
    run = Runner()
    run.run_test()


if __name__ == '__main__':
    runner()
