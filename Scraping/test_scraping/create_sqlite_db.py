
import sqlite3

conn = sqlite3.connect('allo_db.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE allo_parse
             (search_param text, results text);''')
conn.commit()
conn.close()
