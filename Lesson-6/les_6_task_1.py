# Задание № 1 - Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы
# с наиболее эффективным использованием памяти.


import sys
from memory_profiler import profile


@profile()
def my_slice(a):
    print(f'type={type(a)}, size={sys.getsizeof(a[::-1])}, count={sys.getrefcount(a)} obj={a}')
    return a[::-1]


@profile()
def my_reverse(a):
    a = list(a)
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    print(f'type={type(a)}, size={sys.getsizeof(a)}, count={sys.getrefcount(a)} obj={a}')
    return "".join(a)


def my_recursion(a):
    print(f'type={type(a)}, size={sys.getsizeof(a)}, count={sys.getrefcount(a)} obj={a}')
    if len(a) == 1:
        return a
    else:
        return a[-1] + my_recursion(a[:-1])


my_str = "123456789012345678901234567890"

print("Срез:")
print(my_slice(my_str))

print("Список:")
print(my_reverse(my_str))

print("Рекурсия:")
print(my_recursion(my_str))


# Выводы:
# OS -  Windows 10 Pro
# Разрядность - X64
# PYTHON - 3.8.2
# Не понял как посичтать потребляемую память рекурсией. Срез использует меньшее количество памяти по сравнению с со списком.

