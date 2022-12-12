"""
time python main_sum.py
>> python main_sum.py  2.63s user 0.12s system 99% cpu 2.781 total
time pypy main_sumpy
>> pypy3 main_sum.py  0.24s user 0.15s system 95% cpu 0.401 total
"""
from parallel_sum import sum

if __name__ == '__main__':
    input_array = [1] * 100000000
    result = sum(input_array)
    print(result)