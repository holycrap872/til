# Setup VM

- Common configuration:
    - 2048MB Memory
    - "VDI" Disk
    - 200GB Disk space (dynamically allocated)

- Ubuntu 14.04 LTS

## Setting up VM

1) Download Ubuntu from [here]()

2) Start VM

3) Select downloaded image

4) Check option for downloading updates and for downloading extra packages
(such as wifi support)

5) Wait for reboot

6) Enable copying: `Devices->Shared Clipboard->Bidirectional`

7) Guest additions: `Devices->Insert Guest Additions CD image...` and run it

8) `sudo apt-get install git tmux hexedit vim curl python-pip python-dev build-essential python3-pip libtool-bin libtool automake libboost-all-dev g++ scons`

9) See personal setup

## Setting up SSH

1) `sudo apt-get install openssh-server`

2) Shut down vm

3) Setting -> Network

  - Set "Adapter 1" -> "Attached to:" to "Bridged Adapter"

  - Set "Adapter 2" -> "Attached to:" to "NAT"

  - Set "Adapter 2" -> "Cable Connected" to Checked

  - Set "Adapter 2" -> "Port Forwarding" to the following values

    - "Name" : ssh

    - "Protocol" : TCP

    - "Host Port" : 3022

    - "Guest Port" : 22

4) Restart VM

5) Connect **without** any need to do `-p 3022`
