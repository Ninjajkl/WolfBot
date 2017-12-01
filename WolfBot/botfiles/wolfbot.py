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
# ~index
@bot.command(pass_context = True)
async def index(ctx):
    await bot.say("""

    WolfBot:wolf: index - Gabe Frahm

    ~index   - shows all current commands and uses. (duh, you just used it)
    ~beep    - bot replies with boop
    ~nani    - omae wa mou shindeiru
    ~roll    - rolls a die
    ~flip    - flips a coin
    ~git     - sends github link into chat
    ~oof     - oof
    ~lottery - creates a lottery
        ~lotterytickets  - shows all current lottery numbers, and who has the number.
        ~lotteryclear    - clears all lottery numbers currently in lottery.
        ~lotterytotal    - Shows how many lottery tickets are currently held
        ~lotteryconclude - concludes the lottery. selects a winner and mentions them. 

    """)
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
# ~ git
@bot.command(pass_context = True)
async def git(ctx):
    await bot.say('Source code: https://github.com/Wolf20122012/WolfBot')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~oof
@bot.command(pass_context = True)
async def oof(ctx):
    await bot.say('https://vignette3.wikia.nocookie.net/lumber-tycoon-2/images/5/5f/Wobblebobble.png/revision/latest?cb=20160401145738')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~lottery

user_tickets = []
highestnum = 0
@bot.command(pass_context = True)
async def lottery(ctx):
    global user_tickets
    global highestnum
    author_mem = ctx.message.author
    author_str = str(author_mem)
    
    ticket_int = highestnum + 1
    highestnum = ticket_int

    ticket_str = str(ticket_int)
    author = " " + author_str + " "

    user_tickets.append(author)
    user_tickets.append(ticket_int)
    await bot.say(author_str + ": " + ticket_str)

@bot.command(pass_context = True)
async def lotterytickets(ctx):
    await bot.say(user_tickets)

@bot.command(pass_context = True)
async def lotteryclear(ctx):
    global user_tickets
    user_tickets[:] = []
    await bot.say("ALERT: Cleared all lottery tickets")

@bot.command(pass_context = True)
async def lotterytotal(ctx):
    total_int = len(user_tickets)
    total_int2 = total_int / 2
    total = str(total_int2)
    await bot.say("There are a total of " + total + " tickets in the current lottery.")

@bot.command(pass_context = True)
async def lotteryconclude(ctx):
    await bot.say("LOTTERY ALERT: The lottery will now conclude as a winner is chosen...")
    winningnum = random.randint(1,highestnum)
    winningnum_str = str(winningnum)
    if winningnum in user_tickets:
        await bot.say("It appears we have a winner!!!")
        #await bot.say(winningnum)
        name_num = user_tickets.index(winningnum) - 1
        name = user_tickets[name_num]
        #await bot.say(name)
        await bot.say("Congratulations to @" + name + "! You won with the number " + winningnum_str + "!")
        user_tickets[:] = []
        highestnum = 0
    else: 
        await bot.say("Oh man. Something went very very wrong. I guess there are no winners here! *que seinfeld theme*")

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
    print("Wolfbot is now online! Have fun :D")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

bot.run('key')

#TODO:
# Create a credits system