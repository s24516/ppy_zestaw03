# 1. Napisz program, który pobierze od użytkownika liczby rozdzielone
# przecinkiem a następnie
# policzy znajdzie ich max oraz min, bez używania wbudowanych funkcji





a = input("Podaj liczby:\n")
a=a.split(",")
min = a[0]
max = a[0]
for i in a[1::]:
    if i < min:
        min = i
    if i > max:
        max = i
print("max: " + max)
print("min: " + min)
