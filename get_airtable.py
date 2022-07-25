from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import time
from tempmail import TempMail
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import os


class AirTable:
    def __init__(self, link) -> None:
        self.options = uc.ChromeOptions()
        self.add_options()
        self.driver = uc.Chrome(
            executable_path=ChromeDriverManager().install(), options=self.options
        )
        self.wait = WebDriverWait(self.driver, 60)
        self.link = link
        self.tempmail = TempMail("https://tempmailo.com/")

    def get_page(self):
        self.driver.get(self.link)

    def add_options(self):
        dir_path = os.getcwd()

        profile = os.path.join(dir_path, "profile", "airtable")

        self.options.add_argument(r"user-data-dir={}".format(profile))
        # self.options.add_argument("user-data-dir=" + "")
        self.options.add_argument('lang=pt-br')


    def login(self, email, password):
        try:
            sign_in = self.driver.find_element(
                By.XPATH, '//*[@id="marketingHeaderSharedRoot"]/nav/div[2]/a[3]'
            )
            sign_in.click()
            time.sleep(15)
            input_email = self.driver.find_element(By.ID, "emailLogin")
            input_email.send_keys(email)
            time.sleep(2)
            submit_button = self.driver.find_element(
                By.XPATH, '//*[@id="sign-in-form-fields-root"]/button'
            )
            submit_button.click()
            time.sleep(5)
            input_password = self.driver.find_element(By.ID, "passwordLogin")
            input_password.send_keys(password)
            time.sleep(5)
            sign_in_button = self.driver.find_element(
                By.XPATH, '//*[@id="sign-in-form-fields-root"]/button'
            )
            sign_in_button.click()
        except NoSuchElementException:
            self.account_page()

    def account_page(self):
        self.driver.get(self.link + "account/credits")

    def get_email(self):

        email = self.tempmail.get_email()
        return email

    def send_email(self):
        send_link_to_email = self.driver.find_element(
            By.XPATH, '//*[@id="accountRoot"]/div/div[2]/div[1]/label/div[2]/input'
        )
        print(self.get_email())
        send_link_to_email.send_keys(self.get_email())
        time.sleep(1)
        send_link_button = self.driver.find_element(
            By.XPATH, '//*[@id="accountRoot"]/div/div[2]/div[1]/label/div[3]'
        )
        send_link_button.click()

    def register(self):
        self.tempmail.register()

