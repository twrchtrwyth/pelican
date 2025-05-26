---
Title: Pacman
Date: 2024-06-06
Category: linux
Tags: manjaro, linux, command line
Status: published
Slug: pacman
Summary: An overview of Manjaro/Arch Linux's package manager.
---

Manjaro uses the `pacman` package manager.  It is, as is usually the case for Linux, quite idiosyncratic.  Here is a brief introduction including some handy commands.

# Updating

```shell
# Update package database and all system packages
sudo pacman -Syu
```

# Getting Information

```shell
# Get information about a package, including its dependents and dependencies
pacman -Qii packagename
```

# Searching

```shell
# Searches repositories for keyword in name and description
pacman -Ss keyword
# Get more information about the package in the repo
pacman -Si keyword
# Searched installed packages in the same manner
pacman -Qs keyword
# Get more information about the installed package
pacman -Qi keyword
# List all installed packages
pacman -Ql
# Determine which package installed packagename
pacman -Qo /usr/bin/packagename
```

# Installing

```shell
# Install packagename from repo
sudo pacman -Syu packagename
# Install package from local system
sudo pacman -U /path/to/package/location/packagename.pkg.tar.xz
# Install package from the internet
sudo pacman -U https://mirror.url/packagename.pkg.tar.xz
```

# Removing

Add the `-n` flag to the below commands to also remove the backup configuration files that are automatically generated when deleting packages.

```shell
# Remove packagename
sudo pacman -R packagename
# Remove packagename and all unneeded dependencies
sudo pacman -Rsu packagename
# DANGER ZONE #
# Remove package and *everything* that depends on it
# Will offer confirmation (I think)
sudo pacman -Rc packagename
# - EXTREME DANGER ZONE - #
# DO NOT USE THIS.  Like the above but no confirmation option!
sudo pacman -Rcs packagename
```

# Orphans

```shell
# Show packages not used by anything else i.e. no longer required
pacman -Qdt
# Remove all orphan packages
sudo pacman -Rs $(pacman -Qdtq)
```

# Downloading

This can be useful e.g. to transfer a package to a different system that is not connected to the internet.

```shell
# Download packagename to /var/cache/pacman/pkg
sudo pacman -Sw packagename
```

# Cleaning up

```shell
# Clear cache of packages that are no longer installed
sudo pacman -Sc
# Clear the cache completely. Use with care
sudo pacman -Scc
# Below is the safest way to clear the cache
# It will remove cache files except the latest three versions
paccache -rvk3
```

# Updating mirrorlist with fastest mirrors

```shell
# Useful if for some reason download speed becomes very slow
sudo pacman-mirrors --fasttrack && sudo pacman -Syu
```

# Checking the logs

```shell
# To open the full log file
$EDITOR /var/log/pacman.log
# Using grep
cat /var/log/pacman.log | grep -i searchstring
```

# Config

Pacman's settings are located in `/etc/pacman.conf`.  To enable colour output, uncomment the `Color` line.  To add an animation of Pacman eating pills, add the line `ILoveCandy`.

---

# External

[Manjaro Wiki: Pacman Overview][pacman]

[pacman]: https://wiki.manjaro.org/index.php?title=Pacman_Overview
