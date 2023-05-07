# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE,
# которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз,
# он остается без изменений; Если символ
# повторяется более 1 раза, к нему
# добавляется количество повторений.

def RLE(string):
    temp_letter = string[0]
    count = 0
    print_string = ''
    for i in string:
        if i == " ":
            continue
        if temp_letter == i:
            count += 1
        else:
            if count < 2:
                print_string = print_string + temp_letter
            else:
                print_string = print_string + temp_letter + str(count)
            temp_letter = i
            count = 1
    print_string = print_string + temp_letter + str(count)
    print(print_string)



RLE("AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB")
# RLE("")
RLE("AA  BB")
RLE("123")