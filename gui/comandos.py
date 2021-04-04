import tkinter

def sacartexto():
    global Entrada
    texto=Entrada.get()
    print("Entrada"+texto)

def cambiartexto():
    global Entrada,Mitexto
    texto=Entrada.get()
    Mitexto.configure(bg=texto)
ventana=tkinter.Tk()

ventana.title("COMANDOS")
ventana.geometry("400x400")
Entrada=tkinter.Entry(ventana)
Mitexto=tkinter.Label(ventana,text="prueba")
Boton=tkinter.Button(ventana,text="Hazme click!",command=sacartexto)
Boton2=tkinter.Button(ventana,command=cambiartexto)
Mitexto.pack()
Entrada.pack()
Boton.pack()
Boton2.pack()

texto=Entrada.get()
print("hola"+texto)

ventana.mainloop()