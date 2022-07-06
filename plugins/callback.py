from pyrogram import Client as Sree, filters
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Sree.on_callback_query(filters.regex(r"^(start|help|about|close)$"), group=2)
async def callback_data(bot, message: CallbackQuery):

    query_data = message.data

    if query_data == "start":
        buttons = [[
        InlineKeyboardButton('Developers', url='https://t.me/CrazyBotsz'),
        InlineKeyboardButton('Source Code 🧾', url ='https://github.com/CrazyBotsz/Adv-Auto-Filter-Bot-V2')
    ],[
        InlineKeyboardButton('Support 🛠', url='https://t.me/CrazyBotszGrp')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await message.message.edit_caption(
            "Hai",
            reply_markup=reply_markup
        )


    elif query_data == "help":
        buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await message.message.edit_caption(
            "hai",
            reply_markup=reply_markup
        )


    elif query_data == "about": 
        buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await message.message.edit_caption(
            "hai",
            reply_markup=reply_markup
        )


    elif query_data == "help_me":
        await update.answer("Do", show_alert=True)

    elif query_data == "close":
        await update.message.delete()   
