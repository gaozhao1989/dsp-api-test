import os

import pytest

from utils import PathParser


class Runner(object):
    """The generic entrance for run the test cases.

    All test cases in directory 'tests' will be executed by 'pytest'.
    The results for 'pytest' will be stored in report directory(json format).
    After test execution completed, runner will auto invoke the 'allure'
    to generate the html test report.
    """

    def __init__(self):
        """Inits for environment prepare.

        Dirs:
            tests directory setup
            report directory setup
            html report directory setup
        """
        self.path_parser = PathParser()
        self.tests_dir = self.path_parser.path_join(
            self.path_parser.current_path(), 'tests')
        self.report_dir = self.path_parser.path_join(
            self.path_parser.current_path(), 'report')
        self.html_report_dir = self.path_parser.path_join(
            self.report_dir, 'html')
        # remove the latest the results if exists
        self.path_parser.remove_dirs(self.report_dir)

    def run_test(self):
        """Run test and generate test results."""
        self.generate_results()
        self.generate_html_report()

    def generate_results(self):
        """Use 'pytest' to run the tests and generate pytest report."""
        pytest.main([self.tests_dir, '--alluredir=' + self.report_dir])

    def generate_html_report(self):
        """Invoke the 'allure' to generate the html report by system command."""
        cmd = 'allure generate {} -o {}'.format(
            self.report_dir, self.html_report_dir)
        os.system(cmd)


def runner():
    run = Runner()
    run.run_test()


if __name__ == '__main__':
    runner()
