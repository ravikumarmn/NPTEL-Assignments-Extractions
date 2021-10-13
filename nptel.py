from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/ravikumar/Desktop/NPTEL_SCRAPE/chromedriver')

link = "https://swayam.gov.in/"
driver.get(link)
driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "close", " " ))]').click()
driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-lg", " " ))]').click()
driver.implicitly_wait(15)
user = driver.find_element_by_xpath('//*[(@id = "logonIdentifier")]')
user.send_keys('ravikumarnaduvin')
password = driver.find_element_by_xpath('//*[(@id = "password")]')
password.send_keys('Tutorial#77')
driver.find_element_by_xpath('//*[(@id = "next")]').click()
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a/i').click()

driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/ul/li[1]/a').click()
driver.implicitly_wait(15)

driver.find_element_by_xpath('//*[@id="OngoingBlock"]/div[2]/div[2]/div[1]').click()
#driver.find_element_by_xpath('//*[@id="unit_navbar_6"]').click()
#driver.find_element_by_xpath('//*[@id="subunit_navbar_6"]/li[7]/div').click()
driver.find_element_by_xpath('//*[@id="unit_navbar_14"]').click()

driver.find_element_by_xpath('//*[@id="subunit_navbar_14"]/li[8]/div/a').click()
#//*[@id="unit_heading_6"]//*[@id="unit_heading_14"]


with open ("nptel_html.html","w") as f:
    f.write(driver.page_source)
driver.close()

