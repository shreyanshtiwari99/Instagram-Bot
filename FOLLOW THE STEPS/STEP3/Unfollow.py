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
#IMPORTANT : This program will not run without the Follow bot being run once because it required "AccountsFollowed.txt" file to be created to fetch data
from selenium import webdriver
from getpass import getpass
from time import sleep
import random
from selenium.webdriver.common.action_chains import ActionChains
list_accounts = []
file = open('AccountsFollowed.txt', 'r')
lines = file.read().split('\n')
for w in lines:
    list_accounts.append(w)
print(list_accounts) 
print(len(list_accounts))
user_id = input("Enter your instagram account username : ")
print("YOUR ACCOUNT : ", user_id)
print("PLEASE ENTER YOUR PASSWORD BELOW. FOR PRIVACY REASONS YOUR INPUT KEY STROKES WILL BE HIDDEN FOR THE PASSWORD FIELD. DON'T WORRY JUST TYPE THE COMPLETE PASSWORD AND PRESS ENTER")
password = getpass()
print("Starting selenium web browser...")
driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')
sleep(1)
un = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
un.send_keys(user_id)
sleep(2)
pw = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
pw.send_keys(password)
sleep(7)
loginbtn = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
loginbtn.click()
sleep(7)
nonowbtn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
nonowbtn.click()
sleep(7)
notifbtn = driver.find_element_by_class_name('aOOlW')
notifbtn.click()
sleep(5)
def searchtag(acc):
   
    
    print("Account being unfollowed : " +acc)
    try:
        driver.get('https://www.instagram.com/' + acc)
        sleep(3)
        btn_one = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/span").click()
        sleep(3)
        unfollow_btn = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
        sleep(random.randint(10,15))
    except Exception:
        print("Some exception occured")


for l in list_accounts:
    searchtag(l)
print("\n\n*********BOTTING DONE ! IT WAS A PLEASURE TO SERVE YOU!*********")    

