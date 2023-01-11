def personal_information(*stu):
    color_number = {'red': 1, 'green': 2, 'blue': 3, 'orange': 4, 'Cyan': 5, 'yellow': 6, 'purple': 7}
    number_color = {1: 'red', 2: 'green', 3: 'blue', 4: 'orange', 5: 'Cyan', 6: 'yellow', 7: 'purple'}
    data = []
    student_color = []
    student_color_number = []
    num = len(stu)
    # 获得存储在字典中学生的颜色集合
    for i in range(1, num + 1):
        st = stu[i - 1]
        student_color.append(st['color'])
    for t in range(1, num + 1):
        student_color_number.append(color_number[student_color[t - 1]])
        student_color_number.sort()
    # 根据上文定义颜色数字，读出学生颜色
    for p in range(1, num + 1):
        color = number_color[student_color_number[p - 1]]
        if len(data) == 0:
            stu1 = stu[0]
            data.append(stu1)
        number = data[len(data) - 1]['id']
        # 获取所有学生信息
        for i in range(2, num + 1):
            stu1 = stu[i - 1]
            if color == stu1['color'] and stu1['id'] != number:
                data.append(stu1)
    print("排列后:")
    return print(*data, sep='\n')


student1 = {'id': 101, 'name': '刘同学', 'age': 22, 'color': 'red'}
student2 = {'id': 102, 'name': '张同学', 'age': 19, 'color': 'blue'}
student3 = {'id': 103, 'name': '何同学', 'age': 20, 'color': 'yellow'}
student4 = {'id': 104, 'name': '王同学', 'age': 20, 'color': 'green'}
student = [student1, student2, student3, student4]
print("排列前:")
print(*student, sep='\n')
print(personal_information(*student))
