from time import time
from get_airtable import AirTable
from tempmail import TempMail
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import time


def main():
    try:
        airtable = AirTable("https://airtable.com/")
        airtable.get_page()
        time.sleep(5)
        airtable.login("zver.cm@gmail.com", "6253350q1")
        time.sleep(3)
        # airtable.account_page()
        time.sleep(5)
        airtable.send_email()
        time.sleep(10)
        airtable.register()
        time.sleep(5)
        airtable.driver.quit()
        airtable.tempmail.driver.quit()
    except (NoSuchElementException, TimeoutException):
        airtable.driver.quit()
        airtable.tempmail.driver.quit()
        main()


if __name__ == "__main__":
    for i in range(7):
        main()
