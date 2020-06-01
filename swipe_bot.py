from telnetlib import EC

from selenium import webdriver
from time import sleep
from secrets import username, password

class swipeBot():
    def __init__(self):
        self.driver = webdriver.Chrome("C:/bin/chromedriver.exe")

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(3)
        fb_Button = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_Button.click()

        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)
        log_Button = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        log_Button.click()
        sleep(2)
        switchBackWindows = self.driver.switch_to_window(base_window)
        sleep(2)
        allow_Location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_Location.click()
        sleep(1)
        allow_Notifications = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        allow_Notifications.click()

        accept_cookies = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept_cookies.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def auto_swipe(self):
        while True:
            sleep(.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.closeMatch()

    def close_popup(self):
        not_interested = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        not_interested.click()
        close = self.driver.find_element_by_xpath('')


bot = swipeBot()

bot.login
