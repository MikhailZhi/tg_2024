import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '5662951557:AAFUbfCmP8r9uakh28xUgrFxtC5uZZ8rUZQ'
TEXT = 'Ура! Классный апдейт!'
MAX_COUNTER = 10

offset = -2
counter = 0
chat_id: int


while counter < MAX_COUNTER:
    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
        # print(f'update_id= {offset}, chat_id= {chat_id}, text= {result['message']['text']}')

    time.sleep(1)
    counter += 1
