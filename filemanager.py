import json
from os import path, mkdir

EXTENSION = '.json'
SHRINKNAME = 'shrink'
FILENAME = f'settings{EXTENSION}'
APPDIR = '.shrink/'
HOME_DIR = path.expanduser('~')

class FileManager:
    def __init__(self, root: str):
        self.root = root 
        self.basepath = HOME_DIR
        self.filename = FILENAME
        self.foldername = APPDIR
        self.fullpath = path.join(self.basepath, self.foldername, self.filename)

        self.__setup()

    def load(self) -> dict[str, str]:
        data = self.__load()

        if self.root in data:
            return data[self.root]

        return {}

    def set(self, key: str, value: str) -> None:
        with open(self.fullpath, 'r+') as f:
            data = json.loads(f.read())

            if self.root not in data:
                data[self.root] = {}

            data[self.root][key] = value

            json_string = json.dumps(data)

            f.seek(0)
            f.write(json_string)
            f.close()

    def get(self, key: str) -> str | None:
        data = {}

        with open(self.fullpath, 'rb') as f:
            data = json.loads(f.read())
            f.close()

        if self.root not in data:
            return None

        if key not in data[self.root]:
            return None

        return data[self.root][key]

    def remove(self, key: str) -> None:
        data = self.__load()

        if self.root not in data:
            return

        if key not in data[self.root]:
            return

        del data[self.root][key]

        json_string = json.dumps(data)

        with open(self.fullpath, 'w') as f:
            f.seek(0)
            f.write(json_string)
            f.close()

    def __setup(self):
        self.__create_config_file_if_not_exists()

    def __create_config_file_if_not_exists(self) -> None:
        folderpath = path.join(self.basepath, self.foldername)

        folderexists = path.exists(folderpath) and path.isdir(folderpath)
        fileexits = path.exists(self.fullpath) and path.isfile(self.fullpath)

        if not folderexists:
            mkdir(folderpath)

        if not fileexits:
            data = {}
            data[self.root] = {}

            json_string = json.dumps(data)

            with open(self.fullpath, 'w') as f:
                f.write(json_string)
                f.close()


    def __load(self):
        data = {}

        with open(self.fullpath, 'r') as f:
            data = json.loads(f.read())
            f.close()

        return data
