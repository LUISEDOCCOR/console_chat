import tkinter as tk
from tkinter import *
import db
import localdb as ldb
import datetime




def msg(contact_id, chat_id):
    


    x = db.get_data_one_contact(contact_id)
    y = ldb.getData()
    contact_info = x[0]
    
    def send():
        date = datetime.datetime.now()
        data_format = date.strftime("%d/%m/%y %H:%M:%S")
        str(data_format)
        text_msg = entry.get()
        db.sendMsg(text_msg, data_format, y[0], chat_id)
        entry.delete(0, END)
    
    
    def view_chat():
        chat_area.config(state=tk.NORMAL)
        chat_area.delete(1.0, tk.END)
        
        msgs = db.viewMsg(chat_id)
        for data in msgs:
            text = str(data) + '\n'
            chat_area.insert(tk.END, text)
        
        chat_area.config(state=tk.DISABLED)
        root.after(500, view_chat)

    
    root =  tk.Tk()
    root.title(contact_info[2])
    root.resizable(False, False)

    # Etiquetas en la parte superior
    you = 'You: ' + y[1]
    etiqueta1 = tk.Label(root, text=you)
    etiqueta1.pack()

    contact_name = 'Friend: ' + contact_info[1]
    etiqueta2 = tk.Label(root, text=contact_name)
    etiqueta2.pack()

    # Área de chat
    chat_area = tk.Text(root, height=10, width=40)
    chat_area.pack()
    chat_area.config(state=tk.DISABLED)
    
    # Campo de entrada
    entry = tk.Entry(root, width=40)
    entry.pack()

    # Botón de enviar
    enviar_button = tk.Button(root, text="Send", command=lambda: send())
    enviar_button.pack()

    root.attributes('-topmost', 1)

    view_chat()
    root.mainloop()

    
