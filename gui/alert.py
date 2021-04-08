import tkinter
from tkinter import messagebox
def salir():
    global root 
    root.destroy()
def alerta():
    
    prueba=messagebox.askyesnocancel(message="error",title="prueba")
    print (prueba)

root=tkinter.Tk()
boton=tkinter.Button(root,text="oprímeme",command=alerta)
botonsalir=tkinter.Button(root,text="salir",command=salir)
boton.pack()
botonsalir.pack()




root.mainloop()