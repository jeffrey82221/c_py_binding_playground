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
    gw = execnet.makegateway("popen// python")
    channel = build_remote(gw, func)
    @wraps(func)
    def wrapped_func(x):
        channel.send(x)
        return eval(channel.receive())
    return wrapped_func

@pypy
def add_one_func(x):
    return x + 1

result = []
for x in range(10000):
    result.append(add_one_func(x))

