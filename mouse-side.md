# mouse position tool
* update  
  now no
### use tool
pyautogui  
opencv  
## about

this tool can print the mouse position when you press 'a'


このツールは、'a'キーを押すとマウスの位置を表示します。


### code 
```py
import pyautogui
import keyboard

def display_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()
            
            
            if keyboard.is_pressed('a'):
                print(f"\n滑鼠座標: x={x}, y={y}")
                keyboard.wait('a', suppress=True)  # Wait for 'a' key to be released
                continue

    except KeyboardInterrupt:
        print("\n程式結束")

# 顯示滑鼠座標
display_mouse_position()
```
