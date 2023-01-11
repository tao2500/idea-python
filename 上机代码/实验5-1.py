def out():
    st = 0
    kong = 0
    num = 0
    order = 0
    s = input("请输入一串连续的文本:")
    for ss in s:
        # 字符为字符串时
        if str.isalpha(ss) == 1:
            st = st+1
        # 字符为数字时
        elif str.isdigit(ss) == 1:
            num = num+1
        # 字符为空格时
        elif str.isspace(ss) == 1:
            kong = kong+1
        else:
            order = order+1
    print("文本中的字母有%d个，数字有%d个，空格有%d个，其它字符有%d个" % (st, num, kong, order))


# hello world!123
out()
