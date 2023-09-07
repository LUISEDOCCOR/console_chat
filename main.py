import db
import os
import time
import platform
import msg
import localdb as l_db
from colorama import Fore, Back, Style
from tqdm import tqdm


def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def load():
    for i in tqdm(range(int(9e6))):
        pass  

def cookies(Gmail):
    id, name, gmail = db.get_data_user(Gmail)
    l_db.addUser(id, name, gmail)

def add_contact(local_gmail, local_id):
    x = None
    while x != 'y' and x != 'n' and x != 'Y' and x != 'N' :
        x = input('Add contact (y/n) ')
        if x == 'n' or x == 'N':
            welcome()
        else:
            clear()
            name = input('Name: ')
            x = True
            while x:
                gmail = input('Gmail: ') 
                gmail.lower()    
                if gmail == local_gmail:
                    clear()
                    print('thats your gmail')
                else:
                    if not db.viewUser(gmail):
                        clear()
                        print('That gmail does not exist')
                    else:
                        other_id, other_name, other_gmail = db.get_data_user(gmail)
                        del other_name
                        db.addContact(local_id, name, gmail, other_id)
                        x = False    
    

def signup():
    name = input('What is your name: ')
    x = True
    while x:
        gmail = input('What is your gmail: ')
        if not '@' in gmail:
            clear()
            print('This gmail is fake')    
        else:
            if db.viewUser(gmail):
              clear()
              print('This gmail has already been used')  
            else:
                gmail.lower()
                x = False 
    x = True     
    while x:
        password = input('What is your password: ')         
        if len(password) < 5:
            clear()
            print('its password is too short')
        else:
            if ' ' in password:
                clear()
                print('is password has spaces')
            else:
                x = False
    
    clear()
    print(f'Welcome {name}')
    db.addUser(name, gmail, password)
    cookies(gmail)
    chat()

def view_contacts(local_id):
    contacts =  db.getDataContacts(local_id)   
    for contact in contacts:
        print(f'''
            Contact Id: {Fore.RED}{contact[0]}{Style.RESET_ALL}  
            Name: {contact[1]}
            {contact[1]} gmail: {contact[2]}
            ''')

def login():
    x = True
    while x:
        gmail = input('What is your gmail: ')
        if not '@' in gmail:
            clear()
            print('This gmail is fake')    
        else:
            if not db.viewUser(gmail): 
                clear()
                print('Fatal error')
            else:
                x = False
    
    x = True            
    while x:
        password = input('What is your password: ')
        if db.viewPassword(gmail, password):
            x = False
        else:
            clear()
            print('Fatal error')            
    
    clear()
    print(f'Welcome {gmail}')
    cookies(gmail)
    chat()

                        

def chat():
    clear()
    if l_db.verify_local_user():
        print('There is no account')
        time.sleep(1)
        clear()
        welcome()
    else:
        print('ChatAPP\n') 
        local_id, local_name, local_gmail = l_db.getData()
        print('My profile:')   
        print(f'''
              Name: {local_name}
              Gmail: {local_gmail}
              Your id: {Fore.RED}{local_id}{Style.RESET_ALL}
              ''')
        print('Contacts: \n')
        if db.viewContacts(local_id):
            print(f'{Fore.RED} You dont have contacts {Style.RESET_ALL}')
            add_contact(local_gmail, local_id)    
        
        else:
            x = None
            while x != 'y' and x != 'n' and x != 'Y' and x != 'N' :
                clear()
                view_contacts(local_id)
                x = input('Chat with one of your contacts (y/n) ')
            if x == 'n' or x == 'N':
                clear()
                welcome()
            else:
                clear()
                view_contacts(local_id)
                x = True
                while x:
                    contact_id = input('Which contact do you want to talk to (id): ')
                    if db.view_id_contacts(contact_id):
                        clear()
                        print('You dont have that contact')
                        view_contacts(local_id)
                    else:
                        x = False
                clear()    
                load()     
                x = db.get_data_other_user(contact_id)
                other_id = x[0][0]
                if db.create_chat(local_id, other_id):
                    clear()
                    print('The chat has been created correctly')
                    time.sleep(1)
                    clear()
                    msg.msg(other_id)
                else:
                    clear()
                    print('the chat had already been created')
                    time.sleep(1)
                    clear()
                    x = db.get_data_chat(local_id, other_id)
                    msg.msg(other_id, x[0][0])     
                

                
            
            
            
def welcome():
    print('Chat APP')
    time.sleep(.5)
    clear()

    print('What are you going to do?\n')
    print('1 --> Sign Up')
    print('2 --> Login')
    print('3 --> Go to chat')
    print('\n')



    x = None
    while x != 1 and x != 2 and x  != 3:
        x = int(input('Answer: '))
        
        clear()

        if x == 1:
            signup()
        elif x == 2:
            login()
        else:
            chat()    

    
welcome()