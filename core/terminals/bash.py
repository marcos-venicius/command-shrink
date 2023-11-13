from core.terminals.terminal import Terminal

class Bash(Terminal):
    def __init__(self):
        super().__init__('.bashrc')
