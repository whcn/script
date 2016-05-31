#!/usr/bin/python
#-*- coding:utf-8 -*-

username = '329722594@qq.com'
passwd = 'vimeremacser'

province2city = {
         '北京':['大兴',],
         '辽宁':['大连',],
         '上海':['青埔',],
         '安徽':['合肥',],
         '山东':['青岛',],
         '海南':['海口',]
         }

provinces_xpath = {
        '北京':'//*[@id="citySelect"]/dd[1]/a',
        '辽宁':'//*[@id="citySelect"]/dd[6]/a',
        '上海':'//*[@id="citySelect"]/dd[9]/a',
        '安徽':'//*[@id="citySelect"]/dd[12]/a',
        '山东':'//*[@id="citySelect"]/dd[15]/a',
        '海南':'//*[@id="citySelect"]/dd[21]/a'
        }
city_xpath = {
        '大兴':'//*[@id="station_ids[]"]',
        '大连':'//*[@id="station_ids[]"]',
        '青埔':'//*[@id="station_ids[]"]',
        '合肥':'//*[@id="station_ids[]"]',
        '青岛':'//*[@id="station_ids[]"]',
        '海口':'//*[@id="station_ids[]"]'
        }
