import asyncio, keyboard


async def get():
    keyboard.record('enter', True)
    return True

async def main():
    running = True
    while running:
        
        try:
            running = await asyncio.wait_for(get(), 5)
        except asyncio.TimeoutError:
            running = False
        print(running)
    print('Bye')

asyncio.run(main())