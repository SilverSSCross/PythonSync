from pathlib import Path
import datetime

def check_directory():
    directory_logs=Path(__file__).parents[1] / "logs"
    directory_logs.mkdir(exist_ok=True)
    return directory_logs


def log_creator(written_files, deleted_files, files_destination):
    #CREATES THE PATH FOR THE FILE OF THE DAY
    log_file = check_directory() / f"{datetime.date.today()}.txt"

    
    #if log_file.exists(): #Opens on append.
    #    pass #Should make it copy the actual contents and add them at the end prob
    #else:
    with open (log_file, "a", encoding="utf-8") as log:
            log.write("========================================\n")
            log.write(f"Log file for {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
            log.write(f"Moves to {files_destination}\n")
            log.write("---\n")

            for file in written_files:
                log.write(f"Copied: {file}\n")

            log.write("-----------")

            for file in deleted_files:
                log.write(f"Deleted: {file}\n")

            log.write("---\n")
            log.write(f"Total copied files: {len(written_files)}\n")
            log.write(f"Total deleted files: {len(deleted_files)}\n")
            log.write("========================================\n")
        