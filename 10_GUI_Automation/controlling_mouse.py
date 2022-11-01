import pyautogui

print(pyautogui.size())
width, height = pyautogui.size()
print(width)
print(height)

print(pyautogui.position())

pyautogui.moveTo(1490, 560)
pyautogui.moveTo(1290, 760, duration=1.5)

pyautogui.moveRel(0,-300)
pyautogui.moveRel(400, 0, duration=2)

pyautogui.click(600, 16)
pyautogui.moveTo(1490, 560)
pyautogui.rightClick()

pyautogui.displayMousePosition()  # run this ONLY IN cmd
