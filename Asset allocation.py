from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = '5785150011:AAFfBxg0EpqYDtYcuARILwXY8BDlk-_qQzs'  # https://t.me/Mike_sdbot reloc_sd_bot

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Создаю класс конечных состояний для приема и обработки инвестиций
class Investment(StatesGroup):
    new_investment_title = State()
    new_investment_cost = State()
    new_investment_target = State()


@dp.message(Command(commands='start'))  # Обработчик команды start
async def command_start(message):
    print('start')
    # await bot.send_message(chat_id=message.chat.id, text='Hello!', reply_to_message_id=message.message_id)
    await message.reply(text='''Я знаю команды:
                             /start
                             /new_investment''')


@dp.message(Command(commands='new_investment'))  # команда для начала ввода новых инвестиций
async def command_new_investment(message, state):
    await message.reply(text='Введите название инвестиции')
    await state.set_state(Investment.new_investment_title)


@dp.message(Command(commands='cancel'))  # команда для отмены текущего состояния
async def command_cancel(message, state):
    await message.reply(text='Действие отменено.')
    await state.clear()


# @dp.message(OrderFood.choosing_food_size, F.text.in_(available_food_sizes))
@dp.message(Investment.new_investment_title)
async def new_investment_title(message, state):
    # user_data = await state.get_data()
    new_investment_title_data = message.text.lower()
    print(state)
    await message.reply(text=f'Для инвестиции"{new_investment_title_data}"\nВведите цену вложения')
    await state.set_state(Investment.new_investment_cost)


if __name__ == '__main__':
    print('Запускаем!..')
    dp.run_polling(bot)
