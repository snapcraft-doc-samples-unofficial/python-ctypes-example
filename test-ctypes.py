#!/usr/bin/env python3

import ctypes
import os, pprint, sys
from ctypes.util import find_library

if __name__ == '__main__':

    path = find_library('zstd')
    if not path:
        sys.stderr.write('Failed to find libzstd.\n')
        sys.exit(1)

    try:
        lib = ctypes.cdll.LoadLibrary(path)
    except OSError:
        sys.stderr.write('Failed to load libzstd.\n')
        sys.exit(1)

    pprint.pprint(dict(os.environ))
    fn = lib.ZSTD_versionString
    fn.restype = ctypes.c_char_p
    print("libzstd version is " + str(fn(None), "ascii"))
