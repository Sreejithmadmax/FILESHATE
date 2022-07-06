import os
import random
import asyncio
from scripts import Scripted
from pyrogram import Client as Sree, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import re





@Sree.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    button = [[
        InlineKeyboardButton(f'🤴 𝙳𝙴𝚅 🤴', url=f'https://t.me/PromotionMediator')    
        ],[
        InlineKeyboardButton(f'♻️ 𝙷𝙴𝙻𝙿 ♻️', callback_data="help")
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    await message.reply_photo(
         photo="https://telegra.ph/file/e442a24f233fac96ce83f.jpg",
         caption = "(づ｡◕‿‿◕｡)づ\n\n ι αм тєѕт вσт \n\n¢яєαтє∂ ву🤝 @UrvashiTheaters ٩(˘◡˘)۶",
         reply_markup = reply_markup            
     )         
    

@Sree.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(bot, message):
    button = [[
        InlineKeyboardButton(f'🏡 𝙷𝙾𝙼𝙴', callback_data='back'),
        InlineKeyboardButton(f'𝚁𝙴𝙵𝚁𝙴𝚂𝙷 ✅️', callback_data='donate')
        ],[
        InlineKeyboardButton(f'🚫 𝙲𝙻𝙾𝚂𝙴 🚫', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(button)
        await msg.message.edit(
            text="No Help"         
        )

@Sree.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(bot, message):
    button = [[
        InlineKeyboardButton(f'🏡 𝙷𝙾𝙼𝙴', callback_data='back'),
        InlineKeyboardButton(f'𝚁𝙴𝙵𝚁𝙴𝚂𝙷 ✅️', callback_data='donate')
        ],[
        InlineKeyboardButton(f'🚫 𝙲𝙻𝙾𝚂𝙴 🚫', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(button)
        await msg.message.edit(
            text="No about",
        )
  
