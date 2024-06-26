import os
from pyautogui import *
import pyautogui
import time
from pynput import keyboard
import random
import mouse
import pathlib

# Total about of rolls (num * 3 = skystones used)
total = 500

#Config settings if you dont use standard monitor size
confirmX = 1000
confirmY = 750
offsetX = 900
offsetY = 100
resetX = 350
resetY = 950
resetX2 = 1100
resetY2 = 650

#Ultrawide Monitor Settings
# confirmX = 1000+((2560-1920)/2)
# confirmY = 750
# offsetX = 900+((2560-1920)/2)
# offsetY = 100
# resetX = 350+((2560-1920)/2)
# resetY = 950
# resetX2 = 1100+((2560-1920)/2)
# resetY2 = 650

#4k Monitor Settings
# confirmX = 2220
# confirmY = 1470
# offsetX = 1660
# offsetY = 200
# resetX = 735
# resetY = 1900
# resetX2 = 2160
# resetY2 = 1300

#Ignore these
mysticCount = 0
bookmarkCount = 0

#Quit key (press q)
def on_press(key):
    print(key)
    try:
        if key.char == 'q':
          print('terminating')
          os._exit(0)
    except:
        print("An Error has Occured...???")

#Listens for key
listener = keyboard.Listener(
    on_press=on_press)
listener.start()

#Main function - Reads for mystic medal and covenant bookmarks
def check_bookmarks():
    #print("Checking bookmarks")
    time.sleep((random.random() * 0.2) + 1)
    # Standard Images
    mysticLocation=None
    try:
        mysticLocation = pyautogui.locateOnScreen(str(pathlib.Path(__file__).parent.resolve()) + r'\Bookmarks\mystic.png', confidence = .6)
    except:
        pass
    covLocation=None
    try:
        covLocation = pyautogui.locateOnScreen(str(pathlib.Path(__file__).parent.resolve()) + r'\Bookmarks\bookmark.png', confidence = .7)
    except:
        pass

    #4k Images
    # mysticLocation=None
    # try:
    #     mysticLocation = pyautogui.locateOnScreen(str(pathlib.Path(__file__).parent.resolve()) + r"\Bookmarks\mystic2.png", confidence = .8)
    # except:
    #     pass
    # covLocation=None
    # try:
    #     covLocation = pyautogui.locateOnScreen(str(pathlib.Path(__file__).parent.resolve()) + r"\Bookmarks\bookmark2.png", confidence = .9)
    # except:
    #     pass
    
    #Found mystic
    if mysticLocation != None:
        print("You have a mystic bookmark on screen")
        global mysticCount
        mysticCount += 1
        #print("Total mystic medals found: %d" %(mysticCount))
        click(mysticLocation[0]+offsetX,mysticLocation[1]+offsetY)
        time.sleep(random.random() + 1)
        click(confirmX,confirmY)
        time.sleep(random.random() + 1)
    #Found covenant
    elif covLocation != None:
        print("You have a covenant bookmark on screen")
        global bookmarkCount
        bookmarkCount += 1
        #print("Total covenant medals found: %d" %(bookmarkCount))
        click(covLocation[0]+offsetX,covLocation[1]+offsetY)
        time.sleep(random.random() + 1)
        click(confirmX,confirmY)
        time.sleep(random.random() + 1)
    #print("Finished Checking bookmarks")

#Scrolls the shop down
def scroll():
    #print("Scrolling")
    mouse.drag(confirmX + (random.random()*100), confirmY + (random.random()*50), confirmX + (random.random()*100), confirmY-500 + (random.random()*100), absolute=True, duration=0.3)
    time.sleep((random.random() * 0.5) + 0.5)
    #print("Done Scrolling")

#Clicks on the refresh shop
def reset():
    #print("Resetting Shop")
    click(resetX + ((random.random() - 0.5) * 300),resetY + ((random.random() - 0.5) * 10))
    time.sleep((random.random() * 0.5) + 0.5)
    click(resetX2 + ((random.random() - 0.5) * 200),resetY2 + ((random.random() - 0.5) * 10))
    time.sleep((random.random() * 0.5) + 0.5)
    #print("Done Resetting Shop")

#Clicks at a location (twice)
def click(x,y):
    mouse.move(x,y,absolute=True,duration=0)
    mouse.click('left')
    time.sleep((random.random() * 0.5) + 0.5)
    mouse.click('left')

#Main function
pulls = 0
scrolled = False
while pulls < total:
    print("Loop: %d/%d Mystic: %d Covenant: %d" %(pulls,total,mysticCount,bookmarkCount))
    pulls += 1
    check_bookmarks()
    scroll()
    scroll()
    check_bookmarks()
    reset()