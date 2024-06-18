from tkinter.messagebox import *
from database import Database


class TreeviewSortColumn(object):  # Treeview、列名、排列方式
    def table_sort(self, tv, col, reverse):
        """点击表头进行排序"""
        # 因为排序utf-8编号问题所以汉字排序不是按首字母来的所以转化为gbk编码
        if col == 'stu_python' or col == 'stu_c':
            l = [(int(tv.set(k, col)), k) for k in tv.get_children('')]
        else:
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
        if col == 'stu_name':
            l = [(i[0].encode('GBK'), i[1]) for i in l]
            l.sort(reverse=reverse)
            l = [(i[0].decode('GBK'), i[1])for i in l]
        else:
            l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        col_dict = {True: '降序', False: '升序', 'stu_id': '学号', 'stu_name': '姓名', 'stu_python': 'Python成绩', 'stu_c': 'C语言成绩'}
        showinfo("提示", f"已按{col_dict[col]}{col_dict[reverse]}排序")

        tv.heading(col, command=lambda: TreeviewSortColumn().table_sort(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def total_sort(self, tree_view, select=''):
        """对总成绩排序"""
        db = Database()
        db.prepare("select * from student order by c+ python " + select)
        db.update()
        sort_dict = {'': '升序', 'desc': '降序'}
        showinfo("提示", f"已按总成绩{sort_dict[select]}排序")
        x = tree_view.get_children()
        for item in x:
            tree_view.delete(item)
        student_tuple = db.cursor.fetchall()
        db.close()
        for item in student_tuple:
            tree_view.insert("", 'end', values=item)

