# click-speed

### about tool
* $`\textcolor{blue}{Chinese 、\, 中文 \,、中国語}`$
  
一個可以讓滑鼠`連續點擊某處`的類**連點器**  
可用於genshin劇情、搶票等需要連續點擊的場合  

* $`\textcolor{blue}{English 、\, 英文 \,、中国語}`$

A class of autoclicker that enables continuous clicking at a specific location   
for tasks such as Genshin Impact storyline progression, ticket booking, and other scenarios requiring consecutive clicks.

* $`\textcolor{blue}{Japanese 、\, 日文 \,、日本語}`$

指定の場所で連続してクリックすることができるクラスのオートクリッカー。  
Genshin Impactのストーリー進行、チケットの予約など、連続したクリックが必要なシナリオに使用できます。


### use method

* $`\textcolor{blue}{Chinese 、\, 中文 \,、中国語}`$

按下'a'即開始執行程式(連點)   
按下'p'即暫停、再次按下'a'繼續執行  
按下's'結束程式，按下'a'無法再次執行  


* $`\textcolor{blue}{English 、\, 英文 \,、英語}`$

Pressing 'a' starts the execution of the program (autoclicking).  
Pressing 'p' pauses the program, and pressing 'a' again resumes execution.  
Pressing 's' terminates the program, and pressing 'a' will not restart it.  


* $`\textcolor{blue}{Japanese 、\, 日文 \,、日本語}`$

'a'を押すと、プログラムが実行されます（自動クリック）。  
'p'を押すとプログラムが一時停止し、再び'a'を押すと実行が再開されます。  
's'を押すとプログラムが終了し、'a'を再び押しても実行されません。  


## note 

你可以透過改變參數來達到自己的使用需求   
You can tailor the program to meet your specific usage requirements by modifying the parameters.    
プログラムを自分の使用要件に合わせるために、パラメーターを変更することができます。 


* 例如/for example:   
改變熱鍵 /change Hotkey/ ホットキーを変更する  
```py
def click():
    while True:
        pyautogui.click(1300,250,clicks=10,interval=0.0001)
        if keyboard.is_pressed('s'):# ('s')this can change Hotkey about stop programming (1/2side)
            print("end programming ")
            sys.exit(0)
        elif keyboard.is_pressed('p'):# ('p')this can change Hotkey about pause programming
            pause()
```

$`\textcolor{red}{請在執行前先確定已安裝pyauyogui}`$    
$`\textcolor{red}{Please\quad ensure \quad that\quad pyautogui\quad is\quad installed\quad before\quad running}`$  
$`\textcolor{red}{実行する前に \quad pyautogui\quad がインストールされていることを確認してください。}`$  

* install pyautogui (open terminal)
```
pip install pyautogui
```
## code

or u cahn click [this]() to get code
```py
import pyautogui
import time 
import keyboard
import sys 


################################################################
def click():
    while True:
        pyautogui.click(1300,250,clicks=10,interval=0.0001)
        if keyboard.is_pressed('s'):# ('s')this can change Hotkey about stop programming (1/2side)
            print("end programming ")
            sys.exit(0)
        elif keyboard.is_pressed('p'):# ('p')this can change Hotkey about pause programming
            pause()
            
            
def pause():
    print("stop programming...")
    while True:
        time.sleep(0.00001)
        if keyboard.is_pressed ('a'):# ('a')this can change Hotkey about start programming
            print("start programming again")
            click()
            break 
        elif keyboard.is_pressed ('s'):# ('s')this can change Hotkey about stop programming(2/2side)
            print("end programming ")
            sys.exit()
    

def clickfuction(event):
    if event.name == 'a':# ('a')this can change Hotkey about restart programming after programming pause
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



```
