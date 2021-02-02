import baseDatos
import aemet
import ventana
from datetime import datetime
from tkinter import INSERT

def ProvinciaHoy():
    fichero = open("log.txt", "a");
    texto = f"{datetime.now()} Se ha consultado el tiempo actual de {ventana.prov.get()}\n"
    fichero.write(texto);
    fichero.close();

def ProvinciaSemana():
    fichero = open("log.txt", "a");
    texto = f"{datetime.now()} Se ha consultado el tiempo para los proximos 7 dias de {ventana.prov.get()}\n"
    fichero.write(texto);
    fichero.close();

def insertarActividad():
    fichero = open("log.txt", "a");
    texto = f"{datetime.now()} Se han insertado estadisticas de {baseDatos.opcionDeporte()}\n"
    fichero.write(texto);
    fichero.close();

def consultarTodos():
    fichero = open("log.txt", "a");
    texto = f"{datetime.now()} Se han consultado todos los entrenamientos\n"
    fichero.write(texto);
    fichero.close();

def consultarCorrer():
    fichero = open("log.txt", "a");
    texto = f"{datetime.now()} Se han consultado todos los entrenamientos de correr\n"
    fichero.write(texto);
    fichero.close();

def consultarBicicleta():
    fichero = open("log.txt", "a");
    texto = f"{datetime.now()} Se han consultado los entrenamientos de bicicleta\n"
    fichero.write(texto);
    fichero.close();

def leer():
    fichero = open("log.txt")
    linea = fichero.readline()
    texto = ""
    while linea != "":
        texto = texto + linea
        linea = fichero.readline()  
    fichero.close()
    ventana.textoTiempo.insert(INSERT, f"{texto}") 