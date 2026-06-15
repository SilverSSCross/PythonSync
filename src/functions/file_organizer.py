from  pathlib import Path
import glob
import datetime

def move_files(origin_directory, destiny_directory, file_extension):
    
    #Creates the search pattern
    pattern = Path(origin_directory) / f"*.{file_extension}"
    #Returns a list of the files with the pattern
    files=glob.glob(str(pattern))
    
    for file in files:
        file_path=Path(file)
        file_name=file_path.name
        destiny_path= Path(destiny_directory) /file_name
        
        try:
            file_path.move(destiny_path)
            print(f"Moved {file_name} to {destiny_directory}")
        except Exception as e:
            #Error report
            print(f"Error moving {file_name}: {e}")
            
        

def copy_files(origin_directory, destiny_directory, file_extension):
    #Keep track of copied files
    copied_files=[]
    
    #Creates the search pattern
    pattern = Path(origin_directory) / f"*.{file_extension}"
    #Returns a list of the files with the pattern
    files=glob.glob(str(pattern))

    for file in files:
        file_path=Path(file)
        file_name=file_path.name

        #Turning both paths from str to Path
        origin_file_path=Path(origin_directory) / file_name
        destiny_path=Path(destiny_directory) / file_name

        #Taking the stats of both
        origin_info=origin_file_path.stat()
        modify_origin=datetime.datetime.fromtimestamp(origin_info.st_mtime)

        try:
            #Try to take destiny data in a 'try' because it can, not exist    
            destiny_info=destiny_path.stat()
            modify_destiny=datetime.datetime.fromtimestamp(destiny_info.st_mtime)
        except FileNotFoundError:
            modify_destiny=None
            print(f"Doesn't exist")
        
        if not destiny_path.exists() or modify_origin>modify_destiny:
            try:
                origin_file_path.copy_into(str(destiny_directory))
                print(f"Copied {file_name} to {destiny_directory}")
                copied_files.append(file_name)
            except Exception as e:
                #Error report
                print (f"Error to copy {file_name}")
                print(e)
        
        else:
            print("=====")
            print(f"{file_name} already exist on {destiny_directory}")
            print("=====")
        
    return copied_files


def delete_files(origin_directory, destiny_directory, file_extension):
    #List for the deleted files
    deleted_files=[]

    #Creates the search pattern
    pattern = Path(destiny_directory) / f"*.{file_extension}"
    #Returns a list of the files with the pattern
    files=glob.glob(str(pattern))

    for file in files:
        file_path=Path(file)
        file_name=file_path.name

        #Turning both paths from str to Path
        origin_file_path=Path(origin_directory) / file_name
        destiny_path=Path(destiny_directory) / file_name

        if not origin_file_path.exists():
            try:
                destiny_path.unlink()
                print(f"Deleted {file_name} from {destiny_directory}")
                deleted_files.append(file_name)
            except FileNotFoundError as FNF:
                print("File was already deleted")
    
    return deleted_files
