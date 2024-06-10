import mysql.connector
from tkinter import messagebox

HOST="localhost"
USER="YOUR MYSQL USER"
PASS="YOUR MYSQL PASSWORD"
DATABASE="backlog_database"

class Data():
    def __init__(self,email:str,user:str,passw:str) -> None:
        self.acc_database:dict = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASS,
            database=DATABASE
            )
        self.mycursor = self.acc_database.cursor()
        self.email=email
        self.user=user
        self.passw=passw
        self.logged:bool = False

    def login(self) -> None:
        self.mycursor.execute("SELECT email, username, password FROM user_register")
        self.myresult = self.mycursor.fetchall()

        for x in self.myresult:
            if self.email == x[0] or self.user == x[1]:
                if self.passw == x[2]:
                    self.logged = True
                    return
                else:
                    messagebox.showerror(title="Error",message="Incorrect Password!")
                    return
        messagebox.showerror(
            title="Could not find your account",
            message=f"No account associated with this username"
            )

    def register(self) -> None:
        self.mycursor.execute("SELECT * FROM user_register")
        self.myresult = self.mycursor.fetchall()

        for x in self.myresult:
            if self.email == x[0] or self.user == x[1] :
                messagebox.showerror(
                    title="User already registered",
                    message=f"Username or Email already taken"
                    )
                return
        sql:str = "INSERT INTO user_register (email, username, password) VALUES (%s, %s, %s)"
        value:tuple = (self.email, self.user, self.passw)
        self.mycursor.execute(sql, value)
        self.acc_database.commit()
        print(self.mycursor.rowcount, "record inserted.")

if __name__ == "__main__":
    app = Data("test@gmail.com", "test", "test321")
    app.login()
