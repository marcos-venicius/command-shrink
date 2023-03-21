import subprocess
from os import path

class Bashrc:
    def __init__(self):
        self.userpath = path.expanduser('~')
        self.filename = ".bashrc"
        self.fullpath = path.join(self.userpath, self.filename)

        self.__check_if_exists()

    def __str__(self):
        return ".bashrc"

    def __check_if_exists(self) -> None:
        if not path.exists(self.fullpath):
            raise Exception(f'your terminal should consumes ~/{self} file.\nto solve it, make sure you have this file created and your terminal is reading it.')

    def __check_if_has_alias_on_line(self, line: str, aliasname: str) -> bool:
        line = line.strip()

        if line.startswith('alias '):
            has_alias = line.replace('alias ', '').strip().replace(aliasname, '').strip().startswith('=')

            if has_alias:
                return True

        return False


    def aliasexists(self, aliasname: str) -> bool:
        lines = []

        with open(self.fullpath, 'rb') as f:
            lines = f.readlines()
            f.close()

        for line in lines:
            line = line.decode('utf-8')
            line = line.strip()

            if line.startswith('alias'):
                line = line.replace('alias ', '')
                alias = line[:line.index('=')]

                if aliasname == alias:
                    return True

        return False

    def createalias(self, name: str, command: str) -> None:
        text = f'alias {name}="{command}"'.encode('utf-8')

        with open(self.fullpath, 'ab') as f:
            f.write(bytes(text))
            f.write(b'\n')
            f.close()

    def deletealias(self, aliasname: str) -> None:
        aliasname = aliasname.strip()

        lines = []

        with open(self.fullpath, 'rb') as f:
            lines = f.read().splitlines()
            f.close()

        newlines = []

        for line in lines:
            line = line.decode('utf-8')

            if self.__check_if_has_alias_on_line(line, aliasname):
                continue

            # TODO: check if have more than one command on line
            # if has, remove only the alias command and keep the other commands

            newlines.append(line)

        text = '\n'.join(newlines).encode('utf-8')

        with open(self.fullpath, 'wb') as f:
            f.write(text)
            f.close()

    def source(self) -> None:
        print()
        print('PLEASE, SYNC YOUR CONFIGS: ')
        print()
        print(f'source {self.fullpath}')
        print()
