# Задание № 7 - В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

a = 0
b = 0
for x in array:
    if x <= a:
        a, b = x, a
    elif x < b:
        b = x

print(a, b)