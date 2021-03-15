#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: handle_blacklist.py
@time: 2021/3/15 11:58
@desc: 
"""
import allure
from appium.webdriver.common.mobileby import MobileBy
from page.logger import log


def handle_blacklist(func):
    # black list including such as alert window, phone, message, ads
    black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']

    def wrapper(*args, **kwargs):  # args is array, kwargs is dictionary
        self = args[0]
        try:
            log.info("find " + args[2])
            return func(*args, **kwargs)
        except Exception:
            allure.attach(self.screenshot(), attachment_type=allure.attachment_type.PNG)
            # following steps are in order to take out and handle all blocker
            for ele_xpath in black_list:
                # find the blocker whether exists
                eles = self.finds(MobileBy.XPATH, ele_xpath)
                # blocker exists, need to kill
                if len(eles) > 0:
                    eles[0].click()
                    # keep killing until all blockers are handled
                    return func(*args, **kwargs)

    return wrapper