import tkinter
from tkinter import PhotoImage
def sumar():
    global num1,num2,resultado
    entrada1=float(num1.get())
    entrada2=float(num2.get())
    operacion=entrada1+entrada2
    resultado.configure(text=str(operacion))


root=tkinter.Tk()
imagen=PhotoImage(file="imgs/hola.png")

num1=tkinter.Entry(root)
num2=tkinter.Entry(root)
resultado=tkinter.Label(root,text="resultado")
suma=tkinter.Button(root,text="+",command=sumar)

resultado.configure(image=imagen)

num1.pack()
num2.pack()
resultado.pack()
suma.pack()
root.mainloop()