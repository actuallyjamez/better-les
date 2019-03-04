from pathlib import Path

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from watchgod import watch

import config


class Worker(QObject):
    finished = pyqtSignal()
    update_config = pyqtSignal()

    @pyqtSlot(name='config_watcher')
    def config_watcher(self):  # A slot takes no params
        home = str(Path.home())
        for changes in watch(config.CONFIG_DIRECTORY):
            for status, location in changes:
                if location == config.CONFIG_LOCATION_MENU:
                    self.update_config.emit()

        self.finished.emit()
