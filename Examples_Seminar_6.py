import random
# Задача №39. Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# print("----------|  Задача 39  |----------")

# n = int(input("Введите количество элементов в первом массиве N: "))
# list_1 = [random.randint(0, n) for i in range(n)]
# print(*list_1)
# m = int(input("Введите количество элементов в первом массиве M: "))
# list_2 = [random.randint(0, m) for i in range(m)]
# print(*list_2)
# print("Этементы массива N, которых нет в массиве M:")
# for i in list_1:
#     if i not in list_2:
#         print(i, end=" ")

# Задача №41. Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# print("----------|  Задача 41  |----------")

# n = int(input("Введите количество элементов в первом массиве N: "))
# list_N = [random.randint(0, 5) for i in range(n)]
# # или
# list_N = []
# for i in range(n):
#     list_N.append(int(input(f"Введите {i+1} элемент: ")))

# print(*list_N)
# count = 0
# for i in range(1, len(list_N)-2):
#     list_N[i-2] < list_N[i-1] > list_N[i]
#     count += 1
# print(count)

# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую
# необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.

print("----------|  Задача 43  |----------")


# n = int(input("Введите кол-во элементов N: "))
# listN = [random.randint(0, 10) for i in range(n)]
# print(listN)

# count = 0

# while (n > 0):
#     for i in range(1, len(listN)):
#         if listN[0] == listN[i]:
#             count += 1
#             listN.pop(i)
#             n -= 1
#             break
#     n -= 1
#     listN.pop(0)

# print(count)

# Решение Илмира
# def _res(arr: list) -> int:
#     counter = 0
#     for item in arr:
#         counter += (arr.count(item)//2)
#         return counter//2

# def random_list(N: int, min=-100, max=100) -> list:
#     import random
#     arr = []
#     for i in range(N):
#         arr.append(random.randint(min, max))
#         return arr

# if __name__ == "__main__":
#     count = int(input("Введите длину списка: "))
#     arr = random_list(count, 0, 10)
# print(arr)
# print(_res(arr))

# Задача №45. Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите
# все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна
# вывести все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара
# должна быть выведена только один раз (перестановка чисел новую пару не дает).

# N = int(input("Введите число N: "))
# listN = [x + 1 for x in range(N)]
# print(listN)


# def Calc_Sum(N):
#     count = 0
#     for i in range(1, N):
#         if N % i == 0:
#             count += i
#             return count


# for i in range(N):
#     if Calc_Sum(i) in listN and Calc_Sum(i) < i:
#         print(i, end=" ")
#         print(Calc_Sum(i))


# Решение преподавателя
"""
Функция для подсчета суммы делителей числа n
"""
def sum_of_divisors(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
            return divisors_sum

k = int(input())

for n in range(1, k):
    m = sum_of_divisors(n)
    if n < m <= k and sum_of_divisors(m) == n:
        print(n, m)

# Дополнительная задача
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# С помощью рекурсивной функции get_line_list создать на его основе одномерный список
# из значений элементов списка d. Функция должна возвращать новый созданный одномерный список.

print("----------|  Дополнитльная задача  |----------")

# def get_line_list(d,a=[]):
#     res = []
#     for i in d:
#         if type(i) == list:
#             res += get_line_list(i,res)
#         else:
#             res.append(i)
#             return res


# print(get_line_list(d))