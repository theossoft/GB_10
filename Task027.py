# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# Создаем множество для хранения уникальных слов
words_set = set()

# Инициализируем переменные
word_start = None

# Проходим по каждому символу в тексте
for i, char in enumerate(text):
    if not char.isspace() and (i == 0 or text[i-1].isspace() or text[i-1] in '.,;:-!?'):
        # Если текущий символ является первым символом нового слова,
        # запоминаем его позицию
        word_start = i
    elif (char.isspace() or i == len(text)-1) and word_start is not None:
        # Если текущий символ является пробелом или последним символом текста,
        # а предыдущий символ был началом нового слова, то извлекаем слово из текста
        # и добавляем его в множество
        word_end = i if char.isspace() else i+1
        word = text[word_start:word_end].strip('.,;:-!?')   # удаляем знаки препинания с начала и конца слова
        words_set.add(word.lower())   # добавляем слово в множество в нижнем регистре
        word_start = None

# Выводим количество уникальных слов в множестве
print(len(words_set))