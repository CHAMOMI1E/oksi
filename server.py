import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import TOKEN_TEST
from bot.routers.admin import start_router

bot = Bot(TOKEN_TEST, parse_mode=ParseMode.HTML)
dp = Dispatcher()


async def main() -> None:
    dp.include_routers(start_router,)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s"
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
                        stream=sys.stdout)
    try:

        asyncio.run(main())
    except KeyboardInterrupt:
        print('stop')
