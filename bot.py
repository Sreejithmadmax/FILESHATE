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

START_MSG = "<b>Hai {} Bro No Help😂</b>"

   
@sree.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    button = [[
        InlineKeyboardButton(f'🤴 𝙳𝙴𝚅', url=f'https://t.me/PromotionMediator'),
        InlineKeyboardButton(f'𝙰𝙱𝙾𝚄𝚃 🔎', callback_data='about')
        ],[
        InlineKeyboardButton(f'♻️ 𝙷𝙴𝙻𝙿 ♻️', callback_data="help")
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    await message.reply_photo(
         photo="https://telegra.ph/file/e442a24f233fac96ce83f.jpg",
         caption = START_MSG.format(message.from_user.mention),  
         reply_markup = reply_markup            
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
            text="☞ 𝙼𝙾𝚅𝙸𝙴 : Ayan\n☞ 𝚈𝙴𝙰𝚁 : 2009\n☞ 𝚀𝚄𝙰𝙻𝙸𝚃𝚈 : 720p,1080p, 480p\n☞ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝚃𝙰𝙼𝙸",
            reply_markup=reply_markup
        )
    elif msg.data == "kalippan":
        movie1_down_2 = [[                                                 
                  InlineKeyboardButton("Seasons", callback_data="start"),
                  InlineKeyboardButton("close", callback_data="close")
                  ]]
        reply_markup = InlineKeyboardMarkup(movie1_down_2)
        await msg.message.edit_text(
            text="☞ 𝙼𝙾𝚅𝙸𝙴 : Money Heist\n☞ 𝚈𝙴𝙰𝚁 : 2009\n☞ 𝚀𝚄𝙰𝙻𝙸𝚃𝚈 : 720p,1080p, 480p\n☞ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝚃𝙰𝙼𝙸",
            reply_markup=reply_markup
        )
@sree.on_message(filters.command('start') & filters.private)
def start(bot, message):
   text ="കുട്ടാപ്സ് ⚡️",
   reply_markup = InlineKeyboardMarkup(movie1_down_1)
   message.replay(
        text="പോടാ മോനെ ദിനേശാ 😂",
        reply_markup=reply_markup
)
                                
@sree.on_message(filters.regex("Money Heist") & filters.group)
async def my_handle56814(bot, message):
    await message.reply_photo( 
        photo="https://telegra.ph/file/e442a24f233fac96ce83f.jpg",
        caption="""☞ 𝙼𝙾𝚅𝙸𝙴 : Money Heist
☞ 𝚈𝙴𝙰𝚁 : 2009
☞ 𝚀𝚄𝙰𝙻𝙸𝚃𝚈 : 720p,1080p, 480p
☞ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝚃𝙰𝙼𝙸""",
        reply_markup=InlineKeyboardMarkup(movie1_down_2)
    )

movie1_down_2 = [[                                                 
                  InlineKeyboardButton("Seasons", callback_data="start"),
                  InlineKeyboardButton("close", callback_data="close")
                  ]]       

@sree.on_message(filters.regex("ayan") & filters.group)
async def my_handle56814(bot, message):
    await message.reply_photo( 
        photo="https://telegra.ph/file/e442a24f233fac96ce83f.jpg",
        caption="""☞ 𝙼𝙾𝚅𝙸𝙴 :
☞ 𝚈𝙴𝙰𝚁 :
☞ 𝚀𝚄𝙰𝙻𝙸𝚃𝚈 : 720p,1080p, 480p
☞ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙷𝙸𝙽𝙳𝙸, 𝙼𝙰𝙻𝙰𝚈𝙰, 𝚃𝙰𝙼𝙸, 𝚃𝙴𝙻""",
        reply_markup=InlineKeyboardMarkup(movie1_down_2)
    )



sree.run() 
