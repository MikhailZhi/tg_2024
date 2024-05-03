from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = '5785150011:AAFfBxg0EpqYDtYcuARILwXY8BDlk-_qQzs'  # https://t.me/Mike_sdbot reloc_sd_bot

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Создаю класс конечных состояний для приема и обработки инвестиций
class Investment(StatesGroup):
    new_investment_title = State()
    new_investment_cost = State()
    new_investment_target = State()


# список для хранения полученных данных о новой инвестиции
new_investment_data = []


@dp.message(Command(commands='start'))  # Обработчик команды start
async def command_start(message):
    print('start')
    # await bot.send_message(chat_id=message.chat.id, text='Hello!', reply_to_message_id=message.message_id)
    await message.reply(text='''Я знаю команды:
                             /start
                             /new_investment
                             /cancel''')


@dp.message(Command(commands='new_investment'))  # команда для начала ввода новых инвестиций
async def command_new_investment(message, state):
    await message.reply(text='Введите название инвестиции')
    await state.set_state(Investment.new_investment_title)


@dp.message(Command(commands='cancel'))  # команда для отмены текущего состояния
async def command_cancel(message, state):
    await message.reply(text='Действие отменено.')

    await state.clear()


# handler
@dp.message(Investment.new_investment_title)
async def new_investment_title(message, state):
    new_investment_data.append(message.text.lower())
    print(new_investment_data)
    await message.reply(text=f'Для инвестиции "{new_investment_data[0]}"\n'
                             f'Введите цену вложения'
                             f'PS - целое число, без пробелов, в рублях')
    await state.set_state(Investment.new_investment_cost)


# handler
@dp.message(Investment.new_investment_cost)
async def new_investment_cost(message, state):
    new_investment_data.append(message.text)
    print(new_investment_data)
    await message.reply(text='Введите ожидаемую цену продажи:'
                             'PS - целое число, без пробелов, в рублях')
    await state.set_state(Investment.new_investment_target)


# handler
@dp.message(Investment.new_investment_target)
async def new_investment_target(message, state):
    new_investment_data.append(message.text)
    print(new_investment_data)
    await message.answer(text=f'Для инвестиции {new_investment_data[0]}\n'
                              f' Вложения составляют {new_investment_data[1]}\n'
                              f' Цена продажи ожидается {new_investment_data[2]}')
    await state.clear()

if __name__ == '__main__':
    print('Запускаем!..')
    dp.run_polling(bot)
