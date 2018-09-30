# 多线程案例
from concurrent.futures import ThreadPoolExecutor, wait
import time,re

def wait_on_b():
    time.sleep(2)
    print('b')
    return 'b'

def wait_on_a():
    time.sleep(3)
    print('a')
    return 'a'

result = list()
pool = ThreadPoolExecutor(2)

result.append(pool.submit(wait_on_a))
result.append(pool.submit(wait_on_b))

wait(result)
# b
# a
print(result) # [<Future at 0x10533b1d0 state=finished returned str>, <Future at 0x10549a860 state=finished returned str>]
print(result[0].result()) # a
print(result[1].result()) # b
