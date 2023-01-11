item = 0
sun = 0
lis = [1, 2, 3]
while sun <= 1200:
    sun = (lis[item] + lis[item + 1] + lis[item + 2]) / 2
    lis.append((lis[item] + lis[item + 1] + lis[item + 2]) / 2)
    item += 1
item += 3
print("从第%f项开始，数字大于1200,此时数组为" % item)
print(lis)
