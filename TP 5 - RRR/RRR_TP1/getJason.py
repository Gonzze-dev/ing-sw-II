# Compiled at: 2022-06-14 16:15:55
import sys
import json
import os

version = "{0.1}"
jsonName = "\sitedata.json"
arg = sys.argv

def printToken(sToken, dic):
    if tk == 'token 1':
        print version + obj["token1"]
    elif tk == 'token 2':
        print version + obj["token2"]
    else:
        print "el token " + tk + " no existe"

if len(arg) == 1:

    try:
        pathEjecutable = os.getcwd()
        jsonfile = pathEjecutable + jsonName

        with open(jsonfile, 'r') as (myfile):
            data = myfile.read()
    except:
        print "Ups, hubo un error al intentar abrir el archivo sitedata.json"

    try:
        obj = json.loads(data)
    except:
        print "Error, no se pudieron cargar los datos " + jsonName + "\sitedata.json"
    
    tk = raw_input("Ingrese el token: ")

    try:
        printToken(tk, obj)
    except:
        print "ups, hubo un error al intentar mostrar el token"

elif arg[1] in ["-h", "--help"]:
    print "Ejemplo de uso"
    print "Ingrese el token: token 1"
    print version + "XXXX-XXXX-XXXX-XXXX"

    print ""
    print "El archivo json 'sitedata.json' debera encontrarse en la misma carpeta de este mismo programa"
    print "En caso de no encontrarse este archivo, o de que haya algun error al intentar abrirlo aparecera el siguiente mensaje"
    print "Ups, hubo un error al intentar abrir el archivo sitedata.json"

    print ""
    print "Si al cargar los datos del json, estan en un formato que no corresponda, o de cualquier otro error respecto a esto se mostrara el siguiente mensaje"
    print "Error, no se pudieron cargar los datos de " + jsonName

    print ""
    print "printToken recibe los siguiente argumentos printToken(token, json)"
    print "La funcion 'printToken' imprime un token especificado, si este no esta imprimira el siguiente mensaje"
    print "el token " + "'token ingresado por el usuario'" + " no existe"

