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

# Installation on Ubuntu 18.04

First download BitMeter OS v0.7.6 from https://codebox.net/pages/bitmeteros-downloads

Then double click on the `.deb` file to install it.

Test by navigating to http://localhost:2605/index.html

### Install wxPython 4 dependencies

accept MS Eula by using TAB key and ENTER

```
sudo apt install make gcc libgtk-3-dev libwebkitgtk-dev libwebkitgtk-3.0-dev libgstreamer-gl1.0-0 freeglut3 freeglut3-dev python-gst-1.0 python3-gst-1.0 libglib2.0-dev ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev
```

Install pathlib2 dependency

```
pip install pathlib2
```

Takes 5-10 mins, installed version 4.0.7 - March 2020

```
sudo pip3 install wxpython
.
Collecting wxpython
  Downloading https://files.pythonhosted.org/packages/b9/8b/31267dd6d026a082faed35ec8d97522c0236f2e083bf15aff64d982215e1/wxPython-4.0.7.post2.tar.gz (68.9MB)
    100% |████████████████████████████████| 68.9MB 2.5MB/s
Collecting pillow (from wxpython)
  Downloading https://files.pythonhosted.org/packages/f5/79/b2d5695d1a931474fa68b68ec93bdf08ba9acbc4d6b3b628eb6aac81d11c/Pillow-7.0.0-cp37-cp37m-manylinux1_x86_64.whl (2.1MB)
    100% |████████████████████████████████| 2.1MB 50.8MB/s
Requirement already satisfied: six in /home/tim/.local/lib/python3.7/site-packages (from wxpython) (1.13.0)
Requirement already satisfied: numpy in /usr/local/lib/python3.7/site-packages (from wxpython) (1.17.4)
Installing collected packages: pillow, wxpython
  Running setup.py install for wxpython ... done
Successfully installed pillow-7.0.0 wxpython-4.0.7.post2
```

### Clone project

```
cd /usr/local/bin
sudo git clone https://github.com/Qarj/bitmeter-desktop.git
cd bitmeter-desktop
sudo find . -type d -exec chmod a+rwx {} \;
sudo find . -type f -exec chmod a+rw {} \;
```

### Set up desktop icon

```
cp /usr/local/bin/bitmeter-desktop/bitmeter-desktop.desktop ~/Desktop
chmod +x ~/Desktop/bitmeter-desktop.desktop
```

### Start on system boot

Press `Super` key.

Type `startup`, select `Startup Applications`.

Add a new startup program with these values:

| Name | BitMeter Desktop |
| Command | /usr/local/bin/bitmeter-desktop/main.py |
| Comment | Qarj bitmeter-desktop |

### Transparency

The only way I can get transparency to work on Ubuntu 18.04 is by right-clicking
on the graph, select Options, change the Opacity % to a _*different*_ value then click
OK (bottom left button). It will be remembered for the rest of the session only.

# Reference

### Start from command line

```
python /usr/local/bin/bitmeter-desktop/main.py
```
