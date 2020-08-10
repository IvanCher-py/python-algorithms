# Задание № 5 - Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

letter_one, letter_two = input('Введитe две строчные латинские буквы через пробел: ').split()

scii_starta = 96
place_one = ord(letter_one) - ascii_start
place_two = ord(letter_two) - ascii_start
amount_letter = abs(place_one - place_two) - 1

print(f'Буква: {letter_one}, позиция в алфавите: {place_one}')
print(f'Буква: {letter_two}, позиция в алфавите: {place_two}')
print(f'Количество букв между ними: {amount_letter}')
