import discord.ext.commands
import datetime

class AddCommand(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(pass_context=True)
    async def add(self, ctx):
        return

    @add.subcommand()
    @commands.check(is_moderator)
    async def host(self, ctx, *args):
        return

    @add.subcommand()
    async def run(self, ctx, run: str, runsize: int, rundate: date, runtime: time):
        '''Add a new run with a given name, amount of people in the run and a date and time.'''
        return

    @add.error
    async def add_error(self, ctx, error):
        return

    async def is_moderator(self, ctx):
        return