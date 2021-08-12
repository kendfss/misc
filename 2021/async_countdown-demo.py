import asyncio
from math import pi
def differential(time):
    if isinstance(time, int) or time.is_integer():
        return 1
    else:
        return 10**-len(str(time).split('.')[-1])

async def countdown(time):
    delta = differential(time)
    while time > 0:
        print(f'This program will exit in {int(time)} seconds. Press enter to start over.', end='\r')
        await asyncio.sleep(delta)
        time -= delta
    print(f'This program will exit in 0 seconds. Press enter to start over.', end='\r')
    await asyncio.sleep(.5)
    print('\n\nBye\n')
    await asyncio.sleep(1)

# async def get():
    # await input()
        

# asyncio.run(countdown(2.33))
asyncio.run(countdown(5.36900000001))


        