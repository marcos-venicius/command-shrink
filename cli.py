#!/usr/bin/env python3

from os import path,environ
from sys import argv

from filemanager import FileManager
from help import HELP_TEXT

from terminals.bashrc import Bashrc
from terminals.zshrc import Zshrc
from terminals.terminal import Terminal

EXTENSION = '.shrink'
SHRINKNAME = 'shrink'
FILENAME = "settings" + EXTENSION
APPDIR = '.shrink/'
HOME_DIR = path.expanduser('~')

class Cli:
    def __init__(self, filemanager: FileManager, rcfile: Terminal):
        self.programname = 'shrink'
        self.args = argv[1:]
        self.configs = filemanager
        self.aliases = filemanager.readitems(SHRINKNAME)
        self.rcfile = rcfile
        self.options = {
            '-list': lambda args = []: self.__list_available_shrinks_command(),
            '-help': lambda args = []: self.__show_help_command(),
            '-remove': lambda args = []: self.__remove_shrink_command(args)
        }

    def __str__(self):
        return HELP_TEXT

    def __remove_shrink_command(self, args: list[str] = []) -> None:
        args = list(set(args))

        if len(args) == 0:
            raise Exception('missing shrink name\n  |\n  use -help to see how to use')

        deleted = 0

        for arg in args:
            arg = arg.strip()

            if arg in self.aliases:
                self.configs.removeitem(SHRINKNAME, arg)
                self.rcfile.deletealias(arg)
                deleted += 1
            else:
                print(f'[!] shrink {arg} does not exists')

        if deleted > 0:
            print(f'[+] {deleted} shrinks deleted successfully')

            self.rcfile.source()

    def __show_help_command(self) -> None:
        print(str(self).replace('@programname', self.programname))

    def __list_available_shrinks_command(self) -> None:
        print('== SHRINKS ==')
        print()

        if len(self.aliases.keys()) == 0:
            print('has no shrinks created')

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
        if len(self.args) >= 1 and self.args[0] in self.options:
            args = []

            if len(self.args) > 1:
                args = self.args[1:]

            self.options[self.args[0]](args=args)
            return True

        return False

    def run(self) -> None:
        self.configs.create_config_file_if_not_exists()

        if self.__execute_command():
            return

        if len(self.args) == 0:
            return self.__show_help_command()
    
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

def main():
    terminal = environ.get("SHRINK_TERMINAL")

    terminals = {
        'bash': Bashrc,
        'zsh': Zshrc
    }

    if terminal in terminals:
        filemanager = FileManager(HOME_DIR, FILENAME, APPDIR, terminal)

        rcfile = terminals[terminal]()

        cli = Cli(filemanager, rcfile)

        cli.run()
    else:
        raise Exception("we don't have support to this terminal")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'[!] {e}')
        exit(1)
