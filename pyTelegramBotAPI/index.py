import requests
import telebot
import json
import os

API_TOKEN = os.environ['BOT_TOKEN']

bot = telebot.TeleBot(API_TOKEN, threaded=False)


def process_event(event):
    request_body_dict = json.loads(event['body'])
    update = telebot.types.Update.de_json(request_body_dict)

    bot.process_new_updates([update])


def handler(event, context):
    """
    Entry point
    Точка входа в функцию
    (index.handler)
    """
    process_event(event)
    return {
        'statusCode': 200
    }


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    """
    Handle '/start' and '/help'
    """
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    """
    Handle all other messages with content_type 'text' (content_types defaults to ['text'])
    """
    bot.reply_to(message, message.text)
