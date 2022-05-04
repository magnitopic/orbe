from jinja2 import Undefined
import requests
import json


def getPetrolPrice(provincia, producto):
    peticion = requests.get("https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres")
    contenido = json.loads(peticion.content)
    listaEstaciones = contenido["ListaEESSPrecio"]
    provincia = provincia.upper()
    estacionBarata = {
        "precio": None,
        "direccion": None
    }

    for estacion in listaEstaciones:
        try:
            # API uses comas for decimals, god I hate this API
            producto = float(estacion[producto].replace(",", "."))
        except:
            pass
        else:
            if provincia == "ESPAÑA" or provincia == estacion["Provincia"]:                 # We cheeck that the province that we want is the 
                if estacionBarata["precio"] == None or producto < estacionBarata["precio"]:
                    estacionBarata["precio"] = producto
                    estacionBarata["direccion"] = f'{estacion["Localidad"]} {estacion["Provincia"]} {estacion["Dirección"]}'

    return estacionBarata


def getProvincias():
    file = open("./api/provincias.json", "r", encoding="utf-8")
    provincias = file.read()
    # print(provincias)
    provincias = provincias.strip("[\"")
    provincias = provincias.strip("\"]")
    provincias = provincias.split('", "')
    file.close()
    return provincias


def getCombustibles():
    file = open("./api/combustibles.json", "r", encoding="utf-8")
    combustibles = file.read()
    # print(combustibles)
    combustibles = combustibles.strip("[\"")
    combustibles = combustibles.strip("\"]")
    combustibles = combustibles.split('", "')
    file.close()
    return combustibles


def generateProvincias(peticion):
    provincias = ["ESPAÑA"]
    contenido = json.loads(peticion.content)
    listaEstaciones = contenido["ListaEESSPrecio"]
    for estacion in listaEstaciones:
        if estacion["Provincia"] not in provincias:
            provincias.append(estacion["Provincia"])
    f = open("./api/provincias.json", "w")
    f.write(str(provincias).replace("'", '"'))
    f.close()


def generateCombustible(peticion):
    combustibles = []
    contenido = json.loads(peticion.content)
    listaEstaciones = contenido["ListaEESSPrecio"]
    for estacion in listaEstaciones:
        for i in estacion:
            if "Precio " in i and i not in combustibles:
                combustibles.append(i)
    f = open("./api/combustibles.json", "w")
    f.write(str(combustibles).replace("'", '"'))
    f.close()


if __name__ == "__main__":
    peticion = requests.get(
        "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres")
    generateProvincias(peticion)
    generateCombustible(peticion)
