import parse
import os
import telebot
from flask import Flask, request

TOKEN = "2118961153:AAFISocvOir_rVhDEXMGHUL4NCJaaMzg4ng"
APP_URL = 'https://freeepicgamesbot.herokuapp.com/'+TOKEN
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['free'])
def start(message):
    chat_id = message.chat.id
    games = parse.parse()
    text = '*' + game["title"] + '*' + "\n" + game["timer"]
    photo = game["image"]
    url = "https://www.epicgames.com" + game["link"]
    for game in games:
        bot.send_message(chat_id=chat_id, text=text)




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
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))