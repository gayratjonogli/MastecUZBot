import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp, bot, db
from keyboards.default.main_menu import main_menu
from states.main_state import Main
from .messages import whiteMasterbatch


@dp.message_handler(CommandStart(), chat_id=ADMINS, state="*")
async def bot_start(message: types.Message):
    await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
    await Main.main_menu.set()


@dp.message_handler(commands=['add'], state="*")
async def addGrouppp(message: types.Message):
    user_id = message.from_user.id
    # Get the chat ID
    chat_id = message.chat.id
    # Get the chat member info for the user in the chat
    chat_member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    # Check if the user is an admin in the chat
    is_admin = chat_member.is_chat_admin()
    if is_admin:
        group_id = message.chat.id
        data = await bot.get_chat(group_id)
        group_name = data['title']
        await db.add_group(group_name, group_id)
        print(f"Group name {group_name}\nGroup ID {group_id}\n")
    else:
        await message.answer("Sizga ta'qiqlangan!!!")



@dp.message_handler(commands=['adds'], state="*")
async def addSGrouppp(message: types.Message):
    user_id = message.from_user.id
    # Get the chat ID
    chat_id = message.chat.id
    # Get the chat member info for the user in the chat
    chat_member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    # Check if the user is an admin in the chat
    is_admin = chat_member.is_chat_admin()
    if is_admin:
        group_id = message.chat.id
        data = await bot.get_chat(group_id)
        group_name = data['title']
        await db.add_Sgroup(group_name, group_id)
        print(f"Group name {group_name}\nGroup ID {group_id}\n")
    else:
        await message.answer("Sizga ta'qiqlangan!!!")

