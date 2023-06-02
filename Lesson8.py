# with open('example.txt', 'r', encoding='utf-8') as file:
#     print(file)
    # text = file.read() # Запишет все содержимое файла в оперативку
    # print(text)
    # file.seek(2) # Чтение из файла со 2 байта
    #####
    # line = file.readline() # Читает 1 строку
    # print(line)
    #####
    # while True:
    #     line = file.readline()
    #     if not line: # Тоже что и line == ''
    #         break
    #     print(line) # Будет печатать пустые строки, т.к. строка заканчивается /n
    #     print(line[:-1]) # Печатать до предпоследнего символа
    ####
    # text = file.read() # readLines() пихает в массив и добавляет \n
    # print(text.splitlines()) # Тоже что и split('\n') Запихнет все в массив
    ####

# with open('example.txt', 'w', encoding='utf-8') as file:
    # some_list = ['hello', 'world', 'how', 'are', 'you']
    # for el in some_list:
    #     file.write(el + '\n')
    ####
    # some_dict = {1: 2, 2: 3}
    # file.write(str(some_dict)[1:-1])

# Пользователь вводит кол-во строк, затем сами строки
# Нужно записать в новый текстовый файл все эти строки.
# Далее пользователь вводит символ, нужно найти кол-во
# этого символа в новом файле.
# num_strings = int(input('Введите число строк: '))
# string_list = []
# print("Введите строку: ")
# for string in range(num_strings):
#     string_list.append(input(f'{string+1}: ') + '\n')
# with open('example.txt', 'w', encoding='utf-8') as file:
#     file.writelines(string_list)
# user_sign = input("Введите символ для поиска: ")
# with open('example.txt', 'r', encoding='utf-8') as file:
#     find_sign = file.read()
# count = 0
# for i in find_sign:
#     if user_sign == i:
#         count += 1
# print(f"Количество символов \'{user_sign}\': {count} шт.")

# Напишите функцию read_last(lines, file), которая будет открывать
# определенный файл file и выводить на печать построчно последние строки
# в количестве lines (на всякий случай проверим, что задано положительное
# целое число).
# Протестируем функцию на файле "article.txt" со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальну длину (или список слов, если таковых несколько)
with open('article.txt', 'r', encoding='utf-8') as file:
    file_text = file.read().replace('\n', ' ')
list_text = file_text.split(' ')
print(list_text)
len_text = list(map(len, list_text))
max_words = list(filter(lambda x: len(x) == max(len_text), list_text))
print(max_words)
