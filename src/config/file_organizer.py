import shutil
import os
import glob
import datetime 
class FileOrganize:

    def move_file(origin_directory, destiny_directory, file_extension):
        
        pattern = os.path.join(origin_directory, f"*.{file_extension}")
        
        
        files = glob.glob(pattern)
        
        for file in files:
            file_name = os.path.basename(file)
            destiny_path = os.path.join(destiny_directory, file_name)
            
            
            try:
                shutil.move(file, destiny_path)
                print(f"Moved {file_name} to {destiny_directory}")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")
                


        

    def copy_files(origin_directory, destiny_directory, file_extension, divider):    

        # List to keep track of copied files
        copied_files = []

        
        pattern = os.path.join(origin_directory, f"*.{file_extension}")    
        files = glob.glob(pattern)

        if divider == 1:
            #For each file in files it makes the path
            for file in files:
                file_name = os.path.basename(file)
                destiny_path = os.path.join(destiny_directory, file_name)

                origin_file_path = os.path.join(origin_directory, file_name)
                destiny_file_path = os.path.join(destiny_directory, file_name)
                #Gets the date from the 'modified' section on the file from both folders
                try:            
                    modifyOrigin = datetime.datetime.fromtimestamp(os.path.getmtime(origin_file_path))
                    modifyDestiny = datetime.datetime.fromtimestamp(os.path.getmtime(destiny_file_path))
                except FileNotFoundError:
                    #For the code to get at this file there HAS to be a file and with that it comes a timestamp
                    modifyDestiny=None    
                #If the file doesnt exist on destiny or the modified time on the original file is newer to the one on destiny it copies it
                if not os.path.exists(destiny_file_path) or modifyOrigin > modifyDestiny:
                    try:
                        #Using the name and the path it copies the file to the folder
                        shutil.copy(file, destiny_path)
                        print(f"Copied {file_name} to {destiny_directory}")
                        #Saves the name on a list to add it later to the log
                        copied_files.append(file_name)
                    except Exception as e:
                        print(f"Error copying {file_name}: {e}")
                else:
                    print(f"{file_name} already exists in {destiny_directory}, skipping copy.")

        else:
            #Basicaly the same but on reverse
            for file in files:
                file_name = os.path.basename(file)
                destiny_path = os.path.join(destiny_directory, file_name)

                destiny_file_path = os.path.join(destiny_directory, file_name)

                # Checks the files inside "files" list are not present in destiny_directory
            
                if not os.path.exists(destiny_file_path):
                    try:
                        shutil.copy(file, destiny_path)
                        print(f"Copied {file_name} to {destiny_directory}")

                        copied_files.append(file_name)
                    except Exception as e:
                        print(f"Error copying {file_name}: {e}")
                else:
                    print(f"{file_name} already exists in {destiny_directory}, skipping copy.")

        return copied_files



    def delete_files(directory_origin, directory_destiny, file_extension):
        # List to keep track of deleted files
        deleted_files = []
        # Deletes files from directory_destiny that are not present in directory_origin
        pattern = os.path.join(directory_destiny, f"*.{file_extension}")
        files_destiny = glob.glob(pattern)
        for file in files_destiny:
            file_name = os.path.basename(file)
            origin_file_path = os.path.join(directory_origin, file_name)
            
            if not os.path.exists(origin_file_path):
                try:
                    os.remove(file)
                    print(f"Deleted {file_name} from {directory_destiny}")
                    deleted_files.append(file_name)
                except Exception as e:
                    print(f"Error deleting {file_name}: {e}")
        return deleted_files