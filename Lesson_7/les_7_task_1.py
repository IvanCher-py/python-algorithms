# Задание № 1 - Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
my_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def my_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    print(array)


print(my_array)
print('*' * 50)
my_sort(my_array)