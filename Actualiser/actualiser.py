from selenium import webdriver
import time
import urllib
import os
from urllib.request import *


file = os.path.abspath("./geckodriver.exe")
os.environ["Path"] = file

x = input("Lien du site à actualiser : ")
refreshrate = int(input("Temps d'actualisation --> Toute les x secondes : "))
driver = webdriver.Firefox()
driver.get(x)

while True:
    time.sleep(refreshrate)
    driver.get(x)