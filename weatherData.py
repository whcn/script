#!/usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

# ----------------cookie-------------------------
#  PHPSESSID     ->  5t8263n40fqcobi8c9o8a5ql05
#  userLoginKey  ->  d3320017c396c8e84c9c19a71e16b871
#  SERVERID      ->  3de774487f1a2b08a62184a804717207|1464533845|1464533824
#  userName      ->  FA21028B9C8D6F13176B69DC8E17B240
#  trueName      ->  %E5%90%B4%E7%84%95
# ----------------cookie-------------------------
driver.get('http://data.cma.cn/data/detail/dataCode/J.0012.0004P.html')
driver.add_cookie({'name':'userLoginKey', 'value':'d3320017c396c8e84c9c19a71e16b871'})
driver.add_cookie({'name':'userName', 'value':'FA21028B9C8D6F13176B69DC8E17B240'})
driver.add_cookie({'name':'trueName', 'value':'%E5%90%B4%E7%84%95'})
driver.add_cookie({'name':'PHPSESSID', 'value':'5t8263n40fqcobi8c9o8a5ql05'})
driver.add_cookie({'name':'SERVERID', 'value':'3de774487f1a2b08a62184a804717207'})
driver.get('http://data.cma.cn/data/detail/dataCode/J.0012.0004P.html')

provices = {
        '北京':'//*[@id="citySelect"]/dd[1]/a',
        '辽宁':'//*[@id="citySelect"]/dd[6]/a',
        '上海':'//*[@id="citySelect"]/dd[9]/a',
        '安徽':'//*[@id="citySelect"]/dd[12]/a',
        '山东':'//*[@id="citySelect"]/dd[15]/a',
        '海南':'//*[@id="citySelect"]/dd[21]/a'
        }
city = {
        '大兴':'//*[@id="station_ids[]"]',
        '大连':'//*[@id="station_ids[]"]',
        '青埔':'//*[@id="station_ids[]"]',
        '合肥':'//*[@id="station_ids[]"]',
        '青岛':'//*[@id="station_ids[]"]',
        '海口':'//*[@id="station_ids[]"]'
        }

driver.find_element_by_xpath('//*[@id="sub-body-contentDiv"]/div[2]/div[3]/input').click() #降水量
driver.find_element_by_xpath(provices['安徽']).click()
driver.find_element_by_xpath(city['合肥']).click()
driver.find_element_by_xpath('//*[@id="queryForm"]/div/input[3]').click()





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
