import sqlite3

conn = sqlite3.connect('localdb.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS local_user(
                   id TEXT NOT NULL,
                   name TEXT NOT NULL,
                   gmail TEXT NOT NULL
               )
               ''')
conn.commit()


def addUser(Name, Gmail , Password):
    cursor.execute('DELETE FROM local_user')
    conn.commit()
    cursor.execute('INSERT INTO local_user (id, name, gmail) VALUES (?,?,?)', (Name, Gmail, Password))
    conn.commit()
    
def verify_local_user():
    cursor.execute('SELECT * FROM local_user')
    x = cursor.fetchall()
    if not x:
        return True
    else: return False

def getData():
    cursor.execute('SELECT * FROM local_user')
    x = cursor.fetchall()
    return x[0][0], x[0][1], x[0][2]
    
    