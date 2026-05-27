import sqlite3

DB_PATH = 'cves.db'
SQL_PATH = '/home/zakriya/Desktop/NVAS-1/NVAS-1 Main/forgithubthree/pen_testing_module/init_cves.sql'

def init_db():
    with open(SQL_PATH, 'r') as f:
        sql = f.read()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executescript(sql)
    conn.commit()
    conn.close()
    print('Database initialized.')

if __name__ == '__main__':
    init_db()
