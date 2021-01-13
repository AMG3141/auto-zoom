from pynput.keyboard import Key, Controller
import os
import time

def pressRelease(key):
    keyboard.press(key)
    keyboard.release(key)

keyboard = Controller()

os.startfile("C:\\...\\Zoom.exe") #Location of Zoom.exe

time.sleep(2.5)
pressRelease(Key.tab)
pressRelease(Key.enter)
time.sleep(2.5)
keyboard.type("012345789") #Meeting ID
pressRelease(Key.enter)
time.sleep(2.5)
keyboard.type("abcdefg") #Passcode
pressRelease(Key.enter)
