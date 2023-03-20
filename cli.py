#!/usr/bin/env python3

from os import path
from sys import argv

from filemanager import FileManager
from help import HELP_TEXT

FILENAME = "settings.cli"
APPDIR = '.shrink/'
HOME_DIR = path.expanduser('~')

class Cli:
    def __init__(self, filemanager: FileManager):
        self.args = argv[1:]
        self.manager = filemanager

    def __str__(self):
        return HELP_TEXT

    def run(self):
        if len(self.args) == 0:
            print(self)

if __name__ == "__main__":
    filemanager = FileManager(HOME_DIR + "/", FILENAME, APPDIR)

    cli = Cli(filemanager)

    cli.run()
