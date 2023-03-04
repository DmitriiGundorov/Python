import random
"""
# Задача № 17. Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

print("----------|  Задача 17  |----------")
number = int(input("Введите размер списка: "))
listNumber = []
for i in range(number):
    listNumber.append(random.randint(-5, 5))
print(listNumber)

# 1 способ
# print(f"Количество уникальных чисел -> {len(set(listNumber))}")

# 2 способ
newList = []
for j in range(len(listNumber)):
    if i not in newList:
        newList.append(listNumber[j])
        print(newList)

# Задача № 19. Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

print("----------|  Задача 19  |----------")
number = int(input("Введите размер списка: "))
listNumber = []
for i in range(number):
    listNumber.append(random.randint(-5, 5))
print(listNumber)
k = int(input("Введите величину сдвига: "))
k%=len(listNumber) # на случай ввода отрицательных и больших k
# 1-й метод
#print(f"{listNumber[len(listNumber)-k:len(listNumber)]+listNumber[:len(listNumber)-k]}")

# 2-й метод
for i in range(k):
    listNumber.insert(0, listNumber.pop(-1))
print(listNumber)


# Задача №21. Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

print("----------|  Задача 21  |----------")

listFirst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
             {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]

# Решение 1

# listSecond = []
# for d in listFirst:
#     for val in list(d.values()):
#         listSecond.append(val)
# print(listSecond)

# Решение 2

listSecond = set()

for i in listFirst:
    listSecond.add(listFirst[i])

print(listSecond)

"""

# Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая
# подсчитает количество элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

print("----------|  Задача 23  |----------")
a = [0, -1, 5, 2, 3]
count = 0
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        count += 1
        print(f"{a[i]} < {a[i+1]}")
print(count)