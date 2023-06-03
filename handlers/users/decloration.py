from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from loader import db, dp, bot
from aiogram.dispatcher import FSMContext
from states.main_state import Main
from keyboards.default.main_menu import main_menu
from datetime import datetime
import re


@dp.message_handler(text="🗣 E'lon berish", state=Main.main_menu)
async def first_step(message: Message, state: FSMContext):
    groups_list = await db.show_all()
    if len(groups_list) == 0:
        await message.answer("E'lon berishdan avval guruh qo'shing!")
        await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
        await Main.main_menu.set()
    else:
        await db.update_status()
        courses_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
        courses_buttons.add("🏡 Bosh menyu")
        courses_buttons.add("✅ Hammasiga yuborish")
        data = await db.show_groups_name()
        for i in data:
            courses_buttons.add(f"❌ {i[0]}")

        await message.answer("Tanlang: ", reply_markup=courses_buttons)
        await state.set_state("second")


@dp.message_handler(state="second")
async def second_step(message: Message, state: FSMContext):
    real_ids = list()
    group_name = message.text
    if group_name == "🏡 Bosh menyu":
        await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
        await Main.main_menu.set()
    else:

        time_markup = ReplyKeyboardMarkup(resize_keyboard=True)
        time_markup.add("🔛 Bir martalik xabar yuborish")

        real_id = await db.show_groups_id()  # hamma guruhlar ID si keladi
        for j in real_id:
            real_ids.append(j[0])

        if group_name == "✅ Hammasiga yuborish":
            await message.answer("Tanlang: ⬇️", reply_markup=time_markup)
            await state.set_state('get_time')

        elif group_name == "Xabar yozish":
            await message.answer("Xabar kiriting: ⬇️", reply_markup=ReplyKeyboardRemove())
            await state.set_state("bigdata")
        else:
            group_name = group_name[2:]
            data = await db.show_both()
            groups_info = [{'group_name': row[0], 'group_id': row[1]} for row in data]
            for gr in groups_info:
                if gr['group_name'] == group_name:
                    await db.update_group_status(gr['group_id'])

            new_markup = ReplyKeyboardMarkup(resize_keyboard=True)
            new_groups = await db.show_bothStatus()
            if len(new_groups) == 0:
                await message.answer("Guruh qolmadi!")
                await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
                await Main.main_menu.set()
                return
            for j in new_groups:
                new_markup.add(f"❌ {j[0]}")

            new_markup.add("Xabar yozish")

            await message.answer("Tanlang: ", reply_markup=new_markup)


@dp.message_handler(content_types=['text'], state="bigdata")
async def sendBigData(message: Message):
    BigData = message.text
    sendings = await db.show_bothStatusID()
    for send in sendings:
        await bot.send_message(chat_id=send[0], text=BigData)
    await message.answer("✅ Xabar muvvafaqiyatli yuborildi!", reply_markup=main_menu)
    await Main.main_menu.set()


@dp.message_handler(content_types=['photo'], state="bigdata")
async def sendBigPhoto(message: Message, state: FSMContext):
    photo = message.photo[-1].file_id
    caption = message.caption

    back_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn.add("🔄 Yana xabar kiritish")
    back_btn.add("🏡 Bosh menyu")
    groups = await db.show_groups_id()
    for i in groups:
        await bot.send_photo(chat_id=i[0], photo=photo, caption=caption)

    await message.answer("✅ Xabar muvvafaqiyatli yuborildi!", reply_markup=back_btn)
    await state.set_state("again")


@dp.message_handler(state="get_time")
async def choose_time_type(message: Message, state: FSMContext):
    decision = message.text
    if decision == "🔛 Bir martalik xabar yuborish":
        await message.answer("Xabar kiriting: ⬇️", reply_markup=ReplyKeyboardRemove())
        await state.set_state("get_dec")
    else:
        pass



@dp.message_handler(content_types=['photo'], state='get_dec')
async def get_send(message: Message, state: FSMContext):
    photo = message.photo[-1].file_id
    caption = message.caption

    back_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn.add("🔄 Yana xabar kiritish")
    back_btn.add("🏡 Bosh menyu")
    groups = await db.show_groups_id()
    for i in groups:
        await bot.send_photo(chat_id=i[0], photo=photo, caption=caption)

    await message.answer("✅ Xabar muvvafaqiyatli yuborildi!", reply_markup=back_btn)
    await state.set_state("again")


@dp.message_handler(content_types=['text'], state='get_dec')
async def get_send(message: Message, state: FSMContext):
    text = message.text
    back_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn.add("🔄 Yana xabar kiritish")
    back_btn.add("🏡 Bosh menyu")
    groups = await db.show_groups_id()
    for i in groups:
        await bot.send_message(chat_id=i[0], text=text)

    await message.answer("✅ Xabar muvvafaqiyatli yuborildi!", reply_markup=back_btn)
    await state.set_state("again")


@dp.message_handler(state="again")
async def choose_again(message: Message, state: FSMContext):
    again_word = message.text
    if again_word == "🏡 Bosh menyu":
        await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
        await Main.main_menu.set()
    elif again_word == "🔄 Yana xabar kiritish":
        await message.answer("Xabar kiriting: ⬇️", reply_markup=ReplyKeyboardRemove())
        await state.set_state("get_dec")
    else:
        pass
