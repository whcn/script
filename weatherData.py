#!/usr/bin/python
#-*- coding:utf-8 -*-

from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from location import *


# ----------------cookie-------------------------
#  PHPSESSID     ->  5t8263n40fqcobi8c9o8a5ql05
#  userLoginKey  ->  d3320017c396c8e84c9c19a71e16b871
#  SERVERID      ->  3de774487f1a2b08a62184a804717207|1464533845|1464533824
#  userName      ->  FA21028B9C8D6F13176B69DC8E17B240
#  trueName      ->  %E5%90%B4%E7%84%95
# ----------------cookie-------------------------
# driver.get('http://data.cma.cn/data/detail/dataCode/J.0012.0004P.html')
# driver.add_cookie({'name':'userLoginKey', 'value':'d3320017c396c8e84c9c19a71e16b871'})
# driver.add_cookie({'name':'userName', 'value':'FA21028B9C8D6F13176B69DC8E17B240'})
# driver.add_cookie({'name':'trueName', 'value':'%E5%90%B4%E7%84%95'})
# driver.add_cookie({'name':'PHPSESSID', 'value':'5t8263n40fqcobi8c9o8a5ql05'})
# driver.add_cookie({'name':'SERVERID', 'value':'3de774487f1a2b08a62184a804717207'})



# print city info
for item in province2city:
    # print(item, provice2city(item))
    print(item, end=": ")
    for j in province2city[item]:
        print(j, end=" ")
    print()

print()

# select province and city
province = raw_input('请选择省份:')
while not provinces_xpath.has_key(province):
    print("省份错误")
    province = raw_input('请选择省份:')
    
city = raw_input('请选择城市:')
while not city_xpath.has_key(city):
    print("城市错误")
    city = raw_input('请选择城市:')

month = input('请输入月份:')
while not (1 <= month and month <= 12):
    print("月份错误")
    month = input('请输入正确月份:')

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# login in website
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://data.cma.cn/data/detail/dataCode/J.0012.0004P.html')

driver.find_element_by_xpath('//*[@id="sub-body-contentDiv"]/div[2]/div[3]/input').click() #降水量
driver.find_element_by_id('userName').send_keys(username)
driver.find_element_by_id('password').send_keys(passwd)
driver.find_element_by_id('verifyCode').clear()
time.sleep(5)
driver.find_element_by_id('login').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="sub-body-contentDiv"]/div[2]/div[3]/input').click()

# select location and data
driver.find_element_by_xpath(provinces_xpath[province]).click()
driver.find_element_by_xpath(city_xpath[city]).click()
driver.find_element_by_id('dateS').clear()
driver.find_element_by_id('dateS').send_keys('2016-' + '%02d' % month + '-01')
driver.find_element_by_id('dateE').clear()
driver.find_element_by_id('dateE').send_keys('2016-' + '%02d' % month + '-' + str(days[month])) 

driver.find_element_by_xpath('//*[@id="queryForm"]/div/input[3]').click()
driver.find_element_by_id('buttonAddCar').click()



# driver.find_element_by_xpath('//*[@id="loginStatus"]/a/span').click()
# driver.find_element_by_id('userName').clear()
# driver.find_element_by_id('password').clear()
# driver.find_element_by_id('userName').send_keys('329722594@qq.com')
# driver.find_element_by_id('password').send_keys('vimeremacser')
# time.sleep(5)
# driver.find_element_by_id('login').click()

# radar = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/div[1]/ul/li[4]/div/div[1]/div')
# rainfall = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/div[1]/ul/li[4]/div/div[4]/div[6]/div[4]/a')

# ActionChains(driver).move_to_element(radar).click(rainfall).perform()
# driver.find_element_by_xpath('//*[@id="sub-body-contentDiv"]/div[2]/div[3]/input').click()

# time.sleep(2)
# driver.close()
