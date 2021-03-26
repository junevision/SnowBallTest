#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: recursion.py
@time: 2021/3/26 17:24
@desc: Basic skeleton of a mitmproxy addon.
"""
import json
from mitmproxy import ctx, http


class June:

    def request(self, flow: http.HTTPFlow):
        pass

    def response(self, flow: http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            data = self.handle_data(json.loads(flow.response.text))
            flow.response.text = json.dumps(data)

    def handle_data(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                data[key] = self.handle_data(value)
        elif isinstance(data, list):
            # data_new = []
            # for item in data:
            #     data_new.append(handle_data(item))
            data = [self.handle_data(item) for item in data]
        elif isinstance(data, str):
            data = data
            # data = data + "a"
        elif isinstance(data, bool):
            data = data
        elif isinstance(data, (int, float)):
            data = data * 1
        else:
            data = data
        return data


addons = [
    June()
]
