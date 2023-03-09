# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

print("----------|  Задача 26  |----------")


def degree(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b != 1:
        return a*degree(a, b-1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print(f"Число {a} в степени {b} -> {degree(a,b)}\n")

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из всех арифметических операций допускаются
# только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
# 4


print("----------|  Задача 28  |----------")


def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    return a


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print(f"{a} + {b} -> {sum(a,b)}")
