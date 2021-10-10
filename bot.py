import json
import discord
from itertools import cycle
from discord import embeds
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os
from database import DB
import random

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
        await ctx.reply(embed=em)
    else:
        print(error)

@tasks.loop(seconds=5)
async def change_status():
    await BOT.change_presence(activity=discord.Game(next(STATUS)))

for filename in os.listdir('./modulos'):
    if filename.endswith('.py'):
        BOT.load_extension(f'modulos.{filename[:-3]}')

@BOT.command(aliases=['construir'])
async def build(ctx):
    if DB.CrearBase(ctx.author):
        msg = f'Hi {ctx.author.mention}, tu base ha sido construida'
        await ctx.author.send(f'Tu base se construyo en (X, Y): {random.randint(1, 100)}, {random.randint(1, 100)}')
    else:
        msg = f'Hi {ctx.author.mention}, ya tienes una base'
    await ctx.reply(msg)


@BOT.command(aliases=['estadisticas'])
async def stats(ctx, tipo = None):
    if tipo == None:
        content = discord.Embed(title=f'Hola {ctx.author.mention}!, ingresa una opcion:', color=0x00ff00)
        content.add_field(name='Recursos', value='Para ver tus recursos', inline=False)
    elif tipo == "recursos":
        content = discord.Embed(title=f'Hola {ctx.author.mention}!, tienes los siguientes recursos:', color=0x00ff00)
        res = DB.recursos(ctx.author)
        for r in res:
            rec = res[r]
            content.add_field(name=rec['nombre'], value=rec['valor'], inline=False)
    await ctx.reply(embed=content)

BOT.run(TOKEN)