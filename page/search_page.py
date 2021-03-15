#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: search_page.py
@time: 2021/3/15 13:59
@desc: 
"""
import yaml
from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        # input alibaba
        # self.find_and_send(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
        self.parse("../page/search_page.yaml", "search")
