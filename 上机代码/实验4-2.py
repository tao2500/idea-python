def multi(*p1):
    product = 1
    for i in p1:
        product = product * i
    return product
print(multi(1,2,3))