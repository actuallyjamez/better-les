# from AppKit import NSWorkspace
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from pynput import keyboard

# The currently active modifiers
from shortcuts import COMBINATIONS

# The key combination to check

current = set()


class Worker(QObject):
    finished = pyqtSignal()
    command_status = pyqtSignal(bool)

    # active_keys = []

    @pyqtSlot(name='keyboard_watcher')
    def keyboard_watcher(self):

        def on_press(key):
            for i in COMBINATIONS:
                if key in i['key']:
                    current.add(key)
                    if all(k in current for k in i['key']):
                        i['action']()
                if key == keyboard.Key.esc:
                    listener.stop()

            # if any([key in COMBO for COMBO in COMBINATIONS]):
            #     current.add(key)
            #     if any(all(k in current for k, v in COMBO) for COMBO in COMBINATIONS):
            #         pass

            # self.active_keys.append(Key)
            # print(self.active_keys)

            # if key is Key.cmd:
            #     # active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
            #     # print(active_app_name)
            #     self.command_status.emit(True)

        def on_release(key):
            try:
                current.remove(key)
            except KeyError:
                pass
            # self.active_keys.remove(Key)
            #
            # if key is Key.cmd:
            #     self.command_status.emit(False)

        # Collect events until released
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
