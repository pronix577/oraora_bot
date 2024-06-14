from aiogram import types
from loader import dp
from filters import IsAdmin
from keyboards.default import keyboard_menu
from keyboards.inline import inline_kb_menu
from utils.db_api.db_asyncpg import *
from aiogram.types import InputFile
from aiogram.utils.markdown import hlink
from handlers.users.inline_menu import try_delete_call
from data.config import CHANNEL_ID, channel_url
from aiogram.types import CallbackQuery, InputFile, ReplyKeyboardRemove


@dp.message_handler(text=['Начать', "Ещё раз пройти тест"])
async def start_first_test(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())
    text = 'Привет, искатель приключений! Если ты оказался здесь, то наверняка слышал о ценных сокровищах, ' \
           'что прячутся в подземельях. Чтобы получить их, тебе предстоит отправиться в путешествие! ' \
           '\n\nГотов начать квест? 😎'
    photo = InputFile('files/closed-door.jpg')
    markup = keyboard_menu.are_you_ready
    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


async def check_subscription_status(user_id):
    try:
        return (await dp.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)).status
    except:
        return "left"


@dp.callback_query_handler(text='SubCheck')
async def SubCheck(call: types.CallbackQuery):
    if await check_subscription_status(user_id=call.from_user.id) == "left":
        await call.answer('Всё ещё не подписан! :)')
        return
    await try_delete_call(call)
    await send_start_message(chat_id=call.message.chat.id)


@dp.message_handler(commands='start')
async def start_menu(message: types.Message):

    if not await user_exists(user_id=message.from_user.id):
        user_id = message.from_user.id
        await add_user(user_id=user_id, fio=message.from_user.full_name)
        await add_user_in_test1(user_id=user_id)
        await add_user_in_test2(user_id=user_id)

    result = await check_subscription_status(message.from_user.id)
    if result == 'left':
        text = f'Чтобы начать квест, нажми на кнопку и подпишись на {hlink("телеграм-канал ORAORA.", channel_url)}'
        markup = await inline_kb_menu.check_podpiska(url=channel_url)
        await message.answer(text=text, reply_markup=markup)
        return

    await send_start_message(chat_id=message.chat.id)


async def send_start_message(chat_id):
    """text = '<b>Охаё! Пройди квест от аниме-магазина ORAORA и выиграй скидку до 20% и другие подарки!🎁</b>' \
           '\nВ нашем магазине есть фигурки, манга и мерч по твоим любимым аниме. ' \
           'Если ты сейчас в Москве, обязательно заходи к нам в гости в ТЦ Avenue на 4 этаже.'
    photo = InputFile('files/main.jpg')
    markup = keyboard_menu.start"""
    text = 'Привет, искатель приключений! Если ты оказался здесь, то наверняка слышал о ценных сокровищах, ' \
           'что прячутся в подземельях. Чтобы получить их, тебе предстоит отправиться в путешествие! ' \
           '\n\nГотов начать квест? 😎'
    photo = InputFile('files/closed-door.jpg')
    markup = keyboard_menu.are_you_ready

    await dp.bot.send_photo(chat_id=chat_id, caption=text, photo=photo, reply_markup=markup)
