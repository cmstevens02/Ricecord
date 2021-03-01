# imports that keep the bot working
import discord
import os 
from discord.ext import commands
import asyncio
from keepAlive import keepAlive

# cog imports
from cogs.chatting import Chatting


bot = commands.Bot(command_prefix="!r ")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")  

'''
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

'''
bot.add_cog(Chatting(bot))

keepAlive()
bot.run(os.getenv('TOKEN'))
