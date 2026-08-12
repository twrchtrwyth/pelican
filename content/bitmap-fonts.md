---
Title: Enabling Bitmap Fonts on Manjaro
Date: 2024-01-06
Author: Wil Ifan
Category: linux
Tags: linux, fonts, command line, manjaro
Slug: manjaro-bitmap-fonts
Status: published
Summary: How to allow the use of bitmap fonts on Manjaro Linux.
---

# Enabling Bitmap Fonts on Manjaro

For some reason, bitmap fonts appear to be disabled by default on Manjaro.  To re-enable them, it's necessary to delete a file from `/etc/fonts/conf.d` and then create a new directory and file which symlinks to `/etc/fonts/conf.d`

```shell
sudo rm /etc/fonts/conf.d/70-no-bitmaps.conf
sudo mkdir /etc/fonts/conf.avail  # Skip if directory already exists.
sudo ln -s /etc/fonts/conf.avail/70-yes-bitmaps.conf \
/etc/fonts/conf.d/70-yes-bitmaps.conf
```
