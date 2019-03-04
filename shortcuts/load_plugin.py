from time import sleep

from pynput.keyboard import Controller, Key

keyboard = Controller()


def open_plugin(name, search):
    with keyboard.pressed(Key.cmd, Key.shift_l):
        keyboard.press('t')
    # with keyboard.pressed(Key.cmd):
    #     keyboard.press('r')
    # sleep(.2)
    # keyboard.type(name.lower())
    sleep(.2)
    keyboard.press(Key.enter)
    sleep(.2)
    with keyboard.pressed(Key.cmd):
        keyboard.press('f')
    sleep(.2)
    keyboard.type(search)
    sleep(.2)
    keyboard.press(Key.down)
    sleep(.2)
    keyboard.press(Key.enter)
    keyboard.press(Key.esc)
    return True
