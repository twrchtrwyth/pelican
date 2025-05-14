---
Title: Updating the AntiX application menu
Date: 2025-05-02
Author: Wil Ifan
Category: linux
Tags: antix, linux, command line
Slug: antix-applications
Status: published
Summary: How to amend the desktop applications list on AntiX Linux
---

In order to appear in the applications list that is visible upon right-clicking the desktop, software must have a corresponding entry in the following directory:

```
/usr/share/applications
```

The entry should be a plain text file, with the same name as the software in question but with a `.desktop` extension.  Example syntax from the file `surf.desktop` (the [surf][] browser) is below.

[surf]: https://surf.suckless.org

```
[Desktop Entry]
Name=surf
Comment=Simple web browser by suckless
Generic Name=Web Browser
Keywords=browser;internet;web;lightweight;
Exec=surf %u
Terminal=false
X-MultipleArgs=false
Type=Application
Icon=surf
StartupWMClass=surf
Categories=Network;WebBrowser;
MimeType=text/html;text/xml;application/xhtml+xml;application/xml;image/gif;image/jpeg;image/png
```

Icons (for example `.png` files) can be given as an absolute path i.e. can be saved anywhere.  Alternatively, icons can be passed as simply the icon's name (without extension) if placed in the following directory (for example, `surf.png` is saved in the below directory and so can be passed as simply `Icon=surf`):

```
/usr/share/pixmaps
```

Finally, to update the applications list run the following:

```shell
desktop-menu --write-out-global
```

The above will also remove any applications from the menu that are no longer installed. 
