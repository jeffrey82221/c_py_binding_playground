"""
Before nuitka compilation: 

python main_sum.py  2.66s user 0.11s system 99% cpu 2.781 total

After nuitka compilation:

python main_sum.py  1.96s user 0.14s system 86% cpu 2.418 total

=> about 27% speed-up

With whole compilation: 

./main_sum.bin  2.05s user 0.08s system 99% cpu 2.141 total

"""
from sum import sum

if __name__ == '__main__':
    input_array = [1] * 100000000
    result = sum(input_array)
    print(result)