from discord.ext import commands

class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="คำสั่งทดสอบ")
    async def test(self, ctx):
        await ctx.send("ok")


def setup(bot):
    bot.add_cog(Members(bot))