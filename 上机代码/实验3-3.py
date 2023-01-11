import  random

print("欢迎来到猜数游戏！")
item = 0
target = random.randint(0, 100)
star = 1
while star == 1:
    write = int(input("请输入一个100以内的整数: "))
    item += 1
    if write < target:
        print("输入数字过小")
    elif write > target:
        print("输入数字过大")
    elif write == target:
        star = 0
        print("恭喜您猜对啦！共猜了%d次" % item)
        a = input("是否重新开始游戏？ 是or否: ")
        if a == "是":
            target = random.randint(0, 100)
            star = 1
        else: print("欢迎下次再来！")
