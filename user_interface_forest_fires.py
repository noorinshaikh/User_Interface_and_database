"""
UI to take:
State
City
Coordiates
Type
Size/Acres

Widget  does:
View All
Search Entry
Add Entry
Update Selected
Delet Selected
Close
"""

from tkinter import *
import forest_fires_db

def view_all():
    List1.delete(0,END)
    for row in forest_fires_db.view():
        List1.insert(END,row)

def search():
    List1.delete(0, END)
    for row in forest_fires_db.search(state_val.get(),city_val.get(),type_val.get(),size_val.get()):
        List1.insert(END, row)

def add():
    forest_fires_db.insert(state_val.get(),city_val.get(),type_val.get(),size_val.get())
    List1.delete(0,END)
    List1.insert(END,(state_val.get(),city_val.get(),type_val.get(),size_val.get()))

def get_selected_row(event):
    global selection
    index=List1.curselection()[0]
    selection=List1.get(index)
    entry1.delete(0,END)
    entry1.insert(END,selection[1])
    entry2.delete(0,END)
    entry2.insert(END, selection[2])
    entry4.delete(0,END)
    entry4.insert(END, selection[3])
    entry5.delete(0,END)
    entry5.insert(END, selection[4])

def update():
    forest_fires_db.update(selection[0],state_val.get(),city_val.get(),type_val.get(),size_val.get())

def delete():
    forest_fires_db.delete(selection[0])

window=Tk()

window.wm_title("California fires 2019")


label1=Label(window,text="State",font = ("Times", 20))
label1.grid(row=0,column=0,padx=8,pady=8)

label2=Label(window,text="City",font = ("Times", 20))
label2.grid(row=0,column=2,padx=8,pady=8)

label4=Label(window,text="Type",font = ("Times", 20))
label4.grid(row=2,column=0)

label5=Label(window,text="Size/Acres",font = ("Times", 20))
label5.grid(row=2,column=2)

button1=Button(window,text="View All",command=view_all)
button1.config(height=2,width=8)
button1.grid(row=3,column=3,padx=8,pady=8)

button2=Button(window,text="Search",command=search)
button2.config(height=2,width=8)
button2.grid(row=4,column=3,padx=8,pady=8)

button3=Button(window,text="Add",command=add)
button3.config(height=2,width=8)
button3.grid(row=5,column=3,padx=8,pady=8)

button4=Button(window,text="Update",command=update)
button4.config(height=2,width=8)
button4.grid(row=6,column=3,padx=8,pady=8)

button5=Button(window,text="Delete",command=delete)
button5.config(height=2,width=8)
button5.grid(row=7,column=3,padx=8,pady=8)

button6=Button(window,text="Close",command=window.destroy)
button6.config(height=2,width=8)
button6.grid(row=8,column=3,padx=8,pady=8)

List1=Listbox(window,height=13,width=35)
List1.grid(row=3,column=0,rowspan=6,columnspan=2,padx=8,pady=8)

List1.bind('<<ListboxSelect>>',get_selected_row)

scroll=Scrollbar(window)
scroll.grid(row=3,column=2,rowspan=6)

state_val=StringVar()
entry1=Entry(window,textvariable=state_val)
entry1.grid(row=0,column=1,padx=8,pady=8)

city_val=StringVar()
entry2=Entry(window,textvariable=city_val)
entry2.grid(row=0,column=3,padx=8,pady=8)

type_val=StringVar()
entry4=Entry(window,textvariable=type_val)
entry4.grid(row=2,column=1)

size_val=StringVar()
entry5=Entry(window,textvariable=size_val)
entry5.grid(row=2,column=3)

window.mainloop()