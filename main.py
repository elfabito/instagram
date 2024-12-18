import time
import random
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = "target_account"
URL = "https://www.instagram.com/"
USERNAME = "your_account"
PASSWORD = "your_password"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

class InstaFollower():

    def __init__(self):
        driver.get(URL)
        time.sleep(2)

    def login(self):
        user_form = driver.find_element(by=By.NAME, value='username')
        user_form.send_keys(USERNAME)
        user_password = driver.find_element(by=By.NAME, value='password')
        user_password.send_keys(PASSWORD)
        log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        log_in_button.click()
        time.sleep(5)
        button_notnow = driver.find_element(by=By.CSS_SELECTOR, value='.x1i10hfl div')
        button_notnow.click()
        time.sleep(2)
        # button_notification = driver.find_element(by=By.CLASS_NAME,
        #                                     value='_a9_1')
        # button_notification.click()
        driver.maximize_window()
        # time.sleep(2)
        input = driver.find_element(by=By.LINK_TEXT, value='Search')
        input.click()
        # input_search = driver.find_element(by=By.XPATH, value='//*[@id="mount_0_0_Or"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div[1]/nav/div/header/div/div/div[1]/div/div/div/div/div/input')
        input_search = driver.find_element(by=By.CSS_SELECTOR, value='.x1hq5gj4 input')
        input_search.send_keys(SIMILAR_ACCOUNT)
        input_search.send_keys(Keys.ENTER)
        time.sleep(2)
        input_search.send_keys(Keys.ENTER)
        account = driver.find_element(by=By.CSS_SELECTOR, value='.xocp1fn a')
        account.click()
        time.sleep(3)

    def follow(self):
        followers = driver.find_element(by=By.CSS_SELECTOR, value='.x2pgyrj a')
        followers.click()
        time.sleep(2)
        followers_list = driver.find_element(by=By.CSS_SELECTOR, value='.xyi19xy')
        # num_follow = int(driver.find_element(by=By.CSS_SELECTOR, value='._ac2a span').text)
        # print(num_follow)

        for i in range(1000):
                time.sleep(random.randint(500,1000)/1000)

                elements = driver.find_elements(by=By.XPATH, value='//button[contains(.,"Follow")]')
                print(elements)
                if len(elements) != 0 :
                    for element in elements:
                        try:
                            # Scroll into view
                            driver.execute_script("arguments[0].scrollIntoView(true);", element)
                            time.sleep(1)
                            element.click()
                        except ElementClickInterceptedException:
                            print("Click intercepted, to cancel.")
                            try:
                                close_button = driver.find_element(By.CLASS_NAME, "_a9--")  # Adjust the selector
                                close_button.click()
                                time.sleep(1)
                                element.click()
                            except Exception as e:
                                print(f"Failed to handle : {e}")
                        except Exception as e:
                            print(f"Error clicking element: {e}")

user = InstaFollower()
user.login()
user.follow()
