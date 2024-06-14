from loader import dp
from utils.db_api.db_asyncpg import *
from aiogram.types import CallbackQuery
from keyboards.inline import inline_kb_menu
from aiogram.utils.markdown import hlink
from aiogram import types


@dp.callback_query_handler(text='DeleteMessage')
async def DeleteMessage(call: types.CallbackQuery):
    await try_delete_call(call)


async def delete_messages(messages, chat_id):
    for msg_id in messages:
        try:
            await dp.bot.delete_message(chat_id=chat_id, message_id=msg_id)
        except:
            pass


async def try_delete_call(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass


async def try_delete_msg(chatId, msgId):
    try:
        await dp.bot.delete_message(chat_id=chatId, message_id=msgId)
    except:
        pass


async def try_edit_call(callback, text, markup):
    try:
        msg = await callback.message.edit_text(text=text, parse_mode='HTML', reply_markup=markup)
    except:
        await try_delete_call(callback)
        msg = await callback.message.answer(text=text, parse_mode='HTML', reply_markup=markup)
    return msg
