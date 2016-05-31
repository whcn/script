#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.utils import parseaddr, formataddr
from email.header import Header
from email.mime.text import MIMEText
import smtplib

import urllib2

# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = 'autoemailpython@sina.com'
# password = 'toshiba438'
# to_addr = '329722594@qq.com'
# smtp_server = 'smtp.sina.com'

# msg = MIMEText('third test', 'plain', 'utf-8')
# msg['From'] = _format_addr('WuHuan <%s>' % from_addr)
# msg['To'] = _format_addr('administrator <%s>' % to_addr)
# msg['Subject'] = Header('天气预报', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server, 25)
# # server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, to_addr, msg.as_string())
# server.quit()

raw_info = urllib2.urlopen('http://www.weather.com.cn/weather/101220101.shtml#7d')
print raw_info.read()
