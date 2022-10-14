import json
from datetime import date

import pandas as pd
from repo import IngressoApiRepository

ingresso_api = IngressoApiRepository()
cinemas = ingresso_api.get_theaters()

print(cinemas)

filmes = []

for cinema in cinemas['items']:
    city_id = cinema['cityId']
    corporation = cinema['corporation']
    theater_id = cinema['id']
    logo_cinema = cinema['images'][0]
    nome_cinema = cinema['name']
    cidade = cinema['cityName']
    bairro = cinema['neighborhood']
    estado = cinema['state']
    sessions = ingresso_api.get_sessions(city_id, theater_id)

    for session in sessions:

        for movie in session['movies']:

            for room in movie['rooms']:

                for room_section in room['sessions']:

                    filmes_por_cinema = {
                        'title': movie['title'],
                        'corporation': corporation,
                        'nome_cinema': nome_cinema,
                        'sala': room['name'],
                        'type': room_section['type'][0] + ' - ' + room_section['type'][1],
                        'cidade': cidade,
                        'bairro': bairro,
                        'estado': estado,
                        'price': room_section['price'],
                        'dayOfWeek': room_section['realDate']['dayOfWeek'],
                        'dayAndMonth': room_section['realDate']['dayAndMonth'],
                        'hour': room_section['realDate']['hour'],
                        'year': room_section['realDate']['year'],
                        'data': room_section['realDate']['localDate'],
                    }

                    print(filmes_por_cinema)

                    # for dia in dias:
                    filmes.append(filmes_por_cinema)


today = date.today()
file_name = f'importacoes/ingresso_com_{today.strftime("%b-%d-%Y")}'

with open(f'{file_name}.json', 'w') as outfile:
    json.dump(filmes, outfile)


df = pd.read_json(f'{file_name}.json')
df.to_csv(f'{file_name}.csv', index=None, sep=';')
