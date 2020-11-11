jumlah = input()
nilai  = input().split()
nilai = list(map(int,nilai))
jumlah = list(map(int,jumlah))
a = nilai[0]
b = nilai[1]
c = nilai[2]
d = nilai[3]

if a >=75 :
    print("a")
elif b <=45 :
    print("b")
elif c > a+b+c+d :
    print("a")
elif d > 0 :
    print(b)


    