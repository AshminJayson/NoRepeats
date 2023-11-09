import pyautogui as pg
import time
import keyboard

while keyboard.is_pressed('q') == False:
    pass

for i in range(14):
    pg.press('tab')

for i in range(11):
    pg.press('tab')
    pg.press('down')
    pg.press('up')

for i in range(3):
    pg.press('tab')

pg.press('enter')
