from configobj import ConfigObj
from pathlib import Path
from config import FileOrganize
from config import LogManagement
#Clase Base para ambas
class SyncBase:
    def __init__(self):
            #Inicializa las clases
            self.fileorganize=FileOrganize()
            self.logmanagement=LogManagement()
            #! Variables
            #Directorios
            self.newtolocaldirectory = ""
            self.localdirectory = ""
            #Lista 
            self.namelist=[]
            self.values=[]
        
    def getData(self):
        #! Get list of paths
        #Esta linea esta buscando 1 por encima (en vez de buscar en 'core' busca en 'src')
        find_config = Path(__file__).resolve().parent / 'config.ini'

        config = ConfigObj(str(find_config), encoding='UTF8')
        #Saca la parte izquierda de las variables en config.ini
        self.namelist = list(config["Remote_variables"].keys())
        #Saca las variables en config.ini
        self.values = [config["Remote_variables"][key] for key in self.namelist]