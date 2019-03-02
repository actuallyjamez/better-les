from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from pynput import mouse
from pynput.mouse import Button


class Worker(QObject):
    finished = pyqtSignal()
    update_mouse = pyqtSignal(int, int)

    @pyqtSlot(name='mouse_watcher')
    def mouse_watcher(self):
        def on_move(self, x, y):
            print('Pointer moved to {0}'.format(
                (x, y)))

        def on_click(x, y, button, pressed):

            if button == Button.right and pressed is False:
                self.update_mouse.emit(x, y)
            # print('{0} at {1}'.format(
            #     'Pressed' if pressed else 'Released',
            #     (x, y)))

        def on_scroll(x, y, dx, dy):
            print('Scrolled {0} at {1}'.format(
                'down' if dy < 0 else 'up',
                (x, y)))

        with mouse.Listener(
                # on_move=on_move,
                on_click=on_click
                # on_scroll=on_scroll
        ) as listener:
            listener.join()
        self.finished.emit()
