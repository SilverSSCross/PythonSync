from config import ini_checker
def config_cli():
    print()
    print(" =========================")
    print(" USB SYSTEM SINCRONITATION")
    print(" =========================")
    print()
    print("Configuration Menu")
    print("1) Set max remote variables")
    print("9) Back to main menu")
    print("Select an option :", end="")
    
    

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
            inifile=ini_checker.find_iniconfig()
            quantity = input("Enter the number of remote directories to set: ").strip()
            if not quantity.isdigit():
                print("Please enter a valid number.")
            else:
                ini_checker.addvariables(int(quantity), inifile)
                ini_checker.erasevariables(int(quantity), inifile)
                print(f"Remote directories set to {quantity}.")
            return True         
        case 9:
            return False
        case _:
            print("Invalid Option")
            return True
        

def main():
    running=True
    while running:
        config_cli()
        running=handle_option()