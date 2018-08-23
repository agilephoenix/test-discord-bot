import logging
import random

import discord
from discord.ext import commands

from config import token

# LOGGING

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

logger.addHandler(handler)

# BOT

bot = commands.Bot(command_prefix='$', description='bASIC bOT')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')


@bot.command()
async def add(a: int, b: int):
    await bot.say(a+b)


@bot.command()
async def multiply(ctx, a: int, b: int):
    await bot.say(str(a*b))


@bot.command()
async def roll(dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except:
        await bot.say('Format has to be in NdN')
        return

    result = ', '.join([str(random.randint(1, limit)) for r in range(rolls)])
    await bot.say(result)


@bot.command()
async def joined(member: discord.Member):
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


@bot.group(pass_context=True)
async def cool(ctx):
    print(ctx.invoked_subcommand)
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='bot')
async def _bot():
    await bot.say('Yes the bot is cool.')

bot.run(token)
