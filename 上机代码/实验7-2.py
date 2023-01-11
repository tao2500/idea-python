class People:
    name = None
    age = None
    gender = None

    def personInfo(self):
        print("姓名%s —— 性别%s ——  年龄%d" % (self.name, self.gender, self.age))

    def __init__(self, a, b, c):
        self.name = a
        self.gender = b
        self.age = c


class Student(People):
    college = None
    Group = None

    def __init__(self, a, b, c, d, e):
        People.__init__(self, a, b, c)
        self.college = d
        self.Group = e

    def personInfo(self):
        People.personInfo(self)
        print("—— 学院%s ——班级%s" % (self.college, self.Group))


p = People("刘金涛", "男", 21)
p.personInfo()
s = Student("刘金涛", "男", 21, "计算机", "3班")
s.personInfo()
