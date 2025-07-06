import time,pathlib,pyautogui
time.sleep(1)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
time.sleep(4)
with open(f'{pathlib.Path(__file__).stem}.txt') as f:
    for i in f.readlines():
        time.sleep(.1)
        pyautogui.write(i.strip())
        time.sleep(.1)
        pyautogui.press('tab')
        # pyautogui.press('enter')
