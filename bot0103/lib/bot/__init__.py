from discord import Streaming
from discord import Intents
from glob import glob
from discord.ext.commands import Bot as BotBase

PREFIX = "?"

COGS = [aea.split("\\")[-1][:-3] for aea in glob("C:/Users/USER/Desktop/bot2/bot2/lib/cogs/*.py")] 


class Bot(BotBase):
    def __init__(self):
      self.PREFIX = PREFIX
        
          
      super().__init__(command_prefix=PREFIX, intents=Intents.all())

    
    def setup(self):
      for cog in COGS:
        self.load_extension(f"lib.cogs.{cog}")
        print(f"{cog} listo")
      print("inicio listo") 

    def run(self):
        self.setup()

        
        self.TOKEN = "ODA1NjEwOTE4NzMzNjc2NTk0.YBdZog.IkwSUn8rR5T04eOlMDIEPHh0zR8"
            
        super().run(self.TOKEN)
        
    
    async def on_ready(self):
      await self.change_presence(activity=Streaming(name="!!help", url="http://www.twitch.tv/thedanielrity"))    
      print("GAAA")

bot = Bot()

