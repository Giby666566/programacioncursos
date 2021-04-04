import tkinter
from tkinter import PhotoImage
ventana=tkinter.Tk()
ventana.title("FACEBOOK")
ventana.iconbitmap("imgs/facebook.ico")
ventana.geometry("500x500")

Intro=tkinter.Label(ventana, text="BIENVENIDO A TU\n FACEBOOK", font="Helvetica", bg="lightblue",width=25,height=2)
Intro.pack() #side=top, bottom, left or right

miimagen=PhotoImage(file="imgs/fb_icon_325x325.png")
Salir=tkinter.Button(ventana,text="Salir", bg="red", activebackground="yellow",image=miimagen,compound="center")
Salir.pack(side="left")

Lista=tkinter.Listbox(ventana,highlightcolor="red", relief="flat")
Lista.pack()
Lista.insert(0,"hola")
Lista.insert(1,"adios")
Lista.insert(2,"eifjiu")

Seleccion=tkinter.Radiobutton(ventana, text="Opcion 1")
Seleccion.pack()

Entrada=tkinter.Entry(ventana)
Entrada.pack()

#relief=flat, sunken, raised, groove, ridge

ventana.mainloop()


