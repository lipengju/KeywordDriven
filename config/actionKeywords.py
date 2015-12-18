#coding:utf-8

from selenium import  webdriver
import  time  as t

class Page(object):
	def __init__(self,driver):
		self.driver=driver

class ActionKeywords(Page):
	def __init__(self):
		self.driver=webdriver.Firefox()

	def openBrowser(self):
		self.driver.maximize_window()
		print 'openBrowser'

	def navigate(self):
		self.driver.get('http://www.baidu.com')
		self.driver.implicitly_wait(30)
		print 'navigate'

	def click_Login(self):
		t.sleep(3)
		self.driver.find_element_by_id('u1').find_element_by_class_name('lb').click()
		print 'Click_Login'

	def input_Username(self):
		self.driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('username')
		print 'input_Username'

	def input_Password(self):
		self.driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys('password')
		print 'input_Password'

	def waitFor(self):
		t.sleep(2)
		print 'waitFor'

	def click_Login_Button(self):
		self.driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
		print 'click_Login_Button'

	def closeBrowser(self):
		self.driver.quit()
		print 'closeBrowser'