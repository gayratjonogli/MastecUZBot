from loader import dp, db, bot
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from states.main_state import Main
from keyboards.default.main_menu import main_menu

buttons_list = list()


@dp.message_handler(text="❌ Guruh", state=Main.main_menu)
async def delete_group(message: Message, state: FSMContext):
    groups_list = await db.show_all()
    if len(groups_list) == 0:
        await message.answer("Hozircha hech qanday guruh mavjud emas...")
        await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
        await Main.main_menu.set()
    else:
        groups_mrkp = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
        groups_mrkp.add("🏡 Bosh menyu")
        groups = await db.show_groups_name()
        for i in groups:
            groups_mrkp.add(f"❌ {i[0]}")
            buttons_list.append(f"❌ {i[0]}")

        buttons_list.append("🏡 Bosh menyu")
        await message.answer("O'chirmoqchi bo'lgan guruhgizni tanlang! ⬇️", reply_markup=groups_mrkp)
        await state.set_state("delete_gr")


@dp.message_handler(text=buttons_list, state="delete_gr")
async def letsDelete(message: Message, state: FSMContext):
    groups_mrkps = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    groups_mrkps.add("🏡 Bosh menyu")
    course = message.text
    if course == "🏡 Bosh menyu":
        await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
        await Main.main_menu.set()
    else:
        course = course[2:]
        await db.delete_group_by_name(course)
        groups = await db.show_groups_name()
        for i in groups:
            groups_mrkps.add(f"❌ {i[0]}")
            buttons_list.append(f"❌ {i[0]}")
        await message.answer("✅ Guruh muvaffaqiyatli o'chirildi", reply_markup=groups_mrkps)
        await state.set_state("delete_gr")
