import pyautogui
import time
pyautogui.FAILSAFE = False
from win32api import GetSystemMetrics
import os
print("SalesMate + Backup Manu Test")

#get the width and height

width= GetSystemMetrics(0)
height=GetSystemMetrics(1)

#click on the botton left to launch the start menu

print("click on the bottom left launch the start menu")
pyautogui.click(x=41,y=1048)

print("Select the SalesMate + Application")
pyautogui.typewrite("    salesMate +",0.1)

print("Press Enter Key to Launch SalesMate + Application and Wait for 10 Sec")
pyautogui.press("enter",1,7)

print("Now press Esc for full screen mode  ")
pyautogui.press("Esc")

print("Press Enter Key again to close the Tip Of the Day Dialog")
pyautogui.press("enter",1,1)

print("Add New Customer")
pyautogui.press(['alt','c'],1,1)

print("Press A to invoke the new customer details menu")
pyautogui.press('a',1,1)

print("Press alt to select next entry")
pyautogui.press("Tab",2,1)

print("Enter First Name")
pyautogui.typewrite("Samir",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Last Name")
pyautogui.typewrite("Kumar",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Title")
pyautogui.typewrite("Mr",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Address")
pyautogui.typewrite("India",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Phone Number")
pyautogui.typewrite("8789048162",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Email Id")
pyautogui.typewrite("sam2elect@gmail.com",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Press Space to select")
pyautogui.press("Space",1,1)

pyautogui.sleep(2) 
pyautogui.leftClick(x=942, y=502)
pyautogui.sleep(2) 

pyautogui.leftClick(x=1167, y=607)
pyautogui.sleep(2) 

print("Press alt to select next entry")
pyautogui.press("Tab",2,1)

print("Press Arrow up to select")
pyautogui.press('up',4,1)

print("Press alt to select next entry")
pyautogui.press("Tab",2,1)

print("Enter Comment")
pyautogui.typewrite("ktsinfotech",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",2,1)

print("Press alt to select next entry")
pyautogui.press("Space",1,1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter membership fees")
pyautogui.typewrite("12",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Press alt to select next entry")
pyautogui.press("Space",1,1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)


print("Enter membership fees")
pyautogui.typewrite("1234",0.1)

print("Press alt to select next entry")
pyautogui.press("Enter",2,1)