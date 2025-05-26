---
Title: Grimoire
Date: 2022-09-10
Category: linux
Tags: linux, command line
Status: published
Slug: grimoire
Summary: Some useful Linux commands.
Image: grimoire.png
Caption: And the mome raths outgrabe.
---

> Any sufficiently advanced use of the command line is indistinguishable from magic.
>
> <footer>--Arthur C. Clarke</footer>

This page serves as my tome of useful Linux incantations.  Most of these relate to Manjaro, which is my main distro.

<!-- This generates a table of contents with the CSS `toc` class -->
[TOC]

# cat

Prints the contents of a file or files to standard output (stdout).

## Combining multiple files and sorting alphabetically

```shell
cat file1.txt file2.txt file3.txt | sort > file4.txt
```

## Appending file contents to an existing file

```shell
# Note the double chevron
cat file1.txt >> file2.txt
```

## Appending text to a file

The below will allow input of text directly from standard output. Once typed out, hit `Enter` then `Ctrl-D`.

```shell
cat >> file1.txt
```

## Get CPU info

```shell
cat /proc/cpuinfo
```

---

# chmod

`chmod` is used to change permissions assigned to a file.

To give full read, write and execute permissions to a file:

```shell
chmod 777 path/to/file
```

Obviously, care should be taken when doing this, and you will need to be root.

---

# du

Returns the size of a directory.

```shell
# h flag for sensible numbers
du -h name-of-dir
# Only dirs >100MB in size 
du -t 100M -d1 -h
# Organise by size (slow)
du -t 100M -d1 -h | sort -h
```

---

# fc-list

Lists system fonts.

```shell
fc-list -v  # Gives full list of all font names
```

Output can be [piped](#pipes) to [grep][] to search for a specific font.  The verbose flag is useful for finding, for example, the mad names used by `urxvt`.

[grep]: {filename}../grep.md

---

# feh

Displays images.

```shell
# View an image
feh image
# Montage mode: shows all images in one window
feh -m [--thumb width x] [--thumb-height y]
# Multi-window mode: not helpful with current i3 setup
feh -w
# Index mode: useful for quick overview of images in dir
feh -i
```

---

# file

Returns a file's *type*, e.g. binary, ASCII text, &c.

```shell
file filename
```

---

# find

The `find` command will search for matching file names in a directory. For example, to find all files beginning with *t* in the current directory, the following command could be used:

```shell
find ./* -name "t*"
# Files >300 bytes/kilobytes/megabytes/gigabytes
find ./* -size +300{c|k|M|G}
```

## Finding all local git repos

```shell
find / -name .git
```

---

# locate

Searches the system for a file name.

Locate is not live: it uses its own database that is usually updated once a night or once a week (so it might not find new files).  For this reason, it is much faster than `file`.  The `updatedb` command can be used to manually update the database.

---

# Mounting, unmounting and ejecting drives

## mount

Allows access to files and directories on an external device.

```shell
mount path/to/drive path/to/mountpoint
```

The directory used as a mount point must exist.  Use the `df` command to list all drives visible to the system.  `sudo` probably required.

## umount

Prepares a mounted device for ejection.

```shell
umount path/to/mountpoint
```

Note the absence of the letter `n` in the `umount` command.  Great stuff.  `sudo` most likely needed.

## eject

Removes the device from the file system.

```shell
eject path/to/drive
```

Again, `sudo` probably required.

---

# Network

## nmcli

Lists network devices within your device.

```shell
nmcli dev wifi  # Lists all available wifi networks
nmcli dev wifi connect SSID [password PASSWORD]
```

## ip addr

Returns your machine's IP address.  Look for `inet`.

## nmap

Lists devices on a network.

To list all devices connected to the same network as the IP Address provided, use:

```shell
nmap -sn IP.ADD.R.ESS/24
```

Alternatively, you can just pass the IP Address for the router, which is usually `192.168.1.254`. Actually I think you can use `192.168.1.0` and start from there.  The `/24` tells `nmap` to scan all 256 addresses available.

## Change hostname

Add the desired hostname to `/etc/hostname`, and also edit the name in `/etc/hosts`.

---

# pdfjam

Can be used to extract pages from a pdf.

```shell
# Extract pages 73 to 98 from a pdf
pdfjam -o extract.pdf original.pdf 73-98
```

---

# Pipes

Pipes (`|`) are used to pass the output of one command to another.  For example, if wishing to list all files containing `foo` in their name that exist within the `bar` directory, you can pipe the output of the `ls` command to `grep` (the `i` flag ignores case) like so:

```shell
ls bar | grep -i "foo"
```

---

# ps

The `ps -A` command will list all running processes.

Output can be piped to [grep][] to search for a specific process.

[grep]: {filename}/grep.md "A link to my page on grep"

---

# Redirecting output

To direct the output of a command to a file (as opposed to standard output), use the following syntax:

```shell
command [options] [arguments] > file_name  # Overwrite
command [options] [arguments] >> file_name # Append
```

---

# scp

The `scp` (secure copy) command is used to copy files over [SSH](#ssh).

```shell
scp [-P port-number] original_file destination_file
# Use the r flag for directories
scp [-P port-number] -r original_dir destination_dir 
```

*Note that the port flag for `scp` is a **capital** P, unlike the `ssh` command's port flag which is lower case.  Great stuff.*

The naming of the remote file (even if the command is run on the remote computer) must be done in the following manner:

```shell
user@server:/path/to/file
```

---

# Screenshots

## import

Allows selection of area to save as image.

```shell
import ss.png
```

## scrot

```
# Saves screenshot to ss.png after 5s delay
scrot -d 5 -o ss.png
```

---

# sed

Somewhat like `cat`, but can be used to just print one line to stdout, or to append lines to a file using `>>`.

```shell
sed -n 5p filename  # 5th line
sed -n -e 5p -e 8p filename  # 5th & 8th lines
sed -n 5,8p filename  # 5th to 8th lines
sed -n -e 5,8p -e 10p filename  # 5th to 8th lines and 10th line
```

## Insert text at specific point in file

```shell
# Insert line of text and a new line on first line of file
sed -i '1s/^/text to insert\n/' file
```

## Replacing text

```shell
# Replace abc with xyz in file
# Accepts wildcards instead of filenames
sed -i -e 's/abc/xyz/g' file
```

---

# setxkbmap

Change keyboard layout.

```shell
setxkbmap [gb|us|etc.]
```

---

# sort

```shell
sort filename  # Sort alphabetically by first letter of line
sort -k2 filename  # Sort alphabetically by first letter of second word, etc.
```

---

# ssh

SSH stands for **S**ecure **SH**ell.  It is a means of interacting remotely with a device/server on the same network, allowing the user to run commands on the remote machine, copy files between machines, and so on.

To connect:

```shell
ssh [-p port-number] username@hostname
```

`hostname` can be an IP address, or a local address such as `pi-hole.local`.  Upon connection you will be prompted for the password of the remote user (unless you have shared key files with the server--see below).

The default port used for SSH is port 22.  If your server is accessible to traffic from outside your local network, it is advisable to change the default port in order to reduce the risk of unauthorised brute-force access.  The port(s) over which a server will accept SSH connections can be specified in its `/etc/ssh/sshd_config`.

*Note that there may also be a file called `ssh_config` in this directory--setting the port here will not work!*

## Setting an SSH server alias

For each remote server, add the following to the below file to set an alias.  This alias can then be used instead of the user and hostname each time you connect to the machine.

**~/.ssh/config**

```shell
Host alias
	HostName hostname # Usually the IP address
	User username # On remote machine
```

## Getting around the password requirement with key files

```shell
# Generate pair of key files
ssh-keygen -t rsa
# Copy public key to remote server
ssh-copy-id -i ~/.ssh/id_rsa.pub user@server
```

After running the first command, it will ask where you would like to save the key pair.  The default option is fine.  When it asks for a password, simply hit Enter both times to skip.  Note that the public key ends in `.pub`.  This can be shared freely.

**THE PRIVATE KEY SHOULD NEVER BE MOVED OR DUPLICATED.**

---

# upower

Returns information about your battery (e.g. charge level, health, etc.)

```shell
upower -e  # Get battery name
upower -i path-to-battery  # Get information
```

---

# wget

Can be used to download webpages.

The level argument 0 specifies an infinite recursion depth, so the below will download an entire website if run at the site index.

```shell
wget -r -l 0 url
```

---

# whereis

Returns the location of a command's binary file, as well as the location of any source code and manual pages.

```shell
whereis command
```

---

# xdg-open

Opens a file or files using the configured default application.

For example, to see all the files for the default Jekyll `minima` theme, within a Jekyll bundle's folder, run:

```shell
xdg-open $(bundle info --path minima)
```

---

# xdotool

Returns information about window geometry.

```shell
xdotool getwindowfocus getwindowgeometry  # Returns size of current window
xdotool selectwindow getwindowgeometry  # Allows selection of window using mouse
```

---

# xev

Sends to standard output details of keys pressed and released while the `xev` window is in focus.

---

# xkill

Force-close the next window clicked.

---

# xprop

Provides detailed information on the next window clicked after running the command.

Of particular interest are the `WM_NAME` or `\_NET_WM_NAME` sections, which give the *Title* that can be used with i3 Window Manager, and the WM_CLASS section which provides the *Class* used by i3wm.