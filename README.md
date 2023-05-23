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

## What is the benefits?

All right. you could be thinking: "Just use the bash alias".

But, is not too simple.

if you are working on a project and needs to execute a large command to up a docker container for example.

how anoying is to open the bash, create an alias manually, go back to the terminal, source the current session.
if the command is wrong? do it again!
want to remove? do it again!
want to update? do it again!

with the cli you will be able to do this operations by a single command.

**But, I want to save my aliases.**

Ok, you **can**!

just save the file `~/.shrink/settings.shrink`.

if you access another computer, just paste the content of this file on your machine and execute `shrink -sync`.

and, that is it! all done!

**The `-sync` option is not ready yet**

## Installing on bash

execute the command bellow to install the cli

```bash
cd ~ && echo "export SHRINK_TERMINAL=bash" >> ~/.bashrc && mkdir .shrink && cd .shrink && git clone https://github.com/marcos-venicius/command-shrink.git shrink && echo 'shrink() { ~/.shrink/shrink/cli.py "$@"; exec bash; }' >> ~/.bashrc && cd ~ && SHRINK_TERMINAL=bash shrink -help
```

## Installing on zsh

execute the command bellow to install the cli

```bash
cd ~ && echo "export SHRINK_TERMINAL=zsh" >> ~/.zshrc && mkdir .shrink && cd .shrink && git clone https://github.com/marcos-venicius/command-shrink.git shrink && echo 'shrink() { ~/.shrink/shrink/cli.py "$@"; exec zsh; }' >> ~/.zshrc && cd ~ && SHRINK_TERMINAL=zsh shrink -help
```

## -help

```console
Author:     Marcos Venicius @ https://github.com/marcos-venicius
Project:    https://github.com/marcos-venicius/command-shrink

== SHRINK CLI PROGRAM ==

  you can use the "@" to create a new shrink

  like:

    $ shrink <shrink> @ <command>

  example:

    $ shrink all @ ls -la

  with this command you will have access to the "all" command on your terminal
  that will execute "ls -la"


  -help             show this help message
  -list             list all available shrinks

  -remove           remove a shrink
                    example:
                        -remove shrink1 shrink2 shrink3
```
