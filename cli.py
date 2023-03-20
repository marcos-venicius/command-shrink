#!/usr/bin/env python3

from os import path
from sys import argv

from filemanager import FileManager
from help import HELP_TEXT
from terminals.bashrc import Bashrc

EXTENSION = '.shrink'
SHRINKNAME = 'shrink'
FILENAME = "settings" + EXTENSION
APPDIR = '.shrink/'
HOME_DIR = path.expanduser('~')

class Cli:
    def __init__(self, filemanager: FileManager, rcfile: Bashrc):
        self.args = argv[1:]
        self.configs = filemanager
        self.aliases = filemanager.readitems(SHRINKNAME)
        self.rcfile = rcfile
        self.options = {
            '-list': self.__list_available_shrinks,
            '-help': self.__show_help
        }

    def __str__(self):
        return HELP_TEXT

    def __show_help(self) -> None:
        print(self)

    def __list_available_shrinks(self) -> None:
        print('== SHRINKS ==')
        print()

        for key in self.aliases:
            value = self.aliases[key]
            key_show = key.ljust(20, '-').replace(key, f'{key} ')

            print(f'{key_show} {value}')

        print()

    def __get_alias_name(self) -> str:
        aliasname = None

        for idx in range(len(self.args)):
            if self.args[idx].strip() == '@' and idx > 0:
                aliasname = self.args[idx - 1]

        aliasname = aliasname.strip()

        if aliasname is None or len(aliasname) == 0:
            raise Exception(f'invalid arguments:\n\n== HELP ==\n {self}')

        if aliasname.startswith('-'):
            raise Exception(f'you cannot create aliases that starts with "-"')

        return aliasname

    def __get_command(self) -> str:
        args = self.args[2:]

        if len(args) == 0:
            raise Exception(f'invalid arguments:\n\n== HELP ==\n {self}')

        command = ' '.join(args).strip()

        if len(command) == 0:
            raise Exception(f'invalid arguments:\n\n== HELP ==\n {self}')

        return command

    def __execute_command(self) -> bool:
        if len(self.args) == 1 and self.args[0] in self.options:
            self.options[self.args[0]]()
            return True

        return False

    def run(self) -> None:
        self.configs.create_config_file_if_not_exists()

        if self.__execute_command():
            return

        if len(self.args) == 0:
            return self.__show_help()
    
        aliasname = self.__get_alias_name()

        if aliasname in self.aliases:
            print(f'[!] a shrink called "{aliasname}" already exists to command "{self.aliases[aliasname]}"')
            exit(1)

        if self.rcfile.aliasexists(aliasname):
            raise Exception(f'your {self.rcfile} already has an alias called "{aliasname}"')

        command = self.__get_command()

        print(f'[*] creating shrink called "{aliasname}" to command "{command}"')

        try:
            self.configs.writeitem(SHRINKNAME, aliasname, command)
            self.rcfile.createalias(aliasname, command)
            self.rcfile.source()
        except Exception as e:
            print(f'[!] cannot write the shrink\n  |\n  |\n  {e}')
            exit(1)

        print(f'[+] shrink "{aliasname}" created successfully')

if __name__ == "__main__":
    filemanager = FileManager(HOME_DIR, FILENAME, APPDIR)
    bashrc = Bashrc()

    cli = Cli(filemanager, bashrc)

    try:
        cli.run()
    except Exception as e:
        print(f'[!] {e}')
        exit(1)
