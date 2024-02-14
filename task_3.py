from csv import DictReader, DictWriter

# Загруза данных 
with open('songs.csv', encoding='utf-8-sig') as file:
    data = list(DictReader(file, delimiter=';'))


def search_by_artist(data: list, artist: str):
    """
    Поиск строчки в БД по артисту

    data - данные (список)

    artist - имя артиста (строка)

    return: строчка из БД
    """
    for row in data:
        if row['artist_name'] == artist:
            return row
        
    return None


# Цикл программы
while True:
    artist = input('Введите имя артиста: ')

    if artist == '0':
        break
    
    # поиск песни по артисту
    founded = search_by_artist(data, artist)

    if founded is None:
        print('К сожалению, ничего не удалось найти')
    else:
        print(f"У артиста {founded['artist_name']} найдена песня {founded['track_name']}")

