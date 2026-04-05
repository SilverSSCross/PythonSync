import sys
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
        #Comprueba si es un .exe o por linea de comandos
        if getattr(sys, 'frozen', False):
        # Ejecutando como .exe empaquetado
            exe_dir = Path(sys.executable).parent
        else:
    # Ejecutando como script Python
            exe_dir = Path(__file__).resolve().parent
        
        find_config = exe_dir / 'config.ini'

        config = ConfigObj(str(find_config), encoding='UTF8')
        #Saca la parte izquierda de las variables en config.ini
        self.namelist = list(config["Remote_variables"].keys())
        #Saca las variables en config.ini
        self.values = [config["Remote_variables"][key] for key in self.namelist]