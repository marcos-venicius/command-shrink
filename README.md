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

## Options

- `-list` list all available shrinks created
- `-help` show menu help
