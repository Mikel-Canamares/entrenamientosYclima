from tkinter import *
from tkinter import ttk
import aemet
import baseDatos
import log
from tkcalendar import DateEntry
import traduccion

#Ventana de aplicación
raiz = Tk()
raiz.geometry("950x400")

#Pestañas
notebook = ttk.Notebook(raiz)
notebook.pack()
pes1 = ttk.Frame(notebook)
pes2 = ttk.Frame(notebook)
notebook.add(pes1, text = "Entrenamientos")
notebook.add(pes2, text = "El tiempo")

#Barra Menu
barraMenu = Menu(raiz)
raiz.config(menu = barraMenu)

datosMenu = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Base de datos", menu = datosMenu)
datosMenu.add_command(label = "Crear", command = baseDatos.conectar)
datosMenu.add_command(label = "Salir", command = baseDatos.salir)

IdiomaMenu = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Idioma", menu = IdiomaMenu)
IdiomaMenu.add_command(label= "Español", command = traduccion.esp)
IdiomaMenu.add_command(label= "Inglés", command = traduccion.ing)

#Frames
frameDatos = Frame(pes1, width = 950, height = 400, )
frameDatos.pack(side = "left", anchor = "n")
frameTiempo = Frame(pes2, width = 860, height = 400)
frameTiempo.pack()

#Variables
prov = StringVar(frameTiempo)
miTiempo = StringVar(frameDatos)
miDistancia = StringVar(frameDatos)
actividad = StringVar(frameDatos)

#-------------------------Pestaña datos-----------------------------------
actividadLabel=Label(frameDatos, text="Actividad: ")
actividadLabel.grid(row=0,column = 0, sticky = "w", padx = 10, pady = 10)

depOpcion = IntVar()
correr = Radiobutton(frameDatos, text = "Correr", variable = depOpcion, value = 1)
correr.grid(row=0,column=1, sticky = "w")
bicicleta =Radiobutton(frameDatos, text = "Bicicleta", variable = depOpcion, value = 2)
bicicleta.grid(row=0,column=2, sticky = "w")

tiempoLabel=Label(frameDatos, text="Minutos: ")
tiempoLabel.grid(row=1,column = 0, sticky = "w", padx = 10, pady = 10)
tiempoEntry = Entry(frameDatos, textvariable = miTiempo)
tiempoEntry.grid(row=1,column=1,padx=10, pady=10, sticky = "w", columnspan = 4)

distanciaLabel=Label(frameDatos, text="Kilómetros: ")
distanciaLabel.grid(row=2,column = 0, sticky = "w", padx = 10, pady = 10)
distanciaEntry = Entry(frameDatos, textvariable = miDistancia)
distanciaEntry.grid(row=2,column=1,padx=10, pady=10, sticky = "w", columnspan = 4)

buscarLabel=Label(frameDatos, text="--------Buscar-------- ")
buscarLabel.grid(row=3,column = 1, sticky = "n", padx = 10, columnspan = 4)

#Lista desplegable de actividades
actividad.set(baseDatos.actividades[0])
menuDesplegable = OptionMenu(frameDatos, actividad,*baseDatos.actividades)
menuDesplegable.grid(row=4,column = 1, sticky = "n", padx = 10,  columnspan = 3)

#Ventana para mostrar datos
textoDatos = Text(frameDatos, width= 80, height= 20)
textoDatos.grid(row = 0, column = 8, sticky = "e", padx =10, pady=10,rowspan =10 )
#barra desplazamiento para cuadro de texto
scrollVert = Scrollbar(frameDatos, command=textoDatos.yview)#barra desplazamiento
scrollVert.grid(row=0, column=9, sticky = "nsew", rowspan =10)#tamaño barra ajustado a la ventana
textoDatos.config(yscrollcommand= scrollVert.set)#la barra se posiciona en el texto

#Botones
botonLimpiar = Button(frameDatos, text= "Limpiar", command = baseDatos.limpiar)
botonLimpiar.grid(row=4,column=0, sticky = "w", padx=10, pady=5)

botonInsertar = Button(frameDatos, text= "Insertar", command = baseDatos.insertar)
botonInsertar.grid(row=3,column=0, sticky = "w", padx=10, pady=5)

botonBuscar = Button(frameDatos, text= "Buscar", command = baseDatos.buscarDeporte)
botonBuscar.grid(row=6,column=1, sticky = "w", padx=10, pady=5)

#calendarios
fechIni = DateEntry(frameDatos, width =8, background = "darkblue", foreground= 'white', borderwidth= 2)
fechIni.grid(row = 5, column = 1, padx = 4)
fechFin = DateEntry(frameDatos, width =8, background = "darkblue", foreground= 'white', borderwidth= 2)
fechFin.grid(row = 5, column = 2)

#-------------------------Pestaña tiempo---------------------------------
seleccionarProvincia = Label(frameTiempo, text = "Selecciona una provincia:")
seleccionarProvincia.grid(row = 0, column= 0,  sticky = "n", padx = 10, pady = 10)

#Lista desplegable provincias
prov.set(aemet.provincias[0])
menuDesplegable = OptionMenu(frameTiempo, prov,*aemet.provincias)
menuDesplegable.grid(row=0,column = 1, sticky = "n", padx = 10, pady = 10)

#Mostrar datos tiempo
textoTiempo = Text(frameTiempo, width= 70, height= 20)
textoTiempo.grid(row = 0, column = 2, sticky = "n", padx =10, pady=10,rowspan =10 )
#barra desplazamiento para cuadro de texto
scrollVert = Scrollbar(frameTiempo, command=textoTiempo.yview)#barra desplazamiento
scrollVert.grid(row=0, column=3, sticky = "nsew", rowspan =10)#tamaño barra ajustado a la ventana
textoTiempo.config(yscrollcommand= scrollVert.set)#la barra se posiciona en el texto

#Botones
#Boton para mostrar un resumen de los datos de la provincia    
botonProvincia = Button(frameTiempo, text= "Tiempo de hoy", command = aemet.resumenDia)
botonProvincia.grid(row=1,column=0, sticky = "w", padx=10, pady=5)

#Boton para mostrar información detallada de la provincia    
botonDetalle = Button(frameTiempo, text= "Tiempo 7 proximos dias", command = aemet.semanal)
botonDetalle.grid(row=2,column=0, sticky = "w", padx=10, pady=5)

raiz.mainloop()