#Authour name : Shriharsha M Bhat

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
 
driver = webdriver.Firefox()

driver.get("http://site21.way2sms.com/content/index.html")
wait = WebDriverWait(driver,7)
print "Fetched http://site21.way2sms.com/content/index.html"
time.sleep(5)

serch=driver.find_element_by_xpath('//*[@id="username"]')
time.sleep(5)
serch.send_keys("9483904242") #replace this number with your registered phone no with way2sms
print "Entered Mobile number"
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/form/div[2]/input").send_keys("PASSWORD") #replace PASSWORD with your password
print "Entered Password"
time.sleep(5)

driver.find_element_by_xpath(".//*[@id='loginBTN']").click()
print "Pressed Login Button"
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[11]/div/ul/li[2]/a").click()
driver.implicitly_wait(30)

fp = open('Phone_no.txt') #ph0ne_no.txt is a text file containing recipents phone nos
while 1 :
	line = fp.readline()
	if not line :
			print "Reached end of file"
			break
	else :
			driver.switch_to.frame("frame")
			x=driver.find_element_by_xpath(".//*[@id='mobile']")
			time.sleep(2)
			x.click()
			print "Sending message to %s"%line
			time.sleep(2)
			x.send_keys(line)
			print "Entered recipent number"
			z=random.randint(1,2)
			time.sleep(1)	
			if z==1 :
				y=driver.find_element_by_xpath(".//*[@id='greet1']")
				y.click()
			elif z==2 :
				y=driver.find_element_by_xpath(".//*[@id='greet2']")
				y.click()
			elif z==3 :
				y=driver.find_element_by_xpath(".//*[@id='greet3']")
				y.click()
			elif z==4 :
				y=driver.find_element_by_xpath(".//*[@id='greet4']")
				y.click()
			elif z==5 :
				y=driver.find_element_by_xpath(".//*[@id='greet5']")
				y.click()
			else :
				y=driver.find_element_by_xpath(".//*[@id='greet7']")
				y.click()

			print "Selected the message"
			time.sleep(2)
			#y.click()
			#y.send_keys("-Shriharsha M")
			driver.find_element_by_id("Send").click()
			print "Message sent successfully"
			time.sleep(4)
			driver.switch_to.default_content()
			driver.find_element_by_xpath("/html/body/div[11]/div/ul/li[2]/a").click()
			driver.implicitly_wait(30)

driver.switch_to.default_content()
driver.find_element_by_xpath("/html/body/div[9]/div/ul/li[4]").click()
time.sleep(5)
print "Logged out"
print "Closing browser"

driver.close()
