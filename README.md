# BitMeter Desktop 0.2.0

This is a fork of https://github.com/codebox/bitmeteros-python-client

It has been updated to work with wxPython 4.0.6 and Python 2.7.

Tested with Ubuntu 18.04.

Desktop Client for [BitMeter OS](https://github.com/codebox/bitmeteros) (experimental, only works with v0.7.6 of BitMeter OS)

![Screenshot1][resources/Screenshot1.png]
![Screenshot2][resources/Screenshot2.png]
![Screenshot3][resources/Screenshot3.png]

# Installation on Ubuntu 18.04

This program is written for Python 2.7.

Install wxPython dependencies - accept MS Eula by using TAB key and ENTER
```
sudo apt install make gcc libgtk-3-dev libwebkitgtk-dev libwebkitgtk-3.0-dev libgstreamer-gl1.0-0 freeglut3 freeglut3-dev python-gst-1.0 python3-gst-1.0 libglib2.0-dev ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev
```

Install pathlib2 dependency
```
pip install pathlib2
```

Takes 5-10 mins, installed version 4.0.6 - June 2019
```
sudo pip install wxpython
```

Clone project
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
```
crontab -e
```

Add this line at the end
```
@reboot python /usr/local/bin/bitmeter-desktop/main.py
```

### Transparency

The only way I can get transparency to work on Ubuntu 18.04 is by right-clicking
on the graph, select Options, change the Opacity % to a _*different*_ value then click
OK (bottom left button). It will be remembered for the rest of the session only.

# Start from command line

```
python /usr/local/bin/bitmeter-desktop/main.py
```
