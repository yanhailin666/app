"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['login.py']
OPTIONS = { 'includes': ['sip', 'PyQt5.QtCore', 'PyQt5.QtWidgets'],}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
pip3 install PyQt5 -i http://pypi.douban.com/simple/