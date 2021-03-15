#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: logger.py
@time: 2021/3/15 16:35
@desc: 
"""
import logging
import logging.handlers


# define basic content of log
def log_init():
    # set up the format
    log_format_str = '[%(levelname)s] %(asctime)s %(filename)s:%(lineno)d:%(funcName)s: %(message)s'
    format = logging.Formatter(log_format_str)
    # get log according to log identifier
    root = logging.getLogger("my_log")
    # add file handler
    h = logging.handlers.RotatingFileHandler("./tmp.log", mode='a', encoding="utf-8")
    h.setFormatter(format)
    # add stream handler
    s = logging.StreamHandler()
    s.setFormatter(format)
    root.addHandler(h)
    root.addHandler(s)
    root.setLevel(logging.INFO)


# init and get log
log = logging.getLogger("my_log")
