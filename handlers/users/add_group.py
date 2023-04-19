import json
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.main_menu import main_menu
from loader import db, dp, bot
from aiogram.types import Message, ChatType
from states.main_state import Main
from aiogram.dispatcher import FSMContext
from aiogram.utils import exceptions
from keyboards.default.main_menu import back


@dp.message_handler(text="➕ Guruh", state=Main.main_menu)
async def get_gr_name(message: Message):
    text = """
Guruh qo'shish uchun botni qo'shmoqchi 
bo'lgan guruhingizga "admin" qilasiz,
va guruh ichidagi ma'lum bir to'pikka kirib
/add komandasini kiritasiz, agar bot <b>hech narsa
javob bermasa</b>, tabriklaymiz, guruh
muvaffaqiyatli qo'shildi.

<b>Aks xolda,</b> bot <i>"Sizga ta'qiqlangan"</i>
degan xabar yuboradi


    """
    await message.answer(text)
    await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
    await Main.main_menu.set()


@dp.message_handler(state="getid")
async def finish_get(message: Message, state: FSMContext):
    # guruh qo'shishdan oldin, albatta botni guruhga admin qilish kerak
    group_id = message.text
    if group_id == "🏡 Bosh menyu":
        await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
        await Main.main_menu.set()
    else:
        is_in_db = await db.check_id(group_id)
        if is_in_db:
            await message.answer("Bu ID bazada mavjud!")
            return
        else:
            try:
                chat = await bot.get_chat(group_id)
                group_name = chat['title']

                group_id = int(group_id)
                await db.add_group(group_name, group_id)
                await message.answer("✅ Guruh muvaffaqiyatli bazaga qo'shildi!")
                await message.answer("🏡 Bosh menyu", reply_markup=main_menu)
                await Main.main_menu.set()


            except exceptions.ChatNotFound:
                await message.answer(
                    "INVALID ID!\nTRY AGAIN\n\nSabablar: \n1) BOT siz yaratmoqchi bo'lgan guruhda admin emas\n2) Bunday guruh mavjud emas! ")
