#Buatlah program menampilkan segitiga bintang :
angka=int(input())

for i in range(angka) :
    for j in range(angka) :
            if i==0 or i== angka-1 or j==0 or j== angka-1 :
                print ("#", end="")
            else :
                print(" ", end="")
    print ("")
