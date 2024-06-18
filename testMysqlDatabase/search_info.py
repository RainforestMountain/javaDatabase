from database import Database
from tkinter.messagebox import *


class SearchInfo(object):
    def __init__(self, stu_id, stu_name, stu_python, stu_c, tree_view):
        """模糊查询"""
        db = Database()
        x = tree_view.get_children()
        for item in x:
            tree_view.delete(item)
        stu_name = stu_name.get()
        stu_id = stu_id.get()
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

            # 该sql语句筛选出你模糊查询的各种数据（可以组合）
            sql = f'''select * from student where (stu_id like '%{stu_id}%' or if(not stu_id, NULL, '') = '{stu_id}') 
                    and (stu_name like '%{stu_name}%' or if(not stu_name, '', NULL)='{stu_name}') and 
                    (if(not python, NULL, 0)={stu_python} or cast(python as char) like '%{stu_python}%') and 
                    (if(not c, NULL, 0)={stu_c} or cast(c as char) like '%{stu_c}%')'''
            # 只有文本框内有有效数据时才执行该语句
            if (stu_id or stu_name or stu_python or stu_c) and db.prepare(sql):
                db.update()
                showinfo("提示", "已完成查询")
                student_tuple = db.cursor.fetchall()
                for item in student_tuple:
                    tree_view.insert('', 'end', values=item)
            else:
                showerror("查询失败", "未查询到该学生信息")
        except ValueError:
            showerror("查询失败", "成绩只能为数字")
        db.close()

