import asyncio
import time
async def count():
    print("something",end=" ")
    await asyncio.sleep(2)
    print("sometin",end=" ")
    return 'a'
async def count2():
    print("22",end=' ')
async def main():
    await asyncio.gather(count(),count2(),count())
def a(s):
    print(s)
a(asyncio.run(count()))

# st=time.time()
# asyncio.run(main())
# print("\ntime taken",time.time()-st)
# st=time.time()

# def count():
#     print("somekhskfhsfhlsjfthing",end=" ")
#     time.sleep(1)
#     print("sometin",end=" ")
#     time.sleep(1)
# count()
# count()
# count()
# print("\ntime taken",time.time()-st)
