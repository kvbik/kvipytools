
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
    TEST_DIR_STRUCTURE = (
        (join('.'), None),
        (join('.', 'x'), None),
        (join('.', 'x', 'a a a'), 'x\na a a'),
        (join('.', 'a a a'), None),
        (join('.', 'a a a', 'x'), 'a a a\nx'),
    )

    def setUp(self):
        self.options = (('x', 'y'), ('a a a', 'b b b'))

        self.oldcwd = os.getcwd()
        self.directory = mkdtemp(prefix='test_util_parse_')
        os.chdir(self.directory)

        self.create_structure_from_variable(self.TEST_DIR_STRUCTURE)

    def create_structure_from_variable(self, dir_structure):
        '''
        create directory structure via given list of tuples (filename, content,)
        content being None means it is directory
        '''
        for filename, content in dir_structure:
            if content is None:
                try:
                    os.makedirs(filename)
                except OSError:
                    pass
            else:
                f = open(filename, 'w')
                f.write(content)
                f.close()

    def store_directory_structure(self, path):
        '''
        recursivelly traverse directory and store it in format
        that can be given to create_structure_from_variable()
        '''
        d = {}
        for base, dirs, files in os.walk(path):
            d[base] = None
            for i in files:
                fn = join(base, i)
                f = open(fn, 'r')
                d[fn] = f.read()
                f.close()
        return d.items()

    def tearDown(self):
        os.chdir(self.oldcwd)
        rmtree(self.directory)

class TestRenameFiles(TestWithTmpDirCase):
    def test_correct_filenames(self):
        rename_files_dirs(self.options)

        actual_structure = sorted(self.store_directory_structure('.'))
        expected_structure = sorted((
            (join('.'), None),
            (join('.', 'y'), None),
            (join('.', 'y', 'b b b'), 'x\na a a'),
            (join('.', 'b b b'), None),
            (join('.', 'b b b', 'y'), 'a a a\nx'),
        ))

        self.failUnlessEqual(expected_structure, actual_structure)

class TestChangeContent(TestWithTmpDirCase):
    def test_content_renamed(self):
        change_content(self.options)

        actual_structure = sorted(self.store_directory_structure('.'))
        expected_structure = sorted((
            (join('.'), None),
            (join('.', 'x'), None),
            (join('.', 'x', 'a a a'), 'y\nb b b'),
            (join('.', 'a a a'), None),
            (join('.', 'a a a', 'x'), 'b b b\ny'),
        ))

        self.failUnlessEqual(expected_structure, actual_structure)

