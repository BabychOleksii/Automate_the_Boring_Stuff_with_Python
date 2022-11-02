import pyautogui

print(pyautogui.screenshot())
pyautogui.screenshot('screenshot.jpg')

print(pyautogui.locateOnScreen('buildings.png'))
print(pyautogui.locateCenterOnScreen('buildings.png'))
