#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: base_page.py
@time: 2021/3/12 10:48
@desc: 
"""
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy
from page.handle_blacklist import handle_blacklist
from page.logger import log


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_blacklist
    def find(self, locator, value):
        log.info("find " + value)
        element = self.driver.find_element(locator, value)
        return element

    def finds(self, locator, value):
        elements = self.driver.find_elements(locator, value)
        return elements

    def find_and_click(self, locator, value):
        self.find(locator, value).click()

    def find_and_send(self, locator, value, content):
        self.find(locator, value).send_keys(content)

    def swipe_find(self, text, nums=3):
        # default set to swipe triple times
        for num in range(nums):
            if num == nums - 1:
                self.driver.implicitly_wait(5)  # set back to caps
                raise NoSuchElementException(f"Have found {nums} times, but not found.")
            self.driver.implicitly_wait(1)  # enhance performance
            try:  # if element displays on current screen, then just return element directly
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)  # set back to caps
                return element
            except:  # if current page is needed to swipe up for more details, then swipe until finding out element
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.2

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def parse(self, yaml_path, func_name):
        # analysis keyword, complete the relate action
        with open(yaml_path, "r", encoding="utf-8") as f:
            function = yaml.load(f)
        # take function out from keyword
        steps = function.get(func_name)
        # analysis each group of keywords
        for step in steps:
            # if find out the keyword is find and click, then call the find and click function
            if step.get("action") == "find_and_click":
                self.find_and_click(step.get('locator'), step.get('value'))
            elif step.get("action") == "find_and_send":
                self.find_and_send(step.get('locator'), step.get('value'), step.get('content'))

    def screenshot(self):
        return self.driver.get_screenshot_as_png()
