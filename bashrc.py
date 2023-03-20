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
            raise Exception('your terminal should consumes ~/.bashrc file.\nto solve it, make sure you have this file created and your terminal is reading it.')

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

    def createalias(self):
        pass

