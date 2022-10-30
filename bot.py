from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.utils import executor

from config import TOKEN
import parser

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def test(message: types.Message):
    ads = parser.get_list_advertisements()
    for ad in ads:
        photo = InputFile(ad.image_path)
        string = f'{ad.url}\n\n{ad.desc}\n\n{ad.price}\n\n{ad.place}\n'
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=string)

executor.start_polling(dp, skip_updates=True)
