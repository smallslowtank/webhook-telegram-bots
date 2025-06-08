import os
import requests
import json

token = os.getenv('BOT_TOKEN')


def send_message(chat_id, text):
    """
    Send text message function
    """
    url = 'https://api.telegram.org/bot' + token + '/' + 'sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, data=data)
    return r


def handler(event, context):
    """
    Entry point
    Точка входа в функцию
    (index.handler)
    Handler will forward 'Hello, world!' to the sender
    """
    try:
        body = json.loads(event['body'])
        chat_id = body['message']['from']['id']
        text = "Hello, world!"

        send_message(chat_id, text)

        r = {'statusCode': 200, 'body': 'Message sent'}

    except Exception as e:
        r = {'statusCode': 404, 'body': 'Same error'}

    return r