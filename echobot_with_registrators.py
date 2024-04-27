from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

BOT_TOKEN = '5785150011:AAFfBxg0EpqYDtYcuARILwXY8BDlk-_qQzs'  # https://t.me/Mike_sdbot reloc_sd_bot

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Хэндлер для обработки команды "start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Хэндлер для обработки команды "help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Хэндлер для ответа на картинку
async def send_photo_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))  # конструкция для спокойного чтения формата json
    await message.reply_photo(message.photo[0].file_id)


# Хэндлер для ответа на стикер
# async def send_sticker_echo(message: Message):
#     print(message.model_dump_json(indent=4, exclude_none=True))  # конструкция для спокойного чтения формата json
#     await message.reply(text='Это стикер')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)


# этот хэндлер будет отвечать на все, что не обработали ранее
async def send_echo_all(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )

# ! Если не использовать конструкцию "@dp.message()", то придется регистрировать хэндлеры.
# Регистрируем хэндлеры.
# Регистрировать надо ДО точки выхода, но после основной части программы
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
# dp.message.register(send_sticker_echo, F.content_type == ContentType.STICKER)
dp.message.register(send_echo)
dp.message.register(send_echo_all)

if __name__ == '__main__':
    print('Запускаем!...')
    dp.run_polling(bot)
