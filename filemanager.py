from os import path, mkdir

class FileManager:
    def __init__(self, basepath: str, filename: str, foldername: str):
        self.basepath = basepath
        self.filename = filename
        self.foldername = foldername
        self.fullpath = path.join(basepath, foldername, filename)

    def create_config_file_if_not_exists(self) -> None:
        folderpath = path.join(self.basepath, self.foldername)

        folderexists = path.exists(folderpath) and path.isdir(folderpath)
        fileexits = path.exists(self.fullpath) and path.isfile(self.fullpath)

        if not folderexists:
            mkdir(folderpath)

        if not fileexits:
            with open(self.fullpath, 'w') as f:
                f.close()
    
    def __extract_key(self, typ: str, line: str) -> str:
        text = line.replace(f'@{typ} ', '')

        equalIndex = text.index('=')

        return text[:equalIndex].strip()

    def __extract_value(self, line: str) -> str:
        equalIndex = line.index('=')

        return line[equalIndex + 1:].replace('\n', '')

    def readitems(self, typ: str) -> dict[str, str]:
        items = {}

        lines = []

        with open(self.fullpath, 'rb') as f:
            lines = f.readlines()
            f.close()

        for line in lines:
            line = line.decode('utf-8')
            if line.strip().startswith(f'@{typ} '):
                key = self.__extract_key(typ, line)
                value = self.__extract_value(line)

                items[key] = value

        return items

    def writeitem(self, typ: str, key: str, value: str) -> None:
        key = key.strip()
        typ = typ.strip()

        item = f'@{typ} {key}={value}'.encode('utf-8')

        with open(self.fullpath, 'ab') as f:
            f.write(bytes(item))
            f.write(b'\n')
            f.close()
