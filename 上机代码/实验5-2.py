def prime(aa, bb):
    a = int(aa)
    b = int(bb)
    num = 0
    sun = 0
    # 排序变量a保存较小值
    if a > b:
        c = b
        b = a
        a = c
    elif a == b:
        print("不能输入两个相同的数！")
    for d in range(a, b):
        # 判断是否为素数（值为1是表示是素数）
        ok = 1
        for dt in range(2, d):
            if d % dt == 0:
                ok = 0
                break
        if ok == 1:
            num = num + 1
            sun = sun + d
            print(d, end=" ")
    print("范围之内素数的个数为%d，它们的和为%d" % (num, sun))


print("请输入两个数")
x = input("第一个数")
xx = input("第二个数")
prime(x, xx)
