import mysql.connector

class DataBase:
    
    def CreatDatabase(self, title):
        mydb = mysql.connector.connect(host="localhost", user="root", password="password")
        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE DATABASE {title.lower()}")
