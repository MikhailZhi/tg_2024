import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '5662951557:AAFUbfCmP8r9uakh28xUgrFxtC5uZZ8rUZQ'
TEXT = 'Был апдейт'
MAX_COUNTER = 5

offset = -2
updates: dict
chat_id: int
counter = 0
timeout = 40


def do_something() -> None:
    print(TEXT, end=' ')


while True:
    start_time = time.time()
    print(f'\n Запрос № {counter} ', end='')
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if 'result' in updates:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['chat']['id']
            do_something()
        print(f'update_id= {offset}, chat_id= {chat_id}, text= {result['message']['text']} ', end='')

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}', end='')
    if counter >= MAX_COUNTER:
        break
    counter += 1

'''while counter < MAX_COUNTER:
    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
        # print(f'update_id= {offset}, chat_id= {chat_id}, text= {result['message']['text']}')

    time.sleep(3)
    counter += 1'''
