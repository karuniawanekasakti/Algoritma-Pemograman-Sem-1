L = input()
L = L.split()
L = list(map(int, L))
print(L)

k = []
m = []

ratarata = sum(L) / len(L)

for i in L:
    if i <= ratarata:
        m.append(i)
    else:
        k.append(i)

print("List K =",k)
print("List M =",m)

