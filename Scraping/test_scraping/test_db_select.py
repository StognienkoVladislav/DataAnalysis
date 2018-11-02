

import sqlite3

conn = sqlite3.connect('allo_db.sqlite')
c = conn.cursor()

kk = c.execute('SELECT * FROM allo_parse;')
print kk.fetchall()
conn.close()
