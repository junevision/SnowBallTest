#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: map_local.py
@time: 2021/3/23 10:20
@desc: Basic skeleton of a mitmproxy addon.
"""
from mitmproxy import ctx, http


class Junevision:

    def request(self, flow: http.HTTPFlow):
        """
        use request event to complete map local
        :param flow:
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            with open("/Users/jun_lei/Documents/Jun/code/python/SnowBallTest/test_mock/test.json",
                      encoding="utf-8") as f:
                # assign value to flow.response attribute
                # call mitmproxy response object make function
                # the data in make function in response body is str
                flow.response = http.HTTPResponse.make(200,  # (optional) status code
                                                       f.read(),  # (optional) content
                                                       {"Content-Type": "text/html"}  # (optional) headers
                                                       )

    def response(self, flow: http.HTTPFlow):
        pass


# addons is a must name for mitmproxy, store instance
addons = [
    Junevision()
]
