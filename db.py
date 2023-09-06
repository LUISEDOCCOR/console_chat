import mysql.connector
import bcrypt


db_config ={
    'host': '192.168.10.104',
    'user': 'root',
    'password': 'G4NmsyJ/XTruN]e',
    'database': 'chatapp'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# if conn.is_connected:
#     print('EN SERVICIO')
# else:
#     print('FUERA DE SERVICIO')
    
    
def addUser(Name, Gmail, Password):
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(Password.encode('utf-8'), salt)
    cursor.execute('INSERT INTO users (name, gmail, password) VALUES (%s, %s, %s)', (Name, Gmail, hash_password))
    conn.commit()

def viewUser(Gmail): #sigup
    cursor.execute('SELECT * FROM users WHERE gmail = (%s)', (Gmail,))
    x = cursor.fetchall()
    if not x: #si esta vacio ...
        return False
    else:
        return True  

def viewPassword(Gmail, Password):
    cursor.execute('SELECT * FROM users WHERE gmail = (%s)', (Gmail,)) 
    x = cursor.fetchall()
    password = x[0][3].encode('utf-8')
    if bcrypt.checkpw(Password.encode('utf-8'), password):
        return True
    else: 
        return False
    
def get_data_user(Gmail):
    cursor.execute('SELECT * FROM users WHERE gmail = (%s)', (Gmail,))
    x = cursor.fetchall()
    return x[0][0], x[0][1], x[0][2]
       

def addContact(User_id, Name, Gmail, Other_id):
    cursor.execute('INSERT INTO contacts (name, gmail, user_id, other_id) VALUES (%s,%s,%s,%s)', (Name, Gmail, User_id, Other_id))
    conn.commit()

def viewContacts(User_id):
    cursor.execute('SELECT * FROM contacts WHERE user_id = (%s)', (User_id,))
    x = cursor.fetchall()
    if not x:
        return True
    else:
         return False

def getDataContacts(user_id):
    cursor.execute('SELECT * FROM contacts WHERE user_id = (%s) ', (user_id,))
    x = cursor.fetchall()
    return x
        
def view_id_contacts(user_id):
    cursor.execute('SELECT * FROM contacts WHERE user_id = (%s) ', (user_id,))
    x = cursor.fetchall()
    if not x:
        return True
    else:
        return False
    
def get_data_other_user(contact_id):
    cursor.execute('SELECT other_id FROM contacts WHERE id = (%s) ', (contact_id,)) 
    x = cursor.fetchall()
    return x

def create_chat(user_id, other_user_id):
    cursor.execute('INSERT INTO chat (user_id, other_user_id) VALUES (%s, %s)', (user_id, other_user_id))
    conn.commit()


def sendMsg():
    pass

def viewMsg():
    pass