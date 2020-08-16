# Задание № 4 -	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


def create_seq(a, n):
    if n == 1:
        return str(a)
    else:
        return str(a) + " " + create_seq(-1 * a / 2, n - 1)


n = int(input("Введите натуральное число n: "))

if n > 0:
    my_seq = create_seq(1, n)
    print(f"Ряд: {my_seq}")
    y = 0
    for x in my_seq.split():
        x = float(x)
        y += x
    print(f"Сумма элементов: {y}")
else:
    print('Ошибка ввода!')
