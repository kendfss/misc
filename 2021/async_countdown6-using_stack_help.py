import keyboard, asyncio, time as t



async def get(key_checker):
    await key_checker.wait()
    return True

async def countdown(time):
    while time > 0:
        print(f'This program will exit in {int(time)} seconds. Press enter to start over.', end='\r')
        await asyncio.sleep(1)
        time -= 1
    print(f'This program will exit in 0 seconds. Press enter to start over.', end='\r')
    await asyncio.sleep(.75)
    print('bye' + ' ' * len('This program will exit in 0 seconds. Press enter to start over.'))
    return False

def notify(key_checker, event_loop):
    def wrap(*args, **kwargs):
        event_loop.call_soon_threadsafe(key_checker.set)
    return wrap

async def main():
    running = True
    while running:        
        enter_pressed = asyncio.Event()
        loop = asyncio.get_event_loop()
        keyboard.on_press_key('enter', notify(enter_pressed, loop))
        enter_pressed.clear()
        
        clock = asyncio.create_task(countdown(5))
        check = asyncio.create_task(get(enter_pressed))
        
        done, pending = await asyncio.wait({clock, check}, return_when=asyncio.FIRST_COMPLETED)
        print(done)
        keyboard.unhook('enter')
        [*map(lambda x: x.cancel(), pending)]
        running = next(iter(done)).result()
        if running:
            print('Starting over' + ' ' * len('This program will exit in 0 seconds. Press enter to start over.'), end='\r')
            await asyncio.sleep(1)
        
    
        

asyncio.run(main())
