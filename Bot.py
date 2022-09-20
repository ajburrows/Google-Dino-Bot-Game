from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def jump(jumpTime):
    win32api.keybd_event(32,0,0,0)
    time.sleep(jumpTime)         
    win32api.keybd_event(32,0,win32con.KEYEVENTF_KEYUP,0)

def crouch(crouchTime):
    win32api.keybd_event(40,0,0,0)
    time.sleep(crouchTime)
    win32api.keybd_event(40,0,win32con.KEYEVENTF_KEYUP,0)


time.sleep(1)
start = time.time()
speed2 = False
print("Mach 1")
while speed2 == False:
    midDetected = False
    lowDetected = False
    pic = pyautogui.screenshot(region=(670 ,500, 20, 150))
    width, height = pic.size

    
    # check for mid-height obstacles
    for x in range(0, width):
        r,g,b = pic.getpixel((x, 104))
        if r == 83:
            midDetected = True
    
    # check for low-height obstacles
    for x in range(0, width):
        for y in range(2):
            r,g,b = pic.getpixel((x, 144+y))
            if r == 83:
                lowDetected = True
   
    if lowDetected:
        jump(0.4)
    elif midDetected:
        crouch(0.5)
    
    end = time.time()
    if end - start >= 14.5:
        speed2 = True

speed3 = False
print("Mach 2")
while speed2 == True and speed3 == False:
    midDetected = False
    lowDetected = False
    pic = pyautogui.screenshot(region=(775 ,500, 30, 150))
    width, height = pic.size
  
    # check for mid-height obstacles
    for x in range(0, width):
        r,g,b = pic.getpixel((x, 104))
        if r == 83: 
            midDetected = True
    
    # check for low obstacles
    for x in range(0, width):
        for y in range(2):
            r,g,b = pic.getpixel((x, 144+y))
            if r == 83:
                lowDetected = True
            
    if lowDetected:
        jump(0.1)
    elif midDetected:
        crouch(0.55)
    
    end = time.time()
    if end-start >= 27:
        speed3 = True
        speed2 = False

speed4 = False
print("Mach 3")
while speed3 == True and speed4 == False:
    midDetected = False
    lowDetected = False
    pic = pyautogui.screenshot(region=(795,500,30,150))
    width, height = pic.size

    
    # check for mid obstacles
    for x in range(0, width):
        r,g,b = pic.getpixel((x, 104))
        if r == 83:
            midDetected = True
    
    # check for low obstacles
    for x in range(0, width):
            r,g,b = pic.getpixel((x, 144))
            if r == 83:
                lowDetected = True
            
    if lowDetected:
        jump(0.1)
    elif midDetected:
        crouch(0.35)
    end = time.time()
    if end-start >= 100:
        speed4 = True
        speed3 = False

speed5 = False
print("Mach 4")
while speed4 == True and speed5 == False:
    midDetected = False
    lowDetected = False
    pic = pyautogui.screenshot(region=(805,500,30,150))
    width, height = pic.size

    
    # check for mid obstacles
    for x in range(0, width):
        r,g,b = pic.getpixel((x, 104))
        if r == 83: 
            midDetected = True
      
    # check for low obstacles
    for x in range(0, width):
        r,g,b = pic.getpixel((x, 144))
        if r == 83:
            lowDetected = True
            
    if lowDetected:
        jump(0.01)
    elif midDetected:
        crouch(0.3)



