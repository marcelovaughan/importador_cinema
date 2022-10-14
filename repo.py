import requests
import json
import urllib.request


class IngressoApiRepository:

    def __init__(self, *args, **kwargs):
        self.url = 'https://api-content.ingresso.com/v0/'
        self.partnership = 'dtfilmes'

    def request_dados(self, route):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'}

        res = requests.get(self.url + route, headers=headers)

        if res.ok != True:
            return json.loads('{}')

        res = json.loads(str(res.text))
        return res

    def get_theaters(self):
        return self.request_dados('theaters/partnership/' + self.partnership)

    def get_sessions(self, city, theater):
        url = 'sessions/city/' + str(city) + '/theater/' + str(theater) + '?partnership=' + self.partnership
        return self.request_dados(url)
