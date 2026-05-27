import sqlite3

conn = sqlite3.connect('cves.db')
cur = conn.cursor()
cur.execute('SELECT COUNT(*) FROM cves')
count = cur.fetchone()[0]
print(f"Total rows in cves table: {count}")
conn.close()