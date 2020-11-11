
x = input()
y = 0
x=list(map(int, str(x)))
for i in range(5) :
    if x[i] == 0 :
        y+=1
print(y)
