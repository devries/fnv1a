import ctypes
import os

_libname = 'fnv_hash.so'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_libname,)))
_lib = ctypes.cdll.LoadLibrary(_path)

_lib.fnv1a64.argtypes = [ctypes.c_char_p, ctypes.c_ulong]
_lib.fnv1a64.restype = ctypes.c_ulonglong

def fnv1a64(bytestring):
    return _lib.fnv1a64(bytestring, len(bytestring))

def fnv1a64_unicode(unicodestring):
    bytestring = unicodestring.encode('utf-8')

    return _lib.fnv1a64(bytestring, len(bytestring))
