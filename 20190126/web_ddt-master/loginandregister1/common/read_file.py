
import csv
import xlrd


def get_csv_data(csv_path):
    """
    从csv文件中读取数据 将数据以列表的形式返回

    @type csv_path:string
    @param csv_path: csv file path
    @return list
    """
    rows = []
    csv_data = open(csv_path)
    content = csv.reader(csv_data)
    next(content,None)

    for row in content:
        rows.append(row)
    
    return rows



def get_xls_data(xlspath):
    """
    从xls文件中读取数据 将数据以列表的形式返回

    @type xls_path:string
    @param xls_path: xls file path
    @return list
    """
    book = xlrd.open_workbook(xlspath)
    sh = book.sheet_by_index(0)
    rows = sh.nrows
    ncols = sh.ncols
    alldata=[]
    for x in range(rows-1):
        row = []
        for y in range(ncols):
            row.append(sh.cell_value(x+1, y))
        alldata.append(row)

    return alldata
