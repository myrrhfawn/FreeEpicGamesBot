import os
import telebot
from flask import Flask, request

TOKEN = '2118961153:AAFISocvOir_rVhDEXMGHUL4NCJaaMzg4ng'
APP_URL = f'https://git.heroku.com/freeepicgamesbot.git{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.mesage_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'hello,' + message.from_user)

@bot.mesage_handler(func=lamda message: True, cotent_types=['text'])
def echo(message):
    bor.reply_to(message, message.text)

@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_date().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bor.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))