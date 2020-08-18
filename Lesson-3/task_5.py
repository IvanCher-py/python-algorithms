# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_index = 0
for i in range(1, len(array)):
    if array[i] < array[min_index]:
        min_index = i

if array[min_index] < 0:
    negative = min_index
    for i in range(len(array)):
        if array[negative] < array[i] < 0:
            negative = i
    print(f"Максимальный отрицательный элемент: {array[negative]}, индекс: {negative}")
else:
    print("Нет отрицательных чисел!")