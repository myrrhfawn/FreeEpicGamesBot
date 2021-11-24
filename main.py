import parse
import os
import telebot
import time
import schedule
from telebot import types
from flask import Flask, request
from threading import Thread

TOKEN = "2118961153:AAFISocvOir_rVhDEXMGHUL4NCJaaMzg4ng"
APP_URL = 'https://freeepicgamesbot.herokuapp.com/'+TOKEN
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
games = parse.parse()


@bot.message_handler(commands=['free'])
def free(message):
    chat_id = message.chat.id
    print("chat_id is" + str(chat_id))
    for game in games:
        text = '*' + game["title"] + '*' + "\n" + game["timer"]
        photo = game["image"]
        url = "https://www.epicgames.com" + game["link"]
        markup = types.InlineKeyboardMarkup(row_width=1)
        item = types.InlineKeyboardButton('Перейти', url=url)
        markup.add(item)
        bot.send_photo(chat_id=chat_id,
                       parse_mode='Markdown',
                       photo=photo,
                       caption=text,
                       reply_markup=markup
                       )

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(3)

def change_game():
    games = parse.parse()
    for game in games:
        print("game")
        text = '*' + game["title"] + '*' + "\n" + game["timer"]
        photo = game["image"]
        url = "https://www.epicgames.com" + game["link"]
        markup = types.InlineKeyboardMarkup(row_width=1)
        item = types.InlineKeyboardButton('Перейти', url=url)
        markup.add(item)
        bot.send_photo(chat_id=472883978,
                       parse_mode='Markdown',
                       photo=photo,
                       caption=text,
                       reply_markup=markup
                       )
    return games

@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200

if __name__ == '__main__':
    print("start")
    schedule.every(1).minutes.do(change_game)
    Thread(target=schedule_checker).start()
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
