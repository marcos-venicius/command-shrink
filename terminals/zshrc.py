from terminals.terminal import Terminal

class Zshrc(Terminal):
    def __init__(self):
        super().__init__(".zshrc")

    def source(self) -> None:
        print(f"if your terminal not recognize the command execute: source ~/{self}")
