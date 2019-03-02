# main.py
import json
import sys
from functools import partial
from json import JSONDecodeError

from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QSystemTrayIcon
from rumps import rumps

import worker
from load_plugin import open_plugin


def iterate(parent, data):
    for key, value in data.items():
        if isinstance(value, dict):
            new_menu = QMenu(parent)
            new_menu.setTitle(key)
            parent.addMenu(new_menu)
            iterate(new_menu, value)
        else:
            parent.addAction(key, partial(open_plugin, value.lower()))


class Tray(QWidget):

    # noinspection PyArgumentList
    def __init__(self):
        super().__init__()
        self.menu = QMenu()
        self.icon = QIcon("assets/icon.png")
        self.tray = QSystemTrayIcon()

        self.obj = worker.Worker()
        self.thread = QThread()
        self.obj.update_config.connect(self.update_config)
        self.obj.moveToThread(self.thread)
        self.obj.finished.connect(self.thread.quit)
        self.thread.started.connect(self.obj.config_watcher)
        # self.thread.finished.connect(app.exit)

        self.thread.start()

        self.init_ui()

    def init_ui(self):

        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)
        self.rebuild_menu()

    def update_config(self):
        if self.rebuild_menu():
            rumps.notification(title='Better LES', message='Configuration Reloaded', subtitle='')

    def rebuild_menu(self):
        config = None
        success = True
        try:
            with open('config.json') as f:
                config = json.load(f)
        except JSONDecodeError as e:

            print(e)
            error, location = str(e).split(':')
            rumps.notification(title='An error occurred while loading the configuration', message=location,
                               subtitle=error)
            success = False
        self.menu.clear()
        iterate(self.menu, config)
        self.menu.addSeparator()
        self.menu.addAction('Quit Better LES', partial(exit))

        # Add the menu to the tray
        self.tray.setContextMenu(self.menu)
        return success


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

form = Tray()

sys.exit(app.exec_())
