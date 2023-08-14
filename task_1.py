array = []
a1 = int(input("Введите число: "))
n = int(input("Введите колличество: "))
d = int(input("Введите множитель: "))
for i in range(n):
    an = a1 + i * d
    array.append(an)
print(array, end=' ')