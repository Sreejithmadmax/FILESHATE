from pyrogram import Client as Sree, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@sree.on_callback_query()
async def callback(bot, msg: CallbackQuery): 
    if msg.data == "close":
      await msg.message.delete()    
