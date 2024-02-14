from csv import DictReader

alph = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)]) + 'ё'

def is_russian(name: str, alph: str):
    """
    Проверка на наличие русских букв в имени

    name - имя (строка)

    aplh - алфавит (строка)

    return: есть русские буквы - True, иначе - False (bool)
    """
    for s in name.lower():
        if s in alph:
            return True
        
    return False

# Загруза данных 
with open('songs.csv', encoding='utf-8-sig') as file:
    data = list(DictReader(file, delimiter=';'))

# Спиские артистов
russian_artists = []
foreign_artists = []

# Ищем русских и иностранных артистов
for row in data:
    if is_russian(row['artist_name'], alph):
        russian_artists.append(row['artist_name'])
    else:
        foreign_artists.append(row['artist_name'])

# Вывод длин списков
print('Количество российских исполнителей: ', len(russian_artists))
print('Количество иностранных исполнителей: ', len(foreign_artists))

# Записываем в файл российских артистов
with open('russian_artists.txt', 'w', encoding='utf-8-sig') as file:
    file.write('\n'.join(russian_artists))

# Записываем в файл иностранных артистов
with open('foreign_artists.txt', 'w', encoding='utf-8-sig') as file:
    file.write('\n'.join(foreign_artists))