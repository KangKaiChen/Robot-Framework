from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import psutil
from robot.api import logger
class Steps:

    def __init__(self):  # 使用 Chrome
        self.driver = webdriver.Chrome()

    def open_browser(self, login_url):

        self.driver.get(login_url)
        logger.info("Browser opened with URL: " + login_url)

    def maximize_browser_window(self):
        self.driver.maximize_window()
        time.sleep(1)
        logger.info("Browser window maximized")

    def set_selenium_speed(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info(f"Selenium speed set to {seconds} seconds")

    def input_the_username(self, username):
        # 定位到用户名输入框并输入
        self.driver.find_element(By.NAME, 'nosave_Username').send_keys(username)
        logger.info(f"Entered username: {username}")

    def input_the_password(self, password):
        # 定位到密码输入框并输入
        self.driver.find_element(By.ID, 'id_nosave_Password').send_keys(password)
        logger.info("Entered password")

    def click_mobile_checkbox(self):
        # 勾选或取消勾选复选框
        checkbox = self.driver.find_element(By.ID, 'cb_mobile')
        if not checkbox.is_selected():
            checkbox.click()
        logger.info("Clicked on mobile checkbox")

    def click_OK_button_to_submit(self):
        # 提交表单
        self.driver.find_element(By.ID, 'id_login').click()
        time.sleep(3)
        logger.info("Login form submitted")

    def close_my_browser(self):
        self.driver.quit()
        logger.info("Browser closed")
        kill_browser_processes()
    def my_LinkStation_should_be_found(self):
        modelname_prefix = self.driver.find_element(By.XPATH, '//*[@class="modelname_prefix"]')


    def Go_to_the_Firmware(self):
        self.driver.find_element(By.ID, 'panel_ADVANCED').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'AT_ADMIN').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'sub_meu6_3').click()
        time.sleep(2)
        logger.info("Go_to_the_Firmware Success")

    def Firmware_Update(self,file):

            iframe = self.driver.find_element(By.TAG_NAME, 'iframe')
            
            # 切换到 iframe
            self.driver.switch_to.frame(iframe)
            logger.info("Switched to iframe")
            time.sleep(1)  
            self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(file)
            logger.info(f"File {file} has been uploaded.")
            time.sleep(2)  
            time.sleep(270)  
            logger.info("Firmware_Update ")

def kill_browser_processes():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in ['chromedriver.exe', 'chrome.exe']:  # 根據使用的瀏覽器調整名稱
            proc.terminate()  # 強制關閉進程


