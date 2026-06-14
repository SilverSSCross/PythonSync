from  pathlib import Path
import glob
import shutil


def move_files(origin_directory, destiny_directory, file_extension):
    
    #Creates the search pattern
    pattern = Path(origin_directory) / f"*.{file_extension}"
    #Returns a list of the files with the pattern
    files=glob.glob(str(pattern))
    
    for file in files:
        file_name=Path(file).name
        destiny_path=file_name / destiny_directory
        
        try:
            shutil.move(file, destiny_path)
            print(f"Moved {file_name} to {destiny_directory}")
        except Exception as e:
            print(f"Error moving {file_name}: {e}")
            
        

def copy_files(origin_directory, destiny_directory, file_extension):
    #Keep track of copied files
    copied_files=[]
    
    pass


def delete_files(origin_directory, destiny_directory, file_extension):
    pass