
# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го
# члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

print("----------|  Задача 30  |----------")
print("Формула n-го члена арифметической прогрессии an = a1 + (n-1) * d")
a = int(input("Введите опорный элемент арифметической прогрессии a: "))
d = int(input("Введите разность арифметической прогрессии d: "))
n = int(input("Введите количество элементов арифметической прогрессии n: "))

print("Элементы арифметической прогрессии: ")
list=[]
for i in range(n):
    temp = a+(i)*d
    list.append(temp)
    # print(a, end=" ")
print(f"{list}\n")


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

print("----------|  Задача 32  |----------")
import random
n = int(input("Введите количество элементов массива n: "))
lot_1 = []
for i in range(n):
    lot_1.append(random.randint(0, 10))
print(lot_1)
limitMax = int(input("Введите наибольший предел диапазона: "))
limitMin = int(input("Введите наименьший предел диапазона: "))
lot_2 = []

for i in range(len(lot_1)):
    if limitMin < lot_1[i] < limitMax:
        lot_2.append(i)
print(lot_2)