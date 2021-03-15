#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: market_page.py
@time: 2021/3/15 13:59
@desc: 
"""
import yaml
from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage
from page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        # self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')  # search
        self.parse("../page/market_page.yaml", "goto_search")
        return SearchPage(self.driver)
