#coding:utf-8

from selenium import  webdriver
import  sys
from utility.excelUtils import  ExcelUtils
from config.actionKeywords import  ActionKeywords



# driver=webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.get('http://www.baidu.com')
# driver.find_element_by_id('u1').find_element_by_class_name('lb').click()
# driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('username')
# driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys('passwd')
# driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
# driver.quit()





class DrivenScript():
	@staticmethod
	def run():
		for i in range(0,9):
			driver=webdriver.Firefox()
			excel=ExcelUtils()
			sActionKeyword=excel.readExcel(i,3)
			keyWord=ActionKeywords()
			if(cmp(sActionKeyword,'openBrowser')):
				keyWord.openBrowser(driver)
			if(cmp(sActionKeyword,'navigate')):
				keyWord.navigate(driver)
			if(cmp(sActionKeyword,'click_Login')):
				keyWord.click_Login(driver)
			if(cmp(sActionKeyword,'input_Username')):
				keyWord.input_Username(driver)
			if(cmp(sActionKeyword,'input_Password')):
				keyWord.input_Password(driver)
			if(cmp(sActionKeyword,'waitFor')):
				keyWord.waitFor(driver)
			if(cmp(sActionKeyword,'click_Login_Button')):
				keyWord.click_Login_Button(driver)
			if(cmp(sActionKeyword,'closeBrowser')):
				keyWord.closeBrowser(driver)
			break
			sys.exit(1)

#关键字框架的第二版本
class DrivenScript(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Firefox()

	def test_Second(self):
		for i in range(0,9):
			excel=ExcelUtils()
			sActionKeyword=excel.readExcel(i,3)
			self.execute_action(sActionKeyword)

	def execute_action(self,keyword):
		keywords=ActionKeywords()
		if hasattr(keywords,keyword):
			getattr(keywords,keyword)(self.driver)
if __name__=='__main__':
	unittest.main(verbosity=2)





