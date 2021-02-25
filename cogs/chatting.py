import discord
import os 
from discord.ext import commands



class Chatting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None


    @commands.command(
      help = "Say hello to ricecord!"
    )  
    async def hello(self, ctx):
      await ctx.channel.send("Hello! :rice_ball:")

      print("hello"
      )

    @commands.command(
      pwish = ":gun:"
    )
    async def pwish(self, ctx):
      await ctx.channel.send(":gun: :gun:")

    

