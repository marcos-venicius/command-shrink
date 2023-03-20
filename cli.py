#!/usr/bin/env python3

from os import path
from filemanager import FileManager

FILENAME = "settings.cli"
HOME_DIR = path.expanduser('~')

class Cli:
    def __init__(self, filemanager: FileManager):
        self.manager = filemanager

    def run(self):
        print('hello')

if __name__ == "__main__":
    filemanager = FileManager(HOME_DIR + "/", FILENAME)

    cli = Cli(filemanager)

    cli.run()
