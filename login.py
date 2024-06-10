from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from database import Data
import sv_ttk


IMG="plhd.png"
WIN_SIZE="350x365"
TITLE="Backlog"
BGCOLOR = "#68838B"

class Login():
    def __init__(self) -> None:
        self.loginScreen = Tk()
        self.loginScreen.title(TITLE)
        self.loginScreen.geometry(WIN_SIZE)
        self.loginScreen.resizable(False,False)
        self.logged:bool = False
        sv_ttk.set_theme("dark")

        self.img_path = Image.open(IMG)
        self.logo = ImageTk.PhotoImage(self.img_path)
        self.programLogo = Label(image=self.logo, width=350, height=80)
        self.programLogo.grid(row=0, pady=25)

        userLabel = Label(self.loginScreen, text="Username: ")
        userLabel.grid(row=1)
        self.userName = ttk.Entry(self.loginScreen, width=28)
        self.userName.grid(row=2, pady=(0,5))

        passwordLabel = Label(self.loginScreen, text="Password: ")
        passwordLabel.grid(row=3)
        self.password = ttk.Entry(self.loginScreen, show="*", width=28)
        self.password.grid(row=4, pady=(0,5))

        resetPass = Label(self.loginScreen, text="Forgot password", foreground= "gray", cursor="hand2")
        resetPass.grid(row=5)
        resetPass.bind("<Button-1>",self.passwordReset)

        loginButton = ttk.Button(self.loginScreen, text="Login", cursor="hand2", width=15, command=lambda: self.loginUser(self.password.get().strip(),self.userName.get().strip()))
        loginButton.grid(row=6, pady=(25,2))

        createAccountButton = ttk.Button(self.loginScreen, text="Register", cursor="hand2", width=15, command=Register)
        createAccountButton.grid(row=7)

    def loginUser(self, password:str, username:str) -> None:
        data = Data(username,username,password)
        data.login()
        if data.logged:
            self.loginScreen.destroy()
            self.logged = True

    def passwordReset(self,event=None) -> str:
        return print(":(")

    def run(self) -> None:
        self.loginScreen.mainloop()


class Register():
    def __init__(self) -> None:
        self.registerScreen = Toplevel()
        self.registerScreen.title("Register Account")
        self.registerScreen.geometry(WIN_SIZE)
        self.registerScreen.grab_set()
        self.registerScreen.resizable(False,False)

        self.img = Image.open(IMG)
        self.logo = ImageTk.PhotoImage(self.img)
        self.rLbl = Label(self.registerScreen, image=self.logo, width=350, height=80)
        self.rLbl.grid(row=0, columnspan=2, pady=(0,15))

        emailLabel = ttk.Label(self.registerScreen,text="       Email:").grid(column=0, row=1)
        self.email = ttk.Entry(self.registerScreen, width=28)
        self.email.grid(column=1,row=1)

        regUserLabel = ttk.Label(self.registerScreen, text="Username:").grid(column=0, row=2, padx=10, pady=10)
        self.regUser = ttk.Entry(self.registerScreen, width=28)
        self.regUser.grid(column=1, row=2, padx=10, pady=10)

        regPassLabel = ttk.Label(self.registerScreen, text=" Password:").grid(column=0, row=3)
        self.regPass = ttk.Entry(self.registerScreen, width=28)
        self.regPass.grid(column=1, row=3)

        createBtn = ttk.Button(self.registerScreen, text="Create Account", cursor="hand2", width=15, command=self.registerUser)
        createBtn.grid(row=4, pady=20, columnspan=2)

    def registerUser(self) -> None:
        if self.email.get() == "" or self.regUser.get() == "" or self.regPass.get() == "":
            return print("Empty Fields")
        data = Data(self.email.get(),self.regUser.get(),self.regPass.get())
        data.register()
        self.registerScreen.destroy()
        


if __name__ == "__main__":
    app = Login()
    app.run()
