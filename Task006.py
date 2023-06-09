# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

n = int(input("Введите шестизначный номер билетика: "))
if n > 99999 and n < 1000000:
    left = int(int(n / 100000) + int(n / 10000 %10) + int(n / 1000 %10))
    right = int(int(n / 100 %10) + int(n / 10 % 10) + int(n % 10))
    print("Сумма цифр левой половинки = ", left)
    print("Сумма цифр правой половинки = ", right)
    if left == right:
        print("Поздравляем! Вам выпла счастливый билетик!")
    else:
        print("Извините, но билетик оказался самым обычным.")
else:
    print("Вы ввели не шестизначный номер, мы не можем определить уровень счастья, попробуйте снова!")