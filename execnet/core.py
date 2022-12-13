import execnet
import inspect
from functools import wraps


def build_remote(gw, function):
    func_name = function.__name__
    consumer_str = f"""
import sys
sys.setrecursionlimit(10**8)
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