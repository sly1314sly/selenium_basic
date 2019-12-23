import xlrd

def get_userInfo():
    wk = xlrd.open_workbook('data/user.xls')
    ws = wk.sheet_by_name('userinfo')
    ncols = ws.ncols
    nrows = ws.nrows

    alldata = []
   
    for rowNum in range(nrows):
        rowdata = []
        for x in range(ncols):
            print("第{}列，{}行".format(x,rowNum),ws.cell_value(rowNum,x))
            rowdata.append(ws.cell_value(rowNum,x))
            print("rowdata===",rowdata)
        alldata.append(rowdata)

    return alldata



    # [['username','passwd','status','asserText'],['username','passwd','status','asserText'],['username','passwd','status','asserText']]

    

get_userInfo()