# -*- coding: utf8
# @Time: 2020/2/28 2:43
# @Author: Blue_Sky
# @File: setProxy.py
# @descriptions: none

from selenium import webdriver

import requests


# 36.157.89.29
url = 'http://httpbin.org/get'
proxy = '221.225.71.142:8118'   # from https://www.xicidaili.com/
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://221.225.71.142:8118')
browser = webdriver.Chrome(chrome_options=chrome_options)


# browser = webdriver.Chrome()
# response = browser.get(url)
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
# }
# response = requests.get(url=url, proxies=proxies)
# print(response.text)