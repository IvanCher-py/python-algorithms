# Задание № 1 - Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/11XGBjd0RrZeZXHi2zHJw5RLEIZow7Cia/view?usp=sharing

a = int(input('Введите трехзначное целое число: '))

b = a // 100
c = a // 10 % 10
d = a % 10

print(f"Сумма трехзначного числа равна: {b + c + d} \nПроизведение трехзначного числа равна: {b * c * d}")

