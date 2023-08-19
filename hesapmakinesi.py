from tkinter import *
import tkinter as tk
master = Tk()

canvass = Canvas(master, width= 300, height=500)
canvass.pack()
framem= Frame(master, bg="grey")
framem.place(relx =0.05, rely =0.07, relwidth=0.91, relheight=0.09)

Label(framem, text="HESAP MAKİNESİ", bg="grey",fg="#F6EA3C", font="Verdana 10 bold").pack(pady=10, padx=5, anchor = "center")
Label(master, text="Sayi 1:", font="Verdana 10 ",fg="#012d36").place(relx=0.09, rely =0.217)

sayi1 = tk.Entry(master, width=10)
sayi1.place(x=20, y=10, rely = 0.2, relx =0.2)
Label(master,text ="Sayi 2:", font ="Verdana 10 ",fg="#012d36").place(relx =0.09, rely=0.270)
sayi2 = tk.Entry(master, width=10)
sayi2.place(x=20, y=10, rely=0.25, relx=0.2)

frame2= Frame(master)
frame2.place(relx=0.24, rely =0.37, relwidth=0.55, relheight=0.08)

def toplama():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        sa1 = int(sayi1.get())
        sa2 = int(sayi2.get())
        sonuc["text"] = str(sa1+sa2)
    else: 
        pass
def cikarma():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        sa1 = int(sayi1.get())
        sa2 = int(sayi2.get())
        sonuc["text"]=str(sa1-sa2)
    else:
        pass
def carpma():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        sa1 = int(sayi1.get())
        sa2 = int(sayi2.get())
        sonuc["text"] =str(sa1*sa2)
    else:
        pass
def bolme():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        sa1 = float(sayi1.get())
        sa2 = float(sayi2.get())
        sonuc["text"] = str(sa1/sa2)
    else:
        pass
    
sonuc = Label(master, text="...", font="Verdana 10", fg="#012d36")
sonuc.place(x=190,y=120)


cikar = tk.Button(frame2, text="-", font="Verdana 14 ", activebackground="#46453F",bd=5, 
                   command = cikarma, activeforeground="#F6EA3C")
cikar.pack(pady=3, padx=3, side = LEFT)
toplaa = tk.Button(frame2, text="+",font="Verdana 14 ", activebackground="#46453F", bd=5, 
                   command = toplama,activeforeground="#F6EA3C")
toplaa.pack(pady=3, padx=3, side = LEFT) 
carp = tk.Button(frame2, text="*", font="Verdana  14 ", activebackground="#46453F",bd=5, 
                 command = carpma, activeforeground="#F6EA3C")
carp.pack(pady=3,padx=3, side = LEFT)
bol = tk.Button(frame2, font="Verdana 14", text ="/", activebackground="#46453F",bd=5,
                command = bolme, activeforeground="#F6EA3C")
bol.pack(pady=3,padx=3, side= LEFT)


master.mainloop()