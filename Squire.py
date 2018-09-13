import discord
import random
import json
import os

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

bot_config_file = "squire_config.json"
bot_config = {}

if not os.path.isfile(bot_config_file) or os.stat(bot_config_file).st_size == 0:
    print("There's no configuration file ready yet!\n")
    print("Let's generate one now (stop this and enter your config filename into the script now if you have one)...\n")

    bot_config['bot_auth'] = input("Enter the bot's authorization token: ")
    bot_config['bot_name'] = input("Enter the bot's name: ")
    bot_config['bot_owner'] = input("Enter the bot owner's name: ")
    bot_config['bot_owner_username'] = input("Enter the owner's username: ")

    print("Writing everything to your squire_config.json...\n")

    with open(bot_config_file, 'w') as jsonfile:
        json.dump(bot_config, jsonfile)


else:
    with open(bot_config_file, 'r') as jsonfile:
        bot_config = json.load(jsonfile)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def asura(ctx):
    await ctx.send("asura sucks")

@bot.command()
async def haveneast(ctx):
    await ctx.send("Suvy velik Gilbanya!")

@bot.command()
async def fractalgalaxy(ctx):
    await ctx.send("Our five-year mission: To boldly go where- *gurgles*... *thud*... ***unnatural hiss***")

@bot.command()
async def steerpike(ctx):
    await ctx.send("Was I mistaken, or did I catch you looking at me... with all three hundred eyes?")

@bot.command()
async def sparkletwist(ctx):
    await ctx.send("Is it fate, or is it Fate?")

@bot.command()
async def loa(ctx):
    await ctx.send("Mecha and steampunk and talking animals, oh my!")

@bot.command()
async def football(ctx):
    await ctx.send("If you wanna win the game, you gotta score points Jim")

@bot.command()
async def superbright(ctx):
    await ctx.send("ALL-CAPS MENACING GIBBERISH")

@bot.command()
async def hoers(ctx):
    if ctx.message.author.nick == "Hoers":
        await ctx.send("You're a hoers")
    else:
        await ctx.send("You're not a hoers")
        print (ctx.message.author.nick)


@bot.command()
async def roll(ctx, roll : str):

    total = 0
    rolls_str = ""
    rolls = []

    try:
        try:
            count = roll.split('d')[0]
            sides = roll.split('d')[1]


        except Exception as e:
            print(e)
            await ctx.send("Format has to be in #d#.")
            return

        if int(count) > 1000:
            await ctx.send("I cant roll that many dice.")
            return

        rolls, limit = map(int, roll.split('d'))
        for value in range(rolls):

            number = random.randint(1, limit)
            total = total + number

            if rolls_str == '':
                rolls_str += str(number)
            else:
                rolls_str += ', ' + str(number)

        if count == '1' or count == '':
            await ctx.send(ctx.message.author.mention + ": " + "Rolling {0}d{1}".format(count, sides) + "\n**Result**: {0} ".format(rolls_str))
        else:
            await ctx.send(ctx.message.author.mention + ": " + "Rolling {0}d{1}".format(count, sides) + "\n**Result**: **{0}** ".format(str(total)) + "({0})".format(rolls_str))


    except Exception as e:
        print(e)
        return

@bot.command()
async def rollset(ctx, roll : str):

    total = 0
    totals = []
    rolls_str = ""
    rolls = []

    try:
        try:
            parse = roll.split('x')
            sets = parse[0]
            counts_sides = parse[1]
            print("parse is {0}, parse[0] is {1}".format(parse, parse[0]))
            count = counts_sides.split('d')[0]
            sides = counts_sides.split('d')[1]


        except Exception as e:
            print(e)
            await ctx.send("Format has to be in #x#d#.")
            return

        if int(count) > 1000:
            await ctx.send("I cant roll that many dice.")
            return

        rolls, limit = map(int, parse[1].split('d'))

        print("sets is {0}".format(sets))
        iterations = int(sets)
        print("iterations is {0}".format(iterations))
        for iteration in range(iterations):

            total = 0
            rolls_str = ''
            for value in range(rolls):
                number = random.randint(1, limit)
                total = total + number

                if rolls_str == '':
                    rolls_str += str(number)
                else:
                    rolls_str += ', ' + str(number)

            total_rolls_str = "**{0}**".format(str(total)) + " ({0})".format(rolls_str)
            totals.append(total_rolls_str)

        result_str = ""
        for total_rolls in range(iterations):
            if result_str == '':
                result_str += "{0}".format(totals[total_rolls])
            else:
                result_str += ", {0}".format(totals[total_rolls])

        stripped_str = result_str.rstrip(',')
        await ctx.send(ctx.message.author.mention + ": " + "Rolling {0}d{1} {2} times".format(count, sides, sets) + "\n**Results**: {0}".format(stripped_str))

    except Exception as e:
        print(e)
        return


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=bot_config['bot_name'], description="The local dice lackey.", color=0xeee657)

    # give info about you here
    embed.add_field(name=bot_config['bot_owner'], value=bot_config['bot_owner_username'])

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title=bot_config['bot_name'], description=bot_config['bot_owner_username'], color=0xeee657)

    embed.add_field(name="!add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="!multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="!info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="!help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run(bot_config['bot_auth'])
