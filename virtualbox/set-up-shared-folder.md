# Set Up Shared Folder on VirtualBox

In order to set up a shared folder in virtual box, on the host machine
click on `devices/SharedFolderSettings`.  Then navigate to the folder
that you want to share.

In order to set up the shared folder on the guest, simply type

```
mkdir vboxshare
sudo mount -t vboxsf vboxshare vboxshare
```

This will create a shared folder at your current location in the terminal
which you can drag and drop all manner of crap in and out of.

