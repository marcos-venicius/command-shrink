#!/usr/bin/env python3

from os import path,environ
from sys import argv

from filemanager import FileManager
from aliasmanager import AliasManager
from help import HELP_TEXT

from terminals.bashrc import Bashrc
from terminals.zshrc import Zshrc
from terminals.terminal import Terminal

class Cli:
    def __init__(self, aliasmanager: AliasManager, terminal: Terminal):
        self.programname = 'shrink'
        self.args = argv[1:]
        self.aliasmanager = aliasmanager
        self.terminal = terminal
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

            if self.aliasmanager.has(arg):
                self.aliasmanager.delete(arg)
                self.terminal.deletealias(arg)
                deleted += 1
            else:
                print(f'[!] shrink {arg} does not exists')

        if deleted > 0:
            print(f'[+] {deleted} shrinks deleted successfully')

            self.terminal.source()

    def __show_help_command(self) -> None:
        print(str(self).replace('@programname', self.programname))

    def __list_available_shrinks_command(self) -> None:
        print('== SHRINKS ==')
        print()

        if self.aliasmanager.is_empty():
            print('has no shrinks created')

        self.aliasmanager.display()

    def __get_alias_name(self) -> str:
        aliasname = None

        for idx in range(len(self.args)):
            if self.args[idx].strip() == '@' and idx > 0:
                aliasname = self.args[idx - 1].strip()

        if aliasname is None or aliasname == '':
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
        if self.__execute_command():
            return

        if len(self.args) == 0:
            return self.__show_help_command()

        aliasname = self.__get_alias_name()

        if self.aliasmanager.has(aliasname):
            print(f'[!] a shrink called "{aliasname}" already exists to command "{self.aliasmanager.get(aliasname)}"')
            exit(1)

        if self.aliasmanager.has(aliasname):
            raise Exception(f'your {self.terminal} already has an alias called "{aliasname}"')

        command = self.__get_command()

        print(f'[*] creating shrink called "{aliasname}" to command "{command}"')

        try:
            self.aliasmanager.create(aliasname, command)
            self.terminal.createalias(aliasname, command)
            self.terminal.source()
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
        rcfile = terminals[terminal]()

        filemanager = FileManager(str(terminal))
        aliasmanager = AliasManager(filemanager)

        cli = Cli(aliasmanager, rcfile)

        cli.run()
    else:
        raise Exception("we don't have support to this terminal")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'[!] {e}')
        exit(1)
