#----------------------------------PYTHON AND SELENIUM INSTAGRAM BOT BY SHREYANSH TIWARI--------------------------------------------------
#To use this bot make sure tyo go through all the comments to fully understand the key sections of the program
#You are provided with a data folder containing two text files for accounts and hashtags. Feel free to edit them as you want.
#You can edit these files and put any number of accounts and hastags
#Make sure that the data folder has two text files namely hashtags.txt and accounts.txt filled with the hashtags and accounts you wish to target.
#The accounts and hashtags must written in the exact same manner as they are shown and no other way or it may cause the prorgram to stop working.
#The first hashtag in hashtags.txt file must not contain '#' character in the prefix as it will be shown in the pre-populated file.
# Similarly the first account in accounts.txt must not contain '@' character in the prefix as given in the pre-populated file.
# Lastly -MAKE SURE YOUR ACCOUNT DOESN'T HAVE TWO FACTOR AUTHENTICATION ENABLED. IF YOU HAVE THEN PLEASE DISABLE IT FROM INSTAGRAM

#As soon as you run this program a command window will open which will ask for your username, password and number of posts to be targetted. Make sure to enter your instagram account's
#correct username and password
# The bot will only proceed working further after you have entered your username , password and number of posts.
# After entering the details, SIT BACK AND REALAX! LET THE BOT DO THE WORK!

#-----------------------------------------------------------------------------------------------------------------------------------------

# IMPORTANT : To change the comment values go to line number 81

from getpass import getpass

from selenium import webdriver
from time import sleep
from selenium.common.exceptions import *
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
list_accs = []
heart_eyes = "\U0001F60D"
smiley_face = "\U0001F60A"
folded_hands = "\U0001F64F"
heart = "\U0001F929"
starstruck = "\U0001F497"
fire = "\U0001F525"
file = open('./data/accounts.txt', 'r')
lines = file.read().split(' @')
for w in lines:
    list_accs.append(w)
print(list_accs) 
print(len(list_accs))
count = len(list_accs)
user_id = input("Enter your instagram account username : ")
print("YOUR ACCOUNT : ", user_id)
print("PLEASE ENTER YOUR PASSWORD BELOW. FOR PRIVACY REASONS YOUR INPUT KEY STROKES WILL BE HIDDEN FOR THE PASSWORD FIELD. DON'T WORRY JUST TYPE THE COMPLETE PASSWORD AND PRESS ENTER")
password = getpass()
numPosts = input("Enter the number of posts you want to target for each hashtag or account : ")
print("NUMBER OF POSTS TO BE TARGETTED : ", numPosts)
print("Starting selenium web browser...")
driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')

sleep(1)
un = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
un.send_keys(user_id)
sleep(2)
pw = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
pw.send_keys(password)
sleep(3)
loginbtn = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
loginbtn.click()
sleep(7)
nonowbtn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
nonowbtn.click()
sleep(7)
notifbtn = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notifbtn.click()
sleep(3)
def searchacc(account):
        print("Account being botted : ",l ,count, "accounts remaining" )
        driver.get('https://www.instagram.com/' + account)
 
    
def likephoto(amount):
    sleep(6)
    driver.find_element_by_class_name("_9AhH0").click()
    i = 1
    while i <= amount:
        sleep(6)
        if(driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").get_attribute('innerHTML') != user_id):

            like_btn = driver.find_element_by_class_name('wpO6b').find_element_by_class_name('QBdPU').find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span').find_element_by_class_name('_8-yf5')

            if(like_btn.get_attribute("aria-label")=="Like"):
                
                try:
                    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
                    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()#likebutton
                    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()
                    
                    #This list below contains the list of comments which you would like toh be posted on the posts. Feel free to change them.
                    list = ['Wow! This gives me the vibes! '+heart+heart,'Amazing post! '+fire+fire,'Dope! '+fire+fire,'Damn!! '+starstruck+starstruck, 'Surreal! '+starstruck+heart_eyes, 'Mesmerising '+heart_eyes+starstruck, 'Superb ! '+heart_eyes+heart_eyes, 'Thats amazing '+heart_eyes+fire, 'Loved it! '+heart+heart, 'Incredible! '+heart_eyes+starstruck, 'Stunning job '+heart_eyes+fire, 'Outstanding piece of work '+heart_eyes+fire, 'Too good '+starstruck+fire, 'Soooo good '+starstruck+heart_eyes, 'This is just awesome '+heart_eyes+heart]

                    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(random.choice(list))
                    sleep(random.randint(5,10))
                    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()#postbtn
                    print("Comment done!")
                    sleep(random.randint(10,15))
                except NoSuchElementException:
                    print("Some exception occurred")
                    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                    i += 1
                else:
                    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                    i += 1
            else:        
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        else:        
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()    
           
for l in list_accs:
    searchacc(l)
    count = count -1
    likephoto(int(numPosts))
print("\n\n*********BOTTING DONE ! IT WAS A PLEASURE TO SERVE YOU!*********")    
