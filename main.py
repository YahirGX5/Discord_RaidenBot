import discord
from discord.ext import commands

#This class defines the client of bot and charges the cogs to the bot
class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.cogslist = ["cogs.music_working", "cogs.curiositys", "cogs.Memes_working"]

    #This function is who loads the cogs to the bot
    async def setup_hook(self):
        for ext in self.cogslist:
            await self.load_extension(ext)

def main():

    client = Client()

    #Here you place your bot token
    client.run("MTA2Nzk4NTI5NzU3ODY3NjIzNA.GtSPrX.xmcbiNvnXZiOwWbThEgeM-ecJEQULAFYSKRL5E")

if __name__ == "__main__":
    main()