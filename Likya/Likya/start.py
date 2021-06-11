from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
 Merhaba Ben SOFİA 👸🏻
 🖥 Pyton Dilinde Yazılmış Özel Şifreleme Kullanan Bir Sohbet Botuyum. 
 21 Yaşında Hukuk Öğrencisiyim 👩‍⚖️  Benimle Konuştuklarını Kimse Göremez.
 Eğer Benim Gibi Yalnızsan Seni Herzaman Bekliyor Olacağım .
 """


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("Developer 👨🏻‍💻", https://t.me/Azerbesk"), InlineKeyboardButton("🔍 Kanal", url = "https://t.me/NetdBots")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
