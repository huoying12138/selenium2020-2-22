# -*- coding: utf8
# @Time: 2020/2/23 17:01
# @Author: Blue_Sky
# @File: selenium_taobao_search.py
# @descriptions: none
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.parse import quote
from pyquery import PyQuery as pq
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import TimeoutException, NoSuchElementException


import time
import requests
import pymongo


def index_page(page):
    key = 'ipad'
    print('正在抓取：', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(key)
        browser.get(url)
        time.sleep(2)
        if page > 1:
            window.setTimeout(function, milliseconds)
            inputs = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            # browser.execute_script('myVar=window.setInterval(function(){}, 2000)')
            # browser.execute_script('clearTimeout(myVar)')
            browser.execute_script('document.getElementById("srp-footer").scrollIntoView({block: "end", behavior: "smooth"})')
            time.sleep(3)
            submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            inputs.clear()
            inputs.send_keys(page)
            submit.click()
            browser.execute_script('window.scrollTo(0,0)')
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
        time.sleep(3)
    except TimeoutException:
        print('time out')


def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('.m-itemlist .items .item').items()
    for item in items:
        product = {
            'index': item.attr('data-index'),
            'image': 'http:' + item.find('.img').attr('src'),
            'price': item.find('.price').text(),
            'deal-cnt': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text(),
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db_test = client.test
    coll_test = db_test.collection
    try:
        if coll_test.insert(result):
            print('save success')
    except Exception:
        print('save failed')


def login():
    try:
        to_login = browser.find_element_by_css_selector('.J_Quick2Static')
        to_login.click()

        time.sleep(2)

        user = browser.find_element_by_name('TPL_username')
        pwd = browser.find_element_by_name('TPL_password')

        user.clear()
        user.send_keys('13520502028')
        user.send_keys(Keys.RETURN)

        time.sleep(2)

        pwd.clear()
        pwd.send_keys('369369369aaa')
        pwd.send_keys(Keys.RETURN)

        time.sleep(2)

        print('login...')
        log = browser.find_element_by_id('J_SubmitStatic')
        log.click()

        print('loading...')

        time.sleep(4)
    except TimeoutException:
        print('time out')
    except NoSuchElementException:
        print('no element')


def main():
    for i in range(1, 4):
        index_page(i)


# set Chrome headless mode
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)

browser = webdriver.Chrome()
browser.maximize_window()
wait = WebDriverWait(browser, 4)
if __name__ == '__main__':
    main()