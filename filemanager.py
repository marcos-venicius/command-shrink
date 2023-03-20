from os import path

class FileManager:
    def __init__(self, basepath: str, filename: str):
        self.basepath = basepath
        self.filename = filename
        self.fullpath = basepath + filename

        self.__create_if_not_exists()

    def __create_if_not_exists(self) -> None:
        if path.exists(self.fullpath) and path.isfile(self.fullpath):
            return None

        with open(self.fullpath, 'w') as f:
            f.close()

    def writeitem(self, typ: str, key: str, value: str):
        key = key.strip()
        typ = typ.strip()

        item = f'@{typ} {key}={value}'

        with open(self.fullpath, 'wb') as f:
            f.write(bytes(item))
            f.close()
