# Задача №31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# print("----------|  Задача 31  |----------")
# n = int(input("Введите номер числа Фиббоначи N: "))
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return (fib(n-2)+fib(n-1))
# print(f"Число фиббоначи под индексом {n} -> {fib(n)}")


# Задача №33. Хакер Василий получил доступ к классному журналу ихочет заменить
# все свои минимальные оценки на максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
import random
print("----------|  Задача 33  |----------")
scores =[random.randint(1, 5) for x in range(10)]
def changeScores(scor, ln=0):
    if scor[ln]==5:
        scor[ln]=1
    ln+=1
    if len(scor)>ln:
        return changeScores(scor, ln)
    else:
        return scor
print(scores)
print(changeScores(scores))


# Задача №37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# print("----------|  Задача 37  |----------")
n = int(input("Введите натуральное число N: "))


def recReverse(n):
    x = input(f"Введите {n} элемент последовательности: ")
    if n != 0:
        recReverse(n-1)
    print(x)


recReverse(n)


# Дополнительная задача №1. Написать функцию вычисления факториала числа n.

# print("----------|  Дополнительная задача №1  |----------")
# n = int(input("Введите натуральное число n: "))


# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)


# print(f"Факториал числа {n} -> {factorial(n)}")


# Дополнительная задача №2. Написать функцию для нахождения общего делителя двух чисел.

# print("----------|  Дополнительная задача №2  |----------")
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))


# def delitel(a, b):
#     if a < b:
#         a, b = b, a
#     if a%b==0:
#         return b
#     return delitel(b, a%b)
# print(f"Наибольший делитель числа {a} и {b} -> {delitel(a,b)}")

# Дополнительная задача №3. Написать функцию для нахождения суммы цифр числа.

# print("----------|  Дополнительная задача №3  |----------")
# n = int(input("Введите число: "))


# def sumNumber(n):
#     if(n//10)==0:
#         return n%10
#     return sumNumber(n//10)+n%10
# print(f"Сумма цифр числа {n} -> {sumNumber(n)}")