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
                   wall TEXT,
                   coords TEXT);""")
    con.commit()
    return True


def save_day(data):
    con = sqlite3.connect('predprof.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO dayz (date, floors, windows, lights, count, wall, coords) 
                           VALUES (?, ?, ?, ?, ?, ?, ?)
                        """, (data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    con.commit()
    return True


def get_day(date):
    con = sqlite3.connect('predprof.db')
    cur = con.cursor()
    if not date:
        data_all = cur.execute("""SELECT * FROM dayz""").fetchall()
    else:
        try:
            data_all = cur.execute("""SELECT floor_num, windows, lights, count FROM dayz WHERE date=?""", (date,)).fetchall()
        except Exception as e:
            return str(e)[26:]
    context = {el[0]: [el[1], el[2], el[3], el[4], el[5], el[6]] for el in data_all}
    return context
