import discord.ext.commands

class ScheduleCommands(commands.Cog):
    def __init__(self,  bot):
        super().__init__()
        self.bot = bot