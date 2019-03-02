from time import sleep

from pynput.keyboard import Controller, Key

keyboard = Controller()


def open_plugin(string):
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.tab)
    sleep(.2)
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('f')
    sleep(.2)
    keyboard.type(string)
    sleep(.2)
    keyboard.press(Key.down)
    sleep(.2)
    keyboard.press(Key.enter)
    return True
