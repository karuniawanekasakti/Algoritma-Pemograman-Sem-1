a = str(input())
b = str(input())

n=0
for i in range(len(a),0,-1) :
    if a[i-1] == b[i-1] :
        n+=1
    else :
        break
print(n)

#for i in len():
    
    
  
