#!/usr/bin/env python3

import ctypes
import os, sys
from ctypes.util import find_library

if __name__ == '__main__':

    path = find_library('lzma')
    if not path:
        sys.stderr.write('Failed to find liblzma.\n')
        sys.exit(1)

    try:
        lib = ctypes.cdll.LoadLibrary(path)
    except OSError:
        sys.stderr.write('Failed to load liblzma.\n')
        sys.exit(1)

    print(os.getenv("LD_LIBRARY_PATH"))
    fn = lib.lzma_version_string
    fn.restype = ctypes.c_char_p
    print("liblzma version is " + str(fn(None), "ascii"))
