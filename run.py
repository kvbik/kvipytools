#!/usr/bin/env python

import sys, os
from os import path


C = 'cmd'
D = 'ALL'

CMD = '%s -c "import os; print os.getcwd()"' % sys.executable
DIR = os.getcwd()

DEFAULTS = {C:CMD, D:DIR}


def parse_options(argv=[]):
    '''
    parse options from sys.argv
    '''
    if not len(argv):
        return (C, D)
    elif len(argv) == 1:
        return (argv[0], D)
    return argv

def import_config_file(runfile='runcommand.py'):
    '''
    import python file with some config values

    see:
    /usr/lib/python2.6/site-packages/fabric/main.py:load_fabfile
    '''
    runfile = path.join(DIR, runfile)
    if not path.exists(runfile):
        return object()

def eval_option(option, config):
    '''
    evaluate one option from config file
    if it is not there, return what was given
    '''
    return getattr(config, option, DEFAULTS.get(option, option))

def eval_dirs(options, config):
    '''
    evaluate dir variables into actual directories
    or return the same dir name
    '''
    l = [ eval_option(o, config) for o in options[1:] ]
    return l

def eval_command(options, config):
    '''
    evaluate command variable or return the same
    '''
    return eval_option(options[0], config)

def run(command, dirs):
    '''
    run specified command in given directories
    '''
    base = os.getcwd()
    for d in dirs:
        os.chdir(d)
        os.system(CMD)
        os.system(command)
        os.chdir(base)

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    options = parse_options(argv)
    config = import_config_file()

    dirs = eval_dirs(options, config)
    command = eval_command(options, config)

    run(command, dirs)


if __name__ == '__main__':
    main()

