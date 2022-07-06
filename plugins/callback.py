from pyrogram import Client as Sree, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkupasspass




    elif msg.data == "jeeva":
        buttons = [[
            InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('👥 ᴜᴘᴅᴀᴛᴇs', url='https://t.me/movies_club_2019'),
            InlineKeyboardButton('ɢʀᴏᴜᴘ 👥', url='https://t.me/UrvashiTheaters')
            ],[
            InlineKeyboardButton('🦋 ꜱᴛᴀᴛꜱ ', callback_data='stats'),
            InlineKeyboardButton(' ᴀʙᴏᴜᴛ 🦋', callback_data='about')
            ],[
            InlineKeyboardButton('❌ ᴄʟᴏꜱᴇ ᴛʜᴇ ᴘᴀɢᴇ ❌', callback_data='close_pages')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="🤣",
            reply_markup=reply_markup
        )
