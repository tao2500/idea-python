num = int(input("请输入一个数字："))
add = 0
lib = []
star = 0
for i in range(0, int(num / 2)):
    for ii in range(0, num + 1):
        if i * ii == num:
            lib.append(i)
            lib.append(ii)
lib = lib[:1] + lib[2:]
for x in lib:
    add = add + x
if add == num:
    print("true，%d=" % num, end='')
    for i in lib:
        if star != 0:
            print('+', sep='', end='', file=None)
        print(i, sep='', end='', file=None)
        star = 1
else:
    print("false")
