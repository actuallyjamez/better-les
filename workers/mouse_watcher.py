import sys
import time

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from pynput import mouse
from pynput.mouse import Button

if sys.platform == 'darwin':
    from AppKit import NSWorkspace


class Worker(QObject):
    finished = pyqtSignal()
    update_mouse = pyqtSignal(int, int)
    spawn_menu = pyqtSignal(int, int)
    last_click = time.time()

    @pyqtSlot(name='mouse_watcher')
    def mouse_watcher(self):
        def register_click(x, y, button, pressed):
            #
            # if button == Button.right and pressed is False:
            #     self.update_mouse.emit(x, y)
            # # print('{0} at {1}'.format(
            # #     'Pressed' if pressed else 'Released',
            # #     (x, y)))
            # print(time.time() - self.last_click)
            if button == Button.right and not pressed:
                if time.time() - self.last_click < 0.25:
                    # print('double click!')
                    if NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] == 'Live':
                        self.spawn_menu.emit(x, y)
                # else:

                # print('not double click!')
                self.last_click = time.time()

        def on_scroll(x, y, dx, dy):
            print('Scrolled {0} at {1}'.format(
                'down' if dy < 0 else 'up',
                (x, y)))

        with mouse.Listener(
                on_click=register_click
        ) as listener:
            listener.join()
        self.finished.emit()
