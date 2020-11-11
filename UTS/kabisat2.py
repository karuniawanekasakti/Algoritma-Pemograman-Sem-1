#100
tahun = int(input())

if (tahun % 4) == 0:
    if (tahun % 100) == 0 :
        if (tahun % 400) == 0:
            print("kabisat")
        else :
            print("Bukan kabisat")
    else :
        print("kabisat")
else :
    print("Bukan kabisat")

