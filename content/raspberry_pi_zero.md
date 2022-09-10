Title: Raspberry Pi Zero 2 W
Date: 2022-09-09
Category: technology
Tags: raspberrypi
Slug: raspberry-pi-headless-setup
Summary: Notes on setting up a Headless Raspberry Pi Zero

## Headless setup

Here are some of my notes on setting up a headless Raspberry Pi Zero. After loading the OS onto an SD Card (download the image from the RaspberryPi website and burn it to an SD Card: I use Balena Etcher to do the latter, but it's possible to do this via the command line).

### SSH

Navigate to the `/boot` folder on the SD Card, and run `touch ssh` to enable SSH on the Pi.

### WiFi

Also in the `/boot` folder, run `touch wpa_supplicant.conf` Then, in this file, put the following:

```
country=GB
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
ssid="SSID"
psk="PASSWORD"
}
```

(The country code is the `ISO 3166-1` code for that country.)

The Pi should now automatically connect to the WiFi network. The `wpa_supplicant.conf` file will be deleted once the Pi connects to the network.

### Testing Connection

Use `ping -c 5 raspberrypi.local` to test if the pi is reachable.

### Connection via SSH

To connect to the pi when it is plugged into the laptop in gadget mode run `ssh pi@raspberrypi.local`

### Starting the VNC Server on the Pi

If a GUI is needed, after sshing in, run `vncserver :1` (You might need to install this first.) It should now be possible to connect to the Pi from a PC running VNC Server.
