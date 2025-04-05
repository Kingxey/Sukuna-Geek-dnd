class script(object):   
    HELP_TXT = """ʜᴇʏ {}\nʜᴇʀᴇ ɪꜱ ᴍʏ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅꜱ"""

    ABOUT_TXT = """- ᴍʏ ɴᴀᴍᴇ : {}
- ᴄʀᴇᴀᴛᴏʀ : <a href=https://t.me/hyoshAssistantBot>ʜʏᴏꜱʜ ᴄᴏᴅᴇ</a>
- ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
- ʟᴀɴɢᴀɢᴇ : ᴘʏᴛʜᴏɴ 3.10
- ᴅᴀᴛᴀ ʙᴀꜱᴇ : ᴍᴏɴɢᴏᴅʙ
- ʙᴏᴛ ꜱᴇʀᴠᴇʀ : ᴀɴʏᴡʜᴇʀᴇ
- ʙᴜɪʟᴅ ᴠᴇʀꜱɪᴏɴ : ᴘʀᴏꜰᴇꜱꜱᴏʀ-ʙᴏᴛ 𝚟3.0.0"""

    SOURCE_TXT = """<b>ɴᴏᴛᴇ:</b>
- ᴄᴏᴅᴇ ꜱᴏᴜʀᴄᴇꜱ ɪᴄɪ 👉:<a href=https://t.me/hyoshAssistantBot>ʜʏᴏꜱʜ ᴄᴏᴅᴇ</a>

<b>ᴅᴇᴠꜱ:</b>
- 𝙳𝚎𝚟 1 : <a href=https://t.me/hyoshAssistantBot>ʜʏᴏꜱʜ ᴄᴏᴅᴇ</a>
"""

    FILE_TXT = """➤ʜᴇʟᴘ : ꜰɪʟᴇ ꜱᴛᴏʀᴇ ᴍᴏᴅᴜʟᴇ../

<b>ʙʏ ᴜꜱɪɴɢ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴛᴏʀᴇ ꜰɪʟᴇꜱ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇ ꜱᴀᴠᴇᴅ ꜰɪʟᴇꜱ. ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴀ ᴘᴜʙʟɪᴄ ᴄʜᴀɴɴᴇʟ ꜱᴇɴᴅ ᴛʜᴇ ꜰɪʟᴡ ʟɪɴᴋ ᴏɴʟʏ ᴏʀ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ʏᴏᴜ ᴍᴜꜱᴛ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴏɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ꜰɪʟᴇ....//</b>

⪼ ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ ›

➪ /ᴘʟɪɴᴋ ›› ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇᴅɪᴀ ᴛᴏ ɢᴇᴛ ʟɪɴᴋ.
➪ /ᴘʙᴀᴛᴄʜ ›› ᴜꜱᴇ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ʟɪɴᴋ ᴡɪᴛʜ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.
➪ /ʙᴀᴛᴄʜ ›› ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ꜰᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ꜰɪʟᴇꜱ.

⪼ ᴇxᴀᴍᴘʟᴇ ›

<code>/batch https://t.me/hokageclub https://t.me/hyoshAssistantBot</code>

ᴄʀᴇᴅɪᴛꜱ ›› <a href=https://t.me/hyoshAssistantBot>ʜʏᴏꜱʜ ᴄᴏᴅᴇ</a>"""
    
    MANUELFILTER_TXT = """ʜᴇʟᴘ:  <b>ꜰɪʟᴛᴇʀꜱ</b>

-ꜰɪʟᴛᴇʀ ɪꜱ ᴛʜᴇ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ᗩᒍᗩ᙭  ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ

<b>ɴᴏᴛᴇ:</b>
1. <b>ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.</b>
2. <b>ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.</b>
3. <b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.</b>

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• <code>/ꜰɪʟᴛᴇʀ</code> - <b>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</b>
• <code>/ꜰɪʟᴛᴇʀꜱ</code> - <b>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</b>
• <code>/ᴅᴇʟ</code> - <b>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</b>
• <code>/ᴅᴇʟᴀʟʟ</code> - <b>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</b>

• <code>/ɢ_ꜰɪʟᴛᴇʀ ᴏꜰꜰ</code> - <b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴏᴀɴᴅ + ᴏɴ/ᴏꜰꜰ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴄᴏɴᴛʀᴏʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ</b>
"""
   
    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>

-ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.

<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[ʙᴜᴛᴛᴏɴ ᴛᴇxᴛ](ʙᴜᴛᴛᴏɴᴜʀʟ:xxxxxxxxxxxx)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[ʙᴜᴛᴛᴏɴ ᴛᴇxᴛ](ʙᴜᴛᴛᴏɴᴀʟᴇʀᴛ:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>
"""

    AUTOFILTER_TXT = """**ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ᴏɴ/ᴏꜰꜰ ᴍᴏᴅᴜʟᴇ..
<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ</b>

• /ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ᴏɴ - ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ᴇɴᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ
• /ᴀᴜᴛᴏ꜀ɪʟᴛᴇʀ ᴏꜰꜰ - ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ᴅɪꜱᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ 

ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ɪꜱ ᴛʜᴇ ꜰᴇᴀᴛᴜʀᴇ ᴛᴏ ꜰɪʟᴛᴇʀ ᴀɴᴅ ꜱᴀᴠᴇ ᴛʜᴇ ꜰɪʟᴇꜱ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜰʀᴏᴍ ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴇ **ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ᴏɴ/ᴏꜰꜰ ᴍᴏᴅᴜʟᴇ..
&lt;ᴜ&gt;ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ<!--ᴜ-->

• /ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ᴏɴ - ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ᴇɴᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ
• /ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ᴏꜰꜰ - ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ᴅɪꜱᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ 

ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ɪꜱ ᴛʜᴇ ꜰᴇᴀᴛᴜʀᴇ ᴛᴏ ꜰɪʟᴛᴇʀ ᴀɴᴅ ꜱᴀᴠᴇ ᴛʜᴇ ꜰɪʟᴇꜱ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜰʀᴏᴍ ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴏɴ ᴀɴᴅ ᴏꜰꜰ ᴛʜᴇ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ..

ᴄᴏᴍᴍᴀɴᴅꜱ :-
›› /ꜱᴇᴛ_ᴛᴇᴍᴘʟᴀᴛᴇ - ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ꜰᴏʀ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ.
›› /ɢᴇᴛ_ᴛᴇᴍᴘʟᴀᴛᴇ - ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ᴏꜰ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ.

ᴄʀᴇᴅɪᴛꜱ : - <a href=https://t.me/hyoshAssistantBot>ʜʏᴏꜱʜ ᴄᴏᴅᴇ</a**"""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>

- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>ɴᴏᴛᴇ:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>ɴᴏᴛᴇ:</b>
these are the extra features of this bot

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

🔋 <u><b>Basic Command</b></u>
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.</code>

🗂️ <u><b>Database & Server Command</b></u>
• /status - <code>ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ sᴇʀᴠᴇʀ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ᴅᴀᴛᴀᴛʙᴀꜱᴇ ꜱᴛᴀᴛᴜꜱ</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /deleteall - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴇs ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>"""

    US_CHAT_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

📯 <u><b>Chat & User</b></u>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /group_broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /invite - <code>Tᴏ ɢᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ᴄʜᴀᴛ ᴡʜᴇʀᴇ ᴛʜᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ.</code>
• /ban_user  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban_user  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /restart - <code>Tᴏ Rᴇsᴛᴀʀᴛ ᴀ Bᴏᴛ</code>
• /usend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssɢᴀᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Usᴇʀ</code>
• /gsend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssᴀɢᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ</code>

• /clear_junk - clear all delete account & blocked account in database 
• /clear_junk_group - clear add removed group or deactivated groups on db"""

    G_FIL_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

🔥 <u><b>Adv Global Filter </b></u>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs<code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ</code>
"""

    STATUS_TXT = """<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code></b>
<b>᚛› 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>
<b>᚛› 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {a}(<code>{b}</code>)</b>
<b>᚛› 𝐆 𝐈𝐃 ⪼ @{c}
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ {d}</b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {e}</b>

By {f}
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
<b>᚛› 𝐔𝐍 - @{}</b>

By @{} """
   
    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /ɪɴᴋɪᴄᴋ - ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʀᴇQᴜɪʀᴇᴅ ᴀʀɢᴜᴍᴇɴᴛꜱ ᴀɴᴅ ɪ ᴡɪʟʟ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀꜱ ꜰʀᴏᴍ ɢʀᴏᴜᴘ.
• /ɪɴꜱᴛᴀᴛᴜꜱ - ᴛᴏ ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀ ꜰʀᴏᴍ ɢʀᴏᴜᴘ.
• /ɪɴᴋɪᴄᴋ ᴡɪᴛʜɪɴ_ᴍᴏɴᴛʜ ʟᴏɴɢ_ᴛɪᴍᴇ_ᴀɢᴏ - ᴛᴏ ᴋɪᴄᴋ ᴜꜱᴇʀꜱ ᴡʜᴏ ᴀʀᴇ ᴏꜰꜰʟɪɴᴇ ꜰᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ 6-7 ᴅᴀʏꜱ.
• /ɪɴᴋɪᴄᴋ ʟᴏɴɢ_ᴛɪᴍᴇ_ᴀɢᴏ - ᴛᴏ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀꜱ ᴡʜᴏ ᴀʀᴇ ᴏꜰꜰʟɪɴᴇ ꜰᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ ᴀ ᴍᴏɴᴛʜ ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ.
• /ᴅᴋɪᴄᴋ - ᴛᴏ ᴋɪᴄᴋ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ."""

    IMAGE_TXT = """➤ 𝐇𝐞𝐥𝐩: Iᴍᴀɢᴇ

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚎𝚍𝚒𝚝 𝚒𝚖𝚊𝚐𝚎 𝚟𝚎𝚛𝚢 𝚎𝚊𝚜𝚒𝚕𝚢 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺 𝗂𝗆𝖺𝗀𝖾 𝗍𝗈 𝖾𝖽𝗂𝗍 ✨

𝖬𝖺𝖽𝖾 𝖻𝗒 <a href=https://t.me/mr_MKN>Mr.MKN TG</a>"""

    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜꜱᴇ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴛʜᴇɪʀ ɢʀᴏᴜᴘ ᴍᴏʀᴇ ᴇꜰꜰɪᴄɪᴇɴᴛʟʏ.

➪/ʙᴀɴ: ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.
➪/ᴜɴʙᴀɴ: ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
➪/ᴛʙᴀɴ: ᴛᴏ ᴛᴇᴍᴘᴏʀᴀʀɪʟʏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.
➪/ᴍᴜᴛᴇ: ᴛᴏ ᴍᴜᴛᴇ ᴀ ᴜꜱᴇʀ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
➪/ᴜɴᴍᴜᴛᴇ: ᴛᴏ ᴜɴᴍᴜᴛᴇ ᴀ ᴜꜱᴇʀ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
➪/ᴛᴍᴜᴛᴇ: ᴛᴏ ᴛᴇᴍᴘᴏʀᴀʀɪʟʏ ᴍᴜᴛᴇ ᴀ ᴜꜱᴇʀ.

➤ ɴᴏᴛᴇ:
ᴡʜɪʟᴇ ᴜꜱɪɴɢ /ᴛᴍᴜᴛᴇ ᴏʀ /ᴛʙᴀɴ ʏᴏᴜ ꜱʜᴏᴜʟᴅ ꜱᴘᴇᴄɪꜰʏ ᴛʜᴇ ᴛɪᴍᴇ ʟɪᴍɪᴛ.

➛ᴇxᴀᴍᴘʟᴇ: /ᴛʙᴀɴ 2ᴅ ᴏʀ /ᴛᴍᴜᴛᴇ 2ᴅ.
ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴠᴀʟᴜᴇꜱ: ᴍ/ʜ/ᴅ.
 • ᴍ = ᴍɪɴᴜᴛᴇꜱ
 • ʜ = ʜᴏᴜʀꜱ
 • ᴅ = ᴅᴀʏꜱ"""


    PIN_TXT ="""<b>PIN MODULE</b>
<b>𝙿𝙸𝙽 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴../</b>

<b>𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙿𝙻𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴::</b>

<b>📌𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴📌</b>

◉ /pin :- 𝚃𝙾 𝙿𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂
◉ /unpin :- 𝚃𝙾 𝚄𝙽𝙿𝙸𝙽 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙴𝙽𝚃 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝙰𝙰𝙶𝙴"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• These commands works on both pm and group.
• These commands can be used by any group member."""

    TTS_TXT = """Help: <b> TTS 🎤 module:</b>

Translate text to speech

<b>Commands and Usage:</b>

• /tts <text> : convert text to speech

<b>NOTE:</b>

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""

    PINGS_TXT ="""<b>🌟 Ping:</b>

Helps you to know your ping 🚶🏼‍♂️

<b>Commands:</b>

• /alive - To check you are alive.
• /ping - To get your ping.
<b>🏹Usage🏹 :</b>

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me this command reply with Picture or Vide Under (5MB) 

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""

    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""

    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>ɪ ᴡᴏɴ'ᴛ ɢᴏ ᴡʜᴇʀᴇ ɪ ʜᴀᴠᴇɴ'ᴛ ʙᴇᴇɴ ᴍᴀᴅᴇ ᴀɴ ᴀᴅᴍɪɴ, ʙɪɪ... ᴀᴅᴅ ᴍᴇ ᴀɢᴀɪɴ ᴡɪᴛʜ ᴀʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛꜱ.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ʟᴇᴛ'ꜱ ɴᴏᴡ ʟᴇᴀᴠᴇ ᴇᴠᴇʀʏᴛʜɪɴɢ ʙᴇʜɪɴᴅ...</b>"""
      
    CARB_TXT = """☾︎ʜᴇʟᴘ ꜰᴏʀ ᴄᴀʀʙᴏɴ☽︎
ᴄᴀʀʙᴏɴ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀꜱ ꜱʜᴏᴡɴ ɪɴ ᴛʜᴇ ᴛᴏᴘ ᴡɪᴛʜ ʏᴏᴜʀ ᴛᴇxᴛꜱ.
ꜰᴏʀ ᴜꜱɪɴɢ ᴛʜᴇ ᴍᴏᴅᴜʟᴇ ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴛʜᴇ ᴛᴇxᴛ ᴀɴᴅ ʀᴇᴘʟʏ ᴛᴏ ɪᴛ ᴡɪᴛʜ /ᴄᴀʀʙᴏɴ ᴄᴏᴍᴍᴀɴᴅ ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ."""

    FOND_TXT = """☾︎ʜᴇʟᴘ ꜰᴏʀ ꜰᴏɴᴛꜱ☽︎
ꜰᴏɴᴛ ɪꜱ ᴀ ᴍᴏᴅᴜʟᴇ ꜰᴏʀ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴛᴇxᴛ ꜱᴛʏʟɪꜱʜ.
ꜰᴏʀ ᴜꜱᴇ ᴛʜᴀᴛ ꜰᴇᴀᴛᴜʀᴇ ᴛʏᴘᴇ /ꜰᴏɴᴛ <ʏᴏᴜʀ ᴛᴇxᴛ>; ᴛʜᴇɴ ʏᴏᴜʀ ᴛᴇxᴛ ɪꜱ ʀᴇᴀᴅʏ."""

    SHARE_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗦𝗛𝗔𝗥𝗘 𝗧𝗘𝗫𝗧☽︎

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
•/ꜱʜᴀʀᴇ - ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀɴʏ ᴛᴇxᴛ ᴛᴏ ꜱᴇɴᴅ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ"""

    YTDL = """<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴</b>

🍁 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘖𝘳 𝘈𝘶𝘥𝘪𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• /song 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 
• /video or /mp4 𝘈𝘯𝘥 https://youtu.be/*****

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/song mkn</code>
<code>/mp4 https://youtu.be/*******</code>
<code>/video https://youtu.be/*****</code>  """


    


    

