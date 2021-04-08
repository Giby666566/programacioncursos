import tkinter
from tkinter import PhotoImage
from tkinter import filedialog
from PIL import ImageTK,Image

def abrirarchivo():
    global miimagen
    global imagen
    global archivo
    tipos=[("Archivos jpg","*.jpeg"),("Archivos png","*.png"),("todos los archivos","*.*")]
    archivo=tkinter.filedialog.askopenfilename(title="dame un arhivo para abrir...",defaultextension=".jpg",filetypes=tipos)
    imagen=tkinter.PhotoImage(file=archivo)
    miimagen.configure(image=imagen)
    miimagen.image=imagen
    tipodearchivo(archivo)
def alerta():
    prueba=messagebox.showinfo(message=tipos,title="prueba")
    print (prueba)
def tipodearchivo(archivo):
    global i
    for i in range(0,len(archivo)):

       if archivo[i]==".":
           break
    print(archivo[i:len(archivo)-1])



root=tkinter.Tk()
boton=tkinter.Button(root,text="explorar archivo...",command=abrirarchivo)
miimagen=tkinter.Label(root,text="hola")
botonalerta=tkinter.Button(root,text="tipo de archivo...",command=alerta)
boton.pack()
miimagen.pack()
botonalerta.pack()


root.mainloop()