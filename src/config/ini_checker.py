from pathlib import Path
from configobj import ConfigObj

#Here goes all functions

def add_inicontents():
    DEFAULT_CONFIG = {
    'Local_variables': {
        'newtolocal': '',
        'localdirectory': ''
    },
    'Remote_variables': {
        'remotedirectory1': '',
        'remotedirectory2': ''
    }
    }
    return DEFAULT_CONFIG

def find_iniconfig():
    #Creates the path for the .ini file
    exe_dir=Path(__file__).parents[1]
    find_config=exe_dir / 'config.ini'
    
    #Print route
    print(find_config)
    
    #Checks the file exist
    if not find_config.exists():
        #If not exist creates with default contents
        config = ConfigObj(encoding='UTF8')#Creates empty object
        config.filename = str(find_config) #Adds the route
        config.update(add_inicontents())#Adds the contents
        config.write() #This creates the file
        print("Create")
    else:
        #Else just reads it fine
        config = ConfigObj(str(find_config), encoding='UTF8')
        print("Reads")
    return config

def addvariables(numvariable, file_location):
    namelist=list(file_location["Remote_variables"].keys())
    
    for i in range(numvariable):
       var_name = f"remotedirectory{i+1}"
       
       if var_name not in namelist:
            file_location["Remote_variables"][var_name] = None
    
    file_location.write()  

def erasevariables(numvariable, file_location):
    namelist = list(file_location["Remote_variables"].keys())
    
    # Goes backwards till we have the right amount of variables
    for i in range(len(namelist), (numvariable-1), -1): 
       var_name = f"remotedirectory{i+1}"
       
       if var_name in namelist:
           del file_location["Remote_variables"][var_name]
    
    file_location.write()


#Here I execute what I want available when I import addvariable y erasevariable
