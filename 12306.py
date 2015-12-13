#!/usr/bin/python
# it is a test!
from splinter import Browser

with Browser() as browser:
	url="https://kyfw.12306.cn/otn/leftTicket/init"
	browser.visit(url)
	browser.fill('fromStationText',"splinter")
	#button=browser.find_by_id(u"su")
	#button.click()
	if browser.is_text_present('splinter'):
		print "sucess"
	else:
		print"error"
