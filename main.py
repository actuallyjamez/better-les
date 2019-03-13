# main.py
import os
import sys
from functools import partial

from PyQt5.QtCore import QThread, QPoint, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QSystemTrayIcon
from rumps import rumps
from yaml import load

import config as cf
from shortcuts.load_plugin import open_plugin
from workers import config_watcher, mouse_watcher


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def iterate(parent, data):
    for key, value in data.items():
        if isinstance(value, dict):
            new_menu = QMenu(parent)
            new_menu.setTitle(key)
            parent.addMenu(new_menu)
            iterate(new_menu, value)
        else:
            parent.addAction(key, partial(open_plugin, key, value.lower()))


class Tray(QWidget):
    # noinspection PyArgumentList
    def __init__(self):
        super().__init__()
        self.menu = QMenu()
        self.icon = QIcon(resource_path("assets/icon.png"))
        self.icon.setIsMask(True)
        self.tray = QSystemTrayIcon()
        self.menu_active = False
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.obj = config_watcher.Worker()
        self.thread = QThread()
        self.obj.update_config.connect(self.update_config)
        self.obj.moveToThread(self.thread)
        self.obj.finished.connect(self.thread.quit)
        self.thread.started.connect(self.obj.config_watcher)

        # self.obj2 = keyboard_watcher.Worker()
        # self.keyboard_watcher_thread = QThread()
        # self.obj2.command_status.connect(self.command_status)
        # self.obj2.moveToThread(self.keyboard_watcher_thread)
        # self.obj2.finished.connect(self.keyboard_watcher_thread.quit)
        # self.keyboard_watcher_thread.started.connect(self.obj2.keyboard_watcher)
        # self.keyboard_watcher_thread.finished.connect(app.exit)

        self.obj3 = mouse_watcher.Worker()
        self.mouse_watcher_thread = QThread()
        self.obj3.spawn_menu.connect(self.spawn_menu)
        self.obj3.moveToThread(self.mouse_watcher_thread)
        self.obj3.finished.connect(self.mouse_watcher_thread.quit)
        self.mouse_watcher_thread.started.connect(self.obj3.mouse_watcher)
        self.mouse_watcher_thread.finished.connect(app.exit)

        self.thread.start()
        # self.keyboard_watcher_thread.start()
        self.mouse_watcher_thread.start()

        self.init_ui()

    def init_ui(self):
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)
        self.rebuild_menu()
        # self.tray.activated.connect(self.on_systray_activated)

    # def on_systray_activated(self, i_activation_reason):
    #     self.menu.popup(QPoint(20, 20))

    def spawn_menu(self, x, y):
        pass
        # globals.command_pressed = i
        # command_pressed = i
        # print(x, y)
        self.menu.destroy()
        self.menu.popup(QPoint(x, y))

    def update_config(self):
        if self.rebuild_menu():
            rumps.notification(title='Better LES', message='Configuration Loaded', subtitle='', )

    def rebuild_menu(self):
        config = None
        success = True
        try:
            with open(cf.CONFIG_LOCATION_MENU) as f:
                config = load(f)
        except FileNotFoundError:
            cf.create_config()

            success = False
        except Exception as e:
            error_str = str(e).splitlines()

            rumps.notification(title='An error occurred while loading the configuration', message=error_str[1],
                               subtitle=error_str[2])
            success = False

        self.menu.clear()
        if success and config:
            iterate(self.menu, config)
        self.menu.addSeparator()
        options = QMenu(self.menu)
        options.setTitle('Options')
        options.addAction('Configure Menu', partial(os.system, f'open {cf.CONFIG_LOCATION_MENU}'))
        self.menu.addMenu(options)
        self.menu.addSeparator()
        # self.menu.addAction('New Update Available! (1.8.2)', partial(sys.exit))
        self.menu.addAction('Quit Better LES', partial(sys.exit))

        # Add the menu to the tray
        self.tray.setContextMenu(self.menu)
        # self.command_status()
        return success


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

form = Tray()

sys.exit(app.exec_())
