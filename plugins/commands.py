import os
import random
import asyncio
from scripts import Scripted
from pyrogram import Client as Sree, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import re





@Sree.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

