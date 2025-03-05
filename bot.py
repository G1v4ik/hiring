import asyncio
import logging
import sys
from os import environ, getenv
from dotenv import load_dotenv
from time import time

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.methods import DeleteWebhook
from aiogram.types import Message


dp = Dispatcher()

async def main():
    load_dotenv()
    bot = Bot(
        token=getenv('TOKEN'), # type: ignore
        default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    #Удалять сообщения, присланные пока бот был оффлайн
    await bot(DeleteWebhook(drop_pending_updates=True))

    dp.include_routers(

    )

    
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,filename="bot/log/log_file.log",filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")
    
    try:
        asyncio.run(main())
    
    except KeyboardInterrupt:
        ...