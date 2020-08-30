# Задание № 3 -  Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.


import random


n = int(input(f'Введите целое число: '))

SIZE = 2 * n + 1
MIN_ITEM = 0
MAX_ITEM = 50
my_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def cocktail_sort(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1
        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1
    return array


def median(lst):
    my_list = cocktail_sort(lst)
    print(my_list)
    i = (len(lst) - 1) // 2
    return my_list[i]


print(my_array)
print('*' * 50)
print(median(my_array))