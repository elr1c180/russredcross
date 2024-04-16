from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_collect() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Поддержка пострадавших от украинского кризиса")
    kb.button(text="Помощь пострадавшим от обстрелов в приграничных регионах")
    kb.button(text="Теракт в «Крокус Сити Холл»")
    kb.button(text="Взрыв на шахте «Листвяжная»")
    kb.button(text="Наводнение в Приморье")
    kb.button(text="Стрельба в Гимназии № 175 в Казани")
    kb.button(text="Стрельба в Школе № 88 в Ижевске")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)