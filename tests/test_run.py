
import os
from os.path import join
from shutil import rmtree
from unittest import TestCase
from tempfile import mkdtemp

from run import parse_options, import_config_file, eval_dirs, eval_command, run


class TestRun(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

