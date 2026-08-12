---
Title: Fixing a Corrupted Kernel in Manjaro
Date: 2023-09-12
Category: linux
Tags: manjaro, linux, kernel, command line
Status: published
Slug: manjaro-kernel
Summary: One method of restoring access to Manjaro if Grub can't find the kernel.
---

Three times now, after running `pacman -Syu`, Manjaro has, for some reason, suddenly logged me out of my session.  Where this has occurred, upon rebooting the machine Grub cannot find a kernel and so the OS will not load.  This is, of course, very annoying, but the below steps have resolved this problem each time.

1. Make a live Manjaro USB and load on the machine with corrupted kernel
1. Open a terminal and run `lsblk` to find the filesystem of the machine (e.g. `sda1`)
1. Mount the filesystem with `sudo mount /dev/path/to/filesystem /mnt` e.g. `sudo mount /dev/sda1 /mnt`
1. Run `manjaro-chroot /mnt/`
1. Update pacman with `pacman -Syyu` (remove lock file with `rm /var/lib/pacman/db.lck` if problems locking database).  This may not work (e.g. it won't be able to find the mirrors, even with an internet connection)
1. Run `mhwd-kernel -li` to show installed kernels (these will be called something like `linux61`. If I've understood things correctly Manjaro needs at least two kernels installed at any one time in order to work
1. Run `pacman -S --overwrite "*" kernel1 kernel2...` to rebuild the kernels, then reboot and things should work.  Apparently it's not possible to reinstall a kernel from a chroot environment using the `mhwd-kernel` command, hence why this approach is needed.

The above information was gleaned from [this][forum1] and [this][forum2] forum post.

[forum1]: https://forum.manjaro.org/t/grub-cant-find-kernel-and-i-cant-manage-to-show-it-to-it-error-file-boot-vmlinuz-5-10-x86-64-not-found/128280
[forum2]: https://forum.manjaro.org/t/cannot-install-kernel/103154

## Update

I have since resolved this issue.  The problem was with grub which kept borking after kernel updates.  Somewhere, I have detailed the process by which I sorted this out\.\.\. But I can't remember where at the moment.  I'll update this page if I ever find it.
