# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
import random
some_list = [random.randint(1, 10) for i in range(1, 10)]
print(len(set(some_list)))

