from config import IniConfig

class ConfigSubCli:
    def __init__(self):
        self.menus=["1", "9"]
        self.running = True
        self.initialconf=IniConfig

    
    def show_menu(self):
        print("Configuration Menu")
        print("1) Set max remote variables")
        print("9) Back to main menu")
        print("Select an option :", end="")
    
    
    def handle_option(self, option):
        match option:
                case "1":
                    quantity = input("Enter the number of remote directories to set: ").strip()
                    if not quantity.isdigit():
                        print("Please enter a valid number.")                    
                    self.initialconf.addvariables(int(quantity))
                    self.initialconf.erasevariables(int(quantity))
                    print(f"Remote directories set to {quantity}.")
                case "9":
                    print("Returning to main menu.")
                    self.running = False
        
    
    def run(self):
        while self.running:
            self.show_menu
            
            option = input().strip()
            if option == "":
                print("No input provided. Please enter a valid option.")
                continue
            if option not in self.menus:
                print("Invalid option. Please select a valid option from the menu.")
                continue
            self.handle_option(option)