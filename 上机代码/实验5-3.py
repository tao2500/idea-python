import os

# 行号
lineNum = 0
# 正在执行的行号
workLine = 0
# e的个数
count = 0
# 字符最多的行中字符的个数
strNum = 0
os.makedirs("C:\\python\\three")
with open("C:\\python\\three\\message.txt", 'w') as fileObj:
    fileObj.write("name：ZhangSan\nage:18\nphone:138878787877\nbirthday:2004-10-12")
with open("C:\\python\\three\\message.txt", 'r') as fileObj:
    while True:
        workLine = workLine + 1
        line = fileObj.readline()
        if line == "":
            break
        # 每行字母的个数
        temporaryCount = 0
        for s in line:
            temporaryCount = temporaryCount + 1
            if s == "e":
                count = count + 1
        if temporaryCount >= strNum:
            strNum = temporaryCount
            lineNum = workLine
        print(line)
print("字母e出现的次数为%d，第%d行字符出现最多，%d个" % (count, lineNum, strNum))
