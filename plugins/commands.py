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
         caption = "Hai",
         reply_markup = reply_markup            
     )         
    elif query.data == "start":
        button = [[
        InlineKeyboardButton(f'🤴 𝙳𝙴𝚅 🤴', url=f'https://t.me/PromotionMediator')
        ],[
        InlineKeyboardButton(f'♻️ 𝙷𝙴𝙻𝙿 ♻️', callback_data="help")
    ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text= START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup
        )
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('About', callback_data='about')
            ],[
            InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await msg.message.edit_text(
            text= "No Help Click about Know More😒",
            reply_markup=reply_markup 
        )
    elif query.data == "about":
        buttons= [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await msg.message.edit_text(
            text= "@UrvashiTheaters",
            reply_markup=reply_markup  
        )       
@Sree.on_callback_query()
async def callback(bot, msg: CallbackQuery): 
    if msg.data == "close":
      await msg.message.delete()    
  
    
