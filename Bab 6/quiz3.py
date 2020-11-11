n =int(input())
for j in range(n) :
    for i in range(n) :
            if j==0 or j== n -1 :
                print ("#", end="")
            elif i == 0 or i == n-1 :
                print ("#", end= "")
            else :
                print(" ", end="")
    print ("") 