lis = []
num = 1
end = 0
while num <= 100:
    end = num ** 2
    if num < 10:
        end = str(end)
        num = str(num)
        if end[len(str(end)) - 1] == num[len(str(num)) - 1]:
            lis.append(num)
    elif num >= 10:
        end = str(end)
        endNum = str(end[len(str(end)) - 2]) + str(end[len(str(end)) - 1])  # 平方结果的最后两位数
        if num == int(endNum):
            num = repr(num)
            lis.append(num)
    num = int(num)
    num += 1
print("所有同构数如下")
print(lis)
