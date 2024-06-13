import keyboard
import mouse
import time

isClicking = False

def setClicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('work suspended')
    else:
        isClicking = True
        print('work started')

# hotkey to turn the clicker on/off
keyboard.add_hotkey('Ctrl + /', setClicker)

# endless cycle
while True:
    if isClicking == True:

        # endless double click while looping
        mouse.double_click(button = 'left')

        # delay to avoid freezes
        time.sleep(0.01)