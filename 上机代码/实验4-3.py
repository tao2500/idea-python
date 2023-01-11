def multi(p1):
    for k,v in p1.items():
        if len(str(v)) > 2:
            item[k] = v % 100
item = {'p1': 1, 'p2': 22, 'p3': 333, 'p4': 4444}
print("原字典：")
print(item)
multi(item)
print("经过函数格式化后：" )
print(item)