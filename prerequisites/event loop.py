import time
import asyncio
import threading

def gen():
    yield 1
    yield 2
    yield 3
    yield 4
obj=gen()
async def run(sleep):
    print("running...",sleep)
    await asyncio.sleep(sleep)
def lancher():
    loop=asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(run(3),run(obj.__next__())))
    loop.close()
st=time.time()
t1=threading.Thread(target=lancher)
t2=threading.Thread(target=lancher)
t1.start()
t2.start()
t1.join()   
t2.join()
print(time.time()-st)