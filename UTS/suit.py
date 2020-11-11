#100
b = input()
s = input()
if b == "[]" and s == "()" :
    print("Blangkon")
if b == "[]" and s == "8<" :
    print("Semar")
if b == "[]" and s == "[]" :
    print("Seri")
if b == "()" and s == "[]" :
    print("Semar")
if b == "()" and s == "8<" :
    print("Blangkon")
if b == "()" and s == "()" :
    print("Seri")
if b == "8<" and s == "[]" :
    print("Blangkon")
if b == "8<" and s == "()" :
    print("Semar")
if b == "8<" and s == "8<" :
    print("Seri")




