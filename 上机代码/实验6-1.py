class Student:
    id = None
    name = None
    birthday = None

    def __init__(self, data):
        arr = str(data).split()
        self.id = int(arr[0])
        self.name = str(arr[1])
        self.birthday = arr[2]

    def getAge(self, datetime):
        time = str(self.birthday)
        year = 2022 - int(time[:4])
        print("学生的年龄为%d" % year)


a = input("请输入学生的学号、名字以及生日(空格隔开)")
# 202010098231 "刘金涛" 20010101
s = Student(a)
print("学生的学号为%d" % s.id)
print("学生的姓名为%s" % s.name)
print("学生的生日为%s" % s.birthday)
s.getAge(s.birthday)

