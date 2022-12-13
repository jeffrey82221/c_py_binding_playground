from ctypes import cdll

libc = cdll.LoadLibrary("add.cpython-39-darwin.so") 

libc.printf