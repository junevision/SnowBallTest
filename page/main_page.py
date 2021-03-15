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
from page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        # click on blue pen in order to activate alert window which is in black list
        # self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        # self.find_and_click(MobileBy.XPATH, '//*[@text="行情"]')
        self.parse("../page/main_page.yaml", "goto_market")
        return MarketPage(self.driver)

