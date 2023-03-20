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
        self.configs = filemanager
        self.aliases = filemanager.readitems('alias')

    def __str__(self):
        return HELP_TEXT

    def __get_alias_name(self) -> str:
        aliasname = None

        for idx in range(len(self.args)):
            if self.args[idx].strip() == '@' and idx > 0:
                aliasname = self.args[idx - 1]

        aliasname = aliasname.strip()

        if aliasname is None or len(aliasname) == 0:
            raise Exception(f'invalid arguments:\n\n== HELP ==\n {self}')

        return aliasname

    def __get_command(self) -> str:
        args = self.args[2:]

        if len(args) == 0:
            raise Exception(f'invalid arguments:\n\n== HELP ==\n {self}')

        command = ' '.join(args).strip()

        if len(command) == 0:
            raise Exception(f'invalid arguments:\n\n== HELP ==\n {self}')

        return command

    def run(self) -> None:
        self.configs.create_config_file_if_not_exists()

        if len(self.args) == 0:
            return print(self)
    
        aliasname = self.__get_alias_name()

        if aliasname in self.aliases:
            print(f'[!] a shrink called "{aliasname}" already exists to command "{self.aliases[aliasname]}"')
            exit(1)

        command = self.__get_command()

        print(f'[*] creating shrink called "{aliasname}" to command "{command}"')

        try:
            self.configs.writeitem('alias', aliasname, command)
        except Exception as e:
            print(f'[!] cannot write the shrink\n  |\n  |\n  {e}')
            exit(1)

        print(f'[+] shrink "{aliasname}" created successfully')

if __name__ == "__main__":
    filemanager = FileManager(HOME_DIR + "/", FILENAME, APPDIR)

    cli = Cli(filemanager)

    try:
        cli.run()
    except Exception as e:
        print(e)
        exit(1)
