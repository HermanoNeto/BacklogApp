import mysql.connector

"""
RUN THIS FILE ONLY ONCE REMEMBER TO CHANGE THE INFO ON EACH STEP WITH YOUR OWN
"""

def firstStep():
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      password="yourpassword"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE backlog_database")

def secondStep():
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      password="yourpassword",
      database="backlog_database"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE user_register (email VARCHAR(55), username VARCHAR(55), password VARCHAR(55)")


if __name__ == "__main__":
    firstStep()
    secondStep()


