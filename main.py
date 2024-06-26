import asyncio
from aiogram import Bot, Dispatcher
from cfg import TOKEN
from handlers import start, get_users


# Запуск бота
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(start.router, get_users.router)

    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())