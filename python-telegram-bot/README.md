### Код из Cloud Apps Demo Telegram Bot YandexGPT (python-telegram-bot)

https://yandex.cloud/ru/marketplace/products/yc/yagpt-telegram-bot

Телеграм отправляет сообщения на Webhook, в роли которого выступают API-Gateway и Message Queue.

Далее срабатывает триггер и вызывает функцию, которая является телеграм-ботом.

#### Порядок развертывания следующий:

1.создать сервисный аккаунт с необходимыми правами доступа к ресурсам. Для тестирования можно выдать роль editor на каталог.

2.создать очередь

3.создать гейтвей для этой очереди

4.создать функцию

5.создать триггер на очередь и вызов функции

6.подключить вебхук к гейтвею

Практически везде используются настройки по умолчанию.

Ссылки на документацию есть в папке docs