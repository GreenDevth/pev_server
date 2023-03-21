import os
from abc import ABC

import discord
from discord.ext import commands


from config import ServerSetting


class MyClient(commands.Bot, ABC):
    def __init__(self, *args, **kwargs):
        super(MyClient, self).__init__(
            command_prefix=commands.when_mentioned_or("!"),
            owner_id=int(ServerSetting("SERVER")['owner']), *args, **kwargs,
            intents=discord.Intents.all()
        )

bot = MyClient(case_insensitive=True)

@bot.event
async def on_ready():
    print(f"{bot.user.display_name} #{bot.user.discriminator}")

for filname in os.listdir("./cogs"):
    if filname.endswith(".py") and filname != "__ini__.py":
        bot.load_extension(f'cogs.{filname[:-3]}')

bot.run(ServerSetting("SERVER")["token"])

# if __name__ == '__main__':
#     for filename in os.listdir('cogs'):
#         if filename.endswith('.py') and filename != "__init__.py":
#             bot.load_extension('cogs.{}'.format(filename[:-3]))


