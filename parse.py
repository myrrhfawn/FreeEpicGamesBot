import requests
import json
from datetime import datetime, timedelta

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

r = requests.get(url)
response_dict = r.json()
games = response_dict['data']['Catalog']['searchStore']['elements']
for element in games:
    if element['promotions'] and element['promotions']['upcomingPromotionalOffers']:
        date = element['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['endDate']
        d = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.000Z") + timedelta(hours=2)

        endData = f"Бесплатно до {d}"
        print(endData)
    if element['promotions'] and element['promotions']['promotionalOffers']:
        date = element['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']

        d = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.000Z") + timedelta(hours=2)
        endData = f"Бесплатно до {d}"
        print(endData)