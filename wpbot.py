import pyautogui as pg
import time
import os

#place the cursor in the whatsapp chat windows before executing the code
no_of_participants = int(input("Enter the number of participants : "))

time.sleep(5)
for i in range(no_of_participants - 1):
    pg.write('@')
    if i > 0:
        pg.press('down')
    pg.press('enter')
    time.sleep(0.2)

