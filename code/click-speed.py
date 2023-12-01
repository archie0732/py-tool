import pyautogui
import time 
import keyboard
import sys 


################################################################
def click():
    while True:
        pyautogui.click(1300,250,clicks=10,interval=0.0001)
        if keyboard.is_pressed('s'):
            print("end programming ")
            sys.exit(0)
        elif keyboard.is_pressed('p'):
            pause()
            
            
def pause():
    print("stop programming...")
    while True:
        time.sleep(0.00001)
        if keyboard.is_pressed ('a'):
            print("start programming again")
            click()
            break 
        elif keyboard.is_pressed ('s'):
            print("end programming ")
            sys.exit()
    

def clickfuction(event):
    if event.name == 'a':
        pyautogui.moveTo(1300,250)
        print("start programming...")
        click()
         


######################################################################

    

# main function
time.sleep(2)
# ready text 
print("Start typing... \n")
print("#################### \n")
# start with press 'a'
keyboard.on_press_key  ('a',clickfuction)
keyboard.wait()



