import random
import re
import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from fansx.config import OWNER_ID
import psutil
from fansx import *
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import *

from fansx import *

@PY.BOT("freepirzy")
async def _(client, message):
    buttons = BTN.ALWAYSBOYSZ(message)
    sh = await message.reply("""<u><b>𝗙𝗜𝗧𝗨𝗥 𝗙𝗥𝗘𝗘 𝗣𝗜𝗥𝗭𝗬 𝗨𝗦𝗘𝗥𝗕𝗢𝗧!</b></u>
<blockquote><b>/ai -  ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴍᴜ</b>
<b>/brat - ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇxᴛ ᴜɴᴛᴜᴋ ᴅɪ ᴊᴀᴅɪᴋᴀɴ ғᴏᴛᴏ</b>
<b>/adzan - ᴍᴀsᴜᴋᴋᴀɴ ᴋᴏᴛᴀ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴊᴀᴅᴡᴀʟ ᴀᴅᴢᴀɴ</b>
<b>/tourl - ʀᴇᴘʟʏ ғᴏᴛᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪ ᴊᴀᴅɪᴋᴀɴ ʟɪɴᴋ</b>
<b>/tiktok - ʙᴇʀɪᴋᴀɴ ʟɪɴᴋ ᴠᴛ/ʟɪɴᴋ ғɪᴅɪᴏ ᴛɪᴋᴛᴏᴋ ᴜɴᴛᴜᴋ ᴅɪ ᴅᴏᴡɴʟᴏᴀᴅ</b></blockquote>

<blockquote><b>ᴏᴡɴᴇʀ ᴜsᴇʀʙᴏᴛ ᴅɪʙᴀᴡᴀʜ sɪɴɪʜ</b>
<b>ᴏᴡɴᴇʀ ᴜsᴇʀʙᴏᴛ: <a href=https://t.me/Pirzyy1>owner pirzy</a></b></blockquote>""", reply_markup=InlineKeyboardMarkup(buttons))