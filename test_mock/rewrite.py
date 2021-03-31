#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: rewrite.py
@time: 2021/3/23 10:15
@desc: Basic skeleton of a mitmproxy addon.
"""
import json
from mitmproxy import ctx, http


class June:

    def request(self, flow):
        pass

    def response(self, flow: http.HTTPFlow):
        """
        use response event to complete rewrite
        :param flow:
        """
        # verify url request, whether it includes url info
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # receive response data info
            # flow.response.text is str attribute
            # str -> python json
            data = json.loads(flow.response.text)
            percents_items = [0, 0.1, -0.1, -100, 100, 1000]
            for item in range(len(percents_items)):
                data["data"]["items"][item]["quote"]["percent"] = percents_items[item]
                print(item)
            # python json -> str
            flow.response.text = json.dumps(data)
            print(flow.response.text)


# addons is a must name for mitmproxy, store instance
addons = [
    June()
]
