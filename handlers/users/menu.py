import asyncio
from data.config import pokemons
from loader import dp
from keyboards.default import keyboard_menu
from aiogram.types import CallbackQuery, InputFile, ReplyKeyboardRemove
from keyboards.inline import inline_kb_menu
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.db_api.db_asyncpg import *
from aiogram.utils.markdown import hlink
import random


@dp.message_handler(text=['Да!'])
async def are_you_ready_yes(message: types.Message):
    text = 'Супер, тогда начинаем!'
    await message.answer(text=text)
    await asyncio.sleep(1.5)
    await magic_forest(message=message)


@dp.message_handler(text=['Что-то мне страшно 👉👈'])
async def are_you_ready_no(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())
    text = 'Ты вспоминаешь Наруто, который учил никогда не сдаваться. ' \
           '+10 к воодушевлению, +15 к решительности идти вперёд ✨'
    photo = InputFile('files/naruto.jpg')
    markup = keyboard_menu.go_forward

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Идти вперёд!'])
async def magic_forest(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())
    text = 'Твой путь лежит через волшебный лес ✨\n\nДелая несколько шагов вперёд, ты замечаешь сияющие огоньки. ' \
           'Следуя за ними, ты выходишь к поляне, усыпанной разноцветными яйцами, ' \
           'в центре которых стоит древняя статуя 🗿'
    photo = InputFile('files/magic-forest.jpg')
    markup = keyboard_menu.further
    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Дальше', 'Выбрать другого покемона'])
async def further_menu(message: types.Message):
    await message.answer('Как только ты подходишь к статуе, раздаётся голос.')
    text = '🗿: «Вижу в тебе отвагу и доброе сердце. Победи жуткого монстра, что обитает в пещере и пугает ' \
           'всех жителей нашей деревни. Взамен ты получишь сокровища, почёт и респект бесконечный. ' \
           'Одному отправляться опасно. Открой свою душу, и найдёшь верного друга» '
    photo = InputFile('files/statue.jpg')
    markup = keyboard_menu.forward

    await asyncio.sleep(1.5)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Вперёд!'])
async def forward_menu(message: types.Message):
    text = 'Расскажи, куда бы ты отправился отдыхать?'
    markup = keyboard_menu.where_to_relax
    await message.answer(text=text, reply_markup=markup)


@dp.message_handler(text=['Море, потому что пляжные эпизоды самые весёлые', 'Горы и озера - вперёд к приключениям!', 'Город, где одни коты ^^'])
async def capybaras_menu(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())
    user_id = message.from_user.id
    option_number = 1
    if message.text == 'Море, потому что пляжные эпизоды самые весёлые':
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=1)
    elif message.text == 'Горы и озера - вперёд к приключениям!':
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=2)
    else:
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=3)

    text = 'Тебя превратили в капибару. Твои действия?'
    photo = InputFile('files/capybaras.jpg')
    markup = keyboard_menu.you_are_capybara

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Буду чиллить на воде и греться на солнышке', 'Подружусь со всеми животными', 'Конечно же буду постоянно что-то есть! (ом-ном-ном)'])
async def capybaras_action_menu(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())
    user_id = message.from_user.id
    option_number = 2
    if message.text == 'Буду чиллить на воде и греться на солнышке':
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=1)
    elif message.text == 'Подружусь со всеми животными':
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=2)
    else:
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=3)

    text = 'Твоя фраза по жизни'
    markup = keyboard_menu.your_qualities

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer(text=text, reply_markup=markup)


@dp.message_handler(text=['Отдадим наши сердца!', 'Лунная призма, дай мне сил', 'Это мой путь ниндзя'])
async def your_qualities_menu(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())
    user_id = message.from_user.id
    option_number = 3
    if message.text == 'Отдадим наши сердца!':
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=1)
    elif message.text == 'Лунная призма, дай мне сил':
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=2)
    else:
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=3)

    text = 'Насколько ты активный?'
    markup = keyboard_menu.you_are_active

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer(text=text, reply_markup=markup)


@dp.message_handler(text=['Владею особой техникой ниндзя: могу спать весь день или нестись вперёд как Наруто',
                          'Готов лежать в кроватке вечность', 'Делаю 100 дел в секунду'])
async def your_qualities_menu(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())
    user_id = message.from_user.id
    option_number = 4
    if message.text == 'Владею особой техникой ниндзя: могу спать весь день или нестись вперёд как Наруто':
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=1)
    elif message.text == 'Готов лежать в кроватке вечность':
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=2)
    else:
        await set_test1_results_by_option(user_id=user_id, option_number=option_number, option=3)

    results = await get_test1_results(user_id=user_id)
    if None in results:
        await forward_menu(message=message)
        return

    count_option_1 = results.count(1)
    count_option_2 = results.count(2)
    count_option_3 = results.count(3)

    if count_option_1 > count_option_2 and count_option_1 > count_option_3:
        pokemon_id = 1
    elif count_option_2 > count_option_1 and count_option_2 > count_option_3:
        pokemon_id = 2
    elif count_option_3 > count_option_1 and count_option_3 > count_option_2:
        pokemon_id = 3
    else:
        pokemon_id = 4
    await set_test1_pokemon_id(user_id=user_id, pokemon_id=pokemon_id)

    text1 = "Всё вокруг озаряется светом и перед тобой появляется волшебное яйцо ✨" \
            "\n«Тук-тук, кто там? Покемон выбрал тебя, осталось узнать, кто внутри»"
    photo1 = InputFile(f'files/pokemon-egg-{pokemon_id}.jpg')
    markup = keyboard_menu.knock_knock

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text1, photo=photo1, reply_markup=markup)


@dp.message_handler(text=['Тук-тук 👊'])
async def knock_knock_menu(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())
    user_id = message.from_user.id
    pokemon_id = await get_test1_pokemon_id(user_id=user_id)
    if not pokemon_id:
        await your_qualities_menu(message=message)
        return

    text = pokemons[pokemon_id][1]
    photo = InputFile(f'files/pokemon-{pokemon_id}.jpg')
    markup = keyboard_menu.hooray

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Ура!'])
async def hooray_menu(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())
    text = 'Теперь ты готов отправиться в приключение с новым другом!'
    photo = InputFile('files/cave.jpg')
    markup = keyboard_menu.go_to_cave

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Войти в пещеру 👣'])
async def dog_in_cave(message: types.Message):
    await message.answer(text='Нельзя просто так взять и войти в подземелье. '
                              'Сначала тебе придётся одолеть Огненную собаку, верно охраняющую вход 🔥')
    text = 'Как затушить собаку? 🤔'
    photo = InputFile('files/dog-in-cave.jpg')
    markup = keyboard_menu.put_out_dog
    await asyncio.sleep(1.5)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Убежать', 'Облить водой', 'Облить маслом'])
async def put_out_dog_menu(message: types.Message):
    if message.text == 'Убежать':
        text = 'Вечно убегать от проблем не получится. Сражайся, дружище!!!'
        markup = keyboard_menu.put_out_dog
        await message.answer(text=text, reply_markup=markup)

    elif message.text == 'Облить маслом':
        text = 'Собака разгорелась еще сильнее - все вокруг объято пламенем! Нужно ее потушить'
        markup = keyboard_menu.put_out_dog
        await message.answer(text=text, reply_markup=markup)

    else:
        msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

        text = 'Ура, у тебя получилось! Собака пропускает тебя в подземелье. ' \
               'Ты спускаешься глубже и вдалеке видишь имбового монстра. Он значительно выше тебя уровнем! ' \
               'Похоже это и есть тот самый босс, который угрожает всей деревне 😈'
        photo = InputFile('files/monster-in-cave.jpg')
        markup = keyboard_menu.look_around

        await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
        await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Оглядеться по сторонам'])
async def statue_in_cave(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    text = 'Рядом с собой ты замечаешь статую, похожую на ту, что была в лесу. Как только ты подходишь ближе, ' \
           'статуя оживает и говорит: «Чтобы вступить в бой, тебе нужно прокачать покемона. Покемоны связаны со ' \
           'своими владельцами, ты можешь дать ему знания. И он сможет победить с твоей силой отаку» '
    photo = InputFile('files/statue-in-cave.jpg')
    markup = keyboard_menu.pokemon_upgrade

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Прокачать покемона!', "Попробовать ещё", "Да, я попробую ещё раз", "Попробовать ещё раз"])
async def test2_question1(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    text = 'Какого из этих аниме нет в Студии Ghibli?'
    markup = keyboard_menu.test2_options_1
    photo = InputFile('files/question1.jpg')

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Унесённые ветром', 'Мой сосед Тоторо', 'Мальчик и птица'])
async def test2_question2(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    user_id = message.from_user.id
    option_number = 1
    if message.text == 'Унесённые ветром':
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=True)
    else:
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=False)

    text = 'Как звали главного героя в аниме «Клинок рассекающий демонов»?'
    markup = keyboard_menu.test2_options_2

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer(text=text, reply_markup=markup)


@dp.message_handler(text=['Танджиро', 'Гонпачиро', 'Монджиро'])
async def test2_question3(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    user_id = message.from_user.id
    option_number = 2
    if message.text == 'Танджиро':
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=True)
    else:
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=False)

    text = 'Какой из хвостатых демонов был запечатан в Наруто?'
    markup = keyboard_menu.test2_options_3

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer(text=text, reply_markup=markup)


