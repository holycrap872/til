# Expanding the Disk Space on an Ubuntu VM

There are three parts to this

## Expand the size of the VM disk on the Host

First the VM must be off.  Then you can simply run

```
VBoxManage modifyhd "C:\Users\erizzi\VirtualBox VMs\Ubuntu64-13.03-2\Ubuntu64-14.03-2.vdi" --resize 256000
```

To expand the virtual harddrive to 256 gigs.  Note: if you get the pat wrong,
which is highly possible given window's weird tab complietion, the VBoxManage
fails pretty obscurely.

## Expand the Ubuntu Partition

This was way more difficult.  A lot of stuff seemed to be saying to use the
`gparted` live cd, but it didn't play very well with the VM.  I just ended up
seeing and essentiall useless debian screen.

Instead, I installed the Ubuntu live cd and ran it under trial mode.  From here
I ran `sudo gparted`.

At this point, there was still some difficulties since I couldn't resize the
main partition I was working with.  The swap space was hard rooted in there,
preventing me from expanding the main partition.  In order to fix this, I ran
`sudo swapoff -a` which unmounted the swap space.  With this, I could resize
the partition to the size I wanted.  I then added 10GB of swap space at the end
and I had myself a new hard-drive

## Boot Ubuntu

By far the easiest part of the whole thing. The guest OS picked up the changes
and I went for 99% disk usage to 35%.
