import os
from core import RemoteToPc
from core import PcToRemote

class MainCLI:
    
    def __init__(self):
        self.menus = ["1", "2", "3", "4"]
        self.running = True
        os.system("color 0A")
        from cli import ConfigSubCli
        self.subcli=ConfigSubCli()
        self.pctoremote=PcToRemote()
        self.remotetopc=RemoteToPc()

    def show_menu(self):
        print()
        print(" =========================")
        print(" USB SYSTEM SINCRONITATION")
        print(" =========================")
        print()
        print(" 1) Synchronize Local to external")
        print(" 2) Synchronize external to Local")
        print(" 3) Configuration")
        print(" 4) Exit")
        print()
        print(" Select an option [1-4]:", end="")

    def handle_option(self, option):
        match option:
            case "1":
                self.pctoremote.run()
            case "2":
                self.remotetopc.run()
            case "3":
                self.subcli.run()
            case "4":
                print("Exiting the program. Goodbye!")
                self.running = False

    def run(self):
        while self.running:
            self.show_menu()
            option = input().strip()

            if option == "":
                print("No input provided. Please enter a valid option.")
                continue

            if option not in self.menus:
                print("Invalid option. Please select a valid option from the menu.")
                continue

            self.handle_option(option)


# --- Punto de entrada ---
if __name__ == "__main__":
    app = MainCLI()
    app.run()