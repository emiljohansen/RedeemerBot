import discord.ext.commands

class AvailabilityCommands(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @command.command()
    async def available(self, ctx, *args):
        return