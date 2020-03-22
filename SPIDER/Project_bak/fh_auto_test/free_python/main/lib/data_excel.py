import xlwt
from xlutils.copy import copy
import xlrd
import os

class DataWtExcel():

    def create_excel(self):
        excel_cpu_free = xlwt.Workbook()
        sheet = excel_cpu_free.add_sheet('cpu_free_sheet')
        excel_cpu_free.save('cpu_free.xls')

    def write_excel(self,crosswise,vertical,content):
        # xlutils:修改excel
        book1 = xlrd.open_workbook('cpu_free.xls')
        book2 = copy(book1)  # 拷贝一份原来的excel
        sheet = book2.get_sheet(0)
        sheet.write(crosswise,vertical,content)
        book2.save('cpu_free.xls')

    def run_data_excel(self,crosswise,vertical,content):
        dataExcel = DataWtExcel()
        if os.path.isfile('cpu_free.xls'):
            dataExcel.write_excel(crosswise, vertical, content)
        else:
            dataExcel.create_excel()
            dataExcel.write_excel(crosswise, vertical, content)

if __name__ == '__main__':
    data_wt_excel = DataWtExcel()
    data_wt_excel.run_data_excel(crosswise=0,vertical=1,content=6)