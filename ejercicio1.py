def fun1(a,b):
    if a < b:
        print('Vale 0')
        return 0
    else:
        return fun1(a - b, b) + 1

def fun2(a,b):
    if a < b:
        print('Valor' + str(a))
        return a
    else:
        return fun2(a - b, b)

print('R1 - ' + str(fun1(16, 3)))
print('R2 - ' + str(fun2(16, 3)))
print('R3 - ' + str(fun1(312, 4)))
print('R4 - ' + str(fun2(312, 4)))
