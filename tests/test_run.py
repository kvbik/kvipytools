
import os
from os import path
from shutil import rmtree
from unittest import TestCase
from tempfile import mkdtemp

from run import parse_options, import_config_file, eval_dirs, eval_command, run, main
from run import CMD, DIR


RUNCOMMAND = '''\
DIRS = (
    '/tmp/abraka',
    '/tmp/brekeke',
)
command = 'pwd'
'''


def give_mocked_os_system(output):
    def os_system(cmd):
        output.append((os.getcwd(), cmd,))
    return os_system

class TestRun(TestCase):
    def setUp(self):
        # save os.system because of mocking
        self.os_system = os.system

        # create test dir structure
        self.directory = mkdtemp(prefix='test_run_testrun_')

        # store curr path
        self.oldcwd = os.getcwd()

        # make some subdirs
        os.chdir(self.directory)
        for d in ('a', 'b', 'c'):
            os.makedirs(d)

        # create runcommand file
        self.runfile = path.join(self.directory, 'runcommand2.py')
        f = open(self.runfile, 'w')
        f.write(RUNCOMMAND)
        f.close()

    def fail_unless_equal_main_with_this_argv(self, argv, expected, base=None):
        oldcwd = os.getcwd()
        if base is not None:
            os.chdir(base)

        # mock os.system
        output = []
        os.system = give_mocked_os_system(output)

        # call main func without arguments
        main(argv)

        if base is not None:
            os.chdir(oldcwd)

        self.failUnlessEqual(expected, output)

    def test_run_with_dummiest_values(self):
        argv = []
        expected = [
            (DIR, CMD),
            (DIR, CMD),
        ]
        self.fail_unless_equal_main_with_this_argv(argv, expected)

    def test_run_with_some_command(self):
        c = 'command'
        argv = [c]
        expected = [
            (DIR, CMD),
            (DIR, c),
        ]
        self.fail_unless_equal_main_with_this_argv(argv, expected)

    def test_run_with_some_command_and_dirs(self):
        d = self.directory
        c = 'command'
        argv = [c, 'a', 'b', 'c']
        expected = [
            (path.join(d, 'a'), CMD),
            (path.join(d, 'a'), c),
            (path.join(d, 'b'), CMD),
            (path.join(d, 'b'), c),
            (path.join(d, 'c'), CMD),
            (path.join(d, 'c'), c),
        ]
        self.fail_unless_equal_main_with_this_argv(argv, expected, base=self.directory)

    def tearDown(self):
        # unmock os.system
        os.system = self.os_system

        # go back
        os.chdir(self.oldcwd)

        # dir cleanup
        rmtree(self.directory)

