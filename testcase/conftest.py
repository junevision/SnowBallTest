#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: conftest.py
@time: 2021/3/15 15:44
@desc: 
"""
import os
import signal
import subprocess
import pytest
from page.logger import log_init


@pytest.fixture(scope="module", autouse=True)
def record():
    log_init()
    # do something before testcases running
    cmd = "scrcpy -m 1000 -Nr tmp.mkv"  # shell command, activate scrcpy recording function
    p = subprocess.Popen(cmd, shell=True)  # optional: os.system
    yield
    # do something after testcases finish
    os.kill(p.pid, signal.SIGKILL)