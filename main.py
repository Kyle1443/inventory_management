from tkinter import *
import sqlite3
import pandas as pd
import email.message



root = Tk()
root.geometry('700x300')
root.title('Inventory solutions 1.0')
Label(text = 'Warehouse Management', bg = 'grey', height = '2', width = '300', font = ('Calibri', 13))
Label('')


#closes program
def quit():
    root.destroy()

#home screen functionality
Button(text = 'Login', height = '3', width = '40')
Button(text = 'Quit', height = '1', width = '20', command = quit)

#clears text fields on table
def submit():
    item_type.delete(0, END)
    item_name.delete(0, END)
    price.delete(0, END)
    quantity.delete(0, END)


#connect to database
link = sqlite3.connect('inventory.db')
#creating cursor
c = link.cursor()

#initial creation of the table: only needed once
#c.execute(''' CREATE TABLE inventory (
        #item_type text,
        #item_name text,
        #item_price real, 
        #quantity int
        #)
        #''')

#table text boxes
item_type = Entry(root, width=40)
item_type.grid(row=0, column=1)
item_name = Entry(root, width=40)
item_name.grid(row=1, column=1)
price = Entry(root, width=40)
price.grid(row=2, column=1)
quantity = Entry(root, width=40)
quantity.grid(row=3, column=1)

#text box labels
type_label = Label(root, text = 'Item Type')
type_label.grid(row=0, column=0)
name_label = Label(root, text = 'Item Type')
name_label.grid(row=1, column=0)
price_label = Label(root, text = 'Item Type')
price_label.grid(row=2, column=0)
quantity_label = Label(root, text = 'Item Type')
quantity_label.grid(row=3, column=0)

#add button
add_btn = Button(root, text = 'Add record', command = submit)
add_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)



#commit changes
link.commit()

link.close()


root.mainloop()


