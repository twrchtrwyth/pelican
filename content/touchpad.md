---
Title: Toggling the Touchpad on Linux
Date: 2024-06-07
Author: Wil Ifan
Category: linux
Tags: linux, bash, command line, manjaro
Slug: bash-touchpad
Status: published
Summary: A bash script to toggle the touchpad.
---

To bind Fn+F8 on my ThinkPad X220 running Manjaro i3, create the below script, make it executable  with `chmod +x script` and then add this command to the i3 config file:

```text
bindsym XF86TouchpadToggle exec --no-startup-id /path/to/script
```

```shell
!/bin/bash

read TPdevice <<< $( xinput | sed -nre '/TouchPad|Touchpad/s/.*id=([0-9]*).*/\1/p' )
state=$( xinput list-props "$TPdevice" | grep "Device Enabled" | grep -o "[01]$" )

if [ "$state" -eq '1' ];then
    xinput --disable "$TPdevice" && notify-send -i emblem-nowrite "Touchpad" "Disabled"
else
    xinput --enable "$TPdevice" && notify-send -i emblem-nowrite "Touchpad" "Enabled"
fi
```
