import json
import discord
from itertools import cycle
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os

with open("config.json",'r') as f:
    CONFIG = json.load(f)

TOKEN = CONFIG["token"]
PREFIX = CONFIG["bot_prefix"]
INTENTS = discord.Intents.default()
BOT = commands.Bot(command_prefix=PREFIX, intents=INTENTS)
STATUS = cycle(['Try * help','Prefix - *'])

BOT.remove_command("help")

@BOT.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

@BOT.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        em = discord.Embed(title=f"💔Ese comando no existe", c=f"{ctx.author.mention}, intenta usar *ayuda para conocer la lista de comando disponible", color=ctx.author.color) 
        await ctx.reply(embed=em, mention_author=False)

@tasks.loop(seconds=5)
async def change_status():
    await BOT.change_presence(activity=discord.Game(next(STATUS)))

for filename in os.listdir('./modulos'):
    if filename.endswith('.py'):
        BOT.load_extension(f'modulos.{filename[:-3]}')

@BOT.command()
async def hello(ctx):
    msg = f'Hi {ctx.author.mention}'
    await ctx.reply(msg, mention_author=False)

BOT.run(TOKEN)