from csv import DictReader
from string import ascii_lowercase

def hash(string: str, d: dict):
    p = 67
    m = 67 * 10 ** 9

    p_pow = 1

    hash_value = 0

    for symbol in string:
        hash_value = (hash_value + d[symbol] * p_pow) % m

        p_pow = (p * p_pow) % m

    return hash_value

# Генерируеи алфавит
alph = ascii_lowercase + ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)]) + 'ё'
alph += ' ' + alph.upper()
d = dict((row, i) for i, row in enumerate(alph))

# Загруза данных 
with open('songs.csv', encoding='utf-8-sig') as file:
    data = list(DictReader(file, delimiter=';'))

# Хешируем БД
for row in data:
    row['hash'] = hash(row['name'], d)

