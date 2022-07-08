def f1(a, b, c):
    a = b - c * a
    b = c
    c = a
    b = c
    print('4 - el valor de b :' + str(b))
    return b

def f2(x, y, z):
    a = x
    b = y
    c = y

    a = b^z + c^y

    b = c

    print('5 - el balor de a '+ str(a))
    return a

def f3(m, n, l):
    a = m
    b = n
    c = l

    a = b - c
    b = c
    return a

def f4(a, x, m):
    b = x
    c=m

    c=b+c
    b=c
    return b

def main():
    a=1
    b=2
    c=3
    m=4
    n=5
    l=6
    x=7
    y=8
    z=9
    f1(x,y,z)
    f2(a,b,c)
    print('1 - el valor de a' + str(a))
    b = f3(a,b,c)
    print('2 - el valor de b : '+str(b))

    c = f4(m,n,l)
    print('el valor de c: ' + str(c))


main()
