from pprint import pprint
import datetime

import requests


def most_heroes_with_intelligence(heroes):
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/"
    heroes_with_intelligence = []
    for hero in heroes:
        heroes_from_response = requests.get(url + hero).json()['results']
        for hero_current in heroes_from_response:
            if hero_current['name'] == hero:
                hero_with_intelligence = (hero, hero_current['powerstats']['intelligence'])
                heroes_with_intelligence.append(hero_with_intelligence)

    def sorted_by_intelligence(tuple):
        return tuple[1]

    heroes_with_intelligence.sort(key=sorted_by_intelligence, reverse=True)
    return heroes_with_intelligence[0][0]


class YaUploader:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': self.token}

    def upload(self, file_path):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url, params=params, headers=self.headers)
        response = requests.put(response.json()['href'])
        return response.status_code


def questions_with_tag(tag='python'):
    result = []
    url = 'https://api.stackexchange.com/2.2/questions'
    to_date = datetime.date.today()
    from_date = datetime.datetime(to_date.year, to_date.month, to_date.day - 1)
    params = {'order': 'desc', 'sort': 'activity', 'site': 'stackoverflow', 'todate': to_date, 'fromdate': from_date}
    questions =  requests.get(url, params=params).json()['items']
    for question in questions:
        if tag in question['tags']:
            result.append(question['link'])
    return result

if __name__ == '__main__':
    heroes = ['Hulk', 'Captain America', 'Thanos']
    print(most_heroes_with_intelligence(heroes))

    token = ''
    uploader = YaUploader(token)
    print(uploader.upload('upload.txt'))

    #только ссылки вытаскивал
    pprint(questions_with_tag())