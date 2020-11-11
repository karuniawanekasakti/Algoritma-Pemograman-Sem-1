a = int(input("input bilangan prima : "))
cek = True
for i in range(2, a):
    if a % i == 0:
        cek = False
        
    elif cek :
        print ("prima")
        break
    else :
        print ("bukan bilangan prima")
        break
if a < 2:
    print ("tidak ada bilangan prima yang lebih kecil dari 2")

