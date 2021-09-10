import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

username = "deontearchie@icloud.com"
password = "!Ddcewf26"

options = Options()

#find the brave application in your folder
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

url = "https://www.bestbuy.com/identity/signin?token=tid%3Adff09746-1251-11ec-b86f-0a94b1f5db05"

driver_path = '/Users/deontearchie/Downloads/chromedriver'

#called the variable for the brave application and chrome driver
drvr = webdriver.Chrome(options = options, executable_path = driver_path)

drvr.get(url)

drvr.find_element_by_id("fld-e").send_keys(username)
drvr.find_element_by_id("fld-p1").send_keys(password)
drvr.find_element_by_class_name("c-button-secondary").click()


time.sleep(1.3)


#Ps5 browser
drvr.get("https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller-midnight-black/6464307.p?skuId=6464307")



buyButton = False

while not buyButton:

    try:
        #if this work the then the button is not open
        addToCartBtn = addButton = drvr.find_element_by_class_name("c-button-disabled")

         #If button is  ot open restart the script
        print("Button isnt ready yet.")

        #refresh page after the delay
        time.sleep(1)
        drvr.refresh()

    except:
        
        addToCartBtn = addButton = drvr.find_element_by_class_name("c-button-primary")

        #click the button and end the script
        print("Button was clicked.")

        addToCartBtn.click()
        buyButton = True

        time.sleep(2)
        
        addToCartBtn = addButton = drvr.find_element_by_class_name("go-to-cart-button")

        print("Button was clicked.")

        addToCartBtn.click()
        buyButton = True

        time.sleep(1.3)

        addToCartBtn = addButton = drvr.find_element_by_class_name("btn-primary")

        print("Button was clicked.")

        addToCartBtn.click()
        buyButton = True





