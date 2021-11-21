import os
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

URL = 'https://www.epicgames.com/store/ru'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', 'accept': '*/*'}

def get_html(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_SHIM', None)
    browser = webdriver.Chrome(executable_path='C:\Users\rostyk\Downloads\Важливе\FreeEpicGamesBot2.0\chromedriver.exe', chrome_options=chrome_options)
    browser.get(url)
    r = browser.page_source
    browser.quit()
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    tmp = soup.find('div', class_='css-15u9bv0')
    items = tmp.find_all('div', class_='css-5auk98')
    games = []
    for item in items:
        games.append({
            'image': item.find("div", class_="css-1lozana").find('img')['data-image'],
            'title': item.find('div', class_='css-1h2ruwl').get_text(),
            'timer': item.find('span', class_='css-os6fbq').get_text().replace('\xa0', ' '),
            'link' : item.find("div", class_="css-nq799m").find('a')['href']
        })
    return games

def parse():
    html = get_html(URL)
    code = requests.get(URL, headers=HEADERS)
    if code.status_code == 200:
        games = get_content(html)
        print("Sucsess!")
        return games
    else:
        print("Error")

