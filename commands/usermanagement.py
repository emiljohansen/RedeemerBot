import discord.ext.commands

class UserManagement(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    
    @commands.command()
    async def ban(self, ctx, user):
        return
    
    @commands.command()
    async def unban(self, ctx, user):
        return

    @commands.command()
    async def newmod(self, ctx, user):
        return