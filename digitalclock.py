from cgitb import text
from tkinter import *
from time import strftime
root = Tk()
root.geometry("500x400")
root.resizable(0,0)
root.config(bg='pink')
root.title('Python Clock')
Label(root,text="The time is :",font ='Algerian 20 bold').pack(side=TOP)
Label(root,text = 'Anibaba Stores ', font ='arial 20 bold',bg='pink').pack(side=BOTTOM)
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string,bg='pink')
    mark.after(1000, time)
mark = Label(root, 
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'black')
mark.pack(anchor = 'center')
time()
 
mainloop()