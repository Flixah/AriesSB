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

from CEA256 import *
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
# Aries Functions

class aries:
    def console(clear=False):
        if clear:
            os.system("cls")
        print(Fore.RED + logo + Fore.RESET)

aries.console()