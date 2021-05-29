from selenium import webdriver

br = webdriver.Chrome("C:/Users/Abhishek Kumar/Downloads/chromedriver_win32/chromedriver.exe")

br.get("https://www.selenium.dev/")

ele=br.find_element_by_link_text("Downloads")

ele.click()

search=br.find_element_by_id('gsc-i-id1')

search.send_keys('Abhi')