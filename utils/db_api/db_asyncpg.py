from loader import dp


async def get_all_users_data():
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            query = '''
                        SELECT
                            ROW_NUMBER() OVER (ORDER BY u.user_id) AS row_number,
                            u.user_id,
                            u.fio,
                            CASE
                                WHEN u.promocode_id IS NOT NULL THEN p.promocode
                                ELSE 'Промокод не получен'
                            END AS status
                        FROM
                            users u
                        LEFT JOIN
                            promocodes p ON u.promocode_id = p.id;
            '''
            return await connection.fetch(query)


async def admin_list():
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            return await connection.fetch('SELECT "user_id" FROM "users" WHERE "isadmin"=True')


async def user_exists(user_id: int):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            result = await connection.fetchrow('SELECT * FROM "users" WHERE "user_id"=$1', user_id)
            return result is not None


async def add_user(user_id: int, fio: str):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            await connection.execute('INSERT INTO "users" ("user_id", "fio", "isadmin") VALUES ($1, $2, $3)',
                                     user_id, fio, False)


async def add_user_in_test1(user_id: int):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            await connection.execute('INSERT INTO "test1_results" ("user_id") VALUES ($1)', user_id)


async def add_user_in_test2(user_id: int):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            await connection.execute('INSERT INTO "test2_results" ("user_id") VALUES ($1)', user_id)


async def user_is_admin(user_id: int):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            result = await connection.fetchrow('SELECT * FROM "users" WHERE "user_id"=$1 AND "isadmin"=True', user_id)
            return result is not None


async def set_test1_results_by_option(user_id, option_number=1, option=1):
    async with dp['db_pool'].acquire() as connection:
        option_n = f'option_{option_number}'
        async with connection.transaction():
            await connection.execute(f'UPDATE "test1_results" SET "{option_n}"=$1 WHERE "user_id"=$2', option, user_id)


async def get_test1_results(user_id):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            result = await connection.fetchrow(f'SELECT * FROM "test1_results" WHERE "user_id"=$1', user_id)
            return [result["option_1"], result["option_2"], result["option_3"], result["option_4"]]


async def set_test1_pokemon_id(user_id, pokemon_id):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            await connection.execute(f'UPDATE "test1_results" SET "pokemon_id"=$1 WHERE "user_id"=$2', pokemon_id, user_id)


async def get_test1_pokemon_id(user_id):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            result = await connection.fetchrow(f'SELECT * FROM "test1_results" WHERE "user_id"=$1', user_id)
            return result["pokemon_id"]


async def set_test2_results_by_option(user_id, option_number=1, option=False):
    async with dp['db_pool'].acquire() as connection:
        option_n = f'option_{option_number}'
        async with connection.transaction():
            await connection.execute(f'UPDATE "test2_results" SET "{option_n}"=$1 WHERE "user_id"=$2', option, user_id)


async def get_test2_results(user_id):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            result = await connection.fetchrow(f'SELECT * FROM "test2_results" WHERE "user_id"=$1', user_id)
            return [result["option_1"], result["option_2"], result["option_3"], result["option_4"], result["option_5"]]


async def set_test2_probability(user_id, probability):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            await connection.execute(f'UPDATE "test2_results" SET "probability"=$1 WHERE "user_id"=$2', probability, user_id)


async def get_test2_probability(user_id):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            result = await connection.fetchrow(f'SELECT * FROM "test2_results" WHERE "user_id"=$1', user_id)
            return result["probability"]


async def get_user_promocode(user_id):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            result = await connection.fetchrow(f'SELECT * FROM "users" WHERE "user_id"=$1', user_id)
            return result["promocode_id"]


async def get_user_promocode_probability(user_id):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            async with connection.transaction():
                result = await connection.fetchrow(
                    '''
                    SELECT 
                        CASE 
                            WHEN u.promocode_id IS NOT NULL THEN p.probability 
                            ELSE 0 
                        END AS probability 
                    FROM 
                        users u 
                    LEFT JOIN 
                        promocodes p ON u.promocode_id = p.id 
                    WHERE 
                        u.user_id = $1
                    ''',
                    user_id
                )
                return result["probability"]


async def get_free_promocode_by_probability(probability):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            promo_code = await connection.fetchrow('SELECT * FROM "promocodes" WHERE "isfree"=True '
                                                   'AND "probability"=$1', probability)
            if promo_code:
                await connection.execute('UPDATE "promocodes" SET "isfree"=False WHERE "id"=$1', promo_code["id"])
                return promo_code["id"]
            else:
                return None


async def set_user_promocode(user_id, promocode):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            await connection.execute(f'UPDATE "users" SET "promocode_id"=$1 WHERE "user_id"=$2', promocode, user_id)


async def promo_info_by_id(id):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            return await connection.fetchrow('SELECT * FROM "promocodes" WHERE "id"=$1', id)


async def all_promocodes():
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            return await connection.fetch('SELECT * FROM "promocodes"')


async def all_free_promocodes():
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            return await connection.fetch('SELECT * FROM "promocodes" WHERE "isfree"=True')


async def promo_by_title_in_bd(promocode):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            result = await connection.fetchrow('SELECT * FROM "promocodes" WHERE "promocode"=$1', promocode)
            return result is not None


async def add_promocode(promocode, probability):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            await connection.execute('INSERT INTO "promocodes" ("promocode", "probability", "isfree") '
                                     'VALUES ($1, $2, $3)', promocode, probability, True)


async def add_to_test_is_passed(user_id, probability):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            await connection.execute('INSERT INTO "test_is_passed" ("user_id", "probability") VALUES ($1, $2)',
                                     user_id, probability)


async def get_count_passed_by_user(user_id, probability=10):
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            query = 'SELECT COUNT(*) FROM "test_is_passed" WHERE "user_id"=$1 AND "probability"=$2'
            result = await connection.fetchrow(query, user_id, probability)
            return result["count"]


async def get_all_passed():
    async with dp['db_pool'].acquire() as connection:
        async with connection.transaction():
            return await connection.fetch('SELECT * FROM "test_is_passed"')
