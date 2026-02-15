from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from fansx import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ Pemberitahuan</b>
<b>├ Akun : </b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ID : </b> <code>{X.me.id}</code>
<b>╰ Masa aktif telah habis</b></blockquote>
"""

    def START(message):
        return f"""
<blockquote><b>👋 𝐎𝐥𝐚𝐚𝐚 <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

> 𝐅𝐑𝐄𝐄 𝐅𝐈𝐓𝐔𝐑𝐄
/freebiji

𝐏𝐢𝐫𝐳𝐲𝐲 𝐔𝐛𝐨𝐭
<b> 𝐎𝐥𝐚𝐚𝐚 @{bot.me.username} 𝐀𝐝𝐚𝐥𝐚𝐡 𝐛𝐨𝐭 𝐲𝐚𝐧𝐠 𝐝𝐚𝐩𝐚𝐭 𝐦𝐞𝐦𝐛𝐮𝐚𝐭 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐝𝐞𝐧𝐠𝐚𝐧 𝐞𝐟𝐞𝐬𝐢𝐞𝐧 𝐝𝐚𝐧 𝐜𝐞𝐩𝐚𝐭. 𝐁𝐨𝐭 𝐢𝐧𝐢 𝐝𝐢 𝐜𝐢𝐩𝐭𝐚𝐤𝐚𝐧 𝐨𝐥𝐞𝐡 <a href=tg://openmessage?user_id={OWNER_ID}>@zenith_239</a> 𝐉𝐢𝐤𝐚 𝐚𝐝𝐚 𝐤𝐞𝐧𝐝𝐚𝐥𝐚 𝐚𝐭𝐚𝐮 𝐭𝐞𝐫𝐣𝐚𝐝𝐢 𝐞𝐫𝐨𝐫 𝐬𝐞𝐠𝐞𝐫𝐚 𝐡𝐮𝐛𝐮𝐧𝐠𝐢 𝐨𝐰𝐧𝐞𝐫 𝐛𝐨𝐭 𝐢𝐧𝐢 nya</b></blockquote>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├ Qʀɪꜱ ᴀʟʟ ᴘᴀʏᴍᴇɴᴛ </b>
<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ {total}.000</b>
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b> 

OWNER BOT : <a href=tg://openmessage?user_id={OWNER_ID}>@zenith_239</a> 

<b>🛍 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>╭〢Ubotbijijembod_bot</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b>├〢 ᴀᴄᴄᴏᴜɴᴛ </b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b>╰〢ᴜsᴇʀ ɪᴅ </b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """ <blockquote><b>ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇɴᴅᴀʟᴀ sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ  <a href=tg://openmessage?user_id={OWNER_ID}>@zenith_239</a></b></blockquote>
"""
