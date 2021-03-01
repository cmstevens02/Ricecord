import discord
import os 
from discord.ext import commands



class Chatting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None


    @commands.command(
      help = "say hello"
    )  
    async def hello(self, ctx):
      await ctx.channel.send("Hello! :rice_ball:")

      print("hello"
      )

    @commands.command( help = "pwish" )
    async def pwish(self, ctx):
      await ctx.channel.send(":gun:")

    @commands.command(
      help = "say thank you "
    )
    async def thank(self, ctx):
      await ctx.channel.send(file=discord.File('images/ty.png'))
      await ctx.channel.send("Oh... You're Welcome...")

    @commands.command(
      help = "say i love you "
    )
    async def ily(self, ctx):
      await ctx.channel.send(file=discord.File('images/ily.png'))
      await ctx.channel.send("Hehe I love you too!!! :heart::rice_ball::heart:")

    @commands.command(
      help = "say good morning ", 
      pass_context = True , aliases=[ 'gm', 'good morning']
    )
    async def ohio(self, ctx):
      await ctx.channel.send(file=discord.File('images/ohio.png'))
      await ctx.channel.send("Ohio... Good Morning")

    @commands.command(
      help = "say goodnight", 
      pass_context = True , aliases=[ 'gn', 'good night']
    )
    async def oyasumi(self, ctx):
      await ctx.channel.send(file=discord.File('images/oyasumi.png'))
      await ctx.channel.send("Oya Oya Oyasumi")
    

    

