import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

driver= webdriver.Chrome();
driver.get('http://localhost:3000')
driver.implicitly_wait(8);
try:
    modalbtn=driver.find_element(By.ID,'modal-btn')
    modalbtn.click()
except:
    print('no modal appear')





