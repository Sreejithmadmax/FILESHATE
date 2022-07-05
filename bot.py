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

movie1_down_1 = [[                                                 
                  InlineKeyboardButton("🄳🄾🅆🄽🄻🄾🄰🄳", url="https://t.me/Autofilterv50_bot?start=Z2V0LTk0MTU3NjEyMDczMDE0LTk5MTY1OTk1NjkzOTE5")
                  ],[
                  InlineKeyboardButton("🄲🄻🄾🅂🄴", callback_data="close")
                  ]]
     
@sree.on_callback_query()
async def callback(bot, msg: CallbackQuery): 
    if msg.data == "close":
      await msg.message.delete()       
                               
@sree.on_message(filters.regex("ayan") & filters.group)
async def my_handle56814(bot, message):
    await message.reply_photo( 
        photo="https://telegra.ph/file/0797dc53ae22aae6d4fc9.jpg",
        caption="""☞ 𝙼𝙾𝚅𝙸𝙴 : Ayan
☞ 𝚈𝙴𝙰𝚁 : 2009
☞ 𝚀𝚄𝙰𝙻𝙸𝚃𝚈 : 720p,1080p, 480p
☞ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝚃𝙰𝙼𝙸""",
        reply_markup=InlineKeyboardMarkup(movie1_down_1)
    )

movie1_down_2 = [[                                                 
                  InlineKeyboardButton("D O W N L O A D", url="https://t.me/c/1314197326/2"),
                  InlineKeyboardButton("close", callback_data="close")
                  ]]       

@sree.on_message(filters.regex("movie2") & filters.group)
async def my_handle56814(bot, message):
    await message.reply_photo( 
        photo="https://telegra.ph/file/f6f4d7cf4452f2c63dd3d.jpg",
        caption="""☞ 𝙼𝙾𝚅𝙸𝙴 :
☞ 𝚈𝙴𝙰𝚁 :
☞ 𝚀𝚄𝙰𝙻𝙸𝚃𝚈 : 720p,1080p, 480p
☞ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙷𝙸𝙽𝙳𝙸, 𝙼𝙰𝙻𝙰𝚈𝙰, 𝚃𝙰𝙼𝙸, 𝚃𝙴𝙻""",
        reply_markup=InlineKeyboardMarkup(movie1_down_2)
    )

ajvad.run() 
