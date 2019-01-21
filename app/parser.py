from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/seongwon/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.google.com')

driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input').send_keys('cafe')
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[2]/div/div[4]/div[2]/div/div/a').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

