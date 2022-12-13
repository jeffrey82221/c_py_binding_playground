from core import pypy, map_pypy

@pypy
def add_one_func(x):
    return x + 1

def times_two(x):
    return x * 2

def something_very_time_consuming():
    pass

if __name__ == '__main__':
    PARALLEL_CNT = 16
    TOTAL_AMOUNT = 1000000
    if PARALLEL_CNT == 1:
        result = []
        for x in range(TOTAL_AMOUNT):
            result.append(times_two(x))
        print(result[:10])
    else:
        result = map_pypy(times_two, range(TOTAL_AMOUNT), PARALLEL_CNT)
        print(result[:10])

