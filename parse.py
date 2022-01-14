import requests
import json

url = 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=ru&country=UA&allowCountries=UA'


def get_content(r):
    response_dict = r.json()
    games = response_dict['data']['Catalog']['searchStore']['elements']
    return games

def parse():
    r = requests.get(url)
    if r.status_code == 200:
        games = get_content(r)
        print("Sucsess!")
        return games
    else:
        print("Error")


