import pymongo
from pymongo import MongoClient
from pprint import pprint
import bson
import sys

#Se establece la conección con autenticación
#Cliente
client = MongoClient(
    "mongodb://localhost:27017/",
    username="admin",
    password="admin123",
    authSource="admin",
    authMechanism="SCRAM-SHA-256")
#Base de datos
db = client["unidadResidencialTB"]
#Tabla
habitante = db["habitante"].find( {"cedula":1107093927} )

#Bucar e imprimir
for busqueda in habitante:
    pprint(busqueda)
    #pprint(busqueda["fechaRegistro"])
