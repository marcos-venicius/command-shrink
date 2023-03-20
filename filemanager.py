from os import path, mkdir

class FileManager:
    def __init__(self, basepath: str, filename: str, foldername: str):
        self.basepath = basepath
        self.filename = filename
        self.foldername = foldername
        self.fullpath = path.join(basepath, foldername, filename)

        self.__create_if_not_exists()

    def __create_if_not_exists(self) -> None:
        folderpath = path.join(self.basepath, self.foldername)

        folderexists = path.exists(folderpath) and path.isdir(folderpath)
        fileexits = path.exists(self.fullpath) and path.isfile(self.fullpath)

        if not folderexists:
            mkdir(folderpath)

        if not fileexits:
            with open(self.fullpath, 'w') as f:
                f.close()

    def writeitem(self, typ: str, key: str, value: str):
        key = key.strip()
        typ = typ.strip()

        item = bytes(f'@{typ} {key}={value}')

        with open(self.fullpath, 'wb') as f:
            f.write(item)
            f.close()
