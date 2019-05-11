import pymysql


def readSQL():

    # 打开数据库连接
    db = pymysql.connect("localhost","root","root","test")

    # 使用curson()方法创建一个游标对象cursor
    cursor = db.cursor()

    '''
    # 使用execute()方法执行sql查询
    cursor.execute("SELECT VERSION()")

    # 使用fetchone()方法获取单条数据
    data = cursor.fetchone()

    print("Database version : %s"% data)

    # 使用execute() 方法执行SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    '''
    # 使用预处理语句创建表
    sql0 = """CREATE TABLE EMPLOYEE(
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT)"""
    # cursor.execute(sql0)
    # 插入到数据库
    sql1 = """INSERT INTO EMPLOYEE(FIRST_NAME,
            LAST_NAME,AGE,SEX,INCOME)
            VALUES('ZHANG','QUAN','23','M',10000)"""

    # sql2 = "INSERT INTO EMPLOYEE(FIRST_NAME,\
    #        LAST_NAME,AGE,SEX,INCOME)\
    #        VALUES('%s', '%s', '%d', '%c', '%d')"%\
    #       ('Mac', 'Mohan', 20, 'M', 2000)"
    # 更新列表信息
    # sql4 = "update employee set age = age + 1 where sex = '%c'"%('M')
    try:
        # 执行sql语句
        cursor.execute(sql1)
        
        # 提交到数据库执行
        db.commit()
        # 查询列表信息
        sql3 = "select * from employee"
        cursor.execute(sql3)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
                fname = row[0]
                lname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                # 打印结果
                print ("fname = %s, lname = %s, age = %d, sex = %s, income = %d"%\
                    (fname, lname, age, sex, income))
    except:
        # 如果发生错误则回滚
        db.rollback()
        print ("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
if __name__ == '__main__':
    readSQL()
    print("programe run over")
