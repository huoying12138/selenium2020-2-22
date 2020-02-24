# -*- coding: utf8
# @Time: 2020/2/22 14:56
# @Author: Blue_Sky
# @File: seleniumIndex.py
# @descriptions: none
import scrapy
from selenium import webdriver
from selenium.webdriver import common, support, ActionChains
import time


url1 = 'https://www.taobao.com/'
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser = webdriver.Chrome()
browser.get(url)
# put = browser.find_element_by_id('q')
# put.send_keys('iphone')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')
browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[1])
browser.get(url1)

browser.switch_to.window(browser.window_handles[0])
browser.switch_to.frame('iframeResult')
s = browser.find_element_by_css_selector('#draggable')
t = browser.find_element_by_css_selector('#droppable')
action = ActionChains(browser)
action.drag_and_drop(s, t)
action.perform()
time.sleep(8)
browser.close()
