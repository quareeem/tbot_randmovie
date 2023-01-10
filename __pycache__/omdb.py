import os
import requests
import random
import json

API_KEY_OMDB = '58767a9f'
endpoint = 'http://www.omdbapi.com/'
baseurl = 'https://meowfacts.herokuapp.com/'


def get_fact():
    request = requests.get(baseurl)
    # print(request.text)
    return request.json()['data'][0]


def get_random():
    while True:
        rond = ''.join(str(random.randint(0, n)) for n in range(10))
        payload = {'apikey': API_KEY_OMDB, 'type': 'movie', 'i': f'{rond}'}
        rq = requests.get(endpoint, params=payload)
        print(rq.json())

        try:
            print(rq.json()['Genre'] + ' ' + rq.json()['imdbRating'])
            if rq.json()['Genre'] not in ('Short', 'Music'):
                break
        except:
            pass


    res = []
    for k, v in rq.json().items():
        if k in ('Title', 'Year', 'Director', 'Runtime', 'Genre', 'Language'):
            res.append(f'{k}: {v}')
    return res
