
import os
from os.path import join
from shutil import rmtree
from unittest import TestCase
from tempfile import mkdtemp

from rename import parse_options, rename_files_dirs, change_content


class TestParse(TestCase):
    def test_option_parser(self):
        parsed = parse_options(['x=y', 'a a a=b b b'])
        expected = (('x', 'y'), ('a a a', 'b b b'))

        self.failUnlessEqual(tuple(parsed), expected)

class TestWithTmpDirCase(TestCase):
    def setUp(self):
        self.options = (('x', 'y'), ('a a a', 'b b b'))

        self.oldcwd = os.getcwd()
        self.directory = mkdtemp(prefix='test_util_parse_')
        os.chdir(self.directory)

        for dir, fil in (('x', 'a a a'), ('a a a', 'x')):
            os.mkdir(dir)
            f = open(join(dir, fil), 'w')
            f.write('\n'.join([dir, fil]))
            f.close()

    def tearDown(self):
        os.chdir(self.oldcwd)
        rmtree(self.directory)

class TestRenameFiles(TestWithTmpDirCase):
    def test_correct_filenames(self):
        rename_files_dirs(self.options)

        listdir = sorted([ i for i in os.walk('.') ])
        expected = sorted([('.', ['b b b', 'y'], []), ('./b b b', [], ['y']), ('./y', [], ['b b b'])])
        self.failUnlessEqual(listdir, expected)

class TestChangeContent(TestWithTmpDirCase):
    def readfile(self, filename):
        f = open(filename, 'r')
        return f.read()

    def test_content_renamed(self):
        change_content(self.options)

        d = {}
        for base, dirs, files in os.walk('.'):
            for i in files:
                f = join(base, i)
                d[f] = self.readfile(f)

        expected = [('./a a a/x', 'b b b\ny'), ('./x/a a a', 'y\nb b b')]

        self.failUnlessEqual(sorted(d.items()), expected)

