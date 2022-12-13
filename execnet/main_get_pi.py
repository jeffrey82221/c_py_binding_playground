"""

"""
import sys
from core import pypy, map_pypy
sys.setrecursionlimit(10**8)


def get_pi(n):
    def inner_func(n):
        if n == 1:
            return 4
        if n == 2:
            return 8
        return 4 * (-1)**(n+1) * (1/(2*n-1)) + inner_func(n-1) + inner_func(n-2)
    result = inner_func(n)
    return result


if __name__ == '__main__':
    # result = get_pi(35) 
    # python main_get_pi.py  3.89s user 0.06s system 99% cpu 3.963 total
    # result = pypy(get_pi)(35)
    # python main_get_pi.py  4.03s user 0.12s system 99% cpu 4.160 total
    result = list(map(get_pi, [35, 35, 35, 35]))
    # python main_get_pi.py  15.02s user 0.08s system 99% cpu 15.106 total
    # result = list(map_pypy(get_pi, [35, 35, 35, 35], worker_cnt=1))
    # python main_get_pi.py  15.16s user 0.12s system 99% cpu 15.301 total
    # result = list(map_pypy(get_pi, [35, 35, 35, 35]), worker_cnt=4)
    # python main_get_pi.py  15.14s user 0.13s system 99% cpu 15.281 total
    print(result[0])