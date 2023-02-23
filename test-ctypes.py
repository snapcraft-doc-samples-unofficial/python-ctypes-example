#!/usr/bin/env python3

import ctypes
import sys
from ctypes.util import find_library

if __name__ == '__main__':

    path = find_library('z')
    if not path:
        sys.stderr.write('Failed to find zlib.\n')
        sys.exit(1)

    try:
        lib = ctypes.cdll.LoadLibrary(path)
    except OSError:
        sys.stderr.write('Failed to load zlib.\n')
        sys.exit(1)

    zlibVersion = lib.zlibVersion
    zlibVersion.restype = ctypes.c_char_p
    print("zlib version is " + str(zlibVersion(None), "ascii"))
