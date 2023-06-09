from os import path, mkdir

class FileManager:
    def __init__(self, basepath: str, filename: str, foldername: str, basekey: str = None):
        self.basekey = basekey
        self.basepath = basepath
        self.filename = filename
        self.foldername = foldername
        self.fullpath = path.join(basepath, foldername, filename)

        self.__setup()

    def __setup(self):
        self.create_config_file_if_not_exists()

    def __key(self, key: str):
        if self.basekey is not None:
            return f"{self.basekey}__{key}"

        return key

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
                
                if self.basekey is not None and not str(key).startswith(f"{self.basekey}__"):
                    continue

                value = self.__extract_value(line)

                items[key.replace(f"{self.basekey}__", "")] = value

        return items

    def writeitem(self, typ: str, key: str, value: str) -> None:
        key = self.__key(key.strip())
        typ = typ.strip()

        item = f'@{typ} {key}={value}'.encode('utf-8')

        with open(self.fullpath, 'ab') as f:
            f.write(bytes(item))
            f.write(b'\n')
            f.close()

    def removeitem(self, typ: str, key: str) -> None:
        typ = typ.strip()
        key = self.__key(key.strip())

        lines = []

        with open(self.fullpath, 'rb') as f:
            lines = f.read().splitlines()
            f.close()

        newlines = []

        typ_enc = bytes(f'@{typ}'.encode('utf-8'))

        for line in lines:
            if line.strip().startswith(typ_enc):
                linekey = self.__extract_key(typ, line.decode('utf-8'))

                if linekey == key:
                    continue

            newlines.append(line.decode('utf-8'))

        text = bytes('\n'.join(newlines).encode('utf-8'))

        with open(self.fullpath, 'wb') as f:
            f.write(text)
            f.close()

