import execnet
import inspect
from functools import wraps


def build_remote(gw, function):
    func_name = function.__name__
    consumer_str = f"""
{inspect.getsource(function)}
while 1:
    x = channel.receive()
    if x is None:
        break
    channel.send(repr({func_name}(x)))
"""
    consumer_str = consumer_str.replace('@pypy', '')
    channel = gw.remote_exec(consumer_str)
    return channel

def pypy(func):
    gw = execnet.makegateway("popen// pypy")
    channel = build_remote(gw, func)
    @wraps(func)
    def wrapped_func(x):
        channel.send(x)
        return eval(channel.receive())
    return wrapped_func

def map_pypy(func, input_list, worker_cnt=1):
    workers = [pypy(func) for _ in range(worker_cnt)]
    result = []
    for i, item in enumerate(input_list):
        w_index = i % worker_cnt    
        result.append(workers[w_index](item))
    return result

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

