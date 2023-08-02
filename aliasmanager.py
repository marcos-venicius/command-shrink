from filemanager import FileManager

class AliasManager:
    def __init__(self, filemanager: FileManager) -> None:
        self.filemanager = filemanager

    def create(self, alias: str, command: str) -> None:
        self.filemanager.set(alias, command)

    def delete(self, alias) -> None:
        self.filemanager.remove(alias)

    def has(self, alias: str) -> bool:
        aliases = self.filemanager.load()

        return alias in aliases

    def get(self, alias: str) -> str | None:
        return self.filemanager.get(alias)

    def is_empty(self) -> bool:
        aliases = self.filemanager.load()

        return len(aliases.keys()) == 0

    def display(self) -> None:
        aliases = self.filemanager.load()

        for alias in aliases:
            value = aliases[alias]
            alias = alias.ljust(20, '-').replace(alias, f'{alias} ')

            print(f'{alias} {value}')

        print()

