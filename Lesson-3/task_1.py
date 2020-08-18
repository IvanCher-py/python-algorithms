# Задание № 1 - В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [x for x in range(2, 100)]
b = [x for x in range(2, 10)]

print("В диапазоне натуральных чисел от 2 до 99:")
for num in b:
    count = 0
    for num_array in a:
        if num_array % num == 0:
            count += 1

    print(f"Количество чисел кратных {num}: {count}")