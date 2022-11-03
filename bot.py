import asyncio
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.utils import executor
from sqlighter import SQLighter

from config import TOKEN
import parser

logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = SQLighter('db.db')

@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(message.from_user.id)
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, True)

    await message.answer("Вы успешно подписались на рассылку!")


# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы итак не подписаны.")
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписаны от рассылки.")


async def test(wait_for):
    while True:
        ads = parser.get_list_advertisements()
        for ad in ads:
            await asyncio.sleep(wait_for)
            string = f'\nСсылка на объявление: {ad.url}\n\nОписание: {ad.desc}\n\nЦена: {ad.price}\n\nМестоположение: {ad.place}\n'
            subscriptions = db.get_subscriptions()
            for sub in subscriptions:
                photo = InputFile(ad.image_path)
                try:
                    await bot.send_photo(chat_id=sub[1], photo=photo, caption=string)
                except:
                    continue

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(test(1))
    executor.start_polling(dp, skip_updates=True)
