from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


agreement = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Да')],
                                          [KeyboardButton(text='Нет')]],
                                resize_keyboard=True)

probability = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='10'), KeyboardButton('20')],
                                            [KeyboardButton(text='отмена')]],
                                  resize_keyboard=True)

add_promocode = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Готово'),
        ],
        [
            KeyboardButton(text='отмена'),
        ]
    ],
    resize_keyboard=True
)


cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='отмена'),
        ]
    ],
    resize_keyboard=True
)


start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Начать'),
        ]
    ],
    resize_keyboard=True
)


are_you_ready = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да!'),
        ],
        [
            KeyboardButton(text='Что-то мне страшно 👉👈'),
        ]
    ],
    resize_keyboard=True
)

go_forward = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Идти вперёд!'),
        ],
    ],
    resize_keyboard=True
)


further = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Дальше'),
        ],
    ],
    resize_keyboard=True
)


forward = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вперёд!'),
        ],
    ],
    resize_keyboard=True
)


where_to_relax = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Море, потому что пляжные эпизоды самые весёлые'),
        ],
        [
            KeyboardButton(text='Горы и озера - вперёд к приключениям!'),
        ],
        [
            KeyboardButton(text='Город, где одни коты ^^'),
        ]
    ],
    resize_keyboard=True
)

you_are_capybara = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Буду чиллить на воде и греться на солнышке'),
        ],
        [
            KeyboardButton(text='Подружусь со всеми животными'),
        ],
        [
            KeyboardButton(text='Конечно же буду постоянно что-то есть! (ом-ном-ном)'),
        ]
    ],
    resize_keyboard=True
)


your_qualities = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отдадим наши сердца!'),
        ],
        [
            KeyboardButton(text='Лунная призма, дай мне сил'),
        ],
        [
            KeyboardButton(text='Это мой путь ниндзя'),
        ]
    ],
    resize_keyboard=True
)

you_are_active = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Владею особой техникой ниндзя: могу спать весь день или нестись вперёд как Наруто'),
        ],
        [
            KeyboardButton(text='Готов лежать в кроватке вечность'),
        ],
        [
            KeyboardButton(text='Делаю 100 дел в секунду'),
        ]
    ],
    resize_keyboard=True
)

knock_knock = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Тук-тук 👊'),
        ],
    ],
    resize_keyboard=True
)

hooray = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ура!'),
        ],
    ],
    resize_keyboard=True
)

go_to_cave = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Войти в пещеру 👣'),
        ],
    ],
    resize_keyboard=True
)


put_out_dog = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Убежать'),
        ],
        [
            KeyboardButton(text='Облить водой'),
        ],
        [
            KeyboardButton(text='Облить маслом'),
        ]
    ],
    resize_keyboard=True
)

look_around = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Оглядеться по сторонам'),
        ],
    ],
    resize_keyboard=True
)

pokemon_upgrade = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Прокачать покемона!'),
        ],
    ],
    resize_keyboard=True
)


test2_options_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мальчик и птица'),
        ],
        [
            KeyboardButton(text='Унесённые ветром'),
        ],
        [
            KeyboardButton(text='Мой сосед Тоторо'),
        ]
    ],
    resize_keyboard=True
)

test2_options_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Танджиро'),
        ],
        [
            KeyboardButton(text='Гонпачиро'),
        ],
        [
            KeyboardButton(text='Монджиро'),
        ]
    ],
    resize_keyboard=True
)

test2_options_3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мататаби'),
        ],
        [
            KeyboardButton(text='Курама'),
        ],
        [
            KeyboardButton(text='Шукаку'),
        ]
    ],
    resize_keyboard=True
)

test2_options_4 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Шаман Кинг'),
        ],
        [
            KeyboardButton(text='Магическая битва'),
        ],
        [
            KeyboardButton(text='Человек-бензопила'),
        ]
    ],
    resize_keyboard=True
)

test2_options_5 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Армин'),
        ],
        [
            KeyboardButton(text='Энни'),
        ],
        [
            KeyboardButton(text='Эрвин'),
        ]
    ],
    resize_keyboard=True
)


go_to_fight = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вступить в бой'),
        ],
    ],
    resize_keyboard=True
)

go_to_fight_again = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Попробовать ещё'),
        ],
        [
            KeyboardButton(text='Вступить в бой'),
        ],
    ],
    resize_keyboard=True
)

go_to_fight_again_lose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Попробовать ещё'),
        ],
    ],
    resize_keyboard=True
)


decisive_blow = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Решающий удар'),
        ],
    ],
    resize_keyboard=True
)

my_promocode = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Получить промокод'),
        ],
    ],
    resize_keyboard=True
)


monster_win = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Попробовать ещё раз'),
        ],
        [
            KeyboardButton(text='Забрать утешительный приз'),
        ],
    ],
    resize_keyboard=True
)


get_out = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выйти из подземелья'),
        ],
        [
            KeyboardButton(text='Ещё раз пройти тест'),
        ]
    ],
    resize_keyboard=True
)
