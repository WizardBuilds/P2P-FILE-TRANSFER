import os
from UI.home import home_menu
from UI.sendui import send_ui
from UI.receiveui import receive_ui
os.makedirs("files/shared_files",exist_ok=True)
os.makedirs("files/received_files",exist_ok=True)
def clear():
    os.system("cls")# it is only made for window
def main():
    while True:
        clear()
        choice=home_menu()
        if choice=="1":
            send_ui()
            input("\n press Enter to continue..")
        elif choice=="2":
            receive_ui()
            input("\n press Enter to continue..")
        elif choice=="q":
            break
if __name__=="__main__":
    main()
            
 
