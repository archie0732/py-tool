# piano game(broken)

## about 

can play piano tile game in auto

update : now is broken

#### code (py)
```py
import pyautogui
import time 
import keyboard
import sys 
import win32api
import win32con

################################################################
#1. (600,620)
#2. (750,620)
#3. (950,620)
#4. (1100,620)
################################################################
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

################################################################

# main
print("Start typing... ")
time.sleep(2)

if keyboard.is_pressed('a'):
    print("Key 'a' is pressed")

keyboard.wait('a')  # Waits for the 'a' key to be pressed
print("Start... ")

while keyboard.is_pressed('q') == False:
    if  pyautogui.pixel(600, 620)[0] == 0:
        click(600, 620)
    if pyautogui.pixel(750, 620)[0] == 0:
        click(750, 620)
    if pyautogui.pixel(950, 620)[0] == 0:
        click(950, 620)
    if pyautogui.pixel(1100, 620)[0] == 0:
        click(1100, 620)
        
print("End... \n")
```
