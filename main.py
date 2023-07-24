import asyncio
import queue
import random
import time
import os

mainQueue = queue.Queue()

async def updatescreen(mainQueue):

    bigStr = "*******************************"


    delay = 0.5
    thisItem = ""
    while True:
        await asyncio.sleep(delay)
        while not mainQueue.empty():
            thisItem = mainQueue.get()

        os.system('cls')
        print(bigStr)
        print(bigStr)
        print(bigStr)
        print(thisItem)
        print(bigStr)
        print(bigStr)
        print(bigStr)


async def mainThread(mainQueue):
    delay = 0.1



    thisStr = ""
    while True:
        await asyncio.sleep(delay)
        thisStr = chr(random.randint(ord('A'),ord('z')))
        mainQueue.put_nowait(thisStr)


async def main():
    task1 = asyncio.create_task(updatescreen(mainQueue))
    task2 = asyncio.create_task(mainThread(mainQueue))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())