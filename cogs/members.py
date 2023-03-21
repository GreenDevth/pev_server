import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from config import ServerSetting
from includes.profiles import ProfilesView

commands_list = [
    "📂 โปรไฟล์",
    "🎡 กระดานภารกิจ",
    "🏦 ข้อมูลทางการเงิน"
]


guild_id = ServerSetting("SERVER")["guild"]

class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ผู้ใช้งาน", description="คำสั่งใช้งานสำหรับสมาชิกดิสคอร์ด")
    async def player_command(self, ctx:discord.Interaction, cmd:Option(str, "เลือกคำสั่งที่ต้องการ", choices=commands_list)):
        if cmd == commands_list[0]:
            return await ctx.response.send_message(view=ProfilesView(self.bot), ephemeral=True)


    @commands.command(brief="คำสั่งทดสอบ")
    async def test(self, ctx):
        await ctx.send("ok")


def setup(bot):
    bot.add_cog(Members(bot))

class Profiles(discord.ui.Button):
    def __init__(self):
        super(Profiles, self).__init__(label="ข้อมูลผู้ใช้งาน")