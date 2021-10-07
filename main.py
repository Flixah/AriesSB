from asyncio.subprocess import Process
from inspect import EndOfBlock
from io import StringIO
from colorama.initialise import reset_all
import discord
from discord import *
from discord.ext import commands
import json
import sys
from time import sleep
import asyncio
import os
from random import seed
from random import randint
import math
from colorama import init, Fore, Back, Style
import base64
import requests
import re
import random
global detector
    #Checks if config file exists if it dosen't make the user input token to create one
if os.path.exists("./data/config.json"):
    pass
else:
#IF developer config file isn't found ask for the token, set it, then set prefix and token to the correct file (data/config)
    print("   / \   _ __(_) ___  ___")
    print("  / _ \ | '__| |/ _ \/ __|")
    print(" / ___ \| |  | |  __/\__ \"")
    print("/_/   \_\_|  |_|\___||___/")
    key = input("Enter Your Token: ")
    qsr = input("Sniper? (y/n): ")
    snipe = "false"
    if (qsr == "y"):
        snipe = "true"

    data = {
        "token": f"{key}",
        "prefix": ".",
        "sniper": f"{snipe}"
    }
    ISDIR = os.path.isdir("./data")
    if (not ISDIR):
        os.mkdir('./data')
    else:
        pass
    with open("./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))

#Opens the json 
with open("./data/config.json") as f:
#Loads the json to read contents
    config = json.load(f)
prefix = config.get('prefix')
token = config.get('token')
nitro_sniper = config.get('sniper')
bot = commands.Bot(prefix, self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off())
bot.remove_command("help")
bot.remove_command("admin")
@bot.event
#Detects onReady if ready prints connected to the user with their discriminator and name
async def on_ready():  
    os.system('cls' if os.name == 'nt' else 'clear')
    build = "1.0"
    print(Fore.CYAN + "                                                  ___         _          ")
    print(Fore.CYAN + "                                                 /   |  _____(_)__  _____")
    print(Fore.CYAN + "                                                / /| | / ___/ / _ \/ ___/")
    print(Fore.CYAN + "                                               / ___ |/ /  / /  __(__  ) ")
    print(Fore.CYAN + "                                              /_/  |_/_/  /_/\___/____/  ")
    print(Fore.RESET + "\n\n                                             Ram the opposition with Aries")
    print(Fore.RESET + "\n\n------------------------------------------------------------------------------------------------------------------------")
    print("\n" + Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + "21 " + Fore.RESET + "Commands!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "User Is In " + Fore.LIGHTCYAN_EX + str(len(bot.guilds))  + Fore.RESET + " Guilds!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Build " + Fore.LIGHTCYAN_EX + build + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Prefix " + Fore.LIGHTCYAN_EX + str(prefix) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.GREEN + " Connected! Enjoy Aries " + Fore.RESET + f"{bot.user}" + Fore.RESET)       
@bot.event
async def on_message(message):
    #Loads All Embeds it finds
    embeds = message.embeds
    for embed in embeds:
        #Gets Embed contents
        getEmbed = embed.to_dict()
        #Converts embed to a string
        convertedEmbed = str(getEmbed)
        #Searches for luna in contents TODO: Add more checks to improve
        if "Luna" in convertedEmbed:
            #If found print 
         print(Fore.CYAN + "Info" + Fore.RESET + " |" + Fore.RED + " [!]" + Fore.CYAN + " Selfbot Found! On » " + Fore.LIGHTCYAN_EX + str(message.author) + Fore.CYAN + " » Server » " + Fore.LIGHTCYAN_EX + str(message.guild) + Fore.CYAN + " » Selfbot » " + Fore.LIGHTCYAN_EX + "Luna")

    #Detects if it starts with gifting to see if its not just any msg and checks if sniper is active
    if nitro_sniper == 'true' and 'discord.gift/' in message.content:
        code = re.search("discord.gift/(.*)", message.content).group(1)
        if len(code) >= 16:
            code = re.search("discord.gift/(.*)", message.content).group(1)
            r = requests.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
            r = r.text
            if 'This gift has been redeemed already' in r:
                print(Fore.CYAN + " Info |" + Fore.RED + "[Nitro]" + Fore.CYAN + " Sadly this code has been redeemed already. | " + Fore.RESET + f" Code: {code} | " + Fore.RED + "Error")
            elif 'nitro' in r:
                print(Fore.CYAN + "Info |" + Fore.GREEN + "[Nitro] " + Fore.CYAN + " Nitro Sniped Successfully! | " + Fore.RESET +  f"Code: {code}'")
            elif 'Unknown Gift Code' in r:
                print(Fore.CYAN + "Info | " + Fore.YELLOW + "[Nitro] " + Fore.CYAN + f"An invalid code was posted | Code: {code} | " + Fore.RED + "Error")
            else:
                pass
        else:
          #Checks length for fakes
          print(Fore.YELLOW + f"[!] Detected a fake code: {code}")
    await bot.process_commands(message)

@bot.command()
#Help Command
async def help(ctx):
    embed = discord.Embed(title="Aries Help Menu", description = "<> is Usage \nHelp » Display this menu » <.help> » {None}\nAdmin » Display the admin page » <.admin> » {None}\nFun » Display the fun page » <.fun> » {None}\nMisc » Display the Misc page » <.misc> » {None}\nNSFW  » Display the NSFW page » <.NSFW> » {None}\nSettings » Display the Aries Settings page » <.settings> » {None} \nNotes » Display the Aries Notes page » <.notes> » {None}", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed)   
#Admin Command & Categories for "Help"
@bot.command()
async def admin(ctx):
    embed = discord.Embed(title="Aries Administrator Menu", description = "```Ban    » Ban A Member » .ban <Member> \nKick    » Kick A Member » .purge <A mount> \nPurge    » Purge <> of msgs » .purge <Amount> \ncreate <> Create a channel » .Create <Name> \nDelete a channel » .delete <Name>  ```", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Fun Commands
@bot.command()
async def fun(ctx):
    embed = discord.Embed(title="Aries Fun Menu", description = "```RollDice    » Roll a Number! » .roll <No Args> \nRollDice    » Roll a Number! » .roll <No Args>\nAllah    » Talk to ALLAH » .allah <No Args>\nPickup Line » Tell a pickup » .pickup <No Args>\nJoke    » Tell a joke » .joke <No Args>\nRickRoll    » Rick ur friends ;) » .rickroll <No Args>\nleave    » Leave the current server ;) » .leave <No Args>  ```", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Misc Commands
@bot.command()
async def misc(ctx):
    embed = discord.Embed(title="Aries Misc Menu", description = "```Restart    » Restarts Aries » .restart\nUserinfo    » Shows your userinfo » .userinfo\nTodo    » Shows the bots TODO list » .todo\nAvatar    » Display Avatar of a user\nInvite    » Get an invite to Aries```", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#NSFW Commands
@bot.command()
async def nsfw(ctx):
    embed = discord.Embed(title="Aries NSFW Menu", description = "```boobs    » Shows boobs » .boobs```", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Settings Commands
@bot.command()
async def settings(ctx):
    embed = discord.Embed(title="Aries Settings Menu", description = "```Status    » Change your Status » .status <val>\nSniper    » Check sniper status » .sniper <noval>```", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Ban Command
@bot.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    try:
        embed = discord.Embed(title="Aries", description = "Banned " + member.mention + " Successfully! ", color=0x493BB9)    
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
        await member.ban(reason = reason)
        await ctx.send(embed = embed)
    except:
        embed = discord.Embed(title="Aries", description = "Error | Insufficient Perms!", color=0x493BB9)    
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
        await ctx.send(embed = embed) 
@bot.command()
#Kick Commmand
async def kick(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    try:
      embed = discord.Embed(title="Aries", description = "Kicked " + member.mention + " Successfully! ", color=0x493BB9)    
      embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
      await member.kick(reason = reason)
      await ctx.send(embed = embed) 
    except commands.MissingPermissions:
     embed = discord.Embed(title="Aries", description = "Error | Insufficient Perms!", color=0x493BB9)    
     embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
     await ctx.send(embed = embed) 
@bot.command()
#Purge Commmand
async def purge(ctx, limit: int):
    await ctx.message.delete()
    try:
      await ctx.channel.purge(limit=limit)
      embed = discord.Embed(title="Aries", description = "Cleared " + "Successfully", color=0x493BB9)    
      embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
      await asyncio.sleep(10)
      await ctx.send(embed = embed) 
    except commands.MissingPermissions:
     embed = discord.Embed(title="Aries", description = "Error | Insufficient Perms!", color=0x493BB9)    
     embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
     await ctx.send(embed = embed) 
@bot.command()
#Create Commmand
async def create(ctx, name):
    await ctx.message.delete()
    try:
      guild = ctx.guild
	  #channel = await guild.create_text_channel(channel_name)
      await guild.create_text_channel(name)
      embed = discord.Embed(title="Aries", description = "Created " + "Successfully", color=0x493BB9)    
      embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
      await ctx.send(embed = embed) 
    except commands.MissingPermissions:
     embed = discord.Embed(title="Aries", description = "Error | Insufficient Perms!", color=0x493BB9)    
     embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
     await ctx.send(embed = embed) 
     #Delete command
@bot.command()
async def delete(ctx, name):
    await ctx.message.delete()
    try:
      guild = ctx.guild
	  #channel = await guild.create_text_channel(channel_name)
      await guild.delete_text_channel(name)
      embed = discord.Embed(title="Aries", description = "Deleted " + "Successfully", color=0x493BB9)    
      embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
      await ctx.send(embed = embed) 
    except commands.MissingPermissions:
     embed = discord.Embed(title="Aries", description = "Error | Insufficient Perms!", color=0x493BB9)    
     embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
     await ctx.send(embed = embed) 
#RollDice command
@bot.command()
async def roll(ctx):
    await ctx.message.delete()
    numbers = ["", ""]
    embed = discord.Embed(title="RaNdOm NuMbEr", description = str(random.randrange(1, 2000)), color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Restart Commmand
@bot.command()
async def restart(ctx):
    await ctx.message.delete()
    numbers = "1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950"
    embed = discord.Embed(title="Aries Notification", description = "Restarting in 5 seconds...", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
    await asyncio.sleep(5000)
    await exit()
#Boobs Command
@bot.command()
async def boobs(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Aries Boobs", description = "Showing el boobies", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    embed.set_image(url= "https://external-preview.redd.it/_8von5M373BhKDn4sUUtZO0ejyegPnjYcaboJ4LHG18.jpg?width=640&crop=smart&auto=webp&s=08da86e1978676e513b91a2dbc3d88725fb75db1")
    await ctx.send(embed=embed)
#Status Command
@bot.command()
async def status(ctx, *args):
    await ctx.message.delete()
    #AFK
    embed = discord.Embed(title="Aries Notification", description = "Changed Status to AFK", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    #Online
    embed1 = discord.Embed(title="Aries Notification", description = "Changed Status to Online", color=0x493BB9)
    embed1.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed1.set_footer(text = "made with ♡ by bomt")
    #DND
    embed2 = discord.Embed(title="Aries Notification", description = "Changed Status to DND", color=0x493BB9)
    embed2.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed2.set_footer(text = "made with ♡ by bomt")
    stati = {
        "on":       Status.online,
        "online":   Status.online,
        "off":      Status.invisible,
        "offline":  Status.invisible,
        "dnd":      Status.dnd,
        "idle":     Status.idle,
        "afk":      Status.idle
    }
    if args:
        if (args[0] in stati):
            #Checks if Args are equal to AFK ex .status the args would be after status
            if (args[0] == "afk"):
                await bot.change_presence(status=Status.idle, afk=True)
                await ctx.send(embed=embed)
    if (args[0] == "dnd"):
        await bot.change_presence(status=Status.dnd, afk=False)
        await ctx.send(embed=embed2)
    if (args[0] == "online"):
        await bot.change_presence(status=stati[args[0]], afk=False)
        await ctx.send(embed=embed1)
#UserInfo Command
@bot.command()
async def userinfo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Aries Userinfo", description = "Name: " + str(bot.user) + "\nUsers In: " + str(len(bot.guilds)) + " Guilds" + "\nAvatar ↓ ", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    embed.set_image(url = str(bot.user.avatar_url))
    await ctx.send(embed = embed)
#todo command
@bot.command()
async def todo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Aries Todo", description = "New UI\nSecurity\nFinish 30 Commands", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
#Sniper Command
@bot.command()
async def sniper(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title= "Aries Nitro Sniper", description = "", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
#Avatar Command
@bot.command()
async def avatar(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title= str(bot.user) + "'s Avatar", description = "", color=0x493BB9)
    embed.set_image(url = str(bot.user.avatar_url))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
    #Sniper Command
@bot.command()
async def allah(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title= "I AM ALLAH" + "'s Avatar", description = "ALLAH HAS SPOKEN GET ARIES", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def pickup(ctx):
    await ctx.message.delete()
    pickuplines = ["if you were a booger, i'd pick you first", "sup, are you from tennessee? cause your the only 10 i see ", "basic math: add the bed, subtract the clothes, divide the legs, and pray we don't multiply ", "you're so hot, my zipper is falling for you", "Are you an elevator? Because I’ll go up and down on you."]
    embed = discord.Embed(title= "Aries Pickup line", description = random.choice(pickuplines), color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def joke(ctx):
    await ctx.message.delete()
    jokes = ["Why did the orange lose the race? It ran out of juice.", "How you fix a broken pumpkin? With a pumpkin patch", "What's the best thing about Switzerland? I don't know, but the flag is a big plus.", "Why do peppers make such good archers? Because they habanero.", "What did the sink tell the toilet? You look flushed!", "Can February March? No, but April May!Can February March? No, but April May!", "I hated facial hair but then it grew on me.", ]
    embed = discord.Embed(title= "Aries The Comedian", description = random.choice(jokes), color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def rickroll(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title= "Aries Just Ricked YOU!", description = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/758834492931833938/894667218875461652/unknown.png")
    embed.set_image(url = "https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed) 
@bot.command()
async def invite(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title= "Aries Invite", description = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed) 
@bot.command()
async def notes(ctx):
    await ctx.message.delete()
    with open("./data/note.json") as f:
     config = json.load(f)
    embed = discord.Embed(title= "Aries Notes", description = str(config.get()), color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def copy(ctx, person):
    await ctx.message.delete()
    with open("./data/note.json") as f:
     embed = discord.Embed(title= "Aries Notification", description = "Now Copying: " + person, color=0x493BB9)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def leave(ctx,):
    await ctx.message.delete()
    guild = ctx.guild
    print(Fore.CYAN + "Info" + Fore.RESET + " | " + Fore.LIGHTCYAN_EX + "[!] " + Fore.CYAN + "Left Server » " + Fore.LIGHTCYAN_EX + str(guild))
    await asyncio.sleep(1)
    await guild.leave()
try:
#Runs Bot
    bot.run(token)
#Catch Error
except discord.errors.LoginFailure:
    print("Failed to log into provided token")