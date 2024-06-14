from aiogram import types
from aiogram.types import InputFile
from loader import dp
from keyboards.default import keyboard_menu
from keyboards.inline import inline_kb_menu
from filters import IsAdmin
from states.state import AdminSpam, AdminAddPromo
from handlers.users.inline_menu import delete_messages, try_delete_call, try_edit_call
from aiogram.dispatcher import FSMContext
import pandas as pd
import io
from utils.db_api.db_asyncpg import *


@dp.message_handler(IsAdmin(), text='/admin')
async def adminPanel(messsage: types.Message):
    await messsage.answer(f'Здравствуйте, {messsage.from_user.full_name},  вы попали в админ панель!',
                          reply_markup=inline_kb_menu.admin)


@dp.callback_query_handler(IsAdmin(), text='admin_main_menu')
async def manager_call_menu(call: types.CallbackQuery):
    msg_text = f'Здравствуйте, {call.from_user.full_name}, вы попали в меню менеджера!'
    markup = inline_kb_menu.admin

    await try_edit_call(callback=call, text=msg_text, markup=markup)


@dp.callback_query_handler(IsAdmin(), text='admin_send_message')
async def admin_send_message(call: types.CallbackQuery):
    msg = await try_edit_call(callback=call, markup=keyboard_menu.cancel,
                              text=f'Введите сообщения для рассылки всем пользователям')
    await AdminSpam.msg_list.set()
    state = dp.get_current().current_state()
    async with state.proxy() as data:
        data["msg_list"] = [msg.message_id]
        data["callback"] = call

    await AdminSpam.text.set()


@dp.message_handler(state=AdminSpam.text, content_types=types.ContentType.ANY)
async def AdminSpam_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["msg_list"].append(message.message_id)
        if message.text:
            if message.text.lower() == 'отмена':
                msg = await message.answer('Рассылка отменена!', reply_markup=None)
                data["msg_list"].append(msg.message_id)
                await manager_call_menu(call=data["callback"])
                await state.finish()
                await delete_messages(messages=data["msg_list"], chat_id=message.chat.id)

            else:
                data["text"] = message.html_text
                msg = await message.answer(text=data["text"])
                msg2 = await message.answer("Всё верно?", reply_markup=keyboard_menu.agreement)   # Для удаления клавы
                data["msg_list"].append(msg.message_id)
                data["msg_list"].append(msg2.message_id)
                await AdminSpam.confirm.set()
        elif message.video:
            data["text"] = message.html_text
            data["video"] = message.video.file_id
            msg = await message.answer_video(caption=data["text"], video=data["video"])
            msg2 = await message.answer("Всё верно?", reply_markup=keyboard_menu.agreement)  # Для удаления клавы
            data["msg_list"].append(msg.message_id)
            data["msg_list"].append(msg2.message_id)
            await AdminSpam.confirm.set()

        elif message.photo:
            data["text"] = message.html_text
            data["photo"] = message.photo[0].file_id
            msg = await message.answer_photo(caption=data["text"], photo=data["photo"])
            msg2 = await message.answer("Всё верно?", reply_markup=keyboard_menu.agreement)  # Для удаления клавы
            data["msg_list"].append(msg.message_id)
            data["msg_list"].append(msg2.message_id)
            await AdminSpam.confirm.set()

        else:
            await message.answer('Пока что я не поддерживаю такое сообщение для рассылки.')


@dp.callback_query_handler(IsAdmin(), text='admin_all_users_info')
async def admin_all_users_info(call: types.CallbackQuery):
    await try_delete_call(call=call)
    msg = await call.message.answer('Подождите, файл формируется...')

    users = await get_all_users_data()
    df = pd.DataFrame(users, columns=['№', "Telegram id", "ФИО", "Промокод"])

    excel_file_stream = io.BytesIO()
    with pd.ExcelWriter(excel_file_stream, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Users Info')
        workbook = writer.book
        worksheet = writer.sheets['Users Info']

        for idx, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).str.len().max(), len(col)) + 2
            worksheet.set_column(idx, idx, max_len)
    excel_file_stream.seek(0)

    await call.message.answer_document(document=InputFile(excel_file_stream, filename='Список пользователей.xlsx'),
                                       reply_markup=inline_kb_menu.back_to_admin)
    await dp.bot.delete_message(chat_id=call.message.chat.id, message_id=msg.message_id)


