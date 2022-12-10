# Don't ask me why. It just seemed like a good idea at the time 😼

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

import pyautogui as pg
import time
import webbrowser

url = "https://goerlifaucet.com/"


def seleniumRun():
    # Making upgrades
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    #Unfortunately this isn't working 
    # stealth(driver,
    #         languages=["en-US", "en"],
    #         vendor="Google Inc.",
    #         platform="Win32",
    #         webgl_vendor="Intel Inc.",
    #         renderer="Intel Iris OpenGL Engine",
    #         fix_hairline=True,
    #         )       

    driver.get(url)
    timeout = 3
    try:
        element_present = EC.presence_of_element_located((By.ID, 'main'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException as tr:
        print("Timed out waiting for page to load")
        return False



def nativeRun():
    webbrowser.open(url)
    time.sleep(10)

    for i in range(6):
        pg.press('tab')

    time.sleep(1)
    pg.write('0xD726291d19d4DB8f2e071361F04227B23662fD34')
    pg.press('tab')
    pg.press('enter')


if __name__ == '__main__':
    if not seleniumRun():
        nativeRun()
