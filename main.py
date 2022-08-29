import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

driver= webdriver.Chrome();
driver.get('http://localhost:3000')
driver.implicitly_wait(8);
mybtn=driver.find_element(By.ID, 'btn1')
mybtn.click();

WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME,'my_label'),
    'completed!'
))

