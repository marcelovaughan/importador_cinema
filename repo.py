import requests
import json
import os


class IngressoApiRepository:

    def __init__(self, *args, **kwargs):
        self.url = 'https://api-content.ingresso.com/v0/'
        self.partnership = 'dtfilmes'

    def request_dados(self, route):

        res = requests.get(self.url + route)

        if res.ok != True:
            return json.loads('{}')

        res = json.loads(str(res.text))
        return res

    def get_theaters(self):
        return self.request_dados('theaters/partnership/' + self.partnership)

    def get_sessions(self, city, theater):
        url = 'sessions/city/' + str(city) + '/theater/' + str(theater) + '?partnership=' + self.partnership
        return self.request_dados(url)
