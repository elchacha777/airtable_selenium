from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
from webdriver_manager.chrome import ChromeDriverManager


class TempMail:
    def __init__(self, link) -> None:
        self.options = uc.ChromeOptions()
        self.driver = uc.Chrome(
            executable_path=ChromeDriverManager().install(), options=self.options
        )
        self.link = link

    def get_page(self):
        self.driver.get(self.link)

    def get_email(self):
        self.get_page()
        email = self.driver.find_element(By.ID, "i-email").get_attribute("value")
        print(email)
        return email

    def accept_invite(self):
        self.get_page()
        time.sleep(5)
        message = self.driver.find_element(
            By.XPATH, '//*[@id="apptmo"]/div/div[2]/div[1]/ul/li/div[2]/div'
        )
        message.click()
        time.sleep(3)
        iframe = self.driver.find_element(By.XPATH, '//*[@id="fullmessage"]')
        self.driver.switch_to.frame(iframe)
        button = self.driver.find_element(
            By.XPATH, "/html/body/table/tbody/tr[2]/td/p/a"
        )
        href = button.get_attribute("href")
        time.sleep(2)
        return href

    @staticmethod
    def set_name():
        import names

        full_name = names.get_full_name()
        return full_name

    @staticmethod
    def set_password():
        import random

        password_length = 12
        characters = "abcde12345"
        password = ""
        for index in range(password_length):
            password = password + random.choice(characters)
        return password

    def register(self):
        self.driver.get(self.accept_invite())
        wait = WebDriverWait(self.driver, 20)
        time.sleep(3)
        input_name = self.driver.find_element(
            By.XPATH, '//*[@id="signUpForm"]/div[2]/div/label/input'
        )
        time.sleep(1)
        name = self.set_name()
        time.sleep(1)
        input_name.send_keys(name)
        time.sleep(5)
        input_password = self.driver.find_element(
            By.XPATH, '//*[@id="signUpForm"]/label[2]/div/input'
        )
        input_password.send_keys(self.set_password())
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)
        create_button = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="signUpForm"]/button'))
        )
        create_button.click()
        time.sleep(3)
        skip_button1 = self.driver.find_element(
            By.XPATH,
            '//*[@id="workspaceSetupDialogContainer"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]',
        )
        skip_button1.click()
        time.sleep(3)
        skip_button2 = self.driver.find_element(
            By.XPATH,
            '//*[@id="workspaceSetupDialogContainer"]/div[2]/div/div/div[2]/div/div[2]/div[2]',
        )
        skip_button2.click()
        time.sleep(3)


