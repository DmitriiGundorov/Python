# Разбор домашнего задания

# Задача №34. Решение студента

# dictionary = "АЕЁИОУЫЭЮЯ"
# def count_vowel(str):
#     count = 0
#     for l in str:
#         if l.upper() in dictionary:
#             count += 1
#     return count
# string_1 = list(map(count_vowel,string.split()))

# if all(x == string_1[0] for x in string_1):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# Задача №34. Решение преподавателя

# stroka1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka1.split()
# if len(phrases) < 2:
#     print('Количество фраз должно быть больше одной!')
# else:
#     countVowels = []

# for i in phrases:
#     countVowels.append(len([x for x in i if x.lower() in vowels]))

#     if countVowels.count(countVowels[0]) == len(countVowels):
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')

# Из лекции
# list_1 = [x for x in range(1,21)]
# print(list_1)
# list_1=list(map(lambda x: x+100, list_1))
# print(list_1)


# Дополнительная задача №1. Вводится натуральное число N. С помощью list comprehension
# сформировать двумерный список размером N x N, состоящий из нулей, а по главной
# диагонали - единицы. (Главная диагональ - это элементы, идущие по диагонали от верхнего
# левого угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы
# чисел как показано в примере ниже.
# Input: 4
# Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1


# print("----------|  Дополнительная задача №1  |----------")


# def get_matrix(n):
#     return [[int(i == j) for i in range(n)] for j in range(n)]


# print(*get_matrix(5), sep="\n")

# Решение преподавателя

# N = int(input())
# lst = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
# for r in lst:
#     print(*r)

# Дополнительная задача №2. Преобразовать набора списков
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]


# print("----------|  Дополнительная задача №2  |----------")

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]


# list_1 = list(zip(users, ids, salary))
# print(list_1)
# list_2 = list(zip(*zip(users, ids, salary)))
# print(list_2)

# Решение преподавателя

# a, b, c = map(list, zip(users, ids, salary))
# print(a, b, c, sep="\n")
# a, b, c = map(list, zip(a, b, c))

# print(a, b, c, sep="\n")


# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


import csv
print("----------|  Задача 49  |----------")


def show_menu() -> int:
    print("\nСправочник имеет следующие функции:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонент из справочника\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу\n"
          "Выберите необходимое действие:", end=" ")
    choice = int(input())
    return choice


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(",")))
            data.append(record)
    return data


def write_csv(filename: str, data) -> str:  # Запись в справочник с разрешением .csv
    file = open(filename, "w", encoding="utf-8")
    for lines in data:
        s = ", ".join(f"{v}" for k, v in lines.items())
        file.write(s + "\n")


def write_txt(filename: str, data) -> str:  # Запись в справочник с разрешением .txt
    file = open(filename + ".txt", "w", encoding="utf-8")
    for lines in data:
        s = ", ".join(f"{v}" for k, v in lines.items())
        file.write(s + "\n")


def get_file_name() -> str:
    file_name = input("Выберите файл, в который хотите сохранить запись -> ")
    return file_name


def print_result(data) -> list:  # Отображение всего справочника
    print(*data, sep="\n")


def find_by_name(data, sirname) -> str:  # Поиск абонента по Фамилии
    for key in data:
        if key["Фамилия"].upper() == sirname.upper():
            return key.values()
    return ("Данного пользователя в справочнике не существует.")


def find_by_number(data, tel_numbers) -> str:  # Поиск абонента по померу телефона
    for key in data:
        if key["Телефон"] == tel_numbers:
            return key.values()


def add_new_eser() -> dict:  # Добавление абонента в справочник
    record = {
        "Фамилия": input("Введите фамилию -> "),
        "Имя": input("Введите имя -> "),
        "Телефон": input("Введите номер телефона -> "),
        "Описание": input("Введите описание -> ")}
    return record


def add_user(data, new_record) -> list:
    data.append(new_record)
    print(*data, sep="\n")


def delete_user(data: list, last_name: str) -> str:
    for i in range(len(data)):
        if data[i].get("Фамилия") == last_name:
            del data[i]
            return f"Абонент {last_name} успешно удален"
    return "Такой абонент отсутствует в списке"


phone_book = read_csv("phonebook.csv")
choice = show_menu()

while (choice != 7):
    if choice == 1:
        print()
        print_result(phone_book)
    elif choice == 2:
        name = (input("Введите фамилию абонента -> "))
        print(*find_by_name(phone_book, name))
    elif choice == 3:
        number = (input("Введите номер телефона абонента -> "))
        print(*find_by_number(phone_book, number))
    elif choice == 4:
        user_data = add_new_eser()
        add_user(phone_book, user_data)
        write_csv('phonebook.csv', phone_book)
    elif choice == 5:
        user_data = input(
            "Введите фамилию пользователя, которого хотите удалить из справочника -> ")
        delete_user(phone_book, user_data)
        write_csv('phonebook.csv', phone_book)
    elif choice == 6:
        file_name = get_file_name()
        write_txt(file_name, phone_book)
    choice = show_menu()
