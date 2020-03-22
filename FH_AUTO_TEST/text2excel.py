def split_1(line, str):
    '''

    文件中解析每一行，如果有冒号的，就解析冒号前的文字和冒号后的文字，返回一个字典

    '''
    if len(line.split(':', 1)) > 1 and (str in line.split(':', 1)[0]):
        return {str: line.split(':',1)[1].strip()}
    elif len(line.split('：', 1)) > 1 and (str in line.split('：', 1)[0]):
        return {str: line.split('：', 1)[1].strip()}
    else:
        return False

def create_date(path):
    '''

    读文件，解析关键字
    '''
    f = open(path,encoding='utf-8')
    line = True
    list=[]
    dic ={}
    while line :
        line = f.readline()
        if not ('----' in line.strip()):
            if split_1(line,u'软件开发号'):
                dic.update(split_1(line, u'软件开发号'))
            elif split_1(line, 'Date'):
                dic.update(split_1(line, 'Date'))
            elif split_1(line, '代码提交人'):
                dic.update(split_1(line, '代码提交人'))
            elif split_1(line,u'功能点'):
                dic.update(split_1(line, u'功能点'))
            elif split_1(line, u'来源项目编号/版本简称'):
                dic.update(split_1(line, u'来源项目编号/版本简称'))
            elif split_1(line,'问题分类'):
                dic.update(split_1(line, '问题分类'))
            elif split_1(line,u'功能说明/问题现象'):
                dic.update(split_1(line, u'功能说明/问题现象'))
            elif split_1(line,u'方案/解决办法'):
                dic.update(split_1(line,u'方案/解决办法'))
            elif split_1(line, u'报告相关路径'):
                dic.update(split_1(line, u'报告相关路径'))
            elif split_1(line, u'是否完成自测'):
                dic.update(split_1(line, u'是否完成自测'))
            else:
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


def write_excel(path ,list):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('demo2')
    row0 = [u'软件开发号', u'Date', u'代码提交人',u'功能点', u'来源项目编号/版本简称', '问题分类',u'功能说明/问题现象',u'方案/解决办法',u'报告相关路径',u'是否完成自测']
    for i in range(len(row0)):
        data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    print(list)
    for i in range(len(list)):
        data_sheet.write(i + 1, 0, list[i].get(u'软件开发号'), set_style('Times New Roman', 220,))
        data_sheet.write(i + 1, 1, list[i].get('Date'), set_style('Times New Roman', 220, ))
        data_sheet.write(i + 1, 2, list[i].get('代码提交人'), set_style('Times New Roman', 220,))
        data_sheet.write(i + 1, 3, list[i].get(u'功能点'), set_style('Times New Roman', 220))
        data_sheet.write(i + 1, 4, list[i].get('来源项目编号/版本简称'), set_style('Times New Roman', 220))
        data_sheet.write(i + 1, 5, list[i].get(u'问题分类'), set_style('Times New Roman', 220))
        data_sheet.write(i + 1, 6, list[i].get(u'功能说明/问题现象'), set_style('Times New Roman', 220))
        data_sheet.write(i + 1, 7, list[i].get(u'方案/解决办法'), set_style('Times New Roman', 220))
        data_sheet.write(i + 1, 8, list[i].get(u'报告相关路径'), set_style('Times New Roman', 220))
        data_sheet.write(i + 1, 9, list[i].get(u'是否完成自测'), set_style('Times New Roman', 220))


    # 保存文件
    workbook.save(path)


if __name__ == '__main__':
    # 设置 SVN导出的原始数据的路劲
    path_in = 'D:\\DaiXiong\\Python\\practice\\svn_log.log'
    list = create_date(path_in)
	# 设置 导出excel的路径
    path_out = 'D:/DaiXiong/Python/practice/demo.xls'
    write_excel(path_out ,list)
    print(u'文件创建成功')

