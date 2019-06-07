# BitMeter Desktop

Desktop Client for [BitMeter OS](https://github.com/codebox/bitmeteros) (experimental, only works with v0.7.x of BitMeter OS)

This client provides a floating graph window on the desktop, displaying data captured by BitMeter OS. It is in the early stages of development, and will certainly contain bugs. You must install BitMeter OS before using this client, it won't work on its own. You will also need to have Python, and the wxPython libraries, installed on your system - most Linux and OSX systems should have these already, Windows users can download them from here: [Windows Python installer](http://www.python.org/download/releases/), [wxPython libraries](http://www.wxpython.org/download.php).

The source code for this utility should provide a useful reference for for anyone wishing to develop other BitMeter OS clients - Python code is quite easy to understand even if you haven't used the language before.

# This fork has updates to work with wxPython 4


# Installation on Ubuntu 18.04

Program is written in Python 2.

Accept MS Eula by using TAB key then enter
```
sudo apt install make gcc libgtk-3-dev libwebkitgtk-dev libwebkitgtk-3.0-dev libgstreamer-gl1.0-0 freeglut3 freeglut3-dev python-gst-1.0 python3-gst-1.0 libglib2.0-dev ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev
```

```
pip install pathlib2
```

Takes 5+ mins, installed version 4.0.6 - June 2019
```
sudo pip install wxpython
```

```
cd /usr/local/bin
sudo git clone https://github.com/Qarj/bitmeter-desktop.git
cd bitmeter-desktop
sudo find . -type d -exec chmod a+rwx {} \;
sudo find . -type f -exec chmod a+rw {} \;
```

### Set up desktop icon
```
cp bitmeter-desktop.desktop ~/Desktop
chmod +x ~/Desktop/bitmeter-desktop.desktop
```

### Start on system boot
```
crontab -e
```

Add this line at the end
```
@reboot /usr/local/bin/bitmeter-desktop/main.py
```



# Usage

```
python main.py
```
