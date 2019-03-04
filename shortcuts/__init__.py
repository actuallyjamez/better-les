from functools import partial

from pynput.keyboard import Controller, KeyCode, Key

# from .close_current_plugin import close_current_plugin

keyboard = Controller()

COMBINATIONS = [
    # {'key': {Key.cmd}, 'action': partial(close_current_plugin, keyboard)}
]
