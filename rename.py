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
    os.system('''find . -type d | while read f; do mkdir -p "$(echo $f | sed 's/a a a/b b b/g')"; done''')
    os.system('''find . -type d | while read f; do mkdir -p "$(echo $f | sed 's/x/y/g')"; done''')

    os.system('''find . -type f | while read f; do mv "$f" "$(echo $f | sed 's/a a a/b b b/g')"; done''')
    os.system('''find . -type f | while read f; do mv "$f" "$(echo $f | sed 's/x/y/g')"; done''')

    os.system('''find -depth -type d -empty -exec rmdir {} \;''')


def change_content_onefile(path, pattern, replacement):
    """
    replace any occurence of pattern in single file
    """
    pass

def change_content(options):
    """
    take file by file and replace any occurence of pattern by its replacement
    """
    os.system('''grep 'a a a' . -r -l | tr '\\n' '\\0' | xargs -0 sed -i "s/a a a/b b b/g"''')
    os.system('''grep 'x' . -r -l | tr '\\n' '\\0' | xargs -0 sed -i "s/x/y/g"''')

if __name__ == '__main__':
    options = parse_options(sys.argv[1:])
    rename_files_dirs(options)
    change_content(options)

