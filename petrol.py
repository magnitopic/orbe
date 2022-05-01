import requests
import json


def getPetrolPrice(provincia, producto):
    peticion = requests.get(
        "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres")
    contenido = json.loads(peticion.content)
    listaEstaciones = contenido["ListaEESSPrecio"]

    # inicializamos un diccionario. Buscamos la estación de precio menor
    estacionBarata = {}
    for estacion in listaEstaciones:
        if provincia == "España":                       # Se escribe en capitalize
            # no todas las gasolineras tienen Biodiesel, por ejemplo, asi las quitamos
            if estacion[producto] != "":
                if estacionBarata == {}:
                    estacionBarata = estacion
                else:
                    if estacion[producto] < estacionBarata[producto]:
                        estacionBarata = estacion
        # filtramos por provincia
        elif provincia.upper() == estacion["Provincia"]:
            if estacion[producto] != "":
                if estacionBarata == {}:
                    estacionBarata = estacion
                else:
                    if estacion[producto] < estacionBarata[producto]:
                        estacionBarata = estacion

    return estacionBarata[producto]


def getProvincias():
    provincias = []
    peticion = requests.get(
        "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres")
    contenido = json.loads(peticion.content)
    listaEstaciones = contenido["ListaEESSPrecio"]
    for estacion in listaEstaciones:
        if estacion["Provincia"] not in provincias:
            provincias.append(estacion["Provincia"])
    return provincias


def generateProvincias():
    provincias = []
    peticion = requests.get(
        "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres")
    contenido = json.loads(peticion.content)
    listaEstaciones = contenido["ListaEESSPrecio"]
    for estacion in listaEstaciones:
        if estacion["Provincia"] not in provincias:
            provincias.append(estacion["Provincia"])
    print(provincias)
    f = open("./api/provincias.json", "a")
    f.write(str(provincias))
    f.close()


if __name__ == "__main__":
    generateProvincias()
