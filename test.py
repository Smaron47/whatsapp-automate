from selenium import webdriver
from time import sleep
driver=webdriver.Chrome(r'C:\Users\Sam\kwic\proj1\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
name=input("Enter name of user or group")
count=int(input("How many times"))
filepath=input("Ënter your Filepath")
input("Enter anything after scanning QR code")
user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
for i in range(4):
    attachment_box=driver.find_element_by_xpath('//div[@title="Attach"]')
    attachment_box.click()
    image_box=driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)
    sleep(1)
    for i in range(24):
        addfile_button=driver.find_element_by_xpath('//input[@accept="*"]')
        addfile_button.send_keys(filepath)
        sleep(1)
    sleep(4)
    send_button=driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_button.click()
    sleep(1)

