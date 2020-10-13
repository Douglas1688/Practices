from tkinter import *

root = Tk()
miFrame =Frame(root,width=500,height=400)
miFrame.pack(fill="both",expand ="True")
miImagen=PhotoImage(file="img/gifanimado.gif")
miLabel=Label(miFrame,image=miImagen)
miLabel.place(x=0,y=0)
root.mainloop()