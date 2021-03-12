#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_market.py
@time: 2021/3/12 11:14
@desc: 
"""
from page.app import App


class TestMarket:
    def setup(self):
        self.app = App()

    def test_goto_market(self):
        self.app.start().goto_main().goto_market()