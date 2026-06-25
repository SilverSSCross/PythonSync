from cli import cli_options, cli_sync

def main_menu():
    print()
    print(" =========================")
    print(" USB SYSTEM SINCRONITATION")
    print(" =========================")
    print()
    print(" 1) Synchronize")
    print(" 2) Configuration")
    print(" 3) Exit")
    print()
    print(" Select an option :", end="")
    

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
            cli_sync.main_func()           
            return True
        case 2:
            cli_options.main()
            return True
        case 3:
            print("Exiting the program. Goodbye!")
            return False
        case _:
            print("Invalid Option")
            return True
        
def main():
    running=True
    while running:
        main_menu()
        running=handle_option()