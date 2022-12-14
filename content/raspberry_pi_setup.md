---
Title: Setting Up a Headless Raspberry Pi Zero on Linux
Date: 2022-09-10
Category: technology
Tags: raspberry pi, linux, command line
Slug: raspberry-pi-zero-headless-setup
Summary: Notes on setting up a Headless Raspberry Pi Zero on Linux.
Status: published
---

## INSTALLING THE OS

First, install the latest version of Raspberry Pi OS Lite from [the Raspberry Pi website](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit). I generally write this to an SD card using balenaEtcher, but it's possible to use the command line if desired.

---

## ENABLING SSH

First, insert the Pi's SD card into the laptop, and locate the directory where the `/boot` partition is located. This is usually `/run/media/your-username/boot`. Once located, use `touch path-to-boot-partition/ssh` to enable ssh.

---

## CONNECTING TO WIFI

1. Create the file `wpa_supplicant.conf` with the command `touch /path-to-boot-partition/wpa_supplicant.conf`
1. Add the following to the file (obviously, replacing the placeholder text), then save it:

```text
country=GB
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="[NETWORK-SSID]"
psk="[NETWORK-PASSWORD]"
}
```

Once the Pi boots up, the data from this file are used to connect to the network and the file is deleted.

NB: The country code is the `ISO 3166-1` code for that country. This can be looked up online if needed.

---

## ENABLING GADGET MODE/USB CONTROL ON A PI ZERO

Add the following to the end of `config.txt` within the boot partition:

`dtoverlay=dwc2`

Add the following to `cmdline.txt` (also within the boot partition), after the word `rootwait` and before `quiet`:

` modules-load=dwc2,g_ether`

`g_ether` enables the USB port to act as an Ethernet cable (I think).

---

## SETTING A FIXED IP ADDRESS

Log into the pi over ssh using `ssh pi@raspberrypi.local` when it is connected to the laptop. The default password is `pi`: at this point, it's probably a good idea to also run `passwd` on the pi and follow the on-screen prompts in order to change it. Alternatively, use `sudo raspi-config`. Once this is done, run `sudo ifconfig -a`. There should be a network device called `usb0`, which should show an `inet` address.

To fix the address, run `sudo nano /etc/network/interfaces`, and at the end of the file add the following:

```
allow-hotplug usb0
iface usb0 inet static
        address 192.168.7.2
        netmask 255.255.255.0
        network 192.168.7.0
        broadcast 192.168.7.255
        gateway 192.168.7.1
```

This will give the Pi the IP Address `192.168.7.2`. (This could be any address--this is just the one used by the Adafruit tutorial.)

Save the file, then run:

```bash
sudo ifdown usb0  # This might fail, which is fine.
sudo ifup usb0
ifconfig usb0  # This should now show the above IP Address as the inet address.
```

---

## Testing Connection

Use `ping -c 5 raspberrypi.local` to test if the pi is reachable.

---

## CONNECTING WITH A GUI

If a GUI is needed, after sshing in, run `vncserver :1` (You might need to install VNC first.) It should now be possible to connect to the Pi from a PC running VNC Server.
