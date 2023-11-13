import argparse
import re

class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='Shrink',
            description='Shrink your large commands',
            epilog="sk cm 'git commit -m'"
        )
        self.__add_args()

    def __validate_alias(self, value):
        if not re.match('^[a-zA-Z0-9_]+$', value):
            raise argparse.ArgumentTypeError('Alias has an invalid format')

        return value

    def __add_args(self):
        self.parser.add_argument('--add', '-a', help='Add a new alias', action='store_true')
        self.parser.add_argument('--list', '-l', help='List all aliases', action='store_true')
        self.parser.add_argument('--remove', '-r', help='Remove an alias', action='store_true')
        self.parser.add_argument('alias', nargs='?', type=self.__validate_alias, help='Alias name (numbers, letters, underlines)')
        self.parser.add_argument('command', nargs='?', help='Command to shrink')

    def parse(self):
        args = self.parser.parse_args()

        if args.add:
            if not args.alias or not args.command:
                self.parser.error('when using the flag --add, you need to pass the "alias" and the "command"')
            else:
                return {
                    'action': 'add',
                    'arguments': {
                        'alias': args.alias,
                        'command': args.command
                    }
                }
        elif args.list:
            return {
                'action': 'list'
            }
        elif args.remove:
            if not args.alias:
                self.parser.error('when using the flat --remove, you need to pass the "alias" name')
            else:
                return {
                    'action': 'remove',
                    'arguments': {
                        'alias': args.alias
                    }
                }

        self.parser.print_help()

        return None

