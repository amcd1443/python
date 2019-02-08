from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()

driver.get("http://www.thehealthfix.org")
assert "The Health Fix" in driver.title
#elemName = driver.find_element_by_name("logo")
elmClass = driver.find_element_by_class_name("logo")

try: 
	elmHyperLink = driver.find_element_by_partial_link_text("@conac")
except NoSuchElementException as exception:
	print "	element NOT found";


# if (elmHyperLink != False):
# 	print "@concentric works"
# else:
# 	print "Broken @concentric link"


try: 
	assert "social twitter" in driver.page_source
except NoSuchElementException as exception:
	print " social twitter NOT found";


try:
	elmFullName = driver.find_element_by_name("fullname")
	elmFullName.clear()
	elmFullName.send_keys("jack sparrow")
except NoSuchElementException as exception:
	print " full name did NOT fill" 

try: 
	elmOrganization = driver.find_element_by_name("organization")
	elmOrganization.clear()
	elmOrganization.send_keys("black pearl")
except NoSuchElementException as exception:
	print " organization NOT filled"


try: 
	elmEmail = driver.find_element_by_name("email")
	elmEmail.clear()
	elmEmail.send_keys("thisisan@email.com")
except NoSuchElementException as exception:
	print " email NOT filled"

try:
	elmMessage = driver.find_element_by_name("message")
	elmMessage.clear()
	elmMessage.send_keys("This is me testing the message section of the form")
except NoSuchElementException as exception:
	print " message box NOT filled"


try:
	elmPhone = driver.find_element_by_name("phone")
	elmPhone.clear()
	elmPhone.send_keys("555-555-5555") 
except NoSuchElementException as exception: 
	print " phone NOT filled"

driver.find_element_by_class_name("text").click()




#assert "About" in driver.page_source
driver.close()
print "the test's worked"


