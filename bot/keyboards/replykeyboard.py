from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import KeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📋 Состав команды")],
    [KeyboardButton(text="🏀 Расписание")],
    [KeyboardButton(text="📊 Статистика")],
    [KeyboardButton(text="🔔 Уведомления")]
],                                          resize_keyboard=True,
                                            input_field_placeholder="Выберите пункт из меню.")

stat = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📈 Статистика команды")],
    [KeyboardButton(text="📈 Cтатистика игрока")],
    [KeyboardButton(text="↩️ Назад")]
],                                          resize_keyboard=True,
                                            input_field_placeholder="Выберите чью статистику вы хотите посмотреть")
