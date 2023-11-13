import os

from core.terminals.bash import Bash
from core.terminals.zsh import Zsh

class Loader:
    def __init__(self):
        self.terminals = {
            'bash': Bash,
            'zsh': Zsh
        }

    def load(self):
        terminal = os.environ['SHRINK_TERMINAL'] or 'bash'

        if terminal in self.terminals:
            return self.terminals[terminal]()
        
        return None

