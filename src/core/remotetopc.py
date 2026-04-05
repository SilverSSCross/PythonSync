import os
from core import SyncBase

class RemoteToPc(SyncBase):

    def remotetopcfunction(self):
        
        #! Copy files from remote1 to localdirectory
        for directory in self.values:

            if os.path.exists(directory):
                list_copyfiles = self.fileorganize.copy_files(directory, self.localdirectory, "mp3", 1)
                list_deletefiles = self.fileorganize.delete_files(directory, self.localdirectory, "mp3")

                # Log the copied and deleted files
                self.logmanagement.file_write(list_copyfiles, list_deletefiles, self.localdirectory)
            else:
                print(f"Remote directory {directory} does not exist. Skipping copy operation.")

    def run(self):
        self.getData()
        self.remotetopcfunction()