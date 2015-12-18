#coding:utf-8

from selenium import  webdriver
import  sys

# driver=webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.get('http://www.baidu.com')
# driver.find_element_by_id('u1').find_element_by_class_name('lb').click()
# driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('username')
# driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys('passwd')
# driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
# driver.quit()

from utility import  excelUtils
from config import  actionKeywords



class DrivenScript(object):
	def run(self):
		for i in range(0,9):
			excel=excelUtils.ExcelUtils()
			sActionKeyword=excel.readExcel(i,3)
			keyWord=actionKeywords.ActionKeywords()
			if(cmp(sActionKeyword,'openBrowser')):
				keyWord.openBrowser()
			if(cmp(sActionKeyword,'navigate')):
				keyWord.navigate()
			if(cmp(sActionKeyword,'click_Login')):
				keyWord.click_Login()
			if(cmp(sActionKeyword,'input_Username')):
				keyWord.input_Username()
			if(cmp(sActionKeyword,'input_Password')):
				keyWord.input_Password()
			if(cmp(sActionKeyword,'waitFor')):
				keyWord.waitFor()
			if(cmp(sActionKeyword,'click_Login_Button')):
				keyWord.click_Login_Button()
			if(cmp(sActionKeyword,'closeBrowser')):
				keyWord.closeBrowser()
			break
			sys.exit(1)


if __name__=='__main__':
	script=DrivenScript()
	script.run()
