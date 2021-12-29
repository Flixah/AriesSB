# ///////////////////////////////////////////////////////////////
# All Imports

import os
import re
import sys
import json
import time
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
import hashlib
import pwinput
import requests
import threading
import pyPrivnote
import subprocess
import pypresence
import webbrowser
import ctypes.wintypes as wintypes
import platform
from gtts import gTTS
from discord import *
from ctypes import windll
from pytube import YouTube
from os import error, name, system
from datetime import datetime
from licensing.models import *
from pypresence import Presence
from discord.ext import commands
from urllib.request import urlopen
from urllib.parse import quote_plus
from time import localtime, strftime
from licensing.methods import Key, Helpers
from colorama import init, Fore, Back, Style
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, has_permissions

init() # Initialize colorama
#Startup
if (os.path.exists("./data/config.json")):
    pass
else:
    token = input("Token: ")
    prefix = input("Prefix: ")
# ///////////////////////////////////////////////////////////////
# Aries Variables

beta = False
version = "2.0.0"
command_amount = "105 "
authSkip = False
motd = "Its getting Chilly!"
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
        with open(f"./data/themes/theme_2.json") as f:
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
        data = {
            "token": f"{token}",
            "prefix": f"{prefix}"
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

def bot_prefix(bot, message):
    """Get the prefix in the config file"""
    with open("./data/config.json") as f:
        config = json.load(f)
    prefix = config.get('prefix')
    return prefix

bot = commands.Bot(bot_prefix, self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off(), status=Status.online)

# ///////////////////////////////////////////////////////////////
# Events

@bot.event
async def on_ready():
    """Prints a ready log."""
    aries.console(clear=True, line=True)
    print(f"{Fore.RED}Logged in as {bot.user}{Fore.RESET}")


# ///////////////////////////////////////////////////////////////
# Commands



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
files.setup()
print("Loading...")
bot_login()