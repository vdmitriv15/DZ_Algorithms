"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Ряд строить программно - в самой же рекурсивной ф-ции
или даже обойтисть без создания ряда

Элемент в 2 раза меньше предыд и имеет противопол знак
"""


def sum(n, start_num=1):
    if n == 1:
        return start_num
    n -= 1
    return start_num + sum(n, start_num * -0.5)


try:
    count = int(input("введите количество элементов-> "))
    print(f"сумма элеметов = {sum(count)}")
except ValueError:
    print('работает только с числами')

