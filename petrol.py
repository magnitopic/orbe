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


def getStructure():
    peticion = requests.get(
        "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres")
    contenido = json.loads(peticion.content)
    listaEstaciones = contenido["ListaEESSPrecio"]
    


if __name__ == "__main__":
    getStructure()
