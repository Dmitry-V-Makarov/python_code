## Extract email and make a database with histogram

import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor() #similar to handle

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    line = line.strip()
    #domain = re.findall('@([^ ]*[a-z])',line)
    domain = re.findall('^From .*@([a-z.]*)',line)
    if len(domain) != 1 : continue
    domain = domain[0]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))

conn.commit() #outside the loop to speed up

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()