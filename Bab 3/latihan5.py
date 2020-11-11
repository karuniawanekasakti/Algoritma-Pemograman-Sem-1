permen = input().split()
permen = list(map(int,permen))
a = (permen[0] % 3)
b = (permen[1] % 4)
c = (permen[2] % 5)
hasil = a+b+c
print(hasil)
