from core.terminals.terminal import Terminal

class Zsh(Terminal):
    def __init__(self):
        super().__init__('.zshrc')
