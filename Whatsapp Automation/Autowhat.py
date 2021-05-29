from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time

br = webdriver.Chrome("C:/Users/Abhishek Kumar/Downloads/chromedriver_win32/chromedriver.exe")
br.get("https://web.whatsapp.com/")
wait=WebDriverWait(br, 350)

target='"Bittu Jio"'
string="Python"

x_arg='//span[contains(@title, '+ target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box=br.find_element_by_class_name('DuUXI')
for i in range(100):
	input_box.send_keys(string+Keys.ENTER)