#!/usr/bin/env python

import sys, os

def parse_options(opts):
    """
    parse options given on cmdline separated by equal sign:
    >>> tuple(parse_options(['a=b', 'x x x=y y y']))
    (('a', 'b'), ('x x x', 'y y y'))
    """
    return ( tuple(i.split('=')) for i in opts )

def call_command(cmd, options):
    for patrn, repl in options:
        repl = {'patrn': patrn, 'repl': repl,}
        os.system(cmd % repl)

def rename_files_dirs(options):
    """
    rename all dirs and files to new name defined via options

    create dirs first
    than move files
    """
    call_command('''find . -type d | while read f; do mkdir -p "$(echo $f | sed 's/%(patrn)s/%(repl)s/g')"; done''', options)
    call_command('''find . -type f | while read f; do mv "$f"  "$(echo $f | sed 's/%(patrn)s/%(repl)s/g')"; done''', options)

    # delete empty dirs
    call_command('''find -depth -type d -empty -exec rmdir {} \;''', [(True, True)])

def change_content_onefile(path, pattern, replacement):
    """
    replace any occurence of pattern in single file
    """
    pass

def change_content(options):
    """
    take file by file and replace any occurence of pattern by its replacement
    """
    call_command('''grep '%(patrn)s' . -r -l | tr '\\n' '\\0' | xargs -0 sed -i "s/%(patrn)s/%(repl)s/g"''', options)


if __name__ == '__main__':
    options = parse_options(sys.argv[1:])
    rename_files_dirs(options)
    change_content(options)

