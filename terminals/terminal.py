from os import path

class Terminal:
    def __init__(self, filename: str):
        self.userpath = path.expanduser('~')
        self.filename = filename
        self.fullpath = path.join(self.userpath, self.filename)

        self.__check_if_terminal_config_file_exists()

    def check_if_alias_exists(self, aliasname: str) -> bool:
        lines = []

        with open(self.fullpath, 'rb') as f:
            lines = f.readlines()
            f.close()

        for line in lines:
            line = line.decode('utf-8').strip()

            if line.startswith('alias'):
                line = line.replace('alias ', '')
                alias = line[:line.index('=')]

                if aliasname == alias:
                    return True

        return False

    def createalias(self, name: str, command: str) -> None:
        text = f'alias {name}="{command}"'.encode('utf-8')

        with open(self.fullpath, 'ab') as f:
            f.write(b'\n')
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

            if self.__check_if_line_is_alias(line, aliasname):
                continue

            # TODO: check if have more than one command on line
            # if has, remove only the alias command and keep the other commands

            newlines.append(line)

        text = '\n'.join(newlines).encode('utf-8')

        with open(self.fullpath, 'wb') as f:
            f.write(text)
            f.close()

    def __str__(self):
        return self.filename

    def __check_if_terminal_config_file_exists(self) -> None:
        if not path.exists(self.fullpath):
            raise Exception(f'your terminal should consumes ~/{self} file.\nto solve it, make sure you have this file created and your terminal is reading it.')

    def __check_if_line_is_alias(self, line: str, aliasname: str) -> bool:
        line = line.strip()

        return (
            line
                .startswith('alias ') and
            line
                .replace('alias ', '')
                .strip()
                .replace(aliasname, '')
                .strip()
                .startswith('=')
        )
