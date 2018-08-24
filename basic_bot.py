from logger import logger
import random

import discord
from discord.ext import commands

from config import token

# LOGGING
logger()

# BOT

bot = commands.Bot(command_prefix='$', description='bASIC bOT')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)


@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(str(a*b))


@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except:
        await ctx.send('Format has to be in NdN')
        return

    result = ', '.join([str(random.randint(1, limit)) for r in range(rolls)])
    await ctx.send(result)


@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@bot.group()
async def cool(ctx):
    print(ctx.invoked_subcommand)
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes the bot is cool.')


bot.run(token)
