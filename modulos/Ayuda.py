import discord
from discord.ext import commands

class Ayuda(commands.Cog):
    def __init__(self, BOT):
        self.BOT = BOT

    @commands.Cog.listener()

    async def on_ready(self):
        print('✔ Modulo Info')

    @commands.command(aliases=['ayuda', 'help', 'h', 'a'])
    async def _help(self, ctx):
        embedvar = discord.Embed(title="❔Ayuda:",description=None, color=0x00ff00)

        embedvar.add_field(name='*info', value='Para ver el status del bot', inline=False)
        embedvar.add_field(name='*ayuda', value='Para ver esta ayuda', inline=False)

        await ctx.reply(embed=embedvar, mention_author=False)

def setup(BOT):
    BOT.add_cog(Ayuda(BOT))