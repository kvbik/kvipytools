#!/usr/bin/env python

import sys

def parse_options(opts):
    return ( tuple(i.split('=')) for i in opts )

def rename_files_dirs(options):
    pass

def change_content(options):
    pass

if __name__ == '__main__':
    options = parse_options(sys.argv[1:])
    rename_files_dirs(options)
    change_content(options)
