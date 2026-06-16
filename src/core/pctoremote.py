from pathlib import Path
from file_functions import file_organizer
from config import logfile_management

def pctoremote_function(config_file):
    #Takes the name of variables on config.ini
    namelist=list(config_file["Remote_variables"].keys())
    
    values=[config_file["Remote_variables"][key] for key in namelist]

    try:
        local_variables_config=config_file.get("Local_variables",{})
        newtolocal=local_variables_config.get("newtolocal","")
        local_directory=local_variables_config.get("localdirectory","")
    except Exception as e:
        print("Configuration file 'config.ini' not found or invalid. Please errase it and open the program again.")
        print(e)
    finally:
        if not newtolocal:
            print("No route detected for 'New to local'")
        if not local_directory:
            print("No route detected for 'Local directory'")
    
    print(values)

    #Moves from New_to_local to Local_directory
    try:
        file_organizer.move_files(newtolocal, local_directory, "mp3")
    
    except Exception as e:
        print(f"Error moving files from {newtolocal}:{e}")

    for directory in values:
        print(f"Proccessing {directory}")
        if not Path(directory).exists():
            print(f"Remote directory {directory} does not exist. Check the path and configuration")
        else:
            list_copied_files=file_organizer.copy_files(local_directory, directory, "mp3")
            list_deleted_files=file_organizer.delete_files(local_directory, directory, "mp3")
            if directory is None:
                logfile_management.log_creator(list_copied_files, list_deleted_files, directory)

