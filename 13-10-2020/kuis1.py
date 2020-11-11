#Buatlah program membaca bil A.  Lalu menampilkan bil prima terbesar yg lebih kecil dr A.
a = int(input("input bilangan prima : "))
for i in range(a):
    cek = True
    for a in range(2, i):
        if i % a == 0:
            cek = False
            break
    if cek:
        prima = i
if prima < 2:
    print("Tidak ada bilangan prima lebih kecil dari 2")
else:
    print(prima)