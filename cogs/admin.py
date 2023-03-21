import asyncio
import time

from discord.ext import commands



class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="คำสั่งหยุดการใช้งาน extension ของระบบ")
    @commands.is_owner()
    async def unload(self, ctx, cog:str):
        await ctx.message.delete()
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could not unload cog")
            print(e)
            return
        await ctx.send("Cog has been unloaded")

    @commands.command(brief="คำสั่งเปิดการใช้งาน extension ของระบบ")
    @commands.is_owner()
    async def load(self, ctx, cog:str):
        await ctx.message.delete()
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not load cog")
            print(e)
            return
        await ctx.send("Cog has been loaded")

    @commands.command(brief="คำสั่งรีสตาร์ท extension ของระบบ")
    @commands.is_owner()
    async def reload(self, ctx, cog:str):
        await ctx.message.delete()
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            return await ctx.send(f"Could not reload cog !\n` {e} `")
        await ctx.send("Cog has been reloaded.")

    @commands.command(brief="คำสั่งลบข้อความ / Admin only")
    @commands.is_owner()
    async def clear(self, ctx):
        qustion = await ctx.reply("How many message for clear? (all, amount with number)")
        def author_check(res):
            return res.author == ctx.author and res.channel == ctx.channel

        try:
            message = await self.bot.wait_for(event="message", check=author_check, timeout=30)
            msg = message.content

            if msg == "all":
                await message.delete()
                await qustion.edit(content="**All** Message has been deleted.")
                time.sleep(0.5)
                return await ctx.channel.purge()
            if msg.isdigit:
                amount = int(msg)
                await message.delete()
                await qustion.edit(content=f"**{amount}** Message has been deleted.")
                time.sleep(0.5)
                return await ctx.channel.purge(limit=amount + 2)
        except asyncio.TimeoutError:
            await ctx.message.delete()
            return await qustion.edit(content="Your command is timeout!!", delete_after=3)



def setup(bot):
    bot.add_cog(Admin(bot))