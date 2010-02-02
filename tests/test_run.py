
import os
from os.path import join
from shutil import rmtree
from unittest import TestCase
from tempfile import mkdtemp

from run import parse_options, import_config_file, eval_dirs, eval_command, run
from run import CMD, DIR


def give_mocked_os_system(output):
    def os_system(cmd):
        output.append((os.getcwd(), cmd,))
    return os_system

class TestRun(TestCase):
    def setUp(self):
        # save os.system because of mocking
        self.os_system = os.system

    def test_run_with_dummiest_values(self):
        options = parse_options([])
        config = import_config_file()
        dirs = eval_dirs(options, config)
        command = eval_command(options, config)

        # mock os.system
        output = []
        os.system = give_mocked_os_system(output)

        run(command, dirs)

        expected = [
            (DIR, CMD),
            (DIR, CMD),
        ]

        self.failUnlessEqual(expected, output)

    def tearDown(self):
        # unmock os.system
        os.system = self.os_system

