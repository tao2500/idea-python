num = int(input("Please input X Yuan: "))
Fifty = num / 50
Ten = (num - int(Fifty) * 50) / 10
Five = (num - int(Fifty) * 50 - int(Ten) * 10) / 5
One = (num - int(Fifty) * 50 - int(Ten) * 10 - int(Five) * 5)
print("%d Yuan = %d Fifty, %d Ten ,%d Five , %d One" % (num, Fifty, Ten, Five, One))
