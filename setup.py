"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = [('assets', ['assets/icon.png'])]
OPTIONS = {'plist': {'LSUIElement': '1',
                     'CFBundleShortVersionString': '0.0.1'},
           'iconfile': 'assets/icon.icns',
           }

setup(
    app=APP,
    data_files=DATA_FILES,
    name='Better LES',
    version='0.0.1',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    author='actuallyjamez',
    author_email='actuallyjamez@gmail.com',
    description='LES but better',
    install_requires=['PyYAML', 'rumps', 'PyQt5', 'watchgod', 'pynput', 'py2app']
)