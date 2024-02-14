from csv import DictReader, DictWriter
from datetime import datetime

def get_datetime(date_string: str):
    """
    Функция конвертирует дату в виде строки в обьект класса datetime

    date_string - cтрока с датой
    """
    date_raw = date_string.split('.')

    return datetime(year=int(date_raw[-1]), month=int(date_raw[-2]), day=int(date_raw[-3]))

def calculate_streams(artist_name: str, song_name: str, date_now: str, date_public: str):
    """
    Фунция считает кол-во просмотров по заданой формуле

    artist_name - имя артиста

    song_name - название песни

    date_now - время сейчас
    
    date_public - дата публикация песни
    """
    return abs((get_datetime(date_now) - get_datetime(date_public)).days / (len(artist_name) + len(song_name))) * 10000

# Загруза данных 
with open('songs.csv', encoding='utf-8-sig') as file:
    data = list(DictReader(file, delimiter=';'))

# Ввывод всех песен не позже 2002 года
for row in data:
    date = get_datetime(row['date'])
    
    if date <= datetime(year=2002, month=1, day=1):
        print(f"{row['track_name']} - {row['artist_name']} - {row['streams']}")

# Изменение данных в таблице
for row in data:
    if int(row['streams']) == 0:
        row['streams'] = int(calculate_streams(row['artist_name'], row['track_name'], '12.05.23', row['date']))

# Запись данных
with open('songs_new.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = DictWriter(file, fieldnames=['streams', 'artist_name', 'track_name', 'date'])
    writer.writeheader()
    writer.writerows(data)