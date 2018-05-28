from selenium import webdriver
import time
import urllib
from urllib.request import *

x="source.unsplash.com/random"
refreshrate=4
driver = webdriver.Firefox()
driver.get("http://"+x)

while True:
    time.sleep(refreshrate)
    driver.get("http://"+x)