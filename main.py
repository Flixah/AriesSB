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
from notifypy import Notify
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

# ///////////////////////////////////////////////////////////////
# Aries Variables

beta = False
version = "2.0.0"

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
print("Loading...")
bot_login()