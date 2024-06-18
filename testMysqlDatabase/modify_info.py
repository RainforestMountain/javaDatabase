from database import Database
from tkinter.messagebox import *


class ModifyInfo(object):
    def __init__(self, stu_id, stu_name, stu_python, stu_c):
        """修改学生信息"""
        db = Database()
        stu_id = stu_id.get()
        stu_name = stu_name.get()
        try:
            if not (stu_id.strip() and stu_name.strip()):
                raise ValueError
            stu_c = int(stu_c.get())
            stu_python = int(stu_python.get())
            if 0 <= stu_python <= 100 and 0 <= stu_c <= 100:
                if db.prepare(f"select * from student where stu_id={stu_id}") != 0:
                    db.prepare(f"update student set stu_name='{stu_name}', python={stu_python},"
                               f" c={stu_c} where stu_id='{stu_id}'")
                    db.update()
                    showinfo("提示", "修改成功")
                else:
                    showerror("修改失败", "未查询到该同学信息")
            else:
                showerror("修改失败", "各科分数应在0-100之间")
        except ValueError:
            showerror("修改失败", "信息未填写完整或者成绩输入为非数字")
        db.close()