@dp.message_handler(text=['Курама', 'Шукаку', 'Мататаби'])
async def test2_question4(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    user_id = message.from_user.id
    option_number = 3
    if message.text == 'Курама':
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=True)
    else:
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=False)

    text = 'Из какой манги этот кадр?'
    photo = InputFile('files/question4.png')
    markup = keyboard_menu.test2_options_4

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=['Шаман Кинг', 'Магическая битва', 'Человек-бензопила'])
async def test2_question4(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    user_id = message.from_user.id
    option_number = 4
    if message.text == 'Человек-бензопила':
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=True)
    else:
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=False)

    text = 'Чтобы победить чудовище, нужно отбросить человечность. Кто это сказал?'
    markup = keyboard_menu.test2_options_5

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer(text=text, reply_markup=markup)


@dp.message_handler(text=['Армин', 'Энни', 'Эрвин'])
async def test2_question5(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    user_id = message.from_user.id
    option_number = 5
    if message.text == 'Армин':
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=True)
    else:
        await set_test2_results_by_option(user_id=user_id, option_number=option_number, option=False)

    results = await get_test2_results(user_id=user_id)
    if None in results:
        await test2_question1(message=message)
        return

    true_count = results.count(True)
    probability = 100 if true_count >= 4 else 50 if true_count > 1 else 30
    text = f'Путник, сейчас ты ответил верно на {true_count} из 5 вопросов, ' \
           f'с вероятностью {probability}% можешь победить Босса.'
    await set_test2_probability(user_id=user_id, probability=probability)
    await message.answer(text=text)

    if true_count > 3:
        text2 = 'Молодец! Ты готов к бою, приступай'
        markup = keyboard_menu.go_to_fight
    else:
        text2 = 'Попробуешь ещё раз пройти или вступишь в бой?'
        markup = keyboard_menu.go_to_fight_again

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer(text=text2, reply_markup=markup)


@dp.message_handler(text=["Вступить в бой"])
async def go_to_fight_menu(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    user_id = message.from_user.id
    pokemon_id = await get_test1_pokemon_id(user_id=user_id)
    if not pokemon_id:
        await your_qualities_menu(message=message)
        return

    text = f'{pokemons[pokemon_id][0]} против босса! Кто победит? Осталось нанести решающий удар!'
    photo = InputFile(f'files/boss-vs-pokemon-{pokemon_id}.jpg')
    markup = keyboard_menu.decisive_blow

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)


@dp.message_handler(text=["Решающий удар"])
async def decisive_blow_menu(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    user_id = message.from_user.id
    probability = await get_test2_probability(user_id=user_id)
    promocode_probability = 10
    if not probability:
        await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
        await test2_question5(message=message)
        return
    percents = list(range(1, 101))
    random.shuffle(percents)
    chance_to_win = percents[0]

    if chance_to_win <= probability:
        promocode_probability = 20
        pokemon_id = await get_test1_pokemon_id(user_id=user_id)
        if not pokemon_id:
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
            await your_qualities_menu(message=message)
            return

        text = 'Поздравляю, тебе удалось победить монстра и спасти деревню! Теперь тебя ждёт награда 🎉'
        photo = InputFile(f'files/winner-pokemon-{pokemon_id}.jpg')
        markup = keyboard_menu.my_promocode

    else:
        if await get_count_passed_by_user(user_id=user_id, probability=20) > 0:
            text = 'В этот раз тебе не удалось победить босса. Ты можешь попробовать ещё раз.'
        else:
            text = 'В этот раз тебе не удалось победить монстра, однако ты его ослабил и теперь жители ' \
                   'деревни смогут с ним справиться. Ты можешь попробовать ещё раз одолеть его или забрать ' \
                   'утешительный приз – скидку 10% в магазине ORAORA и анимешный стикерпак 🎁'
        photo = InputFile(f'files/monster-win.jpg')
        markup = keyboard_menu.monster_win

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    await message.answer_photo(caption=text, photo=photo, reply_markup=markup)

    await add_to_test_is_passed(user_id=user_id, probability=promocode_probability)
    if await get_user_promocode_probability(user_id=user_id) < promocode_probability:
        promocode_id = await get_free_promocode_by_probability(probability=promocode_probability)
        if promocode_id:
            await set_user_promocode(user_id=user_id, promocode=promocode_id)
        else:
            await message.answer('В данный момент прмокоды закончились, пожалуйста, попробуйте позже!')


@dp.message_handler(text=["Забрать утешительный приз", "Получить промокод"])
async def my_promocode_menu(message: types.Message):
    msg = await message.answer('Ответ получен..', reply_markup=ReplyKeyboardRemove())

    user_id = message.from_user.id
    mouth = 'апреля'

    promocode = await get_user_promocode(user_id=user_id)
    if promocode:
        sticker_id = ''
        sticker_url = ''
        sticker_markup = await inline_kb_menu.url_button(text='Получить стикеры', url=sticker_url)

        await dp.bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
        await message.answer_sticker(sticker=sticker_id)

        promocode_info = await promo_info_by_id(id=promocode)

        if promocode_info["probability"] == 10:
            sticker_text = f'Твоя награда – <b>скидка 10%</b>  в магазине ORAORA по промокоду ' \
                           f'<code>{promocode_info["promocode"]}</code> и {hlink("анимешный стикерпак  🎁", sticker_url)}'
            await asyncio.sleep(1)
            await message.answer(text=sticker_text, reply_markup=sticker_markup)
            await asyncio.sleep(1.5)
            await message.answer(text=f'Промокод можно применить до конца {mouth} в офлайн-магазине ORAORA. '
                                      f'Покажи этот промокод продавцу, и получишь <b>скидку 10%</b> на любые товары! 🎉')

        elif promocode_info["probability"] == 20:
            if await get_count_passed_by_user(user_id=user_id, probability=20) == 1 \
                    and await get_count_passed_by_user(user_id=user_id, probability=10) > 0 \
                    and message.text == 'Получить промокод':
                sticker_text = f'В этот раз у тебя получилось победить монстра! ' \
                               f'В награду мы дарим тебе <b>скидку 20%</b> в магазине ORAORA по промокоду ' \
                               f'<code>{promocode_info["promocode"]}</code> ' \
                               f'и {hlink("анимешный стикерпак  🎁", sticker_url)}'
            elif await get_count_passed_by_user(user_id=user_id, probability=20) == 1 \
                    and await get_count_passed_by_user(user_id=user_id, probability=10) == 0:
                sticker_text = f'🗿: Ты настоящий отаку! В награду мы дарим тебе скидку 20% в магазине ORAORA ' \
                               f'по промокоду <code>{promocode_info["promocode"]}</code> ' \
                               f'и {hlink("анимешный стикерпак  🎁", sticker_url)}'
            else:
                sticker_text = f'У тебя уже есть награда: скидка 20% в магазине ORAORA по промокоду ' \
                               f'<code>{promocode_info["promocode"]}</code> ' \
                               f'и {hlink("анимешный стикерпак  🎁", sticker_url)}'
            await asyncio.sleep(1)
            await message.answer(text=sticker_text, reply_markup=sticker_markup)
            await asyncio.sleep(1.5)
            await message.answer(text=f'Промокод можно применить до конца {mouth} в офлайн-магазине ORAORA. '
                                      f'Покажи этот промокод продавцу, и получишь <b>скидку 20%</b> на любые товары! 🎉')

        await asyncio.sleep(1.5)
        await message.answer(text=f'Адрес магазина: г. Москва, ТЦ Avenue SouthWest, проспект Вернадского, 86а. '
                                  f'(метро "Юго-Западная"). Время работы: каждый день с 10 до 22 часов.'
                                  f'\n\nАссортимент товаров можно посмотреть на сайте '
                                  f'{hlink("https://www.oraorashop.ru", "https://www.oraorashop.ru/?utm_source=tg&utm_medium=smm&utm_campaign=tg_oraora_quest")}',
                             reply_markup=keyboard_menu.get_out)

    else:
        await decisive_blow_menu(message=message)


@dp.message_handler(text=["Выйти из подземелья"])
async def get_out_menu(message: types.Message):
    await message.answer('Будем рады видеть тебя снова!', reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def randomMessage(message: types.Message):
    await message.answer('🫤')
