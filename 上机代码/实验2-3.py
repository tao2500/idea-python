telephone = {'小明': 1330928333, '小红': 19898227822, '小华': 13382398921, '小林': 19833824743}
Str = input("请输入待查联系人姓名:")
state = 0 # 查询联系人是否存在的状态字标记
for key, value in telephone.items():
    if key == Str:
        state = 1
        print(value)
if state == 0:
    print('not found')
    num = int(input("请输入该联系人的联系方式: "))
    telephone[Str] = num
    print('该联系人成功加入电话薄')
    print(telephone)
