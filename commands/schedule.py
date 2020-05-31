import discord.ext.commands

class ScheduleCommands(commands.Cog):
    def __init__(self,  bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def schedulerun(self, ctx):
        '''Automatically schedule a run based on users' availability.'''
        return