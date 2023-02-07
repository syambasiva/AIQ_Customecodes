from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("https://integration-commonsecurity.develgs.com:9015/v1/ui/home")
driver.find_element_by_xpath('//input[@name="username"]').send_keys('commonsecurity@prod.com')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('gainsight01*')
driver.find_element_by_xpath('//span[@class="auth0-label-submit"]').click()
time.sleep(80)
c=driver.get_cookies()
#d=driver.get_cookie('foo')
print(c)
#print(d)
##commonsecurity@prod.com
##gainsight01*