import discord
import pymysql
import tkinter.messagebox as messagebox
import os 
import json

#Class for connect to a MySQL database
class DB_pymysql():
    def __init__(self):

        #Initialize all we need, config file, and the connection object
        self.path_file = os.path.join(r"C:\Users\wearethewarriors\Downloads\Proyectos_personales\Bot de curiosidades\discord music bot\cogs", "config.json")
        self.file = open(self.path_file, "r")
        self.config = json.load(self.file)
        self.connection = self.conn()

    #Function that returns the connection object using the config file 
    def conn(self):
        try:
            conn = pymysql.connect(host=self.config["host"],
                        port=self.config["port"],
                        user=self.config["user"],
                        password=self.config["password"],
                        database=self.config["database"])
            return conn

        except Exception as e:
            messagebox.showerror("Error al conectar a MySQL", e)

    #Returns a cursor object
    def cur(self):
        return self.connection.cursor()
    
    #Commits things like inserts, updates, etc
    def comm(self):
        self.connection.commit()

