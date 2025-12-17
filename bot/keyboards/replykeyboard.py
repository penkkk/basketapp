from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import KeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📋 Состав команды")],
    [KeyboardButton(text="🏀 Расписание")],
    [KeyboardButton(text="📊 Статистика")],
    [KeyboardButton(text="🔔 Уведомления")]
],                                          resize_keyboard=True,
                                            input_field_placeholder="Выберите пункт из меню.")

