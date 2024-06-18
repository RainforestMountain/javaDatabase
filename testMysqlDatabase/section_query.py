from tkinter import *
from database import *
from tkinter.messagebox import *


class SectionQuery(object):
    def __init__(self, tree_view):
        """清空表格中显示的内容"""
        self.db = Database()
        x = tree_view.get_children()
        for item in x:
            tree_view.delete(item)

    def section(self, tree_view, *args):
        """快捷版分段显示"""
        self.db.prepare(f"select * from student where {args[0]}>{args[1]} and {args[0]}<{args[2]}")
        self.insert(tree_view)
        showinfo("提示", f"已筛选出{args[0]}成绩从{args[1]}—{args[2]}的学生的信息")


    def custom(self, tree_view):
        """自定义版分段显示"""
        # 创建自定义分段窗口
        top = Toplevel()
        # 使窗口位于屏幕中央
        screenwidth = top.winfo_screenwidth()
        screenheight = top.winfo_screenheight()
        width = 500
        high = 200
        top.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))

        Label(top, text="Python").place(relx=0.48, rely=0, relwidth=0.1)
        Label(top, text="————").place(relx=0.48, rely=0.2, relwidth=0.1)
        Label(top, text="C语言").place(relx=0.48, rely=0.4, relwidth=0.1)
        Label(top, text="————").place(relx=0.48, rely=0.6, relwidth=0.1)

        python_limit1 = StringVar()
        python_limit2 = StringVar()
        c_limit1 = StringVar()
        c_limit2 = StringVar()

        Entry(top, textvariable=python_limit1).place(relx=0.1, rely=0.2, relwidth=0.35, height=25)
        Entry(top, textvariable=python_limit2).place(relx=0.6, rely=0.2, relwidth=0.35, height=25)
        Entry(top, textvariable=c_limit1).place(relx=0.1, rely=0.6, relwidth=0.35, height=25)
        Entry(top, textvariable=c_limit2).place(relx=0.6, rely=0.6, relwidth=0.35, height=25)

        mb = Menubutton(top, text="筛选", relief=RAISED)
        mb.place(relx=0.5, rely=0.8)

        filemenu = Menu(mb, tearoff=False)
        filemenu.add_command(label="按Python分段", command=lambda: self.section_python(python_limit1, python_limit2, tree_view))
        filemenu.add_command(label="按C语言分段", command=lambda: self.section_c(c_limit1, c_limit2, tree_view))
        filemenu.add_separator()
        filemenu.add_command(label="按Python和C语言分段", command=lambda: self.section_all(python_limit1, python_limit2, c_limit1, c_limit2, tree_view))
        mb.config(menu=filemenu)

    def check_data(self, limit1, limit2):
        """检查输入的数据是否合格"""
        try:
            limit1 = int(limit1.get())
            limit2 = int(limit2.get())

            if limit1 > limit2:
                up = limit1
                down = limit2
            else:
                up = limit2
                down = limit1

            return up, down
        except ValueError:
            showerror("分段筛选失败", "分段区间未填写完整或输入为非数字")

    def section_python(self, python_limit1, python_limit2, tree_view):
        """按python成绩分段筛选"""
        # 由与已有方法对异常进行了处理所以此处出现异常直接pass
        try:
            python_up, python_down = self.check_data(python_limit1, python_limit2)
            if self.db.prepare(f"select * from student where python>{python_down} and python<{python_up}") != 0:
                self.insert(tree_view)
                showinfo("提示", f"已筛选出Python成绩从{python_down}—{python_up}的学生的信息")
            else:
                showinfo("提示", f"没有Python成绩从{python_down}—{python_up}的学生的信息")
        except TypeError:
            pass
        self.db.close()

    def section_c(self, c_limit1, c_limit2, tree_view):
        """按照C语言成绩分段筛选"""
        try:
            c_up, c_down = self.check_data(c_limit1, c_limit2)
            if self.db.prepare(f"select * from student where c>{c_down} and c<{c_up}") != 0:
                self.insert(tree_view)
                showinfo("提示", f"已筛选出C语言成绩从{c_down}—{c_up}的学生的信息")
            else:
                showinfo("提示", f"没有C语言成绩从{c_down}—{c_up}的学生的信息")
        except TypeError:
            pass
        self.db.close()

    def section_all(self, python_limit1, python_limit2, c_limit1, c_limit2, tree_view):
        """按照python和C语言成绩分段筛选"""
        try:
            c_up, c_down = self.check_data(c_limit1, c_limit2)
            python_up, python_down = self.check_data(python_limit1, python_limit2)
            if self.db.prepare(f"select * from student where  c>{c_down} and c<{c_up} and python>{python_down} and python<{python_up}") != 0:
                self.insert(tree_view)
                showinfo("提示", f"已筛选出Python成绩从{python_down}—{python_up}"
                               f"C语言成绩从{c_down}—{c_up}的学生的信息")
            else:
                showinfo("提示", f"没有Python成绩从{python_down}—{python_up}"
                               f"C语言成绩从{c_down}—{c_up}的学生的信息")

        except TypeError:
            pass
        self.db.close()

    def insert(self, tree_view):
        """"向表格中插入筛选出来的数据"""
        student_tuple = self.db.cursor.fetchall()
        for item in student_tuple:
            tree_view.insert("", 'end', values=item)



