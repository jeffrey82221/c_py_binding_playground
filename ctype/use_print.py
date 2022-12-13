import ctypes
import os
lib_path = os.path.join(os.path.dirname(__file__), 'print.so')
clibrary = ctypes.CDLL(lib_path)
clibrary.display()