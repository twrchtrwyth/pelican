---
Title: Linux Commands
Date: 2022-09-10
Category: linux
Tags: linux, command line
Status: published
Slug: linux-guide
Summary: Some notes on using Linux, with a focus on the command line.
---

## Setting file permissions

To give full read, write and execute permissions to a file, use `chmod 777 path/to/file` Obviously, care should be taken when doing this, and you will need to be root.

---

## Getting information about windows

The `xprop` command will list various useful pieces of information about a window. Simply run it in a terminal, then click the window of interest. Or particular interest are the `WM_NAME` or `\_NET_WM_NAME` sections, which give the *Title* that can be used in i3 Window Manager, and the WM_CLASS section which provides the *Class* used by i3wm.

---

## Getting window dimensions

Use `xdotool` to do this. For example:

```bash
$ xdotool getwindowfocus getwindowgeometry  # Returns size of current window.
$ xdotool selectwindow getwindowgeometry  # Allows selection of window.
```

---

## Getting information about key presses

The `xev` command will open a window and output information about any keys pressed whilst this window is highlighted to the terminal.

---

## Sending command output to a file.

`COMMAND [OPTIONS] [ARGUMENTS] > file_name`

---

## Sorting content of a text file.

The `sort` command can be used to do this. It should be followed by the name of the file to sort. To sort by the second "column" of information (e.g. the second word in a sentence), the `-k 2` option can be specified, etc.

---

## Listing running processes.

The `ps -A` command will list all running processes.
This can be piped to [`grep`]({filename}grep.md) to search for a specific process.

---

## Finding files

The `find` command will search for matching file names in a directory. For example, to find all files beginning with `t` in the current directory, the following command could be used:

`find ./* -name "t*"`

To find files larger than 300 bytes, use:

`find ./* -size +300c`

(For some reason `c` is used for bytes, then `k`, `M` and `G` are used for kilo-, mega- and gigabytes, respectively.)

The `locate` command will search the system for a file name. It is not live: it uses its own database that is usually updated once a night or once a week (so it might not find new files). The `updatedb` command can be used to manually update the database. `locate` is much faster than `file`.

### fzf

Alternatively, install the fuzzy finder `fzf` from your distro's repositories and reap all of its wonderful benefits. With some simple configuration this also lets you search through your command history, which is hugely helpful.

---

## Determining file type

Use the `file` command, followed by the name of the file, to do this.

---

## Locating information on a command

Use `whereis` to do this. Will return the binary, source and manual page files for the command.

---

## Opening a link to a folder in file explorer, from the terminal

Use `xdg-open` to do this. For example, to see all the files for the default Jekyll `minima` theme, within a Jekyll bundle's folder run `xdg-open $(bundle info --path minima)`

---

## Mounting and unmounting drives

### Mounting

To mount, use `mount path/to/drive path/to/mountpoint`. The directory used as a mount point must exist. I normally use `~/external-hdd`. Use the `df` command to list all drives visible to the system. `sudo` probably required.

### Unmounting

To unmount, use `umount path/to/mountpoint`. Note the *absence* of `n` in the `umount` command--why anyone thought this was a good idea, I'll never know. Think `sudo` is needed, again.

### Ejecting

To eject a drive, use `eject path/to/drive`. Again, `sudo` probably required.

---

## Piping Commands

This can be used to pass the output of one command to another, and is accomplished with the `|` character. For example, if wishing to list all files containing `foo` in their name within the `bar` directory, you can pipe the output of the `ls` command to `grep` (the `i` flag ignores case) like so:

```shell
ls bar | grep -i "foo"
```

---

## Listing Fonts

Use `fc-list` to show all system fonts. The `-v` flag can be specified to get the full bunch of names that fonts are known by. This is useful for finding the mad names used by `urxvt`. This can be piped to `grep` to find a specific font. Use `grep -i` to ignore case.

---

## Checking Battery Charge, Health, etc.

Use `upower -e` to find the battery name. Select the correct battery from the list, and then run `upower -i path-to-battery` to see information about its health.

---

## Network

### Show available WiFi networks

`nmcli` will do this. If run without arguments, it lists the network devices within your device (I think). When called as `nmcli dev wifi` it will list all available WiFi networks in a pretty little coloured table.

### Connect to network

After determining the SSID as above, use `nmcli dev wifi connect [SSID] password [PASSWORD]` to connect to the network. Tab completion works for the SSID (in Konsole on Manjaro, anyway). If the network is unsecured, simply omit the part after the SSID. 

### Get Device IP Address

Use `ip addr` and look for `inet`

### Listing Devices on a Network

Use the `nmap` command to do this. Will need the IP Address provided by the above command. Use `sudo nmap -sn IP.ADD.R.ESS/24` to list all devices connected to the same network as the IP Address provided. Alternatively, can just pass the IP Address for the router, which is usually `192.168.1.254`. Actually I think you can just use `192.168.1.0` and start from there.

The `/24` tells `nmap` to scan all 256 addresses available.

---

## Dunst

### Configuring shortcuts

Reportedly this is now possible via your window manager. It needs to call `dunstctl`. Will need to look up more information on this.

---

## Force Close a Window

Use the `xkill` command to turn the cursor into a little skull and crossbones, then click the window that you wish to force-quit.

---

## Docker

Used for TILP interface for TI Nspire.

### Starting docker

First, run `sudo systemctl unmask docker` then `sudo systemctl start docker`

### Stopping docker

Run `sudo systemctl stop docker` then `sudo systemctl mask docker` ("Masking" symlinks to `/dev/null`, which I assume totally stops any funny business.)

### Running TILP in docker

First run `xhost +` to disable control of the display---note that this isn't really a great idea but is required to allow display of the GUI within docker. Then run `sudo docker run -ti --rm --privileged -e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev:/dev:rw -v /home/wil:/mnt:rw adriweb/tilp`. The computer's file system is then found in the `/mnt` folder. Once finished, run `xhost -` to only allow authorised clients to access the display.

---

## Extracting pages from a pdf

To extract pages 73 to 98 from a pdf, use `pdfjam -o extract.pdf original.pdf 73-98`

---

## Optimise jpeg files for sharing

Not exactly sure what this does, but `mogrify -auto-orient -define jpeg:dct-method=float -quality 75 -strip -interlace Plane -sampling-factor 4:2:0 -resize '1400x1400>' *.jpg` is recommended online to share a jpeg. Mogrify is part of the ImageMagick suite of tools. Need to look into this.

---

## SSH

### Connecting

Use `ssh username@host.name` 

### Setting a specific port

A specific port can be used with the `-p <port-number>` flag. The port(s) over which the server will accept SSH connections can be specified in `/etc/ssh/sshd_config` (note that there may also be a file called `ssh_config` in this directory--setting the port here will not work!).

### Copying files over SSH

The `scp` (secure copy) command is used to accomplish this. The basic format of the command is as follows:

```shell
scp [options] original_file destination_file
```

The naming of the remote file (even if the command is run on the remote computer) must be done in the following manner:

```shell
user@server:path/to/file
```

To copy whole directories, add the `-r` (recursive) flag.

To transfer along a specific port, use `scp -P <port-number>` Note that this is a capital *P*, unlike the `ssh` command's *port* flag which must be lower case. Great stuff.

### Getting around the password requirement with key files

A pair of key files can be generated with the `ssh-keygen -t rsa` command. The public key can be moved to the server (with `scp`), and the private key left on the computer which generated it. THE PRIVATE KEY SHOULD NEVER BE MOVED OR DUPLICATED.

After running the above command, it will prompt the user as to where they would like to save the key pair. The default option is fine. When it asks for a password, simply hit Enter both times to skip.

#### Copying ssh keys the easy way

After generating keys as described above, use the following command to move it to your server.

```shell
ssh-copy-id -i ~/.ssh/id_rsa.pub user@server
```

---

## The cat command

I'll skip the basics.

### Sorting multiple files alphabetically

```shell
cat file1.txt file2.txt file3.txt | sort > file4.txt
```

### Appending file contents to an existing file

```shell
# note the double chevron
cat file1.txt >> file2.txt
```

### Appending text to a file

The below will allow input of text directly from standard output. Once typed out, hit `Enter` then `Ctrl-D`.

```shell
cat >> file1.txt
```

---

## The sed command

This is like `cat`, but can be used to just print one line to stdout, or to add it to a file using `>>`. Usage is as follows:

```shell
sed -n 5p filename  # 5th line
sed -n -e 5p -e 8p filename  # 5th & 8th lines
sed -n 5,8p filename  # 5th to 8th lines
sed -n -e 5,8p -e 10p filename  # 5th to 8th lines and 10th line
```

It can also be used from the command line to add a single line of text to a file at the given index. This example inserts a line of text and then a newline character in the first line of the given file:

```shell
sed -i '1s/^/text to insert\n/' filename
```

To replace `abc` with `xyz` in `file` using `sed` (accepts wildcards instead of filenames):

```shell
sed -i -e 's/abc/xyz/g' file
```

---

## Get directory size.

Pass the `-h` flag to see sensible numbers.

```shell
du -h name-of-dir
```

To only show directories >100MB in size (the `-d1` flag only shows directories to a depth of 1 below the current directory):
```shell
du -t 100M -d1 -h
```

Output can be piped to `sort -h` to organise directories from smallest to largest---this is quite slow.

---

## Check which packages depend on a given package

On Manjaro linux:

```shell
pamac -Qii <package-name>
```

---

## Get CPU info

```shell
cat /proc/cpuinfo
```

---

## Listing git repos in the terminal

Can direct output to a file for later reference.

```shell
find / -name .git
```

---

## Downloading webpages

The below flags to `wget` will result in `r`ecursive downloads to an infinite `l`evel i.e. the whole website.  Pass numbers other than 0 to specify a level of recursion.

```shell
wget -r -l 0 url
```

---

## Viewing images with Feh

Straightforward use is self-explanatory.  Some other ways to use feh are shown below.

```shell
feh -m  # Montage mode: shows all images within one window
feh -m --thumb-height 150 --thumb width 200
feh -w  # Multi-window mode: not helpful with current i3 setup
feh -i  # Index mode: useful for quick overview of images in dir
```

---

## Taking screenshots

The below will allow selection of an area and then save this to `ss.png`.

```shell
import ss.png
```

---

## Change Keyboard Layout

```shell
setxkbmap [gb|us|etc.]
```

---

## Change hostname

Add the desired hostname to `/etc/hostname`, and also edit the name in `/etc/hosts`.
