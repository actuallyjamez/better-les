from time import sleep

from pynput.keyboard import Controller, Key

keyboard = Controller()


def open_plugin(string):
    with keyboard.pressed(Key.cmd):
        keyboard.press('f')
    sleep(.2)
    keyboard.type(string)
    sleep(.2)
    keyboard.press(Key.down)
    sleep(.2)
    keyboard.press(Key.enter)
    return True
