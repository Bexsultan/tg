import requests

def get_character_data_by_name(name, raw=False):
    url =  f"https://rickandmortyapi.com/api/character/?name={'%20'.join(name.lower().split())}"

    print(url)

    response = requests.get(url)

    if response.status_code == 404:
        raise Exception('Character found!')

    data = response.json()

    if raw:
        return data

    character = data['results'][0]

    return f"""Имя: {character['name']}
Статус: {character['status']}
Спецификация: {character['species']}
Тип: {character['type']}
Гендер: {character['gender']}
Картинка: {character['image']}
Местоположение: {character['location']['name']}
Эпизод: {', '.join('Episode ' + episode.split('/')[-1] for episode in character['episode'])}"""
