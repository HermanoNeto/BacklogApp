from tkinter import *
from login import Login
from database import Data

def main() -> None:
    login = Login()
    login.run()

    if login.logged:
        appWindow = Tk()
        appWindow.state('zoomed')

        
        appWindow.mainloop()

if __name__ == "__main__":
    main()
