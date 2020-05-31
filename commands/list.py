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
        '''List all scheduled runs'''
        return
    
    list.subcommand()
    async def hosts(self, ctx):
        '''List all qualified hosts'''
        return
    
    list.runs.subcommand()
    async def participants(self, ctx):
        '''List all participants in a given run.'''
        return