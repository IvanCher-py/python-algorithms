# Задание № 4 - Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = None
qty_most = 0

for i in array:
    qty = array.count(i)
    if qty > qty_most:
        qty_most = qty
        num = i

print(f"Чаще всего встречаемое число в массиве: {num}")