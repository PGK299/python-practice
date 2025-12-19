#Mouse Moving
import pyautogui as pag
import random
import time

while True:
    x = random.randint(500, 1600)
    y = random.randint(500, 800)
    pag.moveTo(x, y,1)
    pag.scroll(500)
    time.sleep(5)
    a = random.randint(600, 1000)
    b = random.randint(600, 800)
    pag.moveTo(a, b,1)
    time.sleep(5)
    pag.scroll(-500)
    pag.hotkey('alt', 'tab')
    time.sleep(3)
    pag.hotkey('alt', 'tab')
    time.sleep(3)
