from pyrogram import Client as Sree, filters
from pyrogram.types import Message



@Sree.on_message(filters.service)
async def service(bot, Message):
    await Message.delete()
