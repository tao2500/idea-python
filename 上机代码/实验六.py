import sqlite3
import random

cx = sqlite3.connect("shiyanLiu.db")
cu = cx.cursor()
cu.execute(
    'create table if not exists bookList (bookId varchar(10) primary key,bookName varchar(10),author varchar(10),typee varchar(10),num integer)')


def createBookId():
    st = "CN"
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        st += ch
    return st


def fundBook():
    name = input("请输入待查询的书名：")
    cu.execute("select * from bookList where bookName = '%s'" % name)
    result = cu.fetchall()
    count = len(result)
    if count == 0:
        print("--------------------------------查无此书--------------------------------")
    else:
        cu.execute("select * from bookList where bookName = '%s'" % name)
        print("查询到《%s》的信息如下：" % name)
        print("----图书id-----图书作者------图书类别------图书数量-------")
        print(cu.fetchall())
    select()


def fund():
    name = input("请输入书名：")
    cu.execute("select * from bookList where bookName = '%s'" % name)
    print("查询到《%s》的信息如下：" % name)
    print("----图书id-----图书作者------图书类别------图书数量-------")
    print(cu.fetchall())


def addBook():
    bookId = createBookId()
    bookName = input("请输入书名")
    author = input("请输入图书作者")
    typee = input("请输入图书类别")
    num = int(input("请输入图书数量"))
    # 根据id查询以此判断id是否重复
    cu.execute("select * from bookList where bookId = '%s'" % bookId)
    result = cu.fetchall()
    count = len(result)
    # 生成的id重复，重新生成
    if count != 0:
        bookId = createBookId()
    cu.execute("insert into bookList values('%s', '%s', '%s', '%s', '%d')" % (bookId, bookName, author, typee, num))
    cx.commit()
    cu.execute("select * from bookList where typee = '%s'" % typee)
    result = cu.fetchall()
    count = len(result)
    print("添加图书成功，该书id为%s,目前该类别的图书共有%d册" % (bookId, count))
    select()


def updataBook():
    fund()
    inp = input("请输入要修改图书的id")
    bookName = input("请输入修改后的书名")
    author = input("请输入修改后的图书作者")
    typee = input("请输入修改后的图书类别")
    num = int(input("请输入修改后的图书数量"))
    # cu.execute("UPDATE bookList SET bookName=?, author=?,typee=?, num=?, where id=?",
    #            (bookName, author, typee, num, inp,))
    cu.execute("UPDATE bookList SET bookName='%s', author='%s',typee='%s', num='%d' where bookId='%s'" % (bookName, author, typee, num, inp))
    cx.commit()
    print("修改图书信息成功a！")
    select()


def delateBook():
    fund()
    print("请输入要删除图书的id")
    inp = input()
    cu.execute("delete from bookList where bookId = '%s'" % inp)
    cx.commit()
    print("成功删除图书！")
    select()


def select():
    print("---------------------------请选择你要使用的功能！-----------------------------")
    print("----1/查询图书-----2/增加图书------3/修改图书----------4/删除图书-------0/退出系统")
    Temporary = int(input())
    if Temporary == 1:
        fundBook()
    if Temporary == 2:
        addBook()
    if Temporary == 3:
        updataBook()
    if Temporary == 4:
        delateBook()
    else:
        cu.close()
        cx.close()
        print("-------------------------期待您的再次使用，再见！-----------------------------")


print("---------------------------欢迎使用图书管理系统-------------------------------")
select()
