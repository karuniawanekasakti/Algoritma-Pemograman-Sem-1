nilai = input().split()
nilai = list(map(int,nilai))
a = nilai[0]
b = nilai[1]
c = nilai[2]

n = 0
if a <=40 :
    n += 1
if b <=40 :
    n += 1
if c <=40 :
    n += 1

if a > 100 or b > 100 or c > 100 :
    print ("nilai tidak boleh lebih dari 100")
else :
    if n < 2 :
        if (a + b + c) / 3 > 50 :
            print("lulus")
        else :
            print("tidak lulus")
    else :
        print("tidak lulus")

    