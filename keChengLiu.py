#!/usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver
import random
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://219.219.220.222/kechengliu/?fromuser=toshiba438')

for i  in xrange(10):
    browser.implicitly_wait(30)
    browser.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[4]/a').click()

    username = random.randint(100000000, 999999999) 
    passwd = 'passwd'
    email = str(username) + '@mail.ustc.edu.cn'

    check = '该Email地址已被注册'
    while check == '该Email地址已被注册':
        browser.find_element_by_id('USTCkecheng2014name').clear()
        browser.find_element_by_id('USTCkecheng2014pwd').clear()
        browser.find_element_by_id('USTCkecheng2014pwd2').clear()
        browser.find_element_by_id('USTCkecheng2014email').clear()

        browser.find_element_by_id('USTCkecheng2014name').send_keys(username)
        browser.find_element_by_id('USTCkecheng2014pwd').send_keys(passwd)
        browser.find_element_by_id('USTCkecheng2014pwd2').send_keys(passwd)
        browser.find_element_by_id('USTCkecheng2014email').send_keys(email)
        browser.find_element_by_id('registerformsubmit').click()

        try:
            check = browser.find_element_by_id('chk_USTCkecheng2014email').text
        except NoSuchElementException:
            break;

    browser.implicitly_wait(30)
    browser.find_element_by_xpath('//*[@id="um"]/p[1]/a[6]').click()
    time.sleep(3)
browser.quit()
