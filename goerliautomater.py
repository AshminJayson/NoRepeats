# Don't ask me why. It just seemed like a good idea at the time 😼

import pyautogui as pg
import time
import webbrowser

url = "https://goerlifaucet.com/"

webbrowser.open(url)
time.sleep(2)

for i in range(6):
    pg.press('tab')

time.sleep(1)
pg.write('0xD726291d19d4DB8f2e071361F04227B23662fD34')
pg.press('tab')
pg.press('enter')

