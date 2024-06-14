from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


admin = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='📢 Рассылка', callback_data='admin_send_message'),
                                     InlineKeyboardButton(text='📋 Пользователи', callback_data='admin_all_users_info')
                                 ],

                                 [
                                     InlineKeyboardButton(text='Статистика по квестам', callback_data='admin_quest'),
                                     InlineKeyboardButton(text='Промокоды', callback_data='admin_promocodes')
                                 ],
                                 [
                                     InlineKeyboardButton(text='Назад', callback_data='DeleteMessage')
                                 ]
])

add_promocode = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить промокоды', callback_data='admin_add_promocode')],
    [InlineKeyboardButton(text='⬅️ Назад', callback_data='admin_main_menu')]
])


back_to_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data='admin_main_menu')]
])


async def url_button(text, url):
    return InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f'{text}',
                                      url=f'{url}')
            ]
        ]
    )


async def check_podpiska(url):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Подписаться', url=url)],
        [InlineKeyboardButton(text="Я подписался", callback_data=f'SubCheck')]])