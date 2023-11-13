from os import path

class Terminal:
    def __init__(self, filename: str):
        self.userpath = path.expanduser('~')
        self.filename = filename
        self.fullpath = path.join(self.userpath, self.filename)

        self.__check_if_terminal_config_file_exists()

    def __check_if_terminal_config_file_exists(self):
        if not path.exists(self.fullpath):
            raise Exception(f'your terminal should consumes ~/{self} file.\nto solve it, make sure you have this file created and your terminal is reading it.')

    def __str__(self):
        return self.filename

    def __mount_line(self, alias: str, command: str) -> str:
        alias = alias.strip()
        command = command.replace('"', '\\"')

        return bytes(f'alias {alias}="{command}"\n'.encode('utf-8'))

    def __check_if_line_is_alias(self, line: str, alias: str) -> bool:
        line = line.strip()

        return (
            line
                .startswith('alias ') and
            line
                .replace('alias ', '')
                .strip()
                .replace(alias, '')
                .strip()
                .startswith('=')
        )

    def createalias(self, alias: str, command: str) -> None:
        line = self.__mount_line(alias, command)

        with open(self.fullpath, 'ab') as f:
            f.write(line)
            f.close()

    def removealias(self, alias: str):
        aliasname = alias.strip()

        lines = []

        with open(self.fullpath, 'rb') as f:
            lines = f.readlines()
            f.close()

        newlines = []

        for line in lines:
            line = line.decode('utf-8')

            if self.__check_if_line_is_alias(line, aliasname):
                continue

            newlines.append(line)

        text = bytes(''.join(newlines).encode('utf-8'))

        with open(self.fullpath, 'wb') as f:
            f.write(text)
            f.close()

    def has(self, alias: str) -> bool:
        with open(self.fullpath, 'rb') as f:
            lines = f.readlines()

            for line in lines:
                line = line.decode('utf-8').strip()

                if line.startswith('alias'):
                    line = line.replace('alias ', '')
                    linealias = line[:line.index('=')]

                    if linealias == alias:
                        return True

            f.close()

        return False

    def list(self):
        lines = []

        with open(self.fullpath, 'rb') as f:
            lines = f.readlines()
            f.close()

        aliases = []

        for line in lines:
            line = line.decode('utf-8').strip()

            if line.startswith('alias'):
                line = line.replace('alias ', '')

                alias = line[:line.index('=')]
                command = line[line.index('=') + 1:]
                
                aliases.append({
                    'alias': alias,
                    'command': command
                })

        return aliases

