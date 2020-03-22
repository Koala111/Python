def split_1(line, str):
    '''

    文件中解析每一行，如果有冒号的，就解析冒号前的文字和冒号后的文字，返回一个字典

    '''
    if len(line.split("|")) == 4:
        return {
                "版本": line.split("|")[0].strip(),
                #"作者": line.split("|")[1].strip(),
                "日期": line.split("|")[2].strip().split(" ")[0].strip(),
                }
    elif len(line.split(':', 1)) > 1 and (line.split(':', 1)[0] == str):
        return {str: line.split(':', 1)[1].strip()}
    elif len(line.split('：', 1)) > 1 and (line.split('：', 1)[0] == str):
        return {str: line.split('：', 1)[1].strip()}
    else:
        return False


def create_date(path):
    '''

    读文件，解析关键字
    :param path:
    :return:

    '''

    #支持两种编码，gb2312和utf-8
    f = open(path,encoding='gb2312')
    try:
        line = f.readline()
    except UnicodeDecodeError:
        f = open(path, encoding='utf-8')
    line = True
    list = []
    dic = {}
    #标记上一行包含那个关键字
    flag = ""
    while line:
        line = f.readline()
        #
        if 'svn log' in line:
            dic.update({"模块": line.strip()})
            flag = ""
        elif not ('----' in line.strip()):
            if split_1(line, u'版本开发号'):
                dic.update(split_1(line, u'版本开发号'))
            if split_1(line, u'软件开发号'):
                dic.update(split_1(line, u'软件开发号'))
            elif split_1(line, u'版本'):
                dic.update(split_1(line, u'版本'))
            elif split_1(line, u'功能点'):
                dic.update(split_1(line, u'功能点'))
                flag = "功能点"
            elif split_1(line, u'代码提交人'):
                dic.update(split_1(line, u'代码提交人'))
            elif split_1(line, u'功能说明/问题现象'):
                dic.update(split_1(line, u'功能说明/问题现象'))
                flag = "功能说明/问题现象"
            elif split_1(line, u'方案/解决办法'):
                dic.update(split_1(line, u'方案/解决办法'))
                flag = "方案/解决办法"
            elif split_1(line, u'来源项目'):
                dic.update(split_1(line, u'来源项目'))
            elif split_1(line, u'日期'):
                dic.update(split_1(line, u'日期'))
            elif (flag == "功能点") and (line.strip() != ""):
                if not ((":"in line) or ("："in line) or ("|"in line)):
                    print(dic['功能点'])
                    dic['功能点'] = dic['功能点']+line.strip()
                    print(dic['功能点'])
                    flag = "功能点"
                else:
                    flag = ""
            elif (flag == "功能说明/问题现象") and (line.strip() != ""):
                if not ((":"in line) or ("："in line) or ("|"in line)):
                    print(dic['功能说明/问题现象'])
                    dic['功能说明/问题现象'] = dic['功能说明/问题现象']+line.strip()
                    print(dic['功能说明/问题现象'])
                    flag = "功能说明/问题现象"
                else:
                    flag = ""
            elif (flag == "方案/解决办法") and (line.strip() != ""):
                if not ((":"in line) or ("："in line) or ("|"in line)):
                    print(dic['方案/解决办法'])
                    dic['方案/解决办法'] = dic['方案/解决办法']+line.strip()
                    print(dic['方案/解决办法'])
                    flag = "方案/解决办法"
                else:
                    flag = ""
            else:
                flag = ""
                continue
        else:
            if not dic == {}:
                list.append(dic)
                dic = {}
    f.close()
    return list
import xlwt
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()   # 初始化样式
    font = xlwt.Font()       # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def write_excel(path, list):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('demo2')
    row0 = [u'版本开发号', u'对应修改点', 'Revision', u'功能点', 'Author', u'功能说明/问题现象',u'解决办法','项目', '日期']
    for i in range(len(row0)):
        data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    print(list)
    default_style = set_style('Times New Roman', 220, False)
    for i in range(len(list)):
        if u'模块'in list[i]:
            data_sheet.write_merge(i+1, i+1, 0, 6, list[i].get(u'模块'), default_style)
        else:
            print(list[i].get(u'功能点'))
            if list[i].get(u'版本开发号') != None:
                data_sheet.write(i+1, 0, list[i].get(u'版本开发号'), default_style)
            else:
                data_sheet.write(i + 1, 0, list[i].get(u'软件开发号'), default_style)
            data_sheet.write(i+1, 2, list[i].get(u'版本'), default_style)
            data_sheet.write(i+1, 3, list[i].get(u'功能点'), default_style)
            data_sheet.write(i+1, 4, list[i].get(u'代码提交人'), default_style)
            data_sheet.write(i+1, 5, list[i].get(u'功能说明/问题现象'), default_style)
            data_sheet.write(i+1, 6, list[i].get(u'方案/解决办法'), default_style)
            data_sheet.write(i+1, 7, list[i].get(u'来源项目'), default_style)
            data_sheet.write(i + 1, 8, list[i].get(u'日期'), default_style)
    # 保存文件
    workbook.save(path)

import os
#提取文件夹下的地址+文件名，源文件设定排序规则
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                 L.append(file)
        return L


if __name__ == '__main__':
    # 读取文件夹下所有文件
    root_path_in = "E:/python/log"
    root_path_out = "E:/python/log"

    L = file_name(root_path_in)

    # 设置 SVN导出的原始数据的路径
    for file_str in L:
        path_in = root_path_in + "/" + file_str
        list = create_date(path_in)

	    # 设置 导出excel的路径
        path_out_name = file_str.replace("txt", "xls")
        path_out = root_path_out + "/" + path_out_name
        write_excel(path_out ,list)
        print(u'文件创建成功')

"""
  # path_in = 'D:/work/文档/pythen/leaning/HSWB_log2.txt'
  #   list = create_date(path_in)
	# # 设置 导出excel的路劲
  #   path_out = 'D:/work/文档/pythen/leaning/HSWB_log2.xls'
  #   write_excel(path_out ,list)
  #   print(u'文件创建成功')
"""

