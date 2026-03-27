import os
from core import SyncBase

class PcToRemote(SyncBase):
    
    def run(self):
        self.getData()
        self.movenewtolocal()
        self.pctoremotefunction()
            
    def movenewtolocal(self):
        #! Move the files from newtolocaldirectory to localdirectory
        try:
            self.fileorganize.move_file(self.newtolocaldirectory, self.localdirectory, "mp3")
        except Exception as e:
            print(f"Error moving files from {self.newtolocaldirectory} to {self.localdirectory}: {e}")
    
    def pctoremotefunction(self):
        #! Copies files from localdirectory to remote directories.
        #! And deletes them from remote directories if they do not exist in localdirectory
        for directory in self.values:
            print(f"Processing remote directory: {directory}")
            # Checks if remote directories are available
            if not os.path.exists(directory):
                print(f"Remote directory {directory} does not exist. Please check the device and configuration.")
            else:
                list_copyfiles=self.fileorganize.copy_files(self.localdirectory, directory, "mp3", 1)
                list_deletefiles=self.fileorganize.delete_files(self.localdirectory, directory, "mp3")

                # Log the copied and deleted files
                self.logmanagement.file_write(list_copyfiles, list_deletefiles, directory)        
                
