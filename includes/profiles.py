import discord

class Profiles(discord.ui.Select):
    def __init__(self, bot_: discord.Bot):
        self.bot = bot_

        options = [
            discord.SelectOption(
                label="ข้อมูลดิสคอร์ด", description="แสดงข้อมูลดิสคอร์ดของสมาชิก", emoji="📁"
            ),
            discord.SelectOption(
                label="ข้อมูลทางการเงิน", description="แสดงข้อมูลเงินดิสคอร์ด ของสมาชิก", emoji="💵"
            ),
            discord.SelectOption(
                label="ข้อมูลแร็งค์", description="แสดงข้อมูล เลเวล แร็งค์ และค่าประสบการณ์ของสมาชิก", emoji="🏆"
            )

        ]

        super().__init__(
            placeholder="📄 เลือกคำสั่งที่คุณต้องการ...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content=self.values[0],view=None)





class ProfilesView(discord.ui.View):
    def __init__(self, bot_: discord.Bot):
        self.bot = bot_
        super(ProfilesView, self).__init__()

        self.add_item(Profiles(self.bot))