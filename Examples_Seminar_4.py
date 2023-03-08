# Задача №25. Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался. Количество
# повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

""" 
print("----------|  Задача 25  |----------")
# line = (input("Введите строку: "))
line = "a a a b c a a d c d d"
count = {}
for i in line.split():
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

outString = ""
for i in count:
    for j in range(count[i]):
        if j == 0:
            outString += i + " "
        else:
            outString += i + "_" + str(j) +" "
print(outString)

# Решение преподавателя

str = input().split()
result = {}
for i in str:
    if i in result:
        print(f"{i}_{result[i]}", end=" ")
    else:
        print(i, end=" ")
    result[i] = result.get(i, 0)+ 1
print("\n")


# Задача №27. Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих подряд, слова
# разделены одним или большим числом пробелов. Определите, сколько
# различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

print("----------|  Задача 27  |----------")

str = input("Введите строку:\n")
print(f"Количество слов в строке -> {len(set(str.lower().split()))}")
"""
# Задача №29. Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до 
# конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде,
# тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.
import random
print("----------|  Задача 29  |----------")
n=int(input("Введите размер массива: "))
a=[random.randint(0, n) for i in range(n)]
print(a)
count=a[0]
for i in a:
    if i==0:
        break
    if i>count:
        count=i
print(f"Наибольшее значение диапазона -> {count}")