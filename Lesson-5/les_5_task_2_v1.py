# Задание № 2 - Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например,
# пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque


HEX_BASE = 16
HEX_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
HEX_DEC = {HEX_LIST[i]: i for i in range(len(HEX_LIST))}
DEC_HEX = {i: HEX_LIST[i] for i in range(len(HEX_LIST))}


def sum_hex(a, b):
    sum_ = deque()
    add = 0
    for i in range(len(a) - 1, -1, -1):
        a_dec = HEX_DEC[a[i]]

        b_i = len(b) - (len(a) - i)
        if b_i < 0:
            b_dec = 0
        else:
            b_dec = HEX_DEC[b[b_i]]

        sum_dec = a_dec + b_dec + add
        sum_.appendleft(DEC_HEX[sum_dec % HEX_BASE])
        add = sum_dec // HEX_BASE

    if add != 0:
        sum_.appendleft(DEC_HEX[add])

    return sum_


def mult_hex(a, b):
    mult_ = deque()
    for i in range(len(b) - 1, -1, -1):
        add = 0
        mult_i = deque()
        b_dec = HEX_DEC[b[i]]

        for j in range(len(a) - 1, -1, -1):
            a_dec = HEX_DEC[a[j]]

            mult_dec = b_dec * a_dec + add
            mult_i.appendleft(DEC_HEX[mult_dec % HEX_BASE])
            add = mult_dec // HEX_BASE

        mult_i.appendleft(DEC_HEX[add])

        for j in range(len(b) - 1 - i):
            mult_i.append('0')

        mult_ = sum_hex(mult_i, mult_)

    return mult_


def hex_sum_mult(a=None, b=None):
    if a is None and b is None:
        print('Введите два числа в шестнадцатиричной системе исчисления:')
        a = input('a = ')
        b = input('b = ')

    if len(a) < len(b):
        a, b = b, a

    a = deque(a.upper())
    b = deque(b.upper())

    return list(sum_hex(a, b)), list(mult_hex(a, b))


print(hex_sum_mult())