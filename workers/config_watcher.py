import time

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from watchgod import watch



class Worker(QObject):
    finished = pyqtSignal()
    update_config = pyqtSignal()

    @pyqtSlot(name='config_watcher')
    def config_watcher(self):  # A slot takes no params
        for changes in watch('./'):
            for status, location in changes:
                if location == './config.json':
                    self.update_config.emit()

        self.finished.emit()
