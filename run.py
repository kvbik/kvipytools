#!/usr/bin/env python

import sys, os
from os import path


C = '_cmd'
D = '_ALL'

CMD = '%s -c "import os; print os.getcwd()"' % sys.executable


def parse_options(argv=[]):
    '''
    parse options from sys.argv
    '''
    if not len(argv):
        return (C, D)
    elif len(argv) == 1:
        return (argv[0], D)
    return argv

def import_config_file(runfile=''):
    '''
    import python file with some config values

    see:
    /usr/lib/python2.6/site-packages/fabric/main.py:load_fabfile
    '''
    dir = os.getcwd()
    runfile = path.join(dir, runfile)
    if not path.isfile(runfile):
        return object()

def eval_option(option, config):
    '''
    evaluate one option from config file
    if it is not there, return what was given
    '''
    defaults = {
        C: CMD,
        D: os.getcwd(),
    }
    return getattr(config, option, defaults.get(option, option))

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

def main(runfile='', argv=[]):
    options = parse_options(argv)
    config = import_config_file(runfile)

    dirs = eval_dirs(options, config)
    command = eval_command(options, config)

    run(command, dirs)


if __name__ == '__main__':
    runfile = 'runcommand.py'
    argv = sys.argv[1:]

    main(runfile, argv)

