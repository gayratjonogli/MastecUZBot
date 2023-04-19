from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗣 E'lon berish")
        ],
        [
            KeyboardButton(text="➕ Guruh"),
            KeyboardButton(text="❌ Guruh")
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏡 Bosh menyu")
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)
