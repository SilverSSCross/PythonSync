from core import pctoremote, remotetopc
from config import ini_checker
def sync_menu():
    print()
    print(" =========================")
    print(" USB SYSTEM SINCRONITATION")
    print(" =========================")
    print()
    print(" 1) Synchronize Local to external")
    print(" 2) Synchronize external to Local")
    print(" 3) Go Back")
    print()
    print(" Select an option [1-3]:", end="")
    

def pick_option():
    option=input().strip()
    
    if option.isdigit():
        return int(option)
    else:
        print("Enter a valid number")


def handle_option():
    selected_option=pick_option()
    match selected_option:
        case 1:
            pctoremote.pctoremote_function(ini_checker.find_iniconfig())   
            return True    
        case 2:
            remotetopc.remotetopc_funciton(ini_checker.find_iniconfig())
            return True 
        case 3:
            return False
        case _:
            print("Invalid Option")
            return True


def main_func():
    running=True
    while running:
        sync_menu()
        running=handle_option()