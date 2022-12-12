import execnet
gw = execnet.makegateway("popen//pypy")
channel = gw.remote_exec("""
def add_one(x):
    return x + 1

while 1:
    x = channel.receive()
    if x is None:
        break
    channel.send(repr(add_one(x)))
""")

def add_one(x):
    channel.send(x)
    return eval(channel.receive())
result = []
for x in range(10):
    result.append(add_one(x))
print(result)
