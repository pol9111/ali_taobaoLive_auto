import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import *


class Action(object):
    def __init__(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "SM_G9500",
            "appPackage": "com.taobao.taobao",
            "appActivity": "com.taobao.tao.welcome.Welcome",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def entry(self):
        time.sleep(5)
        # 下滑
        self.driver.swipe(FLICK_START_X, FLICK_START_Y + 1500, FLICK_START_X, FLICK_START_Y)
        # 进入直播页
        el0 = self.driver.find_element_by_xpath(
            "//android.widget.FrameLayout[3]/android.widget.ImageView")
        el0.click()
        # 搜索直播
        el1 = self.driver.find_element_by_accessibility_id("search")
        el1.click()
        # 输入内容
        el2 = self.driver.find_element_by_id("com.taobao.taobao:id/taolive_search_edit_text")
        el2.clear()
        el2.send_keys("宝诗嫣")
        # 点击搜索
        el3 = self.driver.find_element_by_id("com.taobao.taobao:id/taolive_search_button")
        el3.click()
        # 点击第一个内容
        el4 = self.driver.find_element_by_id("com.taobao.taobao:id/taolive_search_avatar_info")
        el4.click()
        # 保持driver内存不被清掉
        # while True:
        #     try:
        #         self.driver.find_element_by_id("com.taobao.taobao:id/taolive_global_layout")
        #     except NoSuchElementException:
        #         pass
        #     time.sleep(10)


if __name__ == '__main__':
    action = Action()
    action.entry()

