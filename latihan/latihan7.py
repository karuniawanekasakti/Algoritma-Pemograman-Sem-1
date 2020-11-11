#bab4
data = input().split()
data_float=list(map(float,data))
jarijari =data_float[0]
tinggi = data_float[1]
phi = 3.14
hasil = (2*phi*jarijari*tinggi+2*(phi*jarijari**2))
print(hasil)