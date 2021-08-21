import discord
from discord.ext import commands
import traceback
import sys

# コマンドクラス
class CogCommandSample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def hi(self, ctx):
        await ctx.send("こんにちわ")

    @commands.command()
    async def bye(self, ctx):
        await ctx.send("さようなら")
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('ポン！')

def setup(bot):
    return bot.add_cog(CogCommandSample(bot))