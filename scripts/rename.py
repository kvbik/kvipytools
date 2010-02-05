#!/usr/bin/env python

'''
local shortcut only if library is not installed
'''

import sys
from os import path

p = path.abspath(path.join(path.dirname(__file__), path.pardir))
if p not in sys.path:
    sys.path.insert(0, p)

from kvipytools import rename

if __name__ == '__main__':
    rename.main()

