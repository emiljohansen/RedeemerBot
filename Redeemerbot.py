import logging

import discord
from discord.ext import commands as cmd

import commands, utils.DB

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

token = ""

bot = cmd.Bot(command_prefix='>', description='Reacts to given commands, use !help for list of available commands')

@bot.event()
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    bot.add_cog(AddCommand(bot))
    bot.add_cog(UserManagement(bot))
    bot.add_cog(AvailabiltyCommands(bot))

@bot.event()
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.check
async def is_banned():
    return

if __name__ == "__main__":
    print("hello world")
    bot.run(token)


