
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
import random

print("----------|  Задача 10  |----------")
n = int(input("Введите количество монеток: "))
count_0 = 0
count_1 = 0
for i in range(n):
    coin = random.randint(0, 1)
    # print(coin_tails)
    if coin == 0:
        count_0 += 1
    else:
        count_1 += 1
if count_0 > count_1:
    print(count_1)
else:
    print(count_0)
print()


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате
# по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print("----------|  Задача 12  |----------")
sum = int(input("Введите сумму чисел: "))
composition = int(input("Введите произведение чисел: "))
for i in range(sum):
    for j in range(composition):
        if sum == i+j and composition == i*j:
            x = i
            y = j
print(f"Первое искомое число -> {x}, второе искомое число -> {y}")
print()


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

print("----------|  Задача 14  |----------")
number = int(input("Введите число N: "))
degree = 1
print(f"Степени числа 2, не превышающие число {number}:")
while 2**degree <= number:
    print(f"2^{degree} = {2**degree}")
    degree += 1