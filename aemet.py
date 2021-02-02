from tkinter import END, StringVar, INSERT
import json
import requests
from io import open
from datetime import datetime
from tiempo import tiempo
import ventana
import log

provincias = ["Alava","Albacete", "Alicante", "Almería", "Asturias", "Ávila", "Badajoz", "Islas Baleares", "Barcelona", "Bizkaia", "Burgos", "Cáceres", "Cádiz", "Cantabria", "Castellón", 
"Ceuta", "Ciudad Real", "Córdoba", "A Coruña", "Cuenca", "Girona", "Granada", "Guadalajara", "Gipuzkoa", "Huelva", "Huesca", "Jaén", "León", "Lleida", "Lugo", "Madrid", "Málaga", 
"Melilla", "Murcia", "Navarra", "Oursense", "Palencia", "Las Palmas", "Pontevedra", "La Rioja", "Salamanca", "Santa Cruz de Tenerife", "Segovia", "Sevilla", "Soria", "Tarragona",
 "Teruel", "Toledo", "Valencia", "Valladolid", "Zamora", "Zaragoza" ]

diccionarioProvincias= {"Alava": "01" ,"Albacete": "02", "Alicante":"03", "Almería":"04", "Asturias":"33", "Ávila":"05", "Badajoz":"06", "Islas Baleares":"07", "Barcelona":"08", "Bizkaia":"48", "Burgos":"09", 
"Cáceres":"10", "Cádiz":"11", "Cantabria":"39", "Castellón":"12", "Ceuta":"51", "Ciudad Real":"13", "Córdoba":"14", "A Coruña":"15", "Cuenca":"16", "Girona":"17", "Granada":"18", "Guadalajara":"19", 
"Gipuzkoa":"20", "Huelva":"21", "Huesca":"22", "Jaén":"23", "León":"24", "Lleida":"25", "Lugo":"27", "Madrid":"28", "Málaga":"29", "Melilla":"52", "Murcia":"30", "Navarra":"31", "Oursense":"32", "Palencia":"34",
"Las Palmas":"35", "Pontevedra":"36", "La Rioja":"26", "Salamanca":"37", "Santa Cruz de Tenerife":"38", "Segovia":"40", "Sevilla":"41", "Soria":"42", "Tarragona":"43","Teruel":"44", "Toledo":"45", 
"Valencia":"46", "Valladolid":"47", "Zamora":"49", "Zaragoza":"50"}

diccionarioCodigos = {"Alava": "01059" ,"Albacete": "02003", "Alicante":"03014", "Almería":"04013", "Asturias":"33044", "Ávila":"05019", "Badajoz":"06015", "Islas Baleares":"07040", "Barcelona":"08019", 
"Bizkaia":"48020", "Burgos":"09059", "Cáceres":"10037", "Cádiz":"11012", "Cantabria":"39075", "Castellón":"12040", "Ceuta":"51001", "Ciudad Real":"13034", "Córdoba":"14021", "A Coruña":"15030", "Cuenca":"16078", 
"Girona":"17079", "Granada":"18087", "Guadalajara":"19130", "Gipuzkoa":"20069", "Huelva":"21041", "Huesca":"22125", "Jaén":"23050", "León":"24089", "Lleida":"25120", "Lugo":"27028", "Madrid":"28079", "Málaga":"29067", 
"Melilla":"52001", "Murcia":"30030", "Navarra":"31201", "Oursense":"32054", "Palencia":"34120","Las Palmas":"35016", "Pontevedra":"36038", "La Rioja":"26089", "Salamanca":"37274", "Santa Cruz de Tenerife":"38038", 
"Segovia":"40194", "Sevilla":"41091", "Soria":"42173", "Tarragona":"43148","Teruel":"44216", "Toledo":"45168", "Valencia":"46250", "Valladolid":"47168", "Zamora":"49275", "Zaragoza":"50297"}

def resumenDia ():
    ventana.textoTiempo.delete("1.0", END)
    prov = ventana.prov.get() 
    if prov in diccionarioProvincias:
        codProvincia = diccionarioProvincias[prov] 
        url = f"https://opendata.aemet.es/opendata/api/prediccion/provincia/hoy/{codProvincia}" 
        querystring = {"api_key":"INSERTAR AQUI LA CLAVE DE LA API PROPORCIONADA POR AEMET"}
        response = requests.request("GET", url,  params=querystring)
        respuesta_json = json.loads(response.text)
        datos = respuesta_json["datos"]
        url2 = datos
        respuesta = requests.request("GET", url2,  params=querystring)
        ventana.textoTiempo.insert(INSERT, f"{respuesta.text}")
        log.ProvinciaHoy()
   
def semanal ():
    ventana.textoTiempo.delete("1.0", END)
    prov = ventana.prov.get() 
    if prov in diccionarioCodigos:
        codProvincia =  diccionarioCodigos[prov]
        url = f"https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{codProvincia}" 
        querystring = {"api_key":"INSERTAR AQUI LA CLAVE DE LA API PROPORCIONADA POR AEMET"}
        response = requests.request("GET", url, params=querystring)
        respuesta_json = json.loads(response.text)
        datos = respuesta_json["datos"]
        url2 = datos
        respuesta2 = requests.request("GET", url2, params=querystring)
        respuesta_json2 = json.loads(respuesta2.text)
        texto = ""
        lista = []
        for i in range(0,7): 
            fechas = respuesta_json2[0]["prediccion"]["dia"][i]["fecha"]
            minimas = respuesta_json2[0]["prediccion"]["dia"][i]["temperatura"]["minima"]
            maximas = respuesta_json2[0]["prediccion"]["dia"][i]["temperatura"]["maxima"]
            precipitacion = respuesta_json2[0]["prediccion"]["dia"][i]["probPrecipitacion"][0]["value"]
            cielo = respuesta_json2[0]["prediccion"]["dia"][i]["estadoCielo"][0]["descripcion"]
            humedadMax = respuesta_json2[0]["prediccion"]["dia"][i]["humedadRelativa"]["maxima"]
            humedadMin = respuesta_json2[0]["prediccion"]["dia"][i]["humedadRelativa"]["minima"]
            data = tiempo(fechas, minimas, maximas, precipitacion, cielo, humedadMax, humedadMin)
            lista.append(data)
        for objeto in lista:
            texto = texto +  str(objeto) + "\n"
        ventana.textoTiempo.insert(INSERT, f"{texto}")
        log.ProvinciaSemana()
           
           


 