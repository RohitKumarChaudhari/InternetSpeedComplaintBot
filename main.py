import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
up = float(os.getenv("PROMISED_UP"))
down = float(os.getenv("PROMISED_DOWN"))

username = os.getenv("X_USERNAME")
password = os.getenv("PASSWORD")
SPEED_TEST_URL = "https://www.speedtest.net/"
X_URL = "https://x.com/home"



class InternetSpeedTwitterBot:
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.option)
        self.up = up
        self.down = down


    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        time.sleep(4)
        privacy_button = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        privacy_button.click()
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        go_button.click()
        time.sleep(50)
        speed = self.driver.find_element(By.CSS_SELECTOR, ".result-container-data").text.split()
        down_speed = float(speed[2])
        up_speed = float(speed[5])

        self.tweet_at_provider(up= up_speed, down= down_speed)

    def tweet_at_provider(self, up , down):

        if up < self.up or down < self.down:
            self.driver.get(X_URL)

            time.sleep(10)
            username_intput = self.driver.find_element(By.TAG_NAME, 'input')
            username_intput.send_keys(username)

            next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
            print(next_button.text)
            next_button.click()

            time.sleep(5)
            email_input = self.driver.find_element(By.TAG_NAME, "input")
            email_input.send_keys('demo11941@gmail.com')

            
            next1 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
            print(next1.text)
            next1.click()

            time.sleep(5)
            password_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_input.send_keys(password)

            log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
            print(log_in_button.text)
            log_in_button.click()


            time.sleep(10)
            message = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            content = f"Hi my promised up is {self.up}mbps, and my promised down is {self.down}mbps and i got up {up}mbps and down {down}mbps only."
            message.send_keys(content)

            time.sleep(2)
            post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
            print(post_button.text)
            post_button.click()

            time.sleep(20)
            self.driver.quit()
            print("Task Completed.")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()


