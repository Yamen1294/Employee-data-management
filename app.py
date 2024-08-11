import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import databse

app = customtkinter.CTk()
app.title('Employee Management System')
app.geometry('900x420')
app.config(bg='#161C25')
app.resizable(FALSE,FALSE)

font1 = ('Arial', 20 , 'bold')
font2 = ('Arial', 12 , 'bold')
#----Funs----#
def add_to_treeview():
    employees = databse.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END, values=employee)


def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        role_entry.insert(0,row[2])
        var1.set(row[3])
        status_entry.insert(0,row[4])
    else:
        pass

def insert():
    id = id_entry.get()
    name = name_entry.get()
    role = role_entry.get()
    gender = var1.get()
    status = status_entry.get()
    if not (id and name and role and gender and status):
        messagebox.showerror('Error','Enter all fields.')
    elif databse.id_exists(id):
        messagebox.showerror('Error','ID alread exists...')
    else:
        databse.insert_employee(id,name,role,gender,status)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been inserted.')


def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    role_entry.delete(0,END)
    var1.set('Male')
    status_entry.delete(0,END)


def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose an employee to update.')
    else:
        id = id_entry.get()
        name = name_entry.get()
        role = role_entry.get()
        gender = var1.get()
        status = status_entry.get()
        databse.update_employee(name, role, gender, status, id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been updated')

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose an Employee to delete.')
    else:
        id = id_entry.get()
        databse.delete_employee(id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been deleted.')


id_label = customtkinter.CTkLabel(app,
font=font1,
text='ID:',
text_color='#fff',
bg_color='#161C25')
id_label.place(x=20,y=20)

id_entry = customtkinter.CTkEntry(app,
font=font1,
text_color='#000',
fg_color='#fff',
border_color='#0C9295',
border_width=2,width=180)
id_entry.place(x=100,y=20)

name_label = customtkinter.CTkLabel(app,
font=font1,
text='Name: ',
text_color='#fff',
bg_color='#161C25')
name_label.place(x=23,y=83)

name_entry = customtkinter.CTkEntry(app,
font=font1,
text_color='#000',
fg_color='#fff',
bg_color='#0C9295',
border_width=2,width=180)
name_entry.place(x=100,y=80)

role_label = customtkinter.CTkLabel(app,
font=font1,
text='Role: ',
text_color='#fff',
bg_color='#161C25')
role_label.place(x=20,y=140)

role_entry = customtkinter.CTkEntry(app,
font=font1,
text_color='#000',
fg_color='#fff',
border_color='#0C9295',
border_width=2,width=180)
role_entry.place(x=100,y=140)

gender_label = customtkinter.CTkLabel(app,
font=font1,
text='Gender:',
text_color='#fff',
bg_color='#161C25')
gender_label.place(x=20,y=200)

options = ['Male','Female']
var1 = StringVar()

gender_options = customtkinter.CTkComboBox(app,
font=font1,
text_color='#000',
bg_color='#fff',
dropdown_hover_color='#0C9295',
button_color='#0C9295',
button_hover_color='#0C9295',
border_color='#0C9295',
width=180,
variable=var1,values=options,state='readonly')
gender_options.set('Male')
gender_options.place(x=100,y=200)

status_label = customtkinter.CTkLabel(app,
font=font1,
text='Status:',
text_color='#fff',
bg_color='#161C25')
status_label.place(x=20,y=260)

status_entry = customtkinter.CTkEntry(app,
font=font1,
text_color='#000',
fg_color='#fff',
border_color='#0C9295',
border_width=2,width=180)
status_entry.place(x=100,y=260)

add_button = customtkinter.CTkButton(app,
font=font1,
text_color='#fff',
text='Add Employee',
fg_color='#05A312',
hover_color='#FF5002',
bg_color='#161C25',
cursor="hand2",
corner_radius=15,width=260,
command=insert)
add_button.place(x=20,y=310)

clear_button = customtkinter.CTkButton(app,
font=font1,
text_color='#fff',
text='New Enployee',
fg_color="#161C25",
hover_color='#FF5002',
bg_color='#161C25',
cursor='hand2',
corner_radius=15,width=260,
command=lambda:clear(True))
clear_button.place(x=20,y=360)


update_button = customtkinter.CTkButton(app,
font=font1,
text_color='#fff',
text='Update Enployee',
fg_color="#161C25",
hover_color='#FF5002',
bg_color='#161C25',
cursor='hand2',
corner_radius=15,width=260,
command=update)
update_button.place(x=300,y=360)


delete_button = customtkinter.CTkButton(app,
font=font1,
text_color='#fff',
text='Delete Enployee',
fg_color="#E40404",
hover_color='#FF5002',
bg_color='#161C25',
cursor='hand2',
corner_radius=15,width=260,
command=delete)
delete_button.place(x=580,y=360)

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview', font=font2,foreground='#fff',
background='#000',
fieldbackground='#313837')
style.map('Treeview',background=[('selected','#1A8F2D')])

tree = ttk.Treeview(app,height=15)

tree['columns'] = ('ID','Name','Role','Gender','Status')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.CENTER, width=120)
tree.column('Name', anchor=tk.CENTER, width=120)
tree.column('Role', anchor=tk.CENTER, width=120)
tree.column('Gender', anchor=tk.CENTER, width=100)
tree.column('Status', anchor=tk.CENTER, width=120)


tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Status', text='Status')
tree.place(x=300,y=20)

tree.bind('<ButtonRelease>',display_data)

add_to_treeview()

app.mainloop()