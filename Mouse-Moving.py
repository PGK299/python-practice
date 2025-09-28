#Mouse Moving
import pyautogui as pag
import random
import time

while True:
    x = random.randint(600, 1000)
    y = random.randint(200, 600)
    pag.moveTo(x, y,1)
    time.sleep(3)
