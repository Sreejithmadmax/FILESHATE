import os
import random
import asyncio
from Script import script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import re
import json




@sree.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))


@sree.on_message(filters.regex("Money Heist") & filters.group)
async def my_handle56814(bot, message):
    await message.reply_photo( 
        photo="https://telegra.ph/file/e442a24f233fac96ce83f.jpg",
        caption="𝙼𝙾𝚅𝙸𝙴 : Money Heist",
        reply_markup=InlineKeyboardMarkup(movie1_down_2)
    )

movie1_down_2 = [[                                                 
                  InlineKeyboardButton("Seasons", callback_data="start"),
                  InlineKeyboardButton("close", callback_data="close")
                  ]]
