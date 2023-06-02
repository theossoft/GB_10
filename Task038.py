# Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые
# должны находиться в файле.
#
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска
# определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def import_data(file_path):
    with open(file_path, "r") as f:
        data = []
        for line in f:
            item = line.strip().split(",")
            data.append({"last_name": item[0], "first_name": item[1], "patronymic": item[2], "phone_number": item[3]})
        return data

def export_data(file_path, data):
    with open(file_path, "w") as f:
        for item in data:
            line = ",".join([item["last_name"], item["first_name"], item["patronymic"], item["phone_number"]])
            f.write(line + "\n")

def search_data(data, key, value):
    result = []
    for item in data:
        if item[key] == value:
            result.append(item)
    return result


def main():
    file_path = "phonebook.txt"
    data = import_data(file_path)

    while True:
        print("Выберите действие:")
        print("1. Просмотреть все записи")
        print("2. Добавить новую запись")
        print("3. Найти записи")
        print("4. Экспортировать данные")
        print("5. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == "1":
            for item in data:
                print(f"{item['last_name']} {item['first_name']} {item['patronymic']}: {item['phone_number']}")

        elif choice == "2":
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")

            data.append({"last_name": last_name, "first_name": first_name, "patronymic": patronymic,
                         "phone_number": phone_number})

            print("Запись добавлена успешно!")

        elif choice == "3":
            key = input("Введите ключ для поиска (last_name, first_name, patronymic или phone_number): ")
            value = input("Введите значение для поиска: ")

            result = search_data(data, key, value)

            if len(result) > 0:
                for item in result:
                    print(f"{item['last_name']} {item['first_name']} {item['patronymic']}: {item['phone_number']}")
            else:
                print("Записи не найдены.")

        elif choice == "4":
            export_data(file_path, data)
            print("Данные экспортированы в файл.")

        elif choice == "5":
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    main()