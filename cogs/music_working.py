import discord
from discord.ext import commands
import random
import json
from support_classes import *
import os



#This cog is for play music, pause it, resume it, play another song, and kick the bot of the voice channel
class music_working(commands.Cog):
    def __init__(self, client: commands.Bot):


        #Initialize all we need, the config file, the database, cursor and the music numbers for choosing
        self.pathfile = os.path.join(r"C:\Users\wearethewarriors\Downloads\Proyectos_personales\Bot de curiosidades\discord music bot\cogs", "config.json")
        with open(self.pathfile, "r") as file:
            self.config = json.load(file)
        self.db = PooledDB()
        self.client = client
        self.music = self.config["values_choose"]["musica"]



    async def getMusic(self):
        """
        This function doesn't need any parameters,
        just returns a random song from the database, we also close and open the connectiom
        to the database
        """
        choose = random.randint(self.music["min"], self.music["max"])

        request, parameters = "select musicpath from musicpaths where id = (%s);", (choose,)
        result = self.db.makeRequest(request=request, parameters=parameters)
        return result



    #This help us to get the necessary things to play the music
    async def getThingsToPlayMusic(self, ctx, playAnother=False):
        """
        Function that needs the context (ctx) and play another in True or False
        for determinate if we want to play another song staying in the voice channel
        """

        inVoiceChannel = ctx.author.voice

        
        #With this we check if the user is in a voice channel, otherwise we return none for audio and voice
        #so we can process it in the play function for send a message to user.
        
        if not inVoiceChannel:
            return None, None

        elif playAnother:

            try:
                result = await self.getMusic()
                audio = os.path.join(self.config["paths_music"], result[0])
                voice = ctx.guild.voice_client
                return audio, voice
        
            except Exception as e:
                print(f"Error al reproducir musica {e}")

        elif playAnother == False:

            try:
                result = await self.getMusic()
                audio = os.path.join(self.config["paths_music"], result[0])
                voice = await ctx.author.voice.channel.connect()
                return audio, voice
            
            except Exception as e:
                print(f"Error al reproducir musica {e}")



    #This command, gets the path from database and stores it in variable "audio", then plays it with ffmpeg
    @commands.command()
    async def play(self, ctx):
        

        audio, voice = await self.getThingsToPlayMusic(ctx)

        if audio is None or voice is None:

            answer = Crear_Respuesta("Conectate a voz primero brou", None)
            await ctx.reply(embed=answer.enviar)

        else:

            #Plays the music with FFmpegPCMAudio
            voice.play(discord.FFmpegPCMAudio(source=audio, executable="C:/ffmpeg/bin/ffmpeg.exe"))



    #This command kick the bot from the voice channel
    @commands.command()
    async def salir(self, ctx):
        await ctx.voice_client.disconnect()



    #This pause the song that is already playing
    @commands.command()
    async def pausar(self, ctx):
        await ctx.voice_client.pause()



    #This resumes it 
    @commands.command()
    async def reanudar(self, ctx):
        await ctx.voice_client.resume()



    #And this is for playing another song, staying in the voice channel
    @commands.command()
    async def po(self, ctx):

        #Getting voice object and audio
        audio, voice = await self.getThingsToPlayMusic(ctx, playAnother=True)


        #Checking if audio or voice are none, in that case, we send a message to user for connect to a voice channel
        if audio is None or voice is None:

            answer = Crear_Respuesta("Conectate a voz primero brou", None)
            await ctx.reply(embed=answer.enviar)

        else:

            #Plays the music with FFmpegPCMAudio
            voice.stop()
            voice.play(discord.FFmpegPCMAudio(source=audio, executable="C:/ffmpeg/bin/ffmpeg.exe"))




#This is the setup for loading the cog in the bot
async def setup(client: commands.Bot) -> None:
    await client.add_cog(music_working(client))



        