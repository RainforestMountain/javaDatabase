

import pymssql


class Database(object):
    def __init__(self):
        """连接数据库"""
        self.db = pymssql.connect(host='localhost',  # 这里的host='_'可以用本机ip或ip+端口号
                                  server="192.168.101.24",  # 本地服务器
                                  port="1433",  # TCP端口
                                  user="sa",
                                  password="123456",
                                  database="databaseDesign", charset='GBK')
        self.cursor = self.db.cursor()

    def prepare(self, sql):
        """执行sql语句"""
        return self.cursor.execute(sql)

    def update(self):
        """提交到数据库执行"""
        self.db.commit()

# 假设变量 stu_id, stu_name, stu_python, stu_c 已定义并

    def close(self):
        """关闭数据库"""
        self.db.close()

stu_id = None  # 示例值，实际情况根据需要替换
stu_name = "黄海涛"  # 示例值
stu_python = None  # 示例值，可以是 int 或 None
stu_c = None  # 示例值，可以是 int 或 None

# 连接到SQL Server数据库
conn = Database()
cursor = conn.cursor

# sql =f'''
# SELECT * FROM student
# WHERE
#     ({stu_id} IS NULL OR stu_id LIKE '%' {stu_id} '%')
#     AND ({stu_name} IS NULL OR stu_name LIKE '%' {stu_name}'%')
#     AND ({stu_python} IS NULL OR python = {stu_python})
#     AND ({stu_c} IS NULL OR c = {stu_c});'''

stu_id = "" if stu_id is None else stu_id
stu_name = "" if stu_name is None else stu_name
stu_c = 0 if stu_c is None else stu_c
stu_python = 0 if stu_python is None else stu_python

sql = " select * from student where stu_name = '雨'"

# 执行查询

cursor.execute(sql)
# 获取结果
results = cursor.fetchall()

# 处理结果
for result in results:
    result = list(result)  # 元组转化为列表
    for res in range(len(result)):
        if isinstance(result[res], str):
            result[res] = result[res].replace(' ', '')
    result = tuple(result)  # 列表再转换为元组
    print("处理后：", end="")
    print(result)

