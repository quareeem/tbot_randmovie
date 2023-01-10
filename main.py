import requests
import random 
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY_TMDB')
endpoint = 'https://api.themoviedb.org/3/movie/'


def get_text():
    dic = get_id()
    try:
        var = dic['title']
    except:
        return 'not_found'

    title = dic['title']
    date = dic['release_date'][:4]
    runtime = dic['runtime']
    genres = ', '.join([item['name'] for item in dic['genres']])
    overview = dic['overview']
    vote_avg = dic['vote_average']
    vote_count = dic['vote_count']

    result = f'{title} ({date})\n{runtime} min\n{genres}\nrating: {vote_avg} ({vote_count} votes)\n\n'
    return result + overview


def get_id():
    rond = ''.join(str(random.randint(0, 9)) for n in range(4))
    payload = {'api_key': API_KEY}
    rq = requests.get(endpoint + f'{rond}', params=payload)
    return rq.json()


def get_random():
    while True:
        var = get_text()
        if var != 'not_found':
            return var

