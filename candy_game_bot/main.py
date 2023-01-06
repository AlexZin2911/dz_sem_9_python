from aiogram.utils import executor

import candy_game_bot.handlers as handlers
from candy_game_bot.bot import dp


async def on_startup(_):
    print('Бот запущен')


handlers.registred_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)