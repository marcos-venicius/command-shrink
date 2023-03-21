## Command Shrink

many times we have to use large commands.

This is ok, but when this usage is often, it could be anoying.


To solve this problem i'm writing this cli.


## How it works

basically you can create a "shrink command" to any command that you have on linux


how can i create a new shrink?


```bash
./cli.py <shrink_name> @ <command>
```

this is the basic syntax.

for example, if you want to make the command `all` to list all files in current directory instead of `ls -la`, you could:

```bash
./cli.py all @ ls -la
```

and done.

when you execute `all` in your terminal, the command `ls -la` will be executed.

## Configuring

to configure this cli:

- open your `~/.bashrc`
- add the line `shrink() { ~/path/to/project/folder/cli.py "$@"; exec bash; }` to the bottom of the file
- execute `source ~/.bashrc`
- now, you can execute `shrink -help`

## -help

```console
Author:     Marcos Venicius @ https://github.com/marcos-venicius
Project:    https://github.com/marcos-venicius/command-shrink

== SHRINK CLI PROGRAM ==

  you can use the "@" to create a new shrink

  like:
    
    $ ./cli.py <shrink> @ <command>

  example:

    $ ./cli.py all @ ls -la

  with this command you will have access to the "all" command on your terminal
  that will execute "ls -la"


  -help             show this help message
  -list             list all available shrinks

  -remove           remove a shrink
                    example:
                        -remove shrink1 shrink2 shrink3
```
