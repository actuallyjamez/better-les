import asyncio
import os

import aiosc

# from time import sleep

# from pynput.keyboard import Controller, Key
# from AppKit import NSWorkspace

# keyboard = Controller()
loop = asyncio.get_event_loop()


def open_plugin(name):
    os.system("open -a Ableton\\ Live\\ 10\\ Suite")
    loop.run_until_complete(
        aiosc.send(('127.0.0.1', 9001), '/live/track/create')
    )
    loop.run_until_complete(
        aiosc.send(('127.0.0.1', 9001), '/live/browser/plugins/load', name)
    )

    # if NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] == 'Live':
    #     with keyboard.pressed(Key.cmd, Key.shift_l):
    #         keyboard.press('t')
    #     # with keyboard.pressed(Key.cmd):
    #     #     keyboard.press('r')
    #     # sleep(.2)
    #     # keyboard.type(name.lower())
    #     sleep(.2)
    #     keyboard.press(Key.enter)
    #     sleep(.2)
    #     with keyboard.pressed(Key.cmd):
    #         keyboard.press('f')
    #     sleep(.2)
    #     keyboard.type(search)
    #     sleep(.2)
    #     keyboard.press(Key.down)
    #     sleep(.2)
    #     keyboard.press(Key.enter)
    #     keyboard.press(Key.esc)
    #     return True
