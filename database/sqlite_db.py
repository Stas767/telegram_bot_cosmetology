import sqlite3 as sq

from core import bot


def sql_start():
    global base, cur
    base = sq.connect('sqlite.db')
    cur = base.cursor()
    base.execute(
        'CREATE TABLE IF NOT EXISTS services(title TEXT PRIMARY KEY, description TEXT, photo TEXT, recommend TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO services VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read_servises():
    for ret in cur.execute('SELECT * FROM servises').fetchall():
        await bot.send_photo(
            message.from_user.id, 
            ret[0],
            
             )
