from terminals.terminal import Terminal

class Bashrc(Terminal):
    def __init__(self):
        super().__init__(".bashrc")

    def source(self) -> None:
        print(f"if your terminal not recognize the command execute: source ~/{self}")

