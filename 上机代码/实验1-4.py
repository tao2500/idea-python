Str = input("Please input a String: ")
rts = Str[::-1]  # 倒序输出
if Str == rts:
    print("%s is a HuiWen String" % Str)
else:
    print("%s not a HuiWen String" % Str)
