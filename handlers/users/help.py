# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandHelp
# from aiogram.dispatcher import FSMContext
# from loader import dp, bot
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
#
#
# @dp.message_handler(CommandHelp())
# async def bot_help(message: types.Message):
#     text = ("Buyruqlar: ",
#             "/start - Botni ishga tushirish",
#             "/help - Yordam")
#
#     await message.answer("\n".join(text))
#
# buttons_list = ['button', 'button 2', 'button 3', 'button 4']
#

#
# @dp.message_handler(text='b', state="*")
# async def showButtons(message: types.Message, state: FSMContext):
#     markup = InlineKeyboardMarkup(row_width=2)
#     for key, value in language_btn_txt.items():
#         markup.insert(InlineKeyboardButton(text=key, callback_data=value))
#
#     await message.answer("Tanlang: ", reply_markup=markup)
#     await state.set_state("get")
#
#
# @dp.callback_query_handler(text_contains='btn', state="get")
# async def makeActions(call: CallbackQuery, state: FSMContext):
#     action = call.data
#     if action == "btn1":
#         await call.message.answer("Siz btn 1 bostiz")
#     elif action == "btn2":
#         await call.message.answer("Siz btn 2 bostiz")


for i in range(1,30):
    if i % 2 != 0:
        print(i)