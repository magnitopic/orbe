import requests
import json


def getPetrolPrice(province, producto):
    request = requests.get("https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres")
    content = json.loads(request.content)
    petrolStationList = content["ListaEESSPrecio"]
    province = province.upper()
    cheepStation = {
        "price": None,
        "direccion": None
    }

    for station in petrolStationList:
        try:
            # API uses comas for decimals, god I hate this API
            price = float(station[producto].replace(",", "."))
        except:
            pass
        else:
            # We cheeck that the province that we want is the
            if province == "ESPAÑA" or province == station["Provincia"]:
                if cheepStation["price"] == None or price < cheepStation["price"]:
                    cheepStation["price"] = price
                    cheepStation["direccion"] = f'{station["Localidad"]} {station["Provincia"]} {station["Dirección"]}'

    return cheepStation


def getProvinces():
    with open("./api/provinces.json") as f:
        provinces = json.load(f)
    return provinces


def getFuels():
    with open("./api/fuels.json") as f:
        fuels = json.load(f)
    return fuels


def generateProvincesList(source):
    # "España" is added since it isn't a province, it represents all of them country
    provinces = ["ESPAÑA"]
    content = json.loads(source.content)
    petrolStationList = content["ListaEESSPrecio"]
    for station in petrolStationList:
        if station["Provincia"] not in provinces:
            provinces.append(station["Provincia"])
    f = open("./api/provinces.json", "w")
    f.write(str(provinces).replace("'", '"'))
    f.close()


def generateFuelList(source):
    fuels = []
    content = json.loads(source.content)
    petrolStationList = content["ListaEESSPrecio"]
    for station in petrolStationList:
        for i in station:
            if "Precio " in i and i not in fuels:
                fuels.append(i)
    f = open("./api/fuels.json", "w")
    f.write(str(fuels).replace("'", '"'))
    f.close()


if __name__ == "__main__":
    source = requests.get("https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres")
    generateProvincesList(source)
    generateFuelList(source)
