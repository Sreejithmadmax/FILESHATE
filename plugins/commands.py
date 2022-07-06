import os
import random
import asyncio
from scripts import Scripted
from pyrogram import Client as Sree, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import re





@Sree.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    buttons = [[
        InlineKeyboardButton('Dev', url='https://t.me/PromotionMediator'),
        InlineKeyboardButton('Source', url ='https://t.me/PromotionMediator')
    ],[
        InlineKeyboardButton('Help', callback_data="help")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
         photo="https://telegra.ph/file/452d89674fecc5f6ac878.jpg",
         caption = "(づ｡◕‿‿◕｡)づ\n\n ι αм тєѕт вσт \n\n¢яєαтє∂ ву🤝 @UrvashiTheaters ٩(˘◡˘)۶",
         reply_markup = reply_markup            
     )          
