from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
import parser

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def test(message: types.Message):
    ads = parser.get_list_advertisements()
    for ad in ads:
        # string = f'{ad.url}\n{ad.desc}\n{ad.price}\n{ad.place}\n{ad.image}'
        string = f'{ad.url}\n\n{ad.desc}\n\n{ad.price}\n\n{ad.place}\n'
        await message.answer(string, disable_web_page_preview=True)

executor.start_polling(dp, skip_updates=True)
