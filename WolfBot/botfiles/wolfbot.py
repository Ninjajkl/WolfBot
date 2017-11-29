#Wolfbot by Gabe Frahm
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  _____                            _             
# |_   _|                          | |            
#   | |  _ __ ___  _ __   ___  _ __| |_ ___       
#   | | | '_ ` _ \| '_ \ / _ \| '__| __/ __|      
#  _| |_| | | | | | |_) | (_) | |  | |_\__ \      
# |_____|_| |_| |_| .__/ \___/|_|   \__|___/      
#                 | |                             
#                 |_|                             
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import discord
from discord.ext import commands
import time
import random
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  _____           __ _      
# |  __ \         / _(_)     
# | |__) | __ ___| |_ ___  __
# |  ___/ '__/ _ \  _| \ \/ /
# | |   | | |  __/ | | |>  <                     
# |_|   |_|  \___|_| |_/_/\_\                    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                           
bot = commands.Bot("~")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   _____                                          _     
#  / ____|                                        | |    
# | |     ___  _ __ ___  _ __ ___   __ _ _ __   __| |___ 
# | |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
# | |___| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
#  \_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                        
# ~beep
@bot.command(pass_context = True)
async def beep(ctx):
    await bot.say("Boop!")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~nani
@bot.command(pass_context = True)
async def nani(ctx):
    await bot.say("omae wa mou")
    time.sleep(1)
    await bot.say("shindeiru")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~index
@bot.command(pass_context = True)
async def index(ctx):
    await bot.say("""

    WolfBot:wolf: index - Gabe Frahm

    ~index - shows all current commands and uses. (duh, you just used it)
    ~beep  - bot replies with boop
    ~nani  - omae wa mou shindeiru
    ~roll  - rolls a die
    ~flip  - flips a coin

    """)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~roll
@bot.command(pass_context = True)
async def roll(ctx):
    result = random.randint(1,6)
    await bot.say(result)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~flip
@bot.command(pass_context = True)
async def flip(ctx):
    result = random.randint(1,2)
    if result == 1:
        result2 = 'tails'
    else:
        result2 = 'heads'
    await bot.say(result2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ______               _       
# |  ____|             | |      
# | |____   _____ _ __ | |_ ___ 
# |  __\ \ / / _ \ '_ \| __/ __|
# | |___\ V /  __/ | | | |_\__ \
# |______\_/ \___|_| |_|\__|___/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.event
async def on_member_join(member):
    server = member.server
    fmt = 'Hello {0.mention}, and welcome to {1.name}! If you have any questions about me, just type ~index'
    await client.send_message(discord.Object('377191488234323979'), fmt.format(member, server))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("Wolfbot is now online!")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
bot.run('MjY3NjUzNDE0NjE0MzM1NDkw.DPsOng.3B4TVo1hb5kEXgehNUtYV8NCz9U')