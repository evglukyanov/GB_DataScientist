# Задание # 3
#
# Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список
# из квадратных корней чисел (если число положительное) и самих чисел (если число отрицательное) и возвращает результат
# (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
#
# Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
# 10-20 чисел в списке вполне достаточно.

from random import randint
from math import sqrt


def create_new_list(source):
    return [sqrt(el) if el >= 0 else el for el in source if True]


src_list = [randint(-10, 20) for el in range(20) if True]
print(src_list)

new_list = create_new_list(src_list)
print(new_list)
