#Authour name : Shriharsha M Bhat

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait]
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support import expected_conditions as EC
 
driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,60)
print "Fetched 'http://web.whatsapp.com/'"
print "Scan QR code"

#target = 'Name of your friend'

string = "SPAM SPAM SPAM ;_;" #replace it with any spam text you want to send

#x_arg = '//span[contains(@title,' + target + ')]'
#group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
#group_title.click()

time.sleep(40)
serch=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/label/input')
time.sleep(10)
print "search field"
serch.click()
time.sleep(2)
serch.send_keys("NAME"+Keys.ENTER) #Replace 'NAME' with your friends name.
time.sleep(10)
print "Keys sent"
#serch.send_keys(Keys.ENTER)
print "Enter pressed"

print "Target found..\nChat opened"

input_box=driver.find_element_by_class_name("pluggable-input-body.copyable-text.selectable-text")
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
    print "Spamming in progress..spam count = ",i+1

print "Spam successfull"
print "Closing browser"

driver.close()
