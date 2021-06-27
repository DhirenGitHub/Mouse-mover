import pyautogui
import keyboard

while True:
    pos = pyautogui.position()
    if keyboard.is_pressed('up'):
        pyautogui.moveTo(pos[0], pos[1] - 25)

    if keyboard.is_pressed('down'):
        pyautogui.moveTo(pos[0], pos[1] + 25)

    if keyboard.is_pressed('left'):
        pyautogui.moveTo(pos[0] - 25, pos[1])

    if keyboard.is_pressed('right'):
        pyautogui.moveTo(pos[0] + 25, pos[1])

    if keyboard.is_pressed('z'):
        pyautogui.leftClick()

    if keyboard.is_pressed('x'):
        pyautogui.rightClick()
z