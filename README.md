# BitMeter Desktop 0.2.2

This is a fork of https://github.com/codebox/bitmeteros-python-client

It has been updated to work with wxPython 4.0.7 and Python 3.7.

Tested with Ubuntu 18.04.

Desktop Client for [BitMeter OS](https://github.com/codebox/bitmeteros) (experimental, only works with v0.7.6 of BitMeter OS)

![Screenshot1](resources/Screenshot1.png?raw=true "Screenshot 1")
![Screenshot2](resources/Screenshot2.png?raw=true "Screenshot 2")
![Screenshot3](resources/Screenshot3.png?raw=true "Screenshot 3")
![Screenshot4](resources/Screenshot4.png?raw=true "Screenshot 4 - Transparency")

### Diferences to the official `bitmeteros-python-client` version 0.1.0

-   autoscales the graph
    -   the autoscale option value is now the minimum scale shown (default 1 KB)
    -   the current scale is displayed on the bottom left of the graph e.g. 70 KB
-   graph moves right to left (original moves left to right)
-   transparency enabled for Linux
-   desktop shortcut included with icon
-   default background colour is now black
-   supports wxPython 4.0.7
-   `Hide Graph` menu item removed - not relevant for Ubuntu 18.04 Gnome
-   rough code added to detect if likely off screen due to monitor changes
-   all links fixed
    -   `'webbrowser' is not defined for bitmeteros url` error resolved
    -   link to web interface

# Installation on Ubuntu 18.04, 20.04

First download BitMeter OS v0.7.6 from https://codebox.net/pages/bitmeteros-downloads

Then double click on the `.deb` file to install it.

Test by navigating to http://localhost:2605/index.html

### Install wxPython 4 dependencies

accept MS Eula by using TAB key and ENTER

Ubuntu 18.04

```sh
sudo apt install make gcc libgtk-3-dev libwebkitgtk-dev libwebkitgtk-3.0-dev libgstreamer-gl1.0-0 freeglut3 freeglut3-dev python-gst-1.0 python3-gst-1.0 libglib2.0-dev ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev
```

Ubuntu 20.04, Ubuntu 22.04

```sh
sudo apt install python3-pip make gcc libgtk-3-dev libgstreamer-gl1.0-0 freeglut3 freeglut3-dev python3-gst-1.0 libglib2.0-dev ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev
```

Takes 5-10 mins, installed version 4.2.1 - Sept 2023

```sh
time sudo pip3 install wxpython
.
Collecting wxpython
  Downloading wxPython-4.2.1.tar.gz (73.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.7/73.7 MB 9.6 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Requirement already satisfied: pillow in /usr/lib/python3/dist-packages (from wxpython) (9.0.1)
Requirement already satisfied: six in /usr/lib/python3/dist-packages (from wxpython) (1.16.0)
Collecting numpy
  Downloading numpy-1.26.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.2/18.2 MB 13.4 MB/s eta 0:00:00
Building wheels for collected packages: wxpython
  Building wheel for wxpython (setup.py) ... done
  Created wheel for wxpython: filename=wxPython-4.2.1-cp310-cp310-linux_x86_64.whl size=146717229 sha256=8c713041dcf71034f0f7c35e67554075c74369db335ccd3c9010c3ba45d6d54d
  Stored in directory: /root/.cache/pip/wheels/12/f1/5a/d41ae7a67bafa57317841444cc6e3c9b745df4660e07b54c07
Successfully built wxpython
Installing collected packages: numpy, wxpython
Successfully installed numpy-1.26.0 wxpython-4.2.1
```

### Clone project

```sh
cd /usr/local/bin
sudo git clone https://github.com/Qarj/bitmeter-desktop.git
cd bitmeter-desktop
sudo find . -type d -exec chmod a+rwx {} \;
sudo find . -type f -exec chmod a+rw {} \;
```

### Set up desktop icon

```sh
cp /usr/local/bin/bitmeter-desktop/bitmeter-desktop.desktop ~/Desktop
chmod +x ~/Desktop/bitmeter-desktop.desktop
```

### Start on system boot

Press `Super` key.

Type `startup`, select `Startup Applications`.

Add a new startup program with these values:

| Field   | Value                                   |
| ------- | --------------------------------------- |
| Name    | BitMeter Desktop                        |
| Command | /usr/local/bin/bitmeter-desktop/main.py |
| Comment | Qarj bitmeter-desktop                   |

### Transparency

The only way I can get transparency to work on Ubuntu 18.04 is by right-clicking
on the graph, select Options, change the Opacity % to a _*different*_ value then click
OK (bottom left button). It will be remembered for the rest of the session only.

# Reference

### Start from command line

```sh
python3 /usr/local/bin/bitmeter-desktop/main.py
```