@dp.callback_query_handler(IsAdmin(), text='admin_promocodes')
async def admin_promocodes_menu(call: types.CallbackQuery):
    all_promo = await all_promocodes()
    free_promo = await all_free_promocodes()
    free_10_promo = []
    free_20_promo = []

    for free in free_promo:
        if free["probability"] == 10:
            free_10_promo.append(free)
        if free["probability"] == 20:
            free_20_promo.append(free)

    msg_text = f'📊 Промокоды:' \
               f'\n{" "*5}Свободно  <code>{len(free_promo)}/{len(all_promo)}</code> шт.' \
               f'\n{" "*10}Из них на 20% - <code>{len(free_20_promo)}</code> шт.' \
               f'\n{" "*10}Из них на 10% - <code>{len(free_10_promo)}</code> шт.'
    markup = inline_kb_menu.add_promocode

    await try_edit_call(callback=call, text=msg_text, markup=markup)


@dp.callback_query_handler(IsAdmin(), text='admin_add_promocode')
async def admin_add_promocode(call: types.CallbackQuery):
    msg = await try_edit_call(callback=call, markup=keyboard_menu.probability,
                              text=f'Выберите номинал промокодов')
    await AdminAddPromo.msg_list.set()
    state = dp.get_current().current_state()
    async with state.proxy() as data:
        data["msg_list"] = [msg.message_id]
        data["callback"] = call

    await AdminAddPromo.probability.set()


@dp.message_handler(state=AdminAddPromo.probability)
async def AdminAddPromo_probability(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["msg_list"].append(message.message_id)
        await delete_messages(messages=data["msg_list"], chat_id=message.chat.id)

        if message.text == '20':
            data["probability"] = 20

        elif message.text == '10':
            data["probability"] = 10

        else:
            await admin_promocodes_menu(call=data["callback"])
            await state.finish()
            return

        data["promocodes"] = []

        msg = await message.answer('Отправьте промокоды, в конце нажмите кнопку «Готово»',
                                   reply_markup=keyboard_menu.add_promocode)
        data["msg_list"].append(msg.message_id)
        await AdminAddPromo.promocodes.set()


@dp.message_handler(state=AdminAddPromo.promocodes)
async def AdminAddPromo_promocodes(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["msg_list"].append(message.message_id)
        await delete_messages(messages=data["msg_list"], chat_id=message.chat.id)

        if message.text.lower() not in ['отмена', 'готово']:
            msg = await message.answer('Идёт обработка полученных данных...')
            new_promocodes = []
            for promo in message.text.split():
                if not await promo_by_title_in_bd(promocode=promo):
                    new_promocodes.append(promo)
                    data["promocodes"].append(promo)
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
            msg2 = await message.answer(f'Принято {len(new_promocodes)} новых промокодов')
            msg3 = await message.answer('Отправьте промокоды, в конце нажмите кнопку «Готово»',
                                        reply_markup=keyboard_menu.add_promocode)
            data["msg_list"].append(msg2.message_id)
            data['msg_list'].append(msg3.message_id)
            return

        if message.text.lower() == 'готово':
            new_promo = 0
            for promo in data["promocodes"]:
                try:
                    await add_promocode(promocode=promo, probability=data["probability"])
                    new_promo += 1
                except:
                    pass
            await message.answer(f'Добавлено {new_promo} новых промокодов!')

        await admin_promocodes_menu(call=data["callback"])
        await state.finish()


@dp.callback_query_handler(IsAdmin(), text='admin_quest')
async def admin_quest_menu(call: types.CallbackQuery):
    all_rows = await get_all_passed()
    win_rows = []
    lose_rows = []
    unique_rows = set()

    for row in all_rows:
        if row["probability"] == 10:
            lose_rows.append(row)
        if row["probability"] == 20:
            win_rows.append(row)
        unique_rows.add(row["user_id"])

    msg_text = f'📊 Статистика' \
               f'\n\n{" "*5}Всего битв с боссом: <code>{len(all_rows)}</code>' \
               f'\n{" "*10}Из них побед: <code>{len(win_rows)}</code>' \
               f'\n{" "*10}Из них поражений: <code>{len(lose_rows)}</code>' \
               f'\n\n{" "*5}Уникальных сражений: <code>{len(unique_rows)}</code>'
    markup = inline_kb_menu.back_to_admin

    await try_edit_call(callback=call, text=msg_text, markup=markup)