#read data from excel
import xlrd
data=xlrd.open_workbook('F:\开发中心年会节目.xlsx')
table=data.sheets()[0]
print(table.col_values(1))  #读取第二列
print(table.row_values(0))  #读取表头
