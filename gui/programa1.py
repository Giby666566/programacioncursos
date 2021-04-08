#hacer un programa donde tienes un boton que dice "explorar archivo" donde seleccionas una imagen y 
# esa imagen la pone en un label
import tkinter
from tkinter import PhotoImage
from tkinter import filedialog
from PIL import image
def abrirarchivo():
    global miimagen
    global imagen
    tipos=[("Archivos jpg","*.jpeg"),("Archivos png","*.png"),("todos los archivos","*.*")]
    archivo=tkinter.filedialog.askopenfilename(title="dame un arhivo para abrir...",defaultextension=".jpg",filetypes=tipos)
    imagen=tkinter.PhotoImage(file=archivo)
    miimagen.configure(image=imagen)
    miimagen.image=imagen




root=tkinter.Tk()
boton=tkinter.Button(root,text="explorar archivo...",command=abrirarchivo)
miimagen=tkinter.Label(root,text="hola")

boton.pack()
miimagen.pack()



root.mainloop()