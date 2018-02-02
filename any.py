
def lazy_range_from(up_to):
    """
    生成器返回一个从0到up_to值的整数序列
    """
    index = 0
    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()

def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    while index < up_to:
        yield index
        index += 1 
print('lazy_range')
lr = lazy_range(3)
for n in lr:
    print(n)   

print('lazy_range_from')
lrf = lazy_range_from(3)
for n in lrf:
    print(n)

def bottom():
    # Returning the yield lets the value that goes up the call stack to come right back
    # down.
    return (yield 42)

def middle():
    return (yield from bottom())

def top():
    return (yield from middle())

# Get the generator.
gen = top()
value = next(gen)
print(value)  # Prints '42'.
try:
    value = gen.send(value * 2)
except StopIteration as exc:
    value = exc.value
print(value)  # Prints '84'.

import asyncio
import collections

class AsyncMy:
    def __init__(self):
        self.list = collections.deque([1, 2, 3, 4, 5])

    async def doIt(self):
        await asyncio.sleep(1)

    async def __aiter__(self):
        return self

    async def __anext__(self):
        if list.count > 0:
            return list.pop()

    # async def __await__(self):
    #     return self

am = AsyncMy()

import inspect

di = am.doIt()
loop = asyncio.get_event_loop()
loop.run_until_complete(di)
loop.close()

async def Abc():
    await asyncio.sleep(1)
    yield 0

def main():
    abc = Abc()
    await abc.send(None)

print('Abc是协程函数?', inspect.iscoroutinefunction(Abc))
print('abc是协程对象吗？', inspect.iscoroutine(abc))
print('di是协程对象吗？', inspect.iscoroutine(di))
print('doIt是协程函数吗？', inspect.iscoroutinefunction(AsyncMy.doIt))
print('am是协程对象吗？', inspect.isawaitable(am))
print('sleep?', inspect.iscoroutinefunction(asyncio.sleep))
# def main():
#     async for n in am:
#         print(n)

# main()