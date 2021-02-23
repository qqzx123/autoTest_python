import xlrd


class readExcel:
    #[{},{},{}]
    def read_excelDataDict(self,excel_name,sheet_num):
        workbook = xlrd.open_workbook(excel_name)
        sheet = workbook.sheet_by_index(sheet_num)
        # print(sheet.cell(0,0))
        rows = sheet.nrows
        cols = sheet.ncols
        list=[]
        for row in range(1,rows):
            dict={}
            for col in range(cols):
                dict[sheet.cell(0,col).value]=sheet.cell(row,col).value
            list.append(dict)
        return list

    #("    ",[[],[],[]])
    def read_excelDataList(self,excel_name,sheet_num):
        workbook = xlrd.open_workbook(excel_name)
        sheet = workbook.sheet_by_index(sheet_num)
        # print(sheet.cell(0,0))
        rows = sheet.nrows
        cols = sheet.ncols
        keylist=[]
        valuelist=[]
        #取键
        for col in range(cols):
            keylist.append(sheet.cell(0,col).value)
        key=",".join(keylist)                     #. join()： 连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
                                             #casesNumber,interfaceName,Interface,Priority,Precondition,Description,requestType,isMyToken,Parameters,otherParameters,Expect
       # 取值
        for row in range(1,rows):
            list=[]
            for col in range(cols):
                list.append(sheet.cell(row,col).value)
            valuelist.append(list)
        return key,valuelist

#
# if __name__ == '__main__':
#     jiekou=read()
#     b=jiekou.read_ex()
#     print(b)
# jiekou=read_excelDataList("C:\\Users\\Administrator\\Desktop\\wineReviewExcel1.xlsx")
# print(jiekou)