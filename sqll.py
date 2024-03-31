import sqlite3


def init_database():
    con = sqlite3.connect('predprof.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS dayz(
                   dateid INTEGER PRIMARY KEY,
                   date TEXT UNIQUE,
                   floors INTEGER,
                   windows TEXT,
                   lights TEXT,
                   count INTEGER,
                   wall, coords);""")
    con.commit()
    return True


def save_day(data):
    con = sqlite3.connect('predprof.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO dayz (date, floor_num, windows, lights, count) 
                           VALUES (?, ?, ?, ?, ?)
                        """, (data[0], data[1], data[2], data[3], data[4],))
    con.commit()
    return True


def get_day(date):
    con = sqlite3.connect('predprof.db')
    cur = con.cursor()
    try:
        data = cur.execute("""SELECT floor_num, windows, lights, count FROM dayz WHERE date=?""", (date,)).fetchone()[0]
    except Exception as e:
        return str(e)[26:]
    print(date)
    # return_context = {for el in data}
    # return return_context


def get_all():
    con = sqlite3.connect('predprof.db')
    cur = con.cursor()
    data_all = cur.execute("""SELECT * FROM dayz""").fetchall()
    return data_all


