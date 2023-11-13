#!/usr/bin/env python3

from core.arg_parser import ArgParser
from core.terminals.loader import Loader

def list(terminal):
    aliases = terminal.list()

    for item in aliases:
        alias = item['alias']
        command = item['command']

        if command.startswith('"') and command.endswith('"'):
            command = command[1:-1]

        print(f'{alias}\t\t{command}')

def add(terminal, alias, command):
    if terminal.has(alias):
        print('This alias already exists')
        exit(1)
    else:
        terminal.createalias(alias, command)

def remove(terminal, alias):
    if terminal.has(alias):
        terminal.removealias(alias)
    else:
        print('This alias does not exists')
        exit(1)

def main():
    arg_parser = ArgParser()

    args = arg_parser.parse()

    if args is None: return

    loader = Loader()

    terminal = loader.load()

    if terminal is None:
        print('Invalid terminal')
        exit(1)

    if args['action'] == 'list':
        list(terminal)
    elif args['action'] == 'add':
        add(terminal, args['arguments']['alias'], args['arguments']['command'])
    elif args['action'] == 'remove':
        remove(terminal, args['arguments']['alias'])

if __name__ == "__main__":
    main()
