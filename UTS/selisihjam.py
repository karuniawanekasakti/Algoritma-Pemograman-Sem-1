
jam1 = input().split()
jam2 = input().split()
jam1 = list(map(int,jam1))
jam2 = list(map(int,jam2))
konversijam = ((jam2[0] - jam1[0]) - 1)
konversimenit = (59 - (jam1[1] - jam2[1]))
konversidetik = (60 -(jam1[2] - jam2[2]))
x1 = konversijam
x2 = konversimenit
x3 = konversidetik
print (x1,x2,x3)
