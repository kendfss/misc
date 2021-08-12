import keyboard, asyncio, time as t



async def get():
    await keyboard.record('enter', True)
    return True

async def countdown(time):
    while time > 0:
        print(f'This program will exit in {int(time)} seconds. Press enter to start over.', end='\r')
        await asyncio.sleep(1)
        # t.sleep(1)
        time -= 1
    print(f'This program will exit in 0 seconds. Press enter to start over.', end='\r')
    return False


async def main():
    running = True
    while running:
        # other code
        
        
        clock = asyncio.create_task(countdown(5))
        check = asyncio.create_task(get())
        
        done, pending = await asyncio.wait({clock, check}, return_when=asyncio.FIRST_COMPLETED)
        running = next(iter(done)).result()
        print(running, end='\r')
    print('bye')
        

asyncio.run(main())
# asyncio.run(get())
