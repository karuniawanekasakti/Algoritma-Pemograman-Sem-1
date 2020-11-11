#bab5latihan3
x = input().split()
x = list(map(int,x))
x0 = x[0]
x1 = x[1]
x2 = x[2]
if x0 < x1 and x1 < x2 :
    print(x2)
elif x1 < x2 and x2 < x0 :
    print(x0)
elif x0 < x2 and x2 < x1 :
    print(x1)
