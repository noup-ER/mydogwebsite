import pymysql
import json
def getsql(host,user,port,db,pwd,sql,flag):
    # 打开数据库连接
    db = pymysql.connect(host=host, user=user, port=port, db=db,password=pwd)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    if flag == "search":
        # 执行SQL语句
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        return json.dumps(result)
        # 关闭数据库连接
    elif flag == "add":
        cursor.execute(sql)
        db.commit()
    db.close()
