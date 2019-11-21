from tkinter import *

window=Tk()

def kg_to_po_gm_oz():
    po=(float(entry1_val.get()))*2.20462
    gm=float(entry1_val.get())*1000
    oz=float(entry1_val.get())*35.274
    text1.insert(END,po)
    text2.insert(END,gm)
    text3.insert(END,oz)


label1=Label(window,text="kg to pounds, grams and oz converter",fg="red",font = ("Times", 20))
label1.grid(row=0,column=1)

label0=Label(window,text="kg to pounds, grams and oz converter",fg="black",font = ("Times", 20))
label0.grid(row=0,column=1)

label1=Label(window,text="kg:",font = "Times")
label1.grid(row=1,column=0)

button1=Button(window,text="convert",command=kg_to_po_gm_oz)
button1.grid(row=1,column=2)


entry1_val=StringVar()
entry1=Entry(window,textvariable=entry1_val)
entry1.grid(row=1,column=1)


label2=Label(window,text="Pounds:",fg="grey",font = "Times")
label2.grid(row=2,column=0)

text1=Text(window,height=1,width=20,bg="yellow",bd=5)
text1.grid(row=3,column=0)


label3=Label(window,text="Grams:",fg="grey",font = "Times")
label3.grid(row=2,column=1)

text2=Text(window,height=1,width=20,bg="yellow",bd=5)
text2.grid(row=3,column=1)


label4=Label(window,text="Oz:",fg="grey",font = "Times")
label4.grid(row=2,column=2)

text3=Text(window,height=1,width=20,bg="yellow",bd=5)
text3.grid(row=3,column=2)

window.mainloop()