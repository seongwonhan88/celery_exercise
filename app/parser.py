from selenium import webdriver
from config.settings import session
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/seongwon/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://linkedin.com')
driver.find_element_by_id('login-email').send_keys(session['session_key'])
driver.find_element_by_id('login-password').send_keys(session['session_password'])
driver.find_element_by_id('login-submit').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
title = soup.select('div.relative')
print(title)