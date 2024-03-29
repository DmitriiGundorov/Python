# Задача №47. У вас есть код, который вы не можете менять (так часто бывает, когда
# код в глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.


# print("----------|  Задача 47  |----------")


# def transformation(x): return x


# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transormed_values = list(map(transformation, values))
# print(transormed_values)
# print(values)
# assert transormed_values == values


# Задача №49. Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые
# орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты
# самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется,
# что самая далекая планета ровно одна.


# print("----------|  Задача 49  |----------")

# def find_farthest_orbit(orbits):
#     return max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (100, 100)]
# print(orbits)
# print(find_farthest_orbit(orbits))


# Дополнительная задача №1. Написать функцию, которая принимает список строк и возвращает
# список строк, содержащих только одно слово, с использованием лямбда-функции:
# strings = ["Hello, world!", "This is a sentence.", "Another sentence", "Hi"]
# ["Hello,", "sentence.", "Another"]

# print("----------|  Дополнительная задача №1  |----------")
# strings = ["Hello, world!", "This is a sentence.", "Another sentence", "Hi"]
# strings_1 = list (filter( lambda x: len(x.split())==1, strings))
# print(strings_1)


# Дополнительная задача №2. Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа. Реализовать программу
# с использованием функции filter. Результат отобразить на экране в виде
# последовательности оставшихся чисел в одну строчку через пробел.

# пример - 8 11 0 -23 140 1 => 11 -23

print("----------|  Дополнительная задача №2  |----------")

# numbers = [-8, 11, 0, -23, 140, 1]
# print(*numbers)
# numbers_new = list(filter(lambda x: 10<=x<100 or -10>=x>-100, numbers))
# print(*numbers_new)

# Решение преподвателя
print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))

# Задача №51. Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic
# - это функция, которая принимает объект и вычисляет его характеристику.

print("----------|  Задача 51  |----------")