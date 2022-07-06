import re, asyncio, random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import CallbackQuery
import os

sree = Client(
    "URUVASHI_FILTER",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
START_TXT = """<b>Hᴇʟʟᴏ {}</b>"""
OWNER_TXT = """<b>@PowerOfTg</b>"""

@sree.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    button = [[
        InlineKeyboardButton(f'🤴 𝙳𝙴𝚅', url=f'https://t.me/PromotionMediator')    
        ],[
        InlineKeyboardButton(f'♻️ 𝙷𝙴𝙻𝙿 ♻️', callback_data="help")
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    await message.reply_photo(
         photo="https://telegra.ph/file/e442a24f233fac96ce83f.jpg",
         caption = START_TXT.format(message.from_user.mention),  
         reply_markup = reply_markup            
     )         
    elif query.data == "start":
        button = [[
        InlineKeyboardButton(f'🤴 𝙳𝙴𝚅', url=f'https://t.me/PromotionMediator')
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
            InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_pages')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await msg.message.edit_text(
            text= HELP_TXT.format(message.from_user.mention),
            reply_markup=reply_markup 
        )
    elif query.data == "about":
        buttons= [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await msg.message.edit_text(
            text= OWNER_TXT,
            reply_markup=reply_markup  
        )       
@sree.on_callback_query()
async def callback(bot, msg: CallbackQuery): 
    if msg.data == "close":
      await msg.message.delete()    
  
    elif msg.data == "start":
        buttons = [[
            InlineKeyboardButton('ep 1', url='https://t.me/koiimone')
            ],[
            InlineKeyboardButton('ep2', url='https://t.me/koiimone'),
            InlineKeyboardButton('ep3', url='https://t.me/koiimone')
            ],[
            InlineKeyboardButton('ep5 ', url='https://t.me/koiimone'),
            InlineKeyboardButton(' ep4', url='https://t.me/koiimone')
            ],[
            InlineKeyboardButton('back', callback_data='kalippan')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await msg.message.edit_text(
            text=" 𝙼𝙾𝚅𝙸𝙴 : Money Heist\n 𝚈𝙴𝙰𝚁 : 2009\n 𝚀𝚄𝙰𝙻𝙸𝚃𝚈 : 720p 1080p 480p\n 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝚃𝙰𝙼𝙸",
            reply_markup=reply_markup
        )
    elif msg.data == "kalippan":
        movie1_down_2 = [[                                                 
                  InlineKeyboardButton("Seasons", callback_data="start"),
                  InlineKeyboardButton("close", callback_data="close")
                  ]]
        reply_markup = InlineKeyboardMarkup(movie1_down_2)
        await msg.message.edit_text(
            text=" 𝙼𝙾𝚅𝙸𝙴 : Money Heist\n 𝚈𝙴𝙰𝚁 : 2009\n𝚀𝚄𝙰𝙻𝙸𝚃𝚈 : 720 1080p 480p\n 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝚃𝙰𝙼𝙸",
            reply_markup=reply_markup
        )
                                

sree.run() 
