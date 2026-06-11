---
Title: Connecting to Sonos speakers from Arch
Date: 2026-04-23
Author: Wil Ifan
Category: linux
Tags: linux, command line
Slug: sonos
Status: published
Summary: How to connect to Sonos speakers using noson on Arch running ufw
---

First, download and install the `noson` package from the [AUR](https://wiki.archlinux.org/title/Arch_User_Repository):

```
cd ~/aur
git clone https://aur.archlinux.org/noson-app
cd noson-app
makepkg -si
```

By default, the `ufw` firewall will block access to Sonos speakers via
`noson`.  In order to make speakers accessible, create a file called
`noson` in `/etc/ufw/applications.d` and add the following:

```
[noson]
title=noson Sonos controller app
description=controls Sonos devices on the same network
ports=80,443,445,1400:1410,3400,3401,3405,3445,3500,4070,4444/tcp|136,137,138,139,1900,1901,2869,10243,10280,10281,10282,10283,10284,5353,6969/udp|35382
```

Then, to load the config into `ufw` run the following as root:

```
ufw app update noson
ufw allow noson
```

Source [here](https://github.com/janbar/noson-app/issues/121).
