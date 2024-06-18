from database import Database
from tkinter.messagebox import *


class DelInfo(object):
    def __init__(self, stu_id, stu_name, stu_python, stu_c):
        """模糊删除"""
        db = Database()
        stu_id = stu_id.get()
        stu_name = stu_name.get()
        stu_python = stu_python.get()
        stu_c = stu_c.get()
        try:
            if stu_python != '':
                stu_python = int(stu_python)
            else:
                stu_python = 0
            if stu_c != '':
                stu_c = int(stu_c)
            else:
                stu_c = 0
            stu_id = (stu_id is None) if " " else stu_id
            stu_name = (stu_name is None) if " " else stu_name
            stu_c = (stu_c is None) if " " else stu_c
            stu_python = (stu_id is None) if " " else stu_python

            cursor = db.cursor
            sql = f''' select * from student where (stu_id = {stu_id}) or (stu_name = {stu_name}) or (python = {stu_python}) or (c = {stu_c})'''
            # sql = f'''select * from student where (stu_id like '%{stu_id}%' or if(not stu_id, NULL, '') = '{stu_id}')
            #         and (stu_name like '%{stu_name}%' or if(not stu_name, '', NULL)='{stu_name}') and
            #         (if(not python, NULL, 0)={stu_python} or cast(python as char) like '%{stu_python}%')
            #         and (if(not c, NULL, 0)={stu_c} or cast(c as char) like '%{stu_c}%')'''
            cursor.execute(sql)
            results = cursor.fetchall()
            # if (stu_id or stu_name or stu_python or stu_c) and db.prepare(sql):
            if len(results) != 0:
                db.update()
                for i in range(len(results)):
                    if askokcancel("提示",
                                   f"是否删除该学生的信息(学号:{results[i][0]} 姓名:{results[i][1]} Python:{results[i][2]} C语言:{results[i][3]})"):
                        db.prepare(
                            f"delete from student where (stu_id like '%{stu_id}%' or if(not stu_id, NULL, '') = '{stu_id}') and (stu_name like '%{stu_name}%' or if(not stu_name, '', NULL)='{stu_name}') and (if(not python, NULL, 0)={stu_python} or cast(python as char) like '%{stu_python}%') and (if(not c, NULL, 0)={stu_c} or cast(c as char) like '%{stu_c}%') limit 1")
                        db.update()
                        showinfo("提示", "删除成功")
            else:
                showerror("删除失败", "未查询到该学生信息")
        except ValueError:
            showerror("删除失败", "成绩只能为数字")
