from database import Database


class ShowInfo(object):
    def __init__(self, tree_view):
        """将所有学生信息显示在表格上"""
        db = Database()
        x = tree_view.get_children()
        for item in x:
            tree_view.delete(item)
        db.cursor.execute("select * from student")
        student_tuple = db.cursor.fetchall()
        for item in student_tuple:
            tree_view.insert("", 'end', values=item)
