---
Title: Bash
Date: 2024-06-23
Category: linux
Tags: manjaro, linux, command line
Status: published
Slug: bash
Summary: An overview of bash.
---

Bash (**B**ourne **A**gain **SH**ell) is the usual shell used in Linux distributions.  Here are some useful commands.

# Inspecting Files
```shell
# Show the first 10 lines of a file.
head file.txt
# Show the last 4 lines of a file.
tail -4 file.txt
# Just show the 11th line
head -11 file.txt | tail -1
```

# Listing Files or Directories by Date of Modification
```shell
# Newest last
ls --sort=time
# Oldest last
ls -r --sort=time
```

# Searching man Pages
```shell
# Returns programs whose man pages contain the search phrase.
apropos "search phrase"
```

# Create or Modify Environment Variables
```shell
# Includes example prompt (~ $) for clarity
# Create the environment variable 'myvariable'
~ $ export myvariable='myvalue'
~ $ echo $myvariable
myvalue
# List all currently active environment variables
~ $ env
```

# Show recent command history
```shell
history
```

# External
[Manjaro Wiki: Useful Bash Functions and Aliases](https://forum.manjaro.org/t/tip-useful-bash-functions-and-aliases/90305)
