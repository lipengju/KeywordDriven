#coding:utf-8

import  os,csv,xlrd
import  xml.dom.minidom

class Config(object):
	def __init__(self):
		pass

	@staticmethod
	def data_dirs():
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		DATA_DIRS = (
		os.path.join(BASE_DIR,  'dataEngine'),
		)
		d='/'.join(DATA_DIRS)
		return d

class ExcelUtils(object):
	def __init__(self):
		pass

	def readExcel(self,rowValue,colValue):
		book=xlrd.open_workbook(Config.data_dirs()+'/DataEngine.xlsx')
		sheet=book.sheet_by_index(0)
		return sheet.cell_value(rowValue,colValue)

	def readExcels(self):
		rows=[]
		book=xlrd.open_workbook(Config.data_dirs()+'/DataEngine.xlsx')
		sheet=book.sheet_by_index(0)
		for row in range(1,sheet.nrows):
			rows.append(list(sheet.row_values(row,0,sheet.ncols)))
		return rows


