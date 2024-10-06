# This utilizes PyAutoGui to make a GUI for the user to input the channel IDs, delay, amount, and message to spam. 
# This does not require the user to use a command in the discord server, but instead uses a GUI to input the information and start the bot.
# Supports singular and multiple tokens at once. 
# Requires PySimpleGui to be installed:
# pip install pysimplegui
# You need to make an individual account on PySimpleGui to keep using it.

# Use tokens.txt to store your bot tokens, one per line.
# Use channel.json to store the channel IDs for each token when wanting to start all tokens at once.
# Do not include the quotation marks around the tokens in the tokens.txt file.

import discord
from discord.ext import commands
import asyncio
import PySimpleGUI as sg
import threading
import os
import json

spammers = {}
stop_events = {}

def load_channel_mapping():
    if os.path.exists(r'channel.json'):
        with open(r'channel.json') as f:
            return json.load(f)
    return {}

def run_bot(token, channel_id, amount, delay, message, stop_event):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    bot = commands.Bot(command_prefix='!', self_bot=True, case_insensitive=True, chunk_guilds_at_startup=False, request_guilds=False)

    @bot.event
    async def on_ready():
        print(f'Bot with token {token[:10]}... ready.')
        await spam_messages(channel_id, amount, delay, message, stop_event)

    async def spam_messages(channel_id, amount, delay, message, stop_event):
        try:
            channel = bot.get_channel(int(channel_id))
            if not channel:
                print(f"Could not retrieve channel with ID {channel_id}")
                return
            
            for i in range(amount):
                if stop_event.is_set():
                    print(f"Stopping spamming for token {token[:10]}...")
                    break
                await channel.send(message)
                await asyncio.sleep(delay)
        
        except Exception as e:
            print(f"Error sending messages: {e}")

    loop.run_until_complete(bot.start(token))

def start_spamming(token, channel_id, amount, delay, message):
    stop_event = threading.Event()  
    stop_events[token] = stop_event  

    bot_thread = threading.Thread(target=run_bot, args=(token, channel_id, amount, delay, message, stop_event), daemon=True)
    bot_thread.start()
    spammers[token] = bot_thread

def stop_spamming(token=None):
    global spammers, stop_events
    if token:
        stop_event = stop_events.get(token)
        if stop_event:
            stop_event.set()  
        print(f"Stopping spam for token {token[:10]}...")
    else:
        for token, stop_event in stop_events.items():
            stop_event.set()  
        print("Stopping spam for all tokens.")

def load_tokens():
    if os.path.exists(r'tokens.txt'):
        with open(r'tokens.txt') as f:
            tokens = [line.strip() for line in f.readlines()] 
            return tokens
    return []

def start_all_tokens(amount, delay, message):
    tokens = load_tokens()
    for token in tokens:
        channel_id = channel_mapping.get(token) 
        if channel_id:
            print(f"Starting spamming for token: {token[:10]}")
            start_spamming(token, channel_id, amount, delay, message)
        else:
            print(f"Channel ID not found for token: {token[:10]}, please check your JSON file.")

layout = [
    [sg.Text("Select Token")],
    [sg.Combo(load_tokens(), key="TOKEN", size=(82, 1), enable_events=True)],
    [sg.Text("Channel ID (for Start Spamming)"), sg.InputText(key="CHANNEL_ID", size=(40, 1))],
    [sg.Text("Amount of Messages"), sg.InputText(key="AMOUNT", size=(40, 1))],
    [sg.Text("Delay (seconds)"), sg.InputText(key="DELAY", size=(40, 1))],
    [sg.Text("Message to Send"), sg.InputText(key="MESSAGE", size=(40, 1))],
    [sg.Button("Start Spamming"), sg.Button("Start All Tokens"), sg.Button("Stop Spamming"), sg.Button("Stop All Tokens"), sg.Button("Exit")]
]

window = sg.Window("Discord Spammer GUI", layout)
channel_mapping = load_channel_mapping()

def check_threads():
    finished_tokens = []
    for token, thread in spammers.items():
        if not thread.is_alive():
            finished_tokens.append(token)
    
    for token in finished_tokens:
        del spammers[token]
        del stop_events[token]
        print(f"Thread for token {token[:10]} has finished.")

def event_loop():
    while True:
        event, values = window.read(timeout=100)  

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Start Spamming":
            token = values["TOKEN"]
            channel_id = values["CHANNEL_ID"]  
            amount = int(values["AMOUNT"])
            delay = int(values["DELAY"])
            message = values["MESSAGE"]

            if token and channel_id and amount and delay and message:
                start_spamming(token, channel_id, amount, delay, message)
                sg.popup("Spamming started with token: " + token[:10] + "...")
            else:
                sg.popup("Please fill in all fields, including Channel ID.")

        if event == "Start All Tokens":
            amount = int(values["AMOUNT"])
            delay = int(values["DELAY"])
            message = values["MESSAGE"]

            if amount and delay and message:
                start_all_tokens(amount, delay, message)
                sg.popup("Spamming started for all tokens. Check the console for details.")
            else:
                sg.popup("Please fill in all fields.")

        if event == "Stop Spamming":
            token = values["TOKEN"]
            if token:
                stop_spamming(token)
                sg.popup("Spamming stopped for token: " + token[:10] + "...")
            else:
                sg.popup("Please select a token.")

        if event == "Stop All Tokens":
            stop_spamming()
            sg.popup("Spamming stopped for all tokens.")

        check_threads()

    window.close()

event_thread = threading.Thread(target=event_loop, daemon=True)
event_thread.start()

event_thread.join()
