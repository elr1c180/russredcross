from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton

from aiogram.types import FSInputFile

from aiogram.types import *

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram.utils.keyboard import InlineKeyboardBuilder

import texts

from img import generate


class Form(StatesGroup):
    name = State()
    national_collect = State()
    final = State()

from keyboards.gift import get_gift
from keyboards.collect import get_collect
router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Это бот Российского Красного Креста. Мы хотим поздравить всех с Днем мецената и благотворителя в России. Нам очень важен вклад каждого: словом, делом, лайком, репостом, переводом. Ваша поддержка помогает\nлюдям в трудной ситуации почувствовать заботу и легче пережить невзгоды.\n\nВы дарите шанс на лучшую жизнь миллионам людей. Мы, в свою очередь, хотим сделать вам небольшой виртуальный подарок.",
        reply_markup=get_gift()
    )


@router.message(F.text == 'Получить подарок')
async def gift(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        'Уже упаковываем! Напишите, пожалуйста, свое имя.',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Form.national_collect)

@router.message(Form.national_collect)
async def national_collect(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer(
        "Спасибо! А сейчас выберете наш национальный сбор, в котором вы участвовали. Мы хотим поделиться с вами важной информацией.",
        reply_markup=get_collect()
    )
    await state.set_state(Form.final)

@router.message(Form.final)
async def card(message: Message, state:  FSMContext):
    await state.update_data(national_collect=message.text)
    name = await state.get_data()
    name = name['name']
    national_collect_data = await state.get_data()
    national_collect_data = national_collect_data['national_collect']
    print(national_collect_data)
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="Оформить подписку на пожертвования", url="https://donation.redcross.ru/")
    )
    builder.row(InlineKeyboardButton(
        text='Узнать больше о нашей деятельности', url="https://www.redcross.ru/"
    ))

    if national_collect_data == 'Поддержка пострадавших от украинского кризиса':

        await message.answer_photo(
        FSInputFile(generate(name, 'ua')),
    )
    
    if national_collect_data == 'Стрельба в Гимназии № 175 в Казани': 
        await message.answer_photo(
        FSInputFile(generate(name, 'kazan')),
    )
    
    if national_collect_data == 'Стрельба в Школе № 88 в Ижевске':
        await message.answer_photo(
        FSInputFile(generate(name, 'izevsk')),
    )

    elif national_collect_data == 'Помощь пострадавшим от обстрелов в приграничных регионах':
        await message.answer_photo(
        FSInputFile(generate(name, 'fire')),
    )
        
    elif national_collect_data == 'Теракт в «Крокус Сити Холл»':
        await message.answer_photo(
        FSInputFile(generate(name, 'crocus')),
    )

    elif national_collect_data == 'Взрыв на шахте «Листвяжная»':
        await message.answer_photo(
        FSInputFile(generate(name, 'listv')),
    )
    
    elif national_collect_data == 'Наводнение в Приморье':
        await message.answer_photo(
        FSInputFile(generate(name, 'primor')),
    )

    with open("users.txt", "a") as file:
        file.write(f"\n@{message.from_user.username} - {name} - {national_collect_data}\n")

    await message.answer(
        f'{name}, спасибо вам за ваше участие в деятельности Российского Красного Креста! Эта виртуальная открытка — наш скромный жест благодарности ❤️\n\nДелитесь ею в своих социальных сетях, чтобы каждый знал — любой вклад имеет большое значение, ведь за этими числами стоят реальные люди, которым помогли <b>именно вы.</b>',
        reply_markup=builder.as_markup(),
        parse_mode='html'
    )
    print(await state.get_data())
    await state.clear()