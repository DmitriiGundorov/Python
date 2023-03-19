# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


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