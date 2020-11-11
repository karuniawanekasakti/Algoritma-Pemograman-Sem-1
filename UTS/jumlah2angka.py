#s25
x = input().split()
x = list(map(int,x))
x0 = x[0]
x1 = x[1]
x2 = x[2]
if x0 > x1 and x1 < x2 :
    print(x0 + x2)
elif x0 > x1 and x1 > x2 :
    print(x0 + x1)
elif x0 < x1 and x1 > x2 :
    print(x1 + x2)


