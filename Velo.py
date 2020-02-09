import tkMessageBox
from tkinter import *
from db import Database

db = Database('rooms.db')

def populate_list():
    rooms_list.delete(0, END)
    for row in db.fetch():
        rooms_list.insert(END, row)


def add_item():
    if name_text.get() == '' or apellidoP_text.get() == '' or apellidoM_text.get() == '' or edad_text.get() == '' or room_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(name_text.get(), apellidoP_text.get(), apellidoM_text.get(), edad_text.get(), room_text.get())
    rooms_list.delete(0, END)
    rooms_list.insert(END, (name_text.get(), apellidoP_text.get(), apellidoM_text.get(), edad_text.get(), room_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = rooms_list.curselection()[0]
        selected_item = rooms_list.get(index)

        name.delete(0, END)
        name.insert(END, selected_item[1])
        apellidoP.delete(0, END)
        apellidoM_text.insert(END, selected_item[2])
        apellidoM.delete(0, END)
        apellidoM.insert(END, selected_item[3])
        Edad.delete(0, END)
        Edad.insert(END, selected_item[4])
        Room.delete(0, END)
        Room.insert(END, selected_item[5])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], name_text.get(), apellidoP_text.get(), apellidoM_text.get(), edad_text.get(), room_text.get()) 
    populate_list()


def clear_text():
    name.delete(0, END)
    apellidoP.delete(0, END)
    apellidoM.delete(0, END)
    Edad.delete(0, END)
    Room.delete(0, END)

#Creates the object window  
window = Tk()

#first = Label(window, text = "Sistema de Check-in y Check-out", font=('bold', 14), pady =20, bg= "black", fg= "white")
#first.pack(fill=X)

################################################################
 
window.title("Rooms Tonala")
window.geometry('1000x500')

########################Nombre#################################
name_text = StringVar() 
Name = Label(window, text = "Nombre", font=('bold', 12), pady =20)
Name.grid(column=0, row=1, sticky = W)
name = Entry(window,width=20, textvariable= name_text)
name.grid(column=1, row=1)

#######################Apellido paterno################################
apellidoP_text = StringVar() 
Apellido = Label(window, text = "Apellido Paterno", font=('bold', 12))
Apellido.grid(column=3, row=1)
apellidoP = Entry(window,width=20, textvariable= apellidoP_text)
apellidoP.grid(column=4, row=1) 

#######################Apellido materno################################
apellidoM_text = StringVar()  
Apellido = Label(window, text = "Apellido Materno", font=('bold', 12))
Apellido.grid(column=5, row=1)
apellidoM = Entry(window,width=20, textvariable= apellidoM_text)
apellidoM.grid(column=6, row=1) 

########################Room################################
room_text = StringVar()
room = Label(window, text = "Room", font=('bold', 12))
room.grid(column=1, row=2)
Room = Entry(window,width=20, textvariable= room_text)
Room.grid(column=2, row=2) 
#######################Edad################################
edad_text = StringVar()
edad = Label(window, text = "Edad", font=('bold', 12))
edad.grid(column=1, row=3)
Edad = Entry(window,width=20, textvariable= edad_text)
Edad.grid(column=2, row=3) 

#######################Sexo################################
Sexo = Label(window, text = "Sexo", font=('bold', 12))
Sexo.grid(column=3, row=3)

m = Checkbutton(window, text = "Masculino")
m.grid(column=4, row=3,)

f = Checkbutton(window, text = "Femenino")
f.grid(column=5, row=3,)

#######################################################################
rooms_list= Listbox(window, height=8, width=50, border = 10)
rooms_list.grid(row=6, column=0, columnspan = 10, rowspan = 6)

scrollbar= Scrollbar(window)
scrollbar.grid(row=6, column= 3)

rooms_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command = rooms_list.yview)

rooms_list.bind('<<ListboxSelect>>', select_item)
######################botones##########################################
add_btn = Button(window, text='Add Part', width=12, command=add_item)
add_btn.grid(row=4, column=0, pady=20)

remove_btn = Button(window, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=4, column=1)

update_btn = Button(window, text='Update Part', width=12, command=update_item)
update_btn.grid(row=4, column=2)

clear_btn = Button(window, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=4, column=3)

#def clicked():
#		
#    res = "Welcome to " + txt.get()
# 
#    lbl.configure(text= res)
# 
#btn = Button(window, text="Click Me", command=clicked)
# 
#btn.grid(column=4, row=4)
#

#c = Chekbutton(root, text = "keep me loged in")
#c.grid(columnspan = 2)
 

#Starts the prgram and leaves the window open until I hit the x and
#close the app.
window.mainloop()
