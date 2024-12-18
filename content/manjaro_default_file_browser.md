---
Title: Changing the default file browser using the terminal
Date: 2024-12-05
Category: linux
Tags: manjaro, linux, command line
Status: published
Slug: manjaro-file-browser
Summary: How to change the default file browser in the terminal
---

In order to check which file manager is set as default, run the following command:
```shell
xdg-mime query default inode/directory
```

To change this to, for example, `pcmanfm` run:
```shell
xdg-mime default pcmanfm.desktop inode/directory application
```

Alternatively, edit the line containing, for example, `inode/directory=dolphin.desktop` in the file `~/.local/share/applications/mimeapps.list`

The above information was gleaned from [this](https://forum.manjaro.org/t/how-do-i-change-the-default-file-manager-from-the-terminal/33417) forum post.
