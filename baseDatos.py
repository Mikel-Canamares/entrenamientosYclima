import sqlite3
from tkinter import messagebox
from datetime import datetime, date
from tkinter import INSERT, END
import ventana
import log
import traduccion

actividades = ["Todas" , "Correr" , "Bicicleta"]
   
def conectar():
    miConexion = sqlite3.connect("Deporte.db")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''CREATE TABLE ENTRENAMIENTOS(
            ID_ENTRENAMIENTO INTEGER PRIMARY KEY AUTOINCREMENT,
            FECHA DATE, 
            ACTIVIDAD VARCHAR (10), 
            TIEMPO NUMBER, 
            DISTANCIA NUMBER, 
            MEDIA NUMBER)
        ''') 
        messagebox.showinfo("BBDD", "Tabla de entrenamientos creada con éxito")
    except:
        messagebox.showwarning("Atención", "La tabla de entrenamientos ya existe")
   
def salir():
    decision = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if decision == "yes":
        ventana.raiz.destroy()

def limpiar():
    ventana.miTiempo.set("")
    ventana.miDistancia.set("")

def opcionDeporte():
    opcionDep = ventana.depOpcion.get()
    if opcionDep == 1:
        deporte = "Correr"
    elif opcionDep == 2:
        deporte = "Bicicleta"
    else:
        messagebox.showwarning("Atención", "Selecciona un tipo de actividad")  
    return deporte

def insertar():
    miConexion = sqlite3.connect("Deporte.db")
    miCursor = miConexion.cursor()
    if ventana.tiempoEntry.get() == "" or ventana.distanciaEntry.get() == "":
        messagebox.showwarning("Atención", "Completa todos los campos")
    try:
        distancia = float(ventana.distanciaEntry.get())
        tiempo = float(ventana.tiempoEntry.get())
    except ValueError:
        messagebox.showwarning("Atención", "Debes introducir datos numéricos")    
    else:
        media = (60 *(distancia / tiempo)).__round__(1)
        miCursor.execute(f"INSERT INTO ENTRENAMIENTOS VALUES (NULL, :fecha, :actividad, :tiempo, :distancia, :media)",
            {
                "fecha" : date.today(),
                "actividad": opcionDeporte(),
                "tiempo": tiempo,
                "distancia" : distancia,
                "media" : media
            }
            )
        miConexion.commit()
        miConexion.close
        messagebox.showinfo("","Los datos se han guardado correctamente")
        log.insertarActividad()

def buscarDeporte():
    ventana.textoDatos.delete("1.0", END)
    deporteBuscado = ventana.actividad.get()
    miConexion = sqlite3.connect("Deporte.db")
    miCursor = miConexion.cursor()
    if deporteBuscado == "Correr":
        miCursor.execute(f"SELECT * FROM ENTRENAMIENTOS WHERE ACTIVIDAD LIKE 'Correr' AND FECHA BETWEEN '{ventana.fechIni.get_date()}' AND '{ventana.fechFin.get_date()}'")
        log.consultarCorrer()
    elif deporteBuscado == "Bicicleta":
        miCursor.execute(f"SELECT * FROM ENTRENAMIENTOS WHERE ACTIVIDAD LIKE 'Bicicleta' AND FECHA BETWEEN '{ventana.fechIni.get_date()}' AND '{ventana.fechFin.get_date()}'")
        log.consultarBicicleta()
    else:
        miCursor.execute(f"SELECT * FROM ENTRENAMIENTOS WHERE FECHA BETWEEN '{ventana.fechIni.get_date()}' AND '{ventana.fechFin.get_date()}'")
        log.consultarTodos()
    datos = miCursor.fetchall()
    for entrenamiento in datos:
        ventana.textoDatos.insert(INSERT, f"Fecha:{entrenamiento[1]}\nActividad:{entrenamiento[2]}  Tiempo:{entrenamiento[3]} minutos  Distancia:{entrenamiento[4]}KM  Velocidad media:{entrenamiento[5]}KM/H\n\n")