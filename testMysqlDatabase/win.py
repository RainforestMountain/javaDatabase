from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from show_info import ShowInfo
from modify_info import ModifyInfo
from search_info import SearchInfo
from del_info import DelInfo
from statistics_info import StatisticsInfo
from add_info import AddInfo
from sort import TreeviewSortColumn
from section_query import SectionQuery


class Win(object):
    def __init__(self):
        """主界面基本设置"""
        # 创建窗口
        root = Tk()
        # 设置窗口大小和并将位置设置到屏幕中央
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width = 700
        high = 600
        root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))

        root.title('学生管理系统')

        # 设置各个文本框的标签，并固定位置
        Label(root, text="学号：").place(relx=0, rely=0.05, relwidth=0.1)
        Label(root, text="姓名：").place(relx=0.5, rely=0.05, relwidth=0.1)
        Label(root, text="Python：").place(relx=0, rely=0.1, relwidth=0.1)
        Label(root, text="C语言：").place(relx=0.5, rely=0.1, relwidth=0.1)

        # 设置各个文本框内容所对应的变量
        self.stu_id = StringVar()
        self.stu_name = StringVar()
        self.stu_python = StringVar()
        self.stu_c = StringVar()

        # 设置各个文本框并固定位置
        Entry(root, textvariable=self.stu_id).place(relx=0.1, rely=0.05, relwidth=0.35, height=25)
        Entry(root, textvariable=self.stu_name).place(relx=0.6, rely=0.05, relwidth=0.35, height=25)
        Entry(root, textvariable=self.stu_python).place(relx=0.1, rely=0.1, relwidth=0.35, height=25)
        Entry(root, textvariable=self.stu_c).place(relx=0.6, rely=0.1, relwidth=0.35, height=25)

        # 设置窗口的标题标签
        Label(root, text='学生信息管理', bg='white', fg='red', font=('宋体', 15)).pack(side=TOP, fill='x')

        # 创建表格并设置相关属性
        self.tree_view = ttk.Treeview(root, show='headings', column=('stu_id', 'stu_name', 'stu_python', 'stu_c'))
        sb = Scrollbar(root, orient='vertical', command=self.tree_view.yview)
        sb.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 设置每列的属性
        self.tree_view.configure(yscrollcommand=sb.set)
        self.tree_view.column('stu_id', width=150, anchor="center")
        self.tree_view.column('stu_name', width=150, anchor="center")
        self.tree_view.column('stu_python', width=150, anchor="center")
        self.tree_view.column('stu_c', width=150, anchor="center")
        # 设置每行的属性
        self.tree_view.heading('stu_id', text='学号', command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'stu_id', False))
        self.tree_view.heading('stu_name', text='姓名', command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'stu_name', False))
        self.tree_view.heading('stu_python', text='Python', command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'stu_python', False))
        self.tree_view.heading('stu_c', text='C语言', command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'stu_c', False))
        # 设置表格位置
        self.tree_view.place(relx=0.02, rely=0.3, relwidth=0.96)

        # 设置按钮，并固定位置
        Button(root, text="显示所有信息", command=lambda: ShowInfo(self.tree_view)).place(relx=0.05, rely=0.2, width=80)
        Button(root, text="添加学生信息", command=lambda: AddInfo(self.stu_id, self.stu_name, self.stu_python, self.stu_c)).place(relx=0.20, rely=0.2, width=80)
        Button(root, text="删除学生信息", command=lambda: DelInfo(self.stu_id, self.stu_name, self.stu_python, self.stu_c)).place(relx=0.35, rely=0.2, width=80)
        Button(root, text="修改学生信息", command=lambda: ModifyInfo(self.stu_id, self.stu_name, self.stu_python, self.stu_c)).place(relx=0.50, rely=0.2, width=80)
        Button(root, text="统计学生信息", command=lambda: StatisticsInfo()).place(relx=0.65, rely=0.2, width=80)
        Button(root, text="查询学生信息", command=lambda: SearchInfo(self.stu_id, self.stu_name, self.stu_python, self.stu_c, self.tree_view)).place(relx=0.80, rely=0.2, width=80)

        # 创建一个顶级菜单
        menubar = Menu(root)

        # 创建下拉菜单，然后将它添加到顶级菜单中
        filemenu = Menu(menubar, tearoff=False)
        section_menu = Menu(filemenu, tearoff=False)
        python_menu = Menu(section_menu, tearoff=False)
        c_menu = Menu(section_menu, tearoff=False)
        total_menu = Menu(filemenu, tearoff=False)

        # 设置下拉菜单的label
        menubar.add_cascade(label="选项", menu=filemenu)
        filemenu.add_cascade(label="分段筛选数据", menu=section_menu)
        filemenu.add_cascade(label="按总成绩排序", menu=total_menu)
        filemenu.add_separator()
        filemenu.add_command(label="退出", command=lambda: self.callback(root))
        section_menu.add_cascade(label="Python", menu=python_menu)
        section_menu.add_cascade(label="C语言", menu=c_menu)
        section_menu.add_command(label="自定义区间", command=lambda: SectionQuery(self.tree_view).custom(self.tree_view))
        python_menu.add_command(label="0-60", command=lambda: SectionQuery(self.tree_view).section(self.tree_view, 'python', 0, 60))
        python_menu.add_command(label="60-80", command=lambda: SectionQuery(self.tree_view).section(self.tree_view, 'python', 60, 80))
        python_menu.add_command(label="80-100", command=lambda: SectionQuery(self.tree_view).section(self.tree_view, 'python', 80, 100))
        c_menu.add_command(label="0-60", command=lambda: SectionQuery(self.tree_view).section(self.tree_view, 'c', 0, 60))
        c_menu.add_command(label="60-80", command=lambda: SectionQuery(self.tree_view).section(self.tree_view, 'c', 60, 80))
        c_menu.add_command(label="80-100", command=lambda: SectionQuery(self.tree_view).section(self.tree_view, 'c', 80, 100))
        total_menu.add_command(label="升序", command=lambda: TreeviewSortColumn().total_sort(self.tree_view))
        total_menu.add_command(label="降序", command=lambda: TreeviewSortColumn().total_sort(self.tree_view, "desc"))

        # 显示菜单
        root.config(menu=menubar)

        # 绑定单击离开事件
        self.tree_view.bind('<ButtonRelease-1>', self.tree_view_click)

        # 捕获关闭按钮
        root.protocol("WM_DELETE_WINDOW", lambda: self.callback(root))

        # 事件循环
        root.mainloop()

    def tree_view_click(self, event):
        """点击表格中的一项数据后将其显示在相应文本框上"""
        for item in self.tree_view.selection():
            item_text = self.tree_view.item(item, "values")
            self.stu_id.set(item_text[0])
            self.stu_name.set(item_text[1])
            self.stu_python.set(item_text[2])
            self.stu_c.set(item_text[3])

    def callback(self, root):
        """退出时的询问"""
        if askokcancel("询问", "是否关闭该窗口?"):
            root.destroy()



