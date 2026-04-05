from configobj import ConfigObj
from pathlib import Path
import sys

class IniConfig:
    def __init__(self):
        exe_dir = Path(sys.executable).parent
        find_config = exe_dir / 'config.ini'
        self.config = ConfigObj(str(find_config), encoding='UTF8') #Already reads the file
        



    def addvariables(self, num_external): # Marks the max number if variables that has to exist
        namelist = list(self.config["Remote_variables"].keys())
        
        for i in range(num_external):
            var_name = f"remotedirectory{i+1}"
        
        if var_name not in namelist:
            self.config["Remote_variables"][var_name] = None
        
        self.config.write()    
        

    def erasevariables(self, num_external): # Marks the max number if variables that has to exist
        namelist = list(self.config["Remote_variables"].keys())
        
        # Goes backwards till we have the right amount of variables
        for i in range(len(namelist), (num_external-1), -1): 
            var_name = f"remotedirectory{i+1}"
        
        if var_name in namelist:
            del self.config["Remote_variables"][var_name]
        
        self.config.write()
        



