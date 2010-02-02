#!/usr/bin/env python

import sys, os


CMD = '%s -c "import os; print os.getcwd()"' % sys.executable
DIR = '_'


def parse_options(argv=[]):
    '''
    parse options from sys.argv
    '''
    if not len(argv):
        return (CMD, DIR)
    elif len(argv) == 1:
        return (argv[0], DIR)
    return argv

def import_config_file(file='runcommand.py'):
    '''
    import python file with some config values
    '''
    pass

def eval_option(option, config):
    '''
    evaluate one option from config file
    if it is not there, return what was given
    '''
    pass

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
        print os.getcwd(), command
        os.chdir(base)


if __name__ == '__main__':
    options = parse_options(sys.argv[1:])
    config = import_config_file()

    dirs = eval_dirs(options, config)
    command = eval_command(options, config)

    run(command, dirs)

