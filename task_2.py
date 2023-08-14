import random
list = []
i = 0
count = int(input("Введите колличество элементов: "))
list = [random.randint(1, 101) for i in range(count)]
print(list)
max_number = int(input("Введите max: "))
min_number = int(input("Введите min: "))
for i in range(len(list)):
   if list[i] >= min_number and list[i] <= max_number:
      print(i, end = " ")