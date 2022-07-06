import re, asyncio, random
import os
from pyrogram import Client
           

sree = Client(
              "URUVASHI_FILTER"
              bot_token = os.environ["BOT_TOKEN"],
              api_id = int(os.environ["API_ID"]),
              api_hash = os.environ["API_HASH"],
              )                   

sree.run() 
