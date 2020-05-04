import discord.ext.commands


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
    async def run(self, ctx, run: str, runsize: int):
        return

    @add.error
    async def add_error(self, ctx, error):
        return

    async def is_moderator(self, ctx):
        return