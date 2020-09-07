# Задание № 1 - Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.


def count_subs(string):
    result = set()
    for i in range(1, len(string)):
        for j in range(len(string) - i + 1):
            h = hash(string[j:i+j])
            result.add(h)
            print(string[j:i+j])

    return len(result)


s = input('Введите строку: ')

print(f'В данной строке {count_subs(s)} различных подстрок')