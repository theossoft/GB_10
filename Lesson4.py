import random

# # Задача 25 переделаная. Подсчет количества каждого символа в строке
# some_str = ''.join([chr(random.randint(32, 100)) for _ in range(10 ** 5)])
# count_dict = {}
# for letter in some_str:
#     if letter not in count_dict: # Запись в словарь из строки
#         count_dict[letter] = 1
#     else:
#         count_dict[letter] = count_dict[letter] + 1
# print(count_dict)

# Задача №27.
some_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
some_set = set()

print(some_str)
temp_word = ''
for letter in some_str:
    if letter != ' ':
        temp_word += letter
    else:
        if temp_word:
            some_set.add(temp_word)
        temp_word = ''
some_set.add(temp_word)
print(some_set)
print(len(some_set))