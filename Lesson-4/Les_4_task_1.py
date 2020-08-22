# Задание № 1 - Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

# Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

import timeit
import cProfile


def my_slice(a):
    return a[::-1]


def my_reverse(a):
    a = list(a)
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return "".join(a)


def my_recursion(a):
    if len(a) == 1:
        return a
    else:
        return a[-1] + my_recursion(a[:-1])


print(timeit.timeit('my_slice("12345")', number=1000, globals=globals())) # 0.00015420000000000017
print(timeit.timeit('my_slice("1234567654")', number=1000, globals=globals())) # 0.00015949999999999992
print(timeit.timeit('my_slice("9875461")', number=1000, globals=globals()))# 0.0001566999999999992

print(timeit.timeit('my_reverse("12345")', number=1000, globals=globals())) # 0.0008161999999999996
print(timeit.timeit('my_reverse("1234567654")', number=1000, globals=globals())) # 0.0014386000000000017
print(timeit.timeit('my_reverse("9875461")', number=1000, globals=globals())) # 0.0010631000000000008

print(timeit.timeit('my_recursion("12345")', number=1000, globals=globals())) # 0.0012514999999999991
print(timeit.timeit('my_recursion("1234567654")', number=1000, globals=globals())) # 0.002675300000000002
print(timeit.timeit('my_recursion("9875461")', number=1000, globals=globals())) # 0.0017880999999999973

cProfile.run('my_slice("1234567654654987")')
# 1    0.000    0.000    0.000    0.000 Les_4_task_1.py:11(my_slice)
cProfile.run('my_reverse("1234567654654987")')
# 1    0.000    0.000    0.000    0.000 Les_4_task_1.py:15(my_reverse)
cProfile.run('my_recursion("1234567654654987")')
# 16/1    0.000    0.000    0.000    0.000 Les_4_task_1.py:25(my_recursion)

"""
Вывод:
my_slice():  является самым быстрым алгоритмом, т.к. не используется видимый цикл
my_recursion(): является самым долгим т.к. чем больше n, тем больше
раз функция вызовет сама себя
"""