import discord
import pymysql
import openai
import json
import os
import pymysqlpool


#This class allows us to show an answer with an discord embed 
class Crear_Respuesta():
        def __init__(self, title, content):
            self.title = title
            self.content = content

            self.respuesta = discord.Embed(
                title=self.title,
                description=self.content,
                colour=int("DC75FF", 16)
            )

        @property
        def enviar(self):
            return self.respuesta
        


#This class uses Open AI api to allow the users "talk" with the bot    
class RaidenTalk:
    def __init__(self):
        self.api_key = "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"

    #Function that takes a text provided by user, process it and returns the response
    def generate_text(self, message):
        text = " ".join(message)
        openai.api_key = self.api_key
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.3,
        max_tokens=150)

        return response.choices[0].text


#This class help us to have a pooled db to manage the possible multiple querys that user can do to the bot
class PooledDB:
    def __init__(self) -> None:
        self.pathfile = os.path.join(r"C:\Users\wearethewarriors\Downloads\Proyectos_personales\Bot de curiosidades\discord music bot\cogs", "config.json")
        with open(self.pathfile, "r") as file:
            self.config = json.load(file)
        self.connectionPool = self.getPool()


    def getPool(self):
        try:

            config={'host':self.config['host'], 'user':self.config['user'], 'password':self.config['password'], 'database':self.config['database'], 'autocommit':True}
            pool = pymysqlpool.ConnectionPool(size=5, maxsize=10, pre_create_num=5, name='Raiden _Pool', **config)  

            return pool
        
        except Exception as e:
            print(e)
        

    def makeRequest(self, request, parameters, modify_query=False):

        if modify_query:
            try:


                connection = self.connectionPool.get_connection(retry_num=3, retry_interval=0.5)
                with connection.cursor() as cursor:
                    cursor.execute(request, parameters)
                    connection.commit()
                connection.close()
    
            
            except Exception as e:
                print(e)


        else:
            try:

                connection = self.connectionPool.get_connection(retry_num=3, retry_interval=0.5)
                with connection.cursor() as cursor:
                    cursor.execute(request, parameters)
                    result = cursor.fetchone()
                connection.close()
                return result
            
            except Exception as e:
                print(e)


    
    



    
