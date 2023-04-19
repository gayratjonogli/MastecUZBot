from aiogram import executor
import asyncio
import aioschedule
from loader import dp, db, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.scheduled import start_scheduler


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await db.create()
    await db.create_table_groups()
    await db.create_tableSpecialGroups()
    # await db.create_table_elons()
    await on_startup_notify(dispatcher)
    start_scheduler()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
