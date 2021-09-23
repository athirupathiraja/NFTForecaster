# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
from getpass import getpass
from time import sleep
import webbrowser

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time


# options = EdgeOptions()
# options.us = True
# driver = Edge(options=options)
driver = Chrome()
action = ActionChains(driver)
# driver = webbrowser.get()
# driver = Chrome('open -a/Applications %s')

driver.get("https://twitter.com/i/flow/login")
time.sleep(5)
username = driver.find_element_by_name("username")
username.click()
username.send_keys('athirupathiraja777@gmail.com')
username.send_keys(Keys.RETURN)

time.sleep(3)
myPassword = 'NFTscraper'
password = driver.find_element_by_name("password")
password.click()
password.send_keys(myPassword)
password.send_keys(Keys.RETURN)

time.sleep(3)
search = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
search.click()
search.send_keys('#NFT')
search.send_keys(Keys.RETURN)
latestPosts = driver.find_element_by_link_text('Latest').click()

cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')

card = cards[7]

#username
print(card.find_element_by_xpath('.//span').text)

#text
print(card.find_element_by_xpath('.//span[contains(text(), "@")]').text)
#
# password = driver.find_element_by_xpath('//input[@name="session[password]"]')
# password.send_keys(myPassword)
#
# password.send_keys(Keys.RETURN)





# username = driver.find_element_by_xpath()
# driver.open()
