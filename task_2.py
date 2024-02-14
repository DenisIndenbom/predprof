from random import choice
from csv import DictReader

def fast_sort(arr: list, key = lambda x: x):
    """
    Алгоритм быстрой сортировки

    arr - список, который нужно отсортировать

    key - ключь по которому идёт сортировка (lambda функция или просто функция) 

    return: отсортированный список
    """
    if len(arr) <= 1:
        return arr

    l = [] # lower
    g = [] # greater
    e = [] # equel

    n = choice(arr)

    for row in arr:
        if key(row) < key(n): 
            l.append(row)
        elif key(row) > key(n):
            g.append(row)
        else:
            e.append(row)

    return fast_sort(l, key = key) + e + fast_sort(g, key = key)


# Загруза данных 
with open('songs.csv', encoding='utf-8-sig') as file:
    data = list(DictReader(file, delimiter=';'))

data = fast_sort(data, key=lambda x: x['date'])

# Топ 5 самых ранних песен
for i, row in enumerate(data[:5]):
    print(f"{i + 1} {row['track_name']}, {row['artist_name']}, {row['date']}")