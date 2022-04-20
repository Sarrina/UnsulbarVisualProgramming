from tkinter import *
 
window = Tk()
window.title("Kalkulator by SARINA_D0219413")
window.geometry('300x300')
 
lbl = Label(window, text="Bilangan 1 ",anchor="e",width=20)
lbl.grid(column=0, row=0)
 
nilai1 = Entry(window,width=10)
nilai1.grid(column=1,row=0)
 
 
lbl2 = Label(window, text="Bilangan 2 ",anchor="e",width=20)
lbl2.grid(column=0, row=1)
 
nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=1)
 
lbl3 = Label(window, text="Hasil ",anchor="e",width=20)
lbl3.grid(column=0, row=2)
 
hasil = Label(window, text="0",anchor="w",width=10)
hasil.grid(column=1, row=2)
 
def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))
 
def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))
 
def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))
 
def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))
 
 
btn = Button(window, text="+", bg="pink", fg="white", width=10, command=tambah)
btn.grid(column=0, row=3)
 
btn = Button(window, text="-", bg="orange", fg="white", width=10, command=kurang)
btn.grid(column=1, row=3)
 
btn = Button(window, text="x", bg="grey", fg="white", width=10, command=kali)
btn.grid(column=0, row=4)
 
btn = Button(window, text="/", bg="blue", fg="white", width=10, command=bagi)
btn.grid(column=1, row=4)
 
 
window.mainloop()






























