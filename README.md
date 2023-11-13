# Command Shrink

many times we have to use large commands.

This is ok, but when this usage is often, it could be anoying.

To solve this problem i'm writing this cli.

## How it works

basically you can create a "shrink command" to any command that you have on linux

how can i create a new shrink?

```bash
shrink -a <shrink_name> <command>
```

this is the basic syntax.

for example, if you want to make the command `all` to list all files in current directory instead of `ls -la`, you could:

```bash
shrink -a all "ls -la"
```

and done.

when you execute `all` in your terminal, the command `ls -la` will be executed.

## Benefits

All right. you could be thinking: "Just use the bash alias".

But, is not that simple.

if you are working on a project and needs to execute a large command to up a docker container for example.

how anoying is to open the bash, create an alias manually, go back to the terminal, source the current session.
if the command is wrong? do it again!
want to remove? do it again!
want to update? do it again!

with the cli you will be able to do this operations by a single command.

## Installing

Bash:

```bash
cd ~ && echo "export SHRINK_TERMINAL=bash" >> ~/.bashrc && mkdir .shrink && cd .shrink && git clone https://github.com/marcos-venicius/command-shrink.git sk && echo 'sk() { ~/.shrink/sk/main.py "$@"; exec bash; }' >> ~/.bashrc && cd ~ && exec bash
```

Zsh:

```bash
cd ~ && echo "export SHRINK_TERMINAL=zsh" >> ~/.zshrc && mkdir .shrink && cd .shrink && git clone https://github.com/marcos-venicius/command-shrink.git sk && echo 'sk() { ~/.shrink/sk/main.py "$@"; exec zsh; }' >> ~/.zshrc && cd ~ && exec zsh
```

# Help

```console
usage: Shrink [-h] [--add] [--list] [--remove] [alias] [command]

Shrink your large commands

positional arguments:
  alias         Alias name (numbers, letters, underlines)
  command       Command to shrink

options:
  -h, --help    show this help message and exit
  --add, -a     Add a new alias
  --list, -l    List all aliases
  --remove, -r  Remove an alias

sk cm 'git commit -m'
```
