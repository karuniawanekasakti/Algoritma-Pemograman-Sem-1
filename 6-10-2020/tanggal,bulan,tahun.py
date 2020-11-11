x = str(input()).split()
x = list(map(int, x))
tanggal = x[0]
bulan = x[1]
tahun = x[2]
kabisat = tahun % 4
if bulan % 2 == 0:
    hari = 30
else:
    hari = 31
if kabisat == 0:
    hari = 29
else:
    hari = 28
Tanggal = tanggal >=1 and tanggal <= hari
Bulan = bulan >=1 and bulan <=12
Valid = Tanggal and Bulan
if(Valid):
       print("Valid")
else:
        print("Tidak Valid")