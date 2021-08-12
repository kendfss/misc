import asyncio



async def get():
    response = await input()
    return 'run'

async def countdown(time):
    while time > 0:
        print(f'This program will exit in {int(time)} seconds. Press enter to start over.', end='\r')
        await asyncio.sleep(1)
        time -= 1
    return 'halt'

async def main():
    running = True
    
    while running:
        ## other code
        clock = asyncio.create_task(countdown(5))
        check = asyncio.create_task(get())
        for f in asyncio.as_completed({check, clock}):
            # print(f.cr_frame)
            # print(f.cr_await, f.cr_running, f.cr_origin, f.cr_frame, f.cr_code)
            print(f.cr_await, f.cr_running, f.cr_origin)
            
    print('bye')


asyncio.run(main())