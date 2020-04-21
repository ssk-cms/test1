import xlrd

'''
读取excel工作表内容工具类
'''


class OpenExcelUtils():

    def open_excel(self, tableName, sheetName):
        try:
            book = xlrd.open_workbook(tableName)
        except:
            print("open excel file failed!")
        try:
            sheet = book.sheet_by_name(sheetName)
            return sheet
        except:
            print("locate worksheet in excel failed!")
