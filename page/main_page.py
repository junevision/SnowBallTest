#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: main_page.py
@time: 2021/3/12 11:07
@desc: 
"""
from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage


class MainPage(BasePage):
    def goto_market(self):
        # click on blue pen in order to activate alert window which is in black list
        # self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        self.find_and_click(MobileBy.XPATH, '//*[@text="行情"]')
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')  # search
        # input alibaba
        self.find_and_send(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
