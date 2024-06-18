from database import Database
from tkinter.messagebox import *


class AddInfo(object):
    def __init__(self, stu_id, stu_name, stu_python, stu_c):
        """添加学生信息"""
        self.db = Database()
        stu_id = stu_id.get()
        stu_name = stu_name.get()
        try:
            if not (stu_id.strip() and stu_name.strip()):
                raise ValueError
            stu_python = int(stu_python.get())
            stu_c = int(stu_c.get())
            cursor = self.db.cursor
            if 0 <= stu_python <= 100 and 0 <= stu_c <= 100:
                sql = f"select * from student where stu_id='{stu_id}'"
                cursor.execute(sql)
                results = cursor.fetchall()
                if len(results) == 0:
                    sql = f"insert into student values('{stu_id}', '{stu_name}', {stu_python}, {stu_c})"
                    cursor.execute(sql)
                    self.db.update()
                    showinfo("提示", "添加成功")
                else:
                    showerror("添加失败", "该学号重复")
            else:
                showerror("添加失败", "各科分数应在0-100之间")
        except ValueError:
            showerror("添加失败", "信息未填写完整或者成绩输入为非数字")
