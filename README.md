# BitMeter Desktop 0.2.2

This is a fork of https://github.com/codebox/bitmeteros-python-client

It has been updated to work with wxPython 4.0.7 and Python 3.7.

Tested with Ubuntu 18.04, 20.04, 22.04, 24.04.

Desktop Client for [BitMeter OS](https://github.com/codebox/bitmeteros) (experimental, only works with v0.7.6 of BitMeter OS)

![Screenshot1](resources/Screenshot1.png?raw=true "Screenshot 1")
![Screenshot2](resources/Screenshot2.png?raw=true "Screenshot 2")
![Screenshot3](resources/Screenshot3.png?raw=true "Screenshot 3")
![Screenshot4](resources/Screenshot4.png?raw=true "Screenshot 4 - Transparency")

## Diferences to the official `bitmeteros-python-client` version 0.1.0

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

## Installation on Ubuntu 18.04, 20.04

First download BitMeter OS v0.7.6 from https://codebox.net/pages/bitmeteros-downloads

Then double click on the `.deb` file to install it.

Test by navigating to http://localhost:2605/index.html

### Create a virtual environment and activate it

```sh
cd ~/Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Run the script and follow the instructions, accepting the offer to update your shell profile

```sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Close and reopen your terminal.

### Install Python 3.9.21

```sh
conda create --name bitmeter python=3.9.21
```

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

Ubuntu 24.04

```sh
sudo apt install python3-pip build-essential make gcc gettext libsdl1.2-dev libnotify-dev libgtk-3-dev libgstreamer-gl1.0-0 freeglut3-dev python3-gst-1.0 libglib2.0-dev ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev
```

Note there is not `freeglut3` package for Ubuntu 24.04.

### Install wxPython 4.2.2

Takes 5-10 mins, installed version 4.2.2 - Jan 2025

Check: https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html

```sh
conda activate bitmeter
time pip install wxpython==4.2.2
.
Collecting wxPython
  Using cached wxPython-4.2.2.tar.gz (57.4 MB)
  Preparing metadata (setup.py) ... done
Collecting six (from wxPython)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting numpy (from wxPython)
  Downloading numpy-2.0.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
Downloading numpy-2.0.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (19.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.5/19.5 MB 84.0 MB/s eta 0:00:00
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Building wheels for collected packages: wxPython
  Building wheel for wxPython (setup.py) ... done
  Created wheel for wxPython: filename=wxPython-4.2.2-cp39-cp39-linux_x86_64.whl size=150203744 sha256=86e776f9dc3873306f1be13e20eac9ba85c73cd7db0b69b79409357f393dee94
  Stored in directory: /home/test/.cache/pip/wheels/65/0a/65/6f55ebaf4eef1f76513ac3917a728516020d13bb028f64fa18
Successfully built wxPython
Installing collected packages: six, numpy, wxPython
Successfully installed numpy-2.0.2 six-1.17.0 wxPython-4.2.2

real	16m19.867s
user	52m10.467s
sys   7m41.551s
```

### Clone project

```sh
cd /usr/local/bin
sudo git clone https://github.com/Qarj/bitmeter-desktop.git
cd bitmeter-desktop
sudo find . -type d -exec chmod a+rwx {} \;
sudo find . -type f -exec chmod a+rw {} \;
```

### Test the desktop client

```sh
/usr/local/bin/bitmeter-desktop/main.py
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
