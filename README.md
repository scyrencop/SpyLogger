# SpyLogger

SpyLogger is a multiplatform Script made in Python, to spy and log every keypress, screenshot, web cam capture and clipboard ! 

DO NOT use this script on other systems without their permission. Only use it on your own system and for educational purposes.

## Features

[x] Keylogging on Linux
[] Keylogging on OSX
[] Keylogging on Windows
[x] Saving logs to files locally
[x] Store Clipboard logs Locally
[x] Saving ScreenShot Locally
[x] Sending logs to Email
[] Compress & Send Images to Email
[] Upload logs file to an FTP account
[] Send the logs to a Google Form
[] JSON storing
[] Take snapshots from WebCamera
[] Decode logs into human-readable format
[] Invisible mode (Runs in background)


## Requires
- Python 2.7
### For Linux 
- python-xlib
- pyxhook
### For Windows 
- pyHook
### For Mac OS
- pyObjC

## Instalation & Usage

To use this program
Clone the github repository on your system
Make sure you have Python 2.x installed

### Windows 

You might want to change to an exe by using something like py2exe or PyInstaller. Then just run it. To stop it press Ctrl-E or end the Python process in Task Manager

### Linux

SpyLogger requires python-xlib and gtk-module. install it if you don't have it already

- `sudo apt-get install python-xlib`

- `sudo apt install libcanberra-gtk-module libcanberra-gtk3-module`

Enjoy Using it !


### MAC OSX

- Disabling System Integrity Protection (SIP) by terminal : `csrutil disable` then `reboot` and press enter.

**Important:** *For your own security, remember to re-enable this feature after you’re done testing by following the steps above but entering `csrutil enable` .*
