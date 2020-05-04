import discord.ext.commands

class ListCommand(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @command.command()
    async def list(self, ctx):
        return
    
    list.subcommand()
    async def runs(self, ctx):
        return
    
    list.subcommand()
    async def hosts(self, ctx):
        return
    
    