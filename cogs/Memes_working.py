import discord 
from discord.ext import commands
import random
import os
import json
from support_classes import *

#This cog allows us to show memes from the bot, using a MySQL database and a config file
class Memes_working(commands.Cog):
    def __init__(self, client: commands.Bot):


        #Initialize all we need, the config file, the curiositys numbers for choosing, the database and the cursor
        self.client = client
        self.pathfile = os.path.join(r"C:\Users\wearethewarriors\Downloads\Proyectos_personales\Bot de curiosidades\discord music bot\cogs", "config.json")
        with open(self.pathfile, "r") as file:
            self.config = json.load(file)
        self.cu = self.config["values_choose"]["curiosidades"]
        self.chistes = self.config["values_choose"]["chistes"]
        self.db = PooledDB()
        


    #Command for show a meme, getting the channel who is called the command, choosing a number and getting the path from a MySQL database
    @commands.command()
    async def meme(self, ctx):

        try:

            channel = ctx.message.channel
            choose = random.randint(self.cu["min"], self.cu["max"])


            request, parameters = "select memepath from memepaths where id = (%s);", (choose,)
            result = self.db.makeRequest(request=request, parameters=parameters)
            

            meme = os.path.join(self.config["paths_memes"], result[0])
            await channel.send(file=discord.File(meme))

        except Exception as e:
            print(e)



    #This command sends a black humor joke, choosing a number and getting the path from a MySQL database
    @commands.command()
    async def chistenegro(self, ctx):
        choose = random.randint(self.chistes["min"], self.chistes["max"])

        request, parameters = "select chiste from chistesnegros where id = (%s);", (choose,)
        result = self.db.makeRequest(request=request, parameters=parameters)

        answer = Crear_Respuesta(f"{result[0]}", None)
        await ctx.reply(embed=answer.enviar)



#This is the setup for loading the cog in the bot    
async def setup(client: commands.Bot) -> None:
    await client.add_cog(Memes_working(client))






        

    


        



    
        