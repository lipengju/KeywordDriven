#coding:utf-8

from selenium import  webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
import  time  as t

class Page(object):
	# def __init__(self,driver):
	# 	self.driver=driver

	def find_element(self,*loc):
		try:
			return  self.driver.find_element(*loc)
		except (NoSuchElementException,KeyError,ValueError,Exception),e:
			print 'Error details:%s'%(e.args[0])

	@property
	def wait(self):
		t.sleep(2)

class ActionKeywords(Page):
	def openBrowser(self,driver):
		driver.maximize_window()
		print 'openBrowser'

	def navigate(self,driver):
		driver.get('http://www.baidu.com')
		driver.implicitly_wait(30)
		print 'navigate'

	def click_Login(self,driver):
		self.wait
		driver.find_element_by_id('u1').find_element_by_class_name('lb').click()
		print 'Click_Login'

	def input_Username(self,driver):
		driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('username')
		print 'input_Username'

	def input_Password(self,driver):
		driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys('password')
		print 'input_Password'

	def waitFor(self,driver):
		self.wait
		print 'waitFor'

	def click_Login_Button(self,driver):
		self.wait
		driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
		print 'click_Login_Button'

	def closeBrowser(self,driver):
		self.wait
		driver.quit()
		print 'closeBrowser'