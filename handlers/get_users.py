from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import pandas as pd

from aiogram.types import *
router = Router()
@router.message(Command("get_users"))  # [2]
async def cmd_start(message: Message):
    await message.answer_document(
        document=FSInputFile('users.txt'),
        caption='Список пользователей'
    )