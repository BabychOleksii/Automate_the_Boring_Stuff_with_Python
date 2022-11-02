import pyautogui

pyautogui.click(100, 100)
pyautogui.typewrite('Hello world!')
pyautogui.typewrite('Hello world!', interval=0.2)
pyautogui.typewrite(['enter', 'a', 'b', 'left', 'left', 'X', 'Y'], interval=0.5)
print(pyautogui.KEYBOARD_KEYS)
print(pyautogui.press('f1'))
pyautogui.hotkey('ctrl', 'o')
