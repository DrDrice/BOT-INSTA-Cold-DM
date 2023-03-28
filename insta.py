
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import sys 
import pandas as pd

cookies = False

users_file = open("users.txt", "r", encoding="utf-8")
users_list = users_file.readlines()
users_file.close()

# Définition des messages
with open("messages.txt", "r", encoding="utf-8") as f:
    messages = f.read().split("\n\n")

    random_message = random.choice(messages)



# Instanciation de l'objet driver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://instagram.com')
time.sleep(4)   

# Accepter les cookies
def accept_cookies():
    global cookies
    if (cookies == False):
        cookies = True
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if button.text == "Autoriser les cookies essentiels et optionnels":
                button.click()
                time.sleep(4)
                break

# Se connecter
def login():
    accept_cookies()
    username = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    username.send_keys('NOM_UTILISATEUR')
    time.sleep(5)
    password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    password.send_keys('MOT_DE_PASSE')
    password.submit()
    time.sleep(7)

login()
#Ferme les 2 pop up
def popup():

    PlusTard=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
    time.sleep(5)   
    PlusTard2=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()   
popup()


# Clic sur l'élément Nouveau message du Menu
def dmbtn():
    elemdm = driver.find_element(By.CSS_SELECTOR, '[aria-label="Direct"]')
    elemdm.click()
time.sleep(2)
dmbtn()


# Clic sur l'élément Nouveau message
def dmbtn2():
    elemdm2 = driver.find_element(By.CSS_SELECTOR, '[aria-label="Nouveau message"]')
    elemdm2.click()
time.sleep(2)
dmbtn2()



for user in users_list:
    def setuser():
        arobase=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')
        arobase.send_keys(user)
        time.sleep(3)
        circledm=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div')
        time.sleep(3)
        circledm.click()
        time.sleep(3)
        suivant=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div')
        suivant.click()
        time.sleep(3)
    setuser()

    def writemsg():
        inputmsg=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        inputmsg.click()
        time.sleep(3)
        inputmsg.send_keys(random_message)
        time.sleep(3)
        sendbtn=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div')
        sendbtn.click()
        time.sleep(5)
        elemdm3 = driver.find_element(By.CSS_SELECTOR, '[aria-label="Nouveau message"]')
        elemdm3.click()    
    writemsg()

print("Pas di pwoblem")
input("Press enter to close the browser")


           


