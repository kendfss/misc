"""
Written by W1ndstorm
    https://stackoverflow.com/questions/66112359/asynchronous-countdowns-in-python?noredirect=1#comment116890572_66112359


helped by User4814162342
"""

import asyncio
import keyboard


class Downcounter:
    def __init__(self):
        self.enter_pressed = asyncio.Event()
        self._loop = asyncio.get_event_loop()

    async def get(self):
        await self.enter_pressed.wait()
        return True

    @staticmethod
    async def countdown(time):
        while time > 0:
            print(f'This program will exit in {int(time)} seconds. Press enter to start over.', end='\r')
            await asyncio.sleep(1)
            # t.sleep(1)
            time -= 1
        print(f'This program will exit in 0 seconds. Press enter to start over.')
        return False

    def notify_enter(self, *args, **kwargs):
        # self.enter_pressed.set()
        self._loop.call_soon_threadsafe(self.enter_pressed.set)

    async def main(self):
        running = True
        while running:
            # other code

            keyboard.on_press_key('enter', self.notify_enter)
            self.enter_pressed.clear()
            clock = asyncio.create_task(self.countdown(5))
            check = asyncio.create_task(self.get())

            done, pending = await asyncio.wait({clock, check}, return_when=asyncio.FIRST_COMPLETED)
            keyboard.unhook('enter')  # unbind the listener on enter key_down event
            [*map(lambda x: x.cancel(), pending)]  # Only one of the tasks will complete, so we need to cancel the other one. 
            running = next(iter(done)).result()

        print('bye')


async def main():
    program = Downcounter()
    await program.main()

asyncio.run(main())