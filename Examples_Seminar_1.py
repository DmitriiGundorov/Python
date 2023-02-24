"""
#Задача 1. Найти из двух чисел большее
print("Введите первое число a:")
a=int(input())
print("Введите второе число b:")
b=int(input())
if a>b:
    print( f"Число a = {a} > b = {b}")
elif b>a:
    print( f"Число b = {b} > a = {a}")
else:
    print( f"Число  a = b = {a}")


#Задача 2. За день машина проезжает n километров. Сколько 
# дней нужно, чтобы проехать маршрут длиной m 
# километров? При решении этой задачи нельзя 
# пользоваться условной инструкцией if и циклами.

print("Введите пройденное растояние машины за день, км n:")
n=int(input())
print("Введите дистанцию маршрута, км m:")
m=int(input())
day=(m+n-1)//n
print( f" Время в пути, дней -> {day}")

# Задача 2. В некоторой школе решили набрать три новых 
# математических класса и оборудовать кабинеты для 
# них новыми партами. За каждой партой может сидеть 
# два учащихся. Известно количество учащихся в 
# каждом из трех классов. Выведите наименьшее 
# число парт, которое нужно приобрести для них.

print("Введите количество учеников первого математического класса, class_1:")
с1=int(input())
print("Введите количество учеников второго математического класса, class_2:")
с2=int(input())
print("Введите количество учеников третьего математического класса, class_3:")
с3=int(input())
c=(с1+1)//2+(с2+1)//2+(с3+1)//2
print( f"Необходимое количество парт для учеников -> {c}")



# Задача 3. Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны 
# нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет 
# электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите 
# программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

print("Введите количество вагонов с головы поезда, i:")
i=int(input())
print("Введите количество вагонов с хвоста поезда, j:")
j=int(input())
if i==j:
    print("Недостаточно данных")
else:
    print(f"Количество вагонов в поезде -> {i+j-1}")


    
# Задача 4. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если 
# год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с 
# григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 
# 100, а также если он кратен 400.

print("Введите номер года, year:")
year= int(input())
if(year%4==0 & year%400==0):
    print(f"Год {year} високосный")
elif(year%100!=0):
    print(f"Год {year} не високосный")
else:
    print(f"Год {year} не високосный")

# или другое решение

year= int(input("Введите номер года, year: "))
print(f"{year%4==0 & year%100!=0 or year%400==0}")



# Задача 5. Напишите программу, которая будет принимать 
# на вход дробь и показывать первую цифру дробной части числа

num=float(input("Введите вещественное число: "))
print(f"{int((num*10)%10)}")
"""


# Задача 6. Напишите программу, которая будет принимать на вход
# координаты двух точек и находит расстояние между ними в 2В пространстве.

x1=float(input("Введите координату Х первой точки: "))
y1=float(input("Введите координату Y первой точки: "))
x2=float(input("Введите координату Х второй точки: "))
y2=float(input("Введите координату Y второй точки: "))
print(((x1-x2)**2+(y1-y2)**2)**0.5)