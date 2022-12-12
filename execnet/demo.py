import execnet
gw = execnet.makegateway("popen//pypy")
channel = gw.remote_exec("""
array = []
while 1:
    x = channel.receive()
    if x is None:
        break
    array.append(x)
channel.send(repr(array))
""")
for x in range(10):
    channel.send([x])
channel.send(None)
ans = eval(channel.receive())
print(ans)
