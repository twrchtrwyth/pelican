---
Title: Setting Up a Virtual Machine on Manjaro
Date: 2025-01-27
Category: linux
Tags: manjaro, linux, command line
Status: published
Slug: virtual-machines
Summary: How to set up a virtual machine using KVM and Virtual Machine Manager.
---

This is a half-remembered method for setting up VMs on Manjaro since VirtualBox became an unusable CPU hog.

The method uses the Linux kernel's native virtualisation functionality known as [KVM](https://www.redhat.com/en/topics/virtualization/what-is-KVM).  I've also installed Virtual Machine Manager (or `virt-manager` in the `pacman` repositories) to provide a GUI for creating and launching VMs.

Setup was a touch tricky due to some permissions issues: this was because my VMs live on the hard drive within the Ultrabase, and not at the usual location that KVM/QEMU expects (which I think is at `/var/lib/libvirt`).

## Installing all required software

```bash
sudo pacman -S --needed virt-manager qemu-desktop libvirt \
edk2-ovmf dnsmasq iptables-nft
```

## Starting libvert

```bash
sudo systemctl enable libvirtd.service
```

## Setting the right permissions for running emulators

The user needs to be added to the following groups in order to use system-level virtual machines (change only becomes active after restarting userspace):

```bash
sudo usermod -a -G libvirt,libvirt-qemu,kvm $USER
```

To allow access to specific directories, run the following for each level of the directory:

```bash
setfacl -m user:libvirt-qemu:--x /path/to/dir
# To check it's worked, run this command for each dir
getfacl /path/to/each/dir
# Or try the snazzy all-in-one version (edit as necessary)
getfacl "$HOME"{,/path{,/to{,/dir}}}
```

## Creating a Guest OS with Virt-manager

Create a Connection with hypervisor type `QEMU/KVM` then click on `Create a new virtual machine` and follow the prompts.  At the end choose `Customize configuration before install` and ensure the following are set like so (some may already have defaulted to the below options):

* Change the type of `SATA Disk 1` to `virtio` to improve performance
* Change discard mode to `unmap`
* Change NIC type to `virtio` to improve network performance
* Add TPM chip (TIS model) through the *Emulated device* backend
* Add a watchdog (will reboot the guest when it hangs)--no need to change settings
* Add hardware RNG to get entropy from the host

## Allow file sharing between host/guest

The below shows how to set up Virtio-FS, which uses `hugepages` to share files.

### Setting up hugepages

```bash
# Determine required size of hugepages
# num_hugepages = mem size of vm / Hugepagesize
# e.g. 1024MB / 2MB = 512
# Add a few more for good measure e.g. round up to 550
grep Hugepagesize /proc/meminfo
# Use the following command to create/edit file
# Add the line 'vm.nr_hugepages = num_hugepages'
$EDITOR /etc/sysctl.d/40-hugepage.conf
```

### Configuring the VM

Reboot at this stage to allow the system to allocate hugepages.  Next, prep the VM configuration.

```bash
# To get vmname
virsh list --all
virsh edit vmname
```

Edit the file as follows:

```xml
<domain>
...
  <memoryBacking>
    <hugepages/>
  </memoryBacking>
...
  <cpu ...>
    <numa>
      <cell memory='memory size of virtual machine' unit='KiB' memAccess='shared'/>
    </numa>
  </cpu>
...
  <devices>
    ...
    <filesystem type='mount' accessmode='passthrough'>
      <driver type='virtiofs'/>
      <source dir='path to source folder on host'/>
      <target dir='mount_tag'/>
    </filesystem>
    ...
  </devices>
</domain>
```

### Mounting the directory in the shared machine

On the guest OS, run the following:

```bash
mount -t virtiofs mount_tag /mnt/mount/path
```

Or, to do this automatically when the guest is booted, run the following on the guest OS:

```bash
echo "mount_tag /mnt/mount/path virtiofs rw,noatime,_netdev 0 0" >> /etc/fstab
```

---

# External
[Manjaro Wiki: Virt-manager](https://wiki.manjaro.org/index.php?title=Virt-manager)
[ArchWiki: libvirt](https://wiki.archlinux.org/title/Libvirt)
