######################### cmd cleaner #########################
from os import system
system('cls')
#-------------------------------------------------------------#
########################### comments ##########################
#-------------------------------------------------------------#

########################### ToDo ##########################
'''
Certainly! Let’s break down the task into smaller steps:

Get a Word from the User:
We’ll create a Python function that prompts the user to input a word.
We’ll use the input() function to get the user’s input.
Search in Google Using Firefox:
We’ll automate the Google search using Selenium, a browser automation tool.
We’ll open Firefox, perform the search, and retrieve the search results.
Scroll Through Results Until Finding the Word:
We’ll iterate through the search results and check if the word appears in any of them.
Write the Clicker Function:
Once we find the word, we’ll create a function to click on the corresponding search result.

'''
########################### modules ###########################

#-------------------------------------------------------------#

############################# code ############################
# def get_user_word():
#     """
#     Prompts the user to input a word and returns it.
#     """
#     user_word = input("Please enter a word: ")
#     return user_word

# # Example usage:
# user_input_word = get_user_word()
# print(f"You entered: {user_input_word}")
##########################



# -----------------------------

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from selenium.webdriver.firefox.options import Options

keyWord = "لوله گالوانیزه سبک 1 اینچ"
# runTimes = int(input("Enter no. of exec. prog: "))
runTimes = 1
def waiter(text,a, b):
    waitTime = randint(a, b)
    # count += 1
    print(f"{text}==> {waitTime} seconds")
    time.sleep(waitTime)

def moreResultClicker():
    for i in range (3):
        # old # moreResult = driver.find_element(By.XPATH,"//div[5]/div/div[10]/div/div[4]/div/div[3]/div[4]/a[1]/h3/div/span[2]")
        try:
            moreResult = driver.find_element(By.XPATH,"//div[4]/div/div[13]/div/div[4]/div/div[4]/div[4]/a[1]/h3/div") # more result
        except:
            moreResult = driver.find_element(By.XPATH,"//div[4]/div/div[13]/div/div[4]/div/div[3]/table/tbody/tr/td[12]/a/span[2]") # Next
            
        
        moreResult.click()
        waiter("inside moreResult", 2, 5)
        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        # waiter("b", 1, 2)



counter = 1

for i in range (runTimes):

    while True:
        print("      ||||||||||")
        print(f"{counter} run")
        print("||||||||||||||||||||||||")
        counter += 1

        firefox_options = Options()
        firefox_options.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(options=firefox_options)
        driver.get('https://www.google.com')
        waiter("wait before search", 5, 9)

        search_input = driver.find_element("name", 'q')
        search_input.send_keys(keyWord)
        waiter("keyword entered", 2, 4)

        search_input.send_keys(Keys.ENTER)
        waiter("keyword searched", 4, 7)

        html = driver.find_element(By.TAG_NAME, 'html')

        for i in range(8):
            html.send_keys(Keys.END)
            waiter("more result?", 1, 2)
            try:
                moreResultClicker()
            except:
                pass
            waiter("scroll", 2, 3)
        waiter("end of resault page", 4, 5)

        print("try to click on more result")

        try:
            moreResultClicker()
        except:
            pass

        myUrls = driver.find_element(By.XPATH, '//div[@class="yuRUbf"]//a[starts-with(@href,"https://www.seify.ir")]')
        myUrls.click()
        waiter("found url clicked!", 4, 7)

        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        waiter("wait on found page", 45, 77)
        # ToDo change time to 50, 76


        driver.close()
        waiter("K", 3, 5)







#-------------------------------------------------------------#



if __name__ == '__main__':
    pass # run main function