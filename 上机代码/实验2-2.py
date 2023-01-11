alist = [8, 10, 6, 4]
blist = [3, 1, 4, 6, 9]
addList = alist + blist
clist = list(set(addList))
print(sorted(clist, reverse=True))
