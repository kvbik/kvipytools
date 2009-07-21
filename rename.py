#!/usr/bin/env python

import sys, os

def parse_options(opts):
    """
    parse options given on cmdline separated by equal sign:
    >>> tuple(parse_options(['a=b', 'x x x=y y y']))
    (('a', 'b'), ('x x x', 'y y y'))
    """
    return ( tuple(i.split('=')) for i in opts )

def rename_files_dirs(options):
    """
    rename all dirs and files to new name defined via options

    create dirs first
    than move files
    """
    pass

def change_content_onefile(path, pattern, replacement):
    """
    replace any occurence of pattern in single file
    """
    pass

def change_content(options):
    """
    take file by file and replace any occurence of pattern by its replacement
    """
    pass

if __name__ == '__main__':
    options = parse_options(sys.argv[1:])
    rename_files_dirs(options)
    change_content(options)

