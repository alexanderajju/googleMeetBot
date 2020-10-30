from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import requests
import getpass

geckopath = r""  #Path for GeckoDriver on your system

gmailId = input("enter your college email Id\n")  
passWord=getpass.getpass("Enter password for : %s \n" % gmailId) 

duration =int(input("Enter the time required in minutes\n"))
meetingLink=input("enter the meeting link\n")

options = FirefoxOptions()
options.set_preference("permissions.default.microphone", 2)
options.set_preference("permissions.default.camera", 2)
driver = webdriver.Firefox(options=options,executable_path=geckopath)


def switch_focus():
    Window_List = driver.window_handles
    driver.switch_to_window(Window_List[-1])


        

def start_bot():
    print("[+]Connencting to gmail account")
    driver.get("https://www.gmail.com") 

    email_field = driver.find_element_by_name('identifier')
    email_field.send_keys(gmailId)
    email_field.send_keys(Keys.ENTER)
    time.sleep(3)

    password_field = driver.find_element_by_name("password")
    password_field.send_keys(passWord)
    password_field.send_keys(Keys.ENTER)
    time.sleep(6)

def meet():
    print("[+]connecting to Google meet")
    driver.execute_script("window.open('');")
    switch_focus()
    driver.get(meetingLink) #Meeting Link
    time.sleep(3)
    buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Join now')]")
    
    if(buttons):
        print("button")
        for btn in buttons:
            time.sleep(10)
            btn.click()
    else:
        print("not Found")
    time.sleep(duration*60)
    driver.close()
    switch_focus()
    print("exited")
    driver.close()
    
   


start_bot()
meet()

