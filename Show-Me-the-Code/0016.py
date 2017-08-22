import os,json
from openpyxl import Workbook

def json2xlsx(xlsx_path,json_path):
    wb=Workbook()
    ws1=wb.active
    ws1.title=xlsx_path.split('.')[0].split('\\')[-1]
    with open(json_path) as f:
        fulljson=f.read()
    j=json.loads(fulljson)
    for i in j:
        ws1.append(i)
    wb.save(xlsx_path)

if __name__=='__main__':
    path=r'C:\Users\chauncey\Desktop'
    xlsx_name='numbers.xlsx'
    json_name='numbers.txt'
    json2xlsx(path+os.sep+xlsx_name,path+os.sep+json_name)
