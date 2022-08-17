from SingletonMeta import SingletonMeta
import json

class SingletonGetJson(metaclass=SingletonMeta):

    fileName = "sitedata"
    jsonFile = ".\sitedata.json"
    data = None
    obj = None

    def getJasonToken(self):
        try:

            with open(self.jsonFile, 'r') as (myfile):
                self.data = myfile.read()
        except:
            print ("Ups, hubo un error al intentar abrir el archivo sitedata.json")

        try:
            self.obj = json.loads(self.data)
        except:
            print ("Error, no se pudieron cargar los datos " + cls.jsonFile + "\sitedata.json")


    def getToken(self, tk):
        if self.obj is None:
            self.getJasonToken()

        return self.obj[tk]