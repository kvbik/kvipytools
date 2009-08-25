#!/usr/bin/env python

import sys, os

class OptionParser(object):
    def __init__(self, escape_char='\\', escape_replacement=-1, splitter_char='=', splitter_replacement=-2):
        self.escape_char = escape_char
        self.escape_replacement = escape_replacement
        self.splitter_char = splitter_char
        self.splitter_replacement = splitter_replacement

    def split_string(self, string):
        return [ c for c in string ]

    def replace_pair(self, chars, pair, replacement):
        '''
        go through chars in pairs and if two chars equals given pair
        put some special mark instead
        '''
        escaped_chars = []
        for p in zip(chars[::2], chars[1::2]):
            if p == pair:
                escaped_chars.append(replacement)
            else:
                escaped_chars.extend(p)

        # handle odd length of chars list
        if len(chars) % 2:
            escaped_chars.append(chars[-1])

        return escaped_chars

    def escape_escape(self, chars):
        pair = (self.escape_char, self.escape_char)
        return self.replace_pair(chars, pair, self.escape_replacement)

    def escape_split(self, chars):
        pair = (self.escape_char, self.splitter_char)
        return self.replace_pair(chars, pair, self.splitter_replacement)

    def split_via_equalsign(self, chars, splitter='='):
        index = chars.index(splitter)
        return (chars[:index], chars[index+1:])

    def join_tuple(self, twins):
        return tuple(map(lambda x: ''.join(x), twins))

    def __call__(self, opts):
        """
        parse options given on cmdline separated by equal sign:
        >>> OptionParser()(['a=b', 'x x x=y y y'])
        [('a', 'b'), ('x x x', 'y y y')]
        """
        parsed_opts = []
        for o in opts:
            o = self.escape_escape(o)
            o = self.escape_split(o)
            t = self.split_via_equalsign(o)
            parsed_opts.append(self.join_tuple(t))
        return parsed_opts

def call_command(cmd, options):
    """
    helper function that call shell command for every tuple in options
    """
    for patrn, repl in options:
        repl = {'patrn': patrn, 'repl': repl,}
        command = cmd % repl
        print 'running: %s' % command
        os.system(command)

def rename_files_dirs(options):
    """
    rename all dirs and files to new name defined via options
    """
    # create dirs first
    call_command('''find . -type d | while read f; do mkdir -p "$(echo $f | sed 's/%(patrn)s/%(repl)s/g')"; done''', options)
    # than move files
    call_command('''find . -type f | while read f; do mv "$f"  "$(echo $f | sed 's/%(patrn)s/%(repl)s/g')"; done''', options)
    # delete empty dirs
    call_command('''find -depth -type d -empty -exec rmdir {} \;''', [(1,1)])

def change_content(options):
    """
    take file by file and replace any occurence of pattern by its replacement
    """
    call_command('''grep '%(patrn)s' . -r -l | tr '\\n' '\\0' | xargs -0 sed -i "s/%(patrn)s/%(repl)s/g"''', options)


if __name__ == '__main__':
    parse_options = OptionParser()
    options = parse_options(sys.argv[1:])
    rename_files_dirs(options)
    change_content(options)

