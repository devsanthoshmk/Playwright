import time
from asyncio import gather,run,sleep
from asyncio import Future

async def one(future):
    print("waiting for 3 sec")
    await sleep(3)
    print("future doneing")
    future.done()
    future.set_result("future is done")
async def two(future):
    print("two will wait for future")
    await future
    print("altlast future is done subbahhh")
async def main():
    future=Future()
    await gather(two(future),one(future))
st=time.time()
run(main())
print(f'\'{(time.time()-st):0.2f}')