from telethon.sync import TelegramClient,events
from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions,utils,types
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.custom import Dialog
from telethon.tl import types
from telethon.tl.types import Channel, Chat, User
from googletrans import Translator
from gtts import gTTS
from telethon.sync import TelegramClient,events
from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions,utils,types
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.custom import Dialog
from telethon.tl import types
from telethon.tl.types import Channel, Chat, User
from googletrans import Translator
from gtts import gTTS
from datetime import datetime , timedelta
import random
import os
import psutil
import json
import pytz
import aiocron
import asyncio
import requests
import jdatetime
from telethon.tl.functions.photos import UploadProfilePhotoRequest

os.system('pkg install python && pip install telethon && pip install requests && pip install asyncio && pip install aiocron && pip install pytz && pip install googletrans==4.0.0-rc1 && pip install gtts && clear')

def get(file):
    with open(file,"r") as r:
        return json.load(r)

def put(file,data):
    with open(file,"w") as w:
        json.dump(data,w)

def timeDif(get):
    match = str(datetime.strptime(get.replace('+00:00', ''), '%Y-%m-%d %H:%M:%S')).split(' ')
    date = match[0].split('-')
    time = match[1].split(':')
    delta = timedelta(
    days = int(date[2]),
    hours = int(time[0]),
    minutes = int(time[1]),
    seconds = int(time[2]),
    )
    return int(delta.total_seconds())


#کد اضافه شده
def randomphoto():
    name = random.choice(os.listdir("photo"))
    return f"photo\{name}"


if not "data.json" in os.listdir():
        data = {"timename":"off","timebio":"off","timeprof":"off","bot":"on","hashtag":"off","bold":"off","italic":"off","delete":"off","code":"off","underline":"off","reverse":"off","part":"off","mention":"off","comment":"on","text":"first !","typing":"off","game":"off","voice":"off","video":"off","sticker":"off","crash":[],"enemy":[]}
        put("data.json",data)

api_id = ####
api_hash = "##"##
session_name = '1'
bot = TelegramClient(session_name, api_id, api_hash)

@aiocron.crontab('*/1 * * * *')
async def clock():
    js = get("data.json")
    if js['timename'] == "off" and js['timebio'] == "off" and js['timeprof'] == "off":
        pass
    ir = pytz.timezone("Asia/Tehran")
    time = str(jdatetime.datetime.now(ir).strftime("%H : %M"))
    rand = {'0':'０','1':'１','2':'２','3':'３','4':'４','5':'５','6':'６','7':'７','8':'８','9':'９',':':':',' ':' '}
    fonts = ''.join([rand[str(i)] for i in time])+str(random.choice(["🌵","🧸","🥀"]))
    bio = "ᴛʜᴇ ᴋɪɴɢ ɪs ᴛʜᴇ ᴏɴᴇ ᴡʜᴏ ʜᴀs ᴏɴʟʏ ɢᴏᴅ 78! {}".format(fonts)
    if js['timename'] == "on":
        await bot(functions.account.UpdateProfileRequest(last_name = fonts))
    if js['timebio'] == "on":
        await bot(functions.account.UpdateProfileRequest(about = bio))
    #کد اضافه شده
    if js['timeprof'] == "on":
        photo = randomphoto()
        await bot(UploadProfilePhotoRequest(await bot.upload_file(photo)))

@bot.on(events.NewMessage())
async def updateMessage(event):
    js = get("data.json")
    fromid = event.sender_id
    if fromid in js['enemy']:
        await event.delete()
    elif fromid in js['crash']:
        emoticons = ["🤍","🖤","💜","💙","💚","💛","🧡","❤️","🤎","💖"]
        await event.reply(random.choice(emoticons))
        await event.forward_to('me')
    elif js['comment'] == "on" and not event.fwd_from is None:
        if not event.fwd_from.saved_from_peer is None:
            await event.reply(js['text'])

@bot.on(events.ChatAction)
async def newMember(event):
    if event.user_joined:
        await event.reply("ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ!")

@bot.on(events.NewMessage())
async def updateAction(event):
    js = get("data.json")
    for type in ["typing","game","voice","video","sticker"]:
        if js[type] == "on":
            async with bot.action(event.chat_id,type):
                await asyncio.sleep(2)

@bot.on(events.NewMessage(pattern=r'(help|راهنما)', outgoing=True))
async def help(event):

    memoryUse = psutil.Process(os.getpid()).memory_info()[0] / 1073741824
    memoryPercent = psutil.virtual_memory()[2]
    cpuPercent = psutil.cpu_percent()
    me = await bot.get_me()
    name = me.first_name
    js = get("data.json")
    help = f"нelp мeɴυ {name} :\n\n⟩••• ᴛɪᴍᴇ ɴᴀᴍᴇ : {js['timename']}\n⟩••• ᴛɪᴍᴇ ʙɪᴏ : {js['timebio']}\n⟩••• time prof : {js['timeprof']}\n⟩••• ʙᴏᴛ ɴᴏᴡ ɪs : {js['bot']}\n⟩••• ʜᴀsʜᴛᴀɢ : {js['hashtag']}\n⟩••• ʙᴏʟᴅ : {js['bold']}\n⟩••• ɪᴛᴀʟɪᴄ : {js['italic']}\n⟩••• ᴅᴇʟᴇᴛᴇ : {js['delete']}\n⟩••• ᴄᴏᴅᴇ : {js['code']}\n⟩••• ᴜɴᴅᴇʀʟɪɴᴇ : {js['underline']}\n⟩••• ʀᴇᴠᴇʀsᴇ : {js['reverse']}\n⟩••• ᴘᴀʀᴛ : {js['part']}\n⟩••• ᴍᴇɴᴛɪᴏɴ : {js['mention']}\n⟩••• coммeɴт : {js['comment']}\n⟩••• тeхт coммeɴт : {js['text']}\n\n⟩••• ᴛʏᴘɪɴɢ : {js['typing']}\n⟩••• ɢᴀᴍᴇ : {js['game']}\n⟩••• ᴠᴏɪᴄᴇ : {js['voice']}\n⟩••• ᴠɪᴅᴇᴏ : {js['video']}\n⟩••• sᴛɪᴄᴋᴇʀ : {js['sticker']}\n\n⟩••• .timebio (oɴ|oғғ)\n⟩••• .timename (oɴ|oғғ)\n⟩••• .timeprof (oɴ|oғғ)\n⟩••• .comment (oɴ|oғғ)\n⟩••• .commentText (тeхт)\n\n⟩••• hashtag (oɴ|oғғ)\n⟩••• bold (oɴ|oғғ)\n⟩••• italic (oɴ|oғғ)\n⟩••• delete (oɴ|oғғ)\n⟩••• code (oɴ|oғғ)\n⟩••• underline (oɴ|oғғ)\n⟩••• reverse (oɴ|oғғ)\n⟩••• part (oɴ|oғғ)\n⟩••• mention (oɴ|oғғ)\n\n⟩••• typing (oɴ|oғғ)\n⟩••• game (oɴ|oғғ)\n⟩••• voice (oɴ|oғғ)\n⟩••• video (oɴ|oғғ)\n⟩••• sticker (oɴ|oғғ)\n\n⟩••• .addenemy (ιd)\n⟩••• .delenemy (ιd)\n⟩••• listenemy\n⟩••• .addcrash (ιd)\n⟩••• .delcrash (ιd)\n⟩••• listcrash\n\n⟩••• .reaction (тeхт)\n⟩••• heart\n⟩••• tagall\n⟩••• tagadmins\n⟩••• .check (тeхт)\n⟩••• download\n\n⟩••• info (ιd)(reply)\n⟩••• status\n⟩••• .clean (ιɴт)\n\n• ᴍᴇᴍᴏʀʏ ᴜsᴇᴅ : {memoryUse}\n• ᴍᴇᴍᴏʀʏ : {memoryPercent} %\n• ᴄᴘᴜ : {cpuPercent} %\n• ᴄʀ : @Mrr_php !"
    await bot.send_message(event.chat_id,help,reply_to = event.message.id)
    results = await bot.inline_query('like','ＤＯ ＹＯＵ ＬＩＫＥ ＭＹ ＲＯＢＯＴ ? ')
    await results[0].click(event.chat_id)


@bot.on(events.NewMessage(pattern=r'\.dice (1|2|3|4|5|6)', outgoing=True))
async def dice(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    send = await bot.send_file(event.chat_id, types.InputMediaDice('🎲'))
    while(send.media.value != int(input_str)):
        await bot.delete_messages(event.chat_id,send.id)
        send = await bot.send_file(event.chat_id, types.InputMediaDice('🎲'))

@bot.on(events.NewMessage(pattern=r'\.reaction (.*)', outgoing=True))
async def reaction(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "love":
        emoticons = ["🤍","🖤","💜","💙","💚","💛","🧡","❤️","🤎","💖"]
    elif input_str in "oclock":
        emoticons = ["🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚","🕛","🕜","🕝","🕞","🕟","🕠","🕡","🕢","🕣","🕤","🕥","🕦","🕧"]
    elif input_str in "star":
        emoticons = ["💥","⚡️","✨","🌟","⭐️","💫"]
    elif input_str in "snow":
        emoticons = ["❄️","☃️","⛄️"]		
    for i in range(10):
        await asyncio.sleep(0.5)
        await event.edit(random.choice(emoticons))

@bot.on(events.NewMessage(pattern=r'(heart|قلب)', outgoing=True))
async def heart(event):
    if event.fwd_from:
        return
    for x in range(1,4):
        for i in range(1,11):
            txt = "➣ " + str(x) + " ❦" * i + " | " + str(10 * i) + "%"
            await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'\.clean (.*)', outgoing=True))
async def clean(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    message_id = event.message.id
    for i in range(int(input_str)):
        await bot.delete_messages(event.chat_id,message_id)
        message_id -= 1
    await bot.send_message(event.chat_id,f"{input_str} мeѕѕαɢeѕ were deleтe . . . !")

@bot.on(events.NewMessage(pattern=r'\.addcrash (.*)', outgoing=True))
async def addcrash(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    js = get("data.json")
    if int(input_str) in js['crash']:
        txt = "• [ᴜsᴇʀ](tg://user?id={}) ᴡᴀs ɪɴ crαѕн ʟɪsᴛ !".format(int(input_str))
        await event.edit(txt)
    else:
        js["crash"].append(int(input_str))
        put("data.json",js)
        txt = "• [ᴜsᴇʀ](tg://user?id={}) ɴᴏᴡ ɪɴ crαѕн ʟɪsᴛ !".format(int(input_str))
        await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'\.delcrash (.*)', outgoing=True))
async def delcrash(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    js = get("data.json")
    if int(input_str) in js['crash']:
        js["crash"].remove(int(input_str))
        put("data.json",js)
        txt = "• [ᴜsᴇʀ](tg://user?id={}) ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ crαѕн ʟɪsᴛ !".format(int(input_str))
        await event.edit(txt)
    else:
        txt = "• [ᴜsᴇʀ](tg://user?id={}) ɪs ɴᴏᴛ ɪɴ ᴛʜᴇ crαѕн ʟɪsᴛ !".format(int(input_str))
        await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'(listcrash|لیست کراش)', outgoing=True))
async def listcrash(event):
    txt = "crαѕн ʟɪsᴛ :\n"
    js = get("data.json")
    for i in js['crash']:
        lo += "\n• [{}](tg://user?id={})".format(i,i)
    await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'\.addenemy (.*)', outgoing=True))
async def addenemy(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    js = get("data.json")
    if int(input_str) in js['enemy']:
        txt = "• [ᴜsᴇʀ](tg://user?id={}) ᴡᴀs ɪɴ ᴇɴᴇᴍʏ ʟɪsᴛ !".format(int(input_str))
        await event.edit(txt)
    else:
        js["enemy"].append(int(input_str))
        put("data.json",js)
        txt = "• [ᴜsᴇʀ](tg://user?id={}) ɴᴏᴡ ɪɴ ᴇɴᴇᴍʏ ʟɪsᴛ !".format(int(input_str))
        await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'\.delenemy (.*)', outgoing=True))
async def delenemy(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    js = get("data.json")
    if int(input_str) in js['enemy']:
        js["enemy"].remove(int(input_str))
        put("data.json",js)
        txt = "• [ᴜsᴇʀ](tg://user?id={}) ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ ᴇɴᴇᴍʏ ʟɪsᴛ !".format(int(input_str))
        await event.edit(txt)
    else:
        txt = "• [ᴜsᴇʀ](tg://user?id={}) ɪs ɴᴏᴛ ɪɴ ᴛʜᴇ ᴇɴᴇᴍʏ ʟɪsᴛ !".format(int(input_str))
        await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'(listenemy|لیست انمی)', outgoing=True))
async def listenemy(event):
    txt = "ᴇɴᴇᴍʏ ʟɪsᴛ :\n"
    js = get("data.json")
    for i in js['enemy']:
        lo += "\n• [{}](tg://user?id={})".format(i,i)
    await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'\.timename (on|off)', outgoing=True))
async def timename(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    js = get("data.json")
    js["timename"] = str(input_str)
    put("data.json",js)
    await event.edit(f"⟩••• ᴛʜᴇ ᴛɪᴍᴇ ɴᴀᴍᴇ ɴᴏᴡ ɪs {input_str}")

@bot.on(events.NewMessage(pattern=r'\.timeprof (on|off)', outgoing=True))
async def timeprof(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    js = get("data.json")
    js["timeprof"] = str(input_str)
    put("data.json",js)
    await event.edit(f"⟩••• ᴛʜᴇ ᴛɪᴍᴇ prof ɴᴏᴡ ɪs {input_str}")


@bot.on(events.NewMessage(pattern=r'\.timebio (on|off)', outgoing=True))
async def timebio(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    js = get("data.json")
    js["timebio"] = str(input_str)
    put("data.json",js)
    await event.edit(f"⟩••• ᴛʜᴇ ᴛɪᴍᴇ ʙɪᴏ ɴᴏᴡ ɪs {input_str}")

@bot.on(events.NewMessage(pattern=r'\.comment (on|off)', outgoing=True))
async def comment(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    js = get("data.json")
    js["comment"] = str(input_str)
    put("data.json",js)
    await event.edit(f"⟩••• ᴛʜᴇ coммeɴт ɴᴏᴡ ɪs {input_str}")

@bot.on(events.NewMessage(pattern=r'\.commentText (.*)', outgoing=True))
async def comment(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    js = get("data.json")
    js["text"] = str(input_str)
    put("data.json",js)
    await event.edit(f"⟩••• ᴛʜᴇ coммeɴт тeхт ɴᴏᴡ ɪs {input_str}")

@bot.on(events.NewMessage(pattern=r'(tagall|تگ)', outgoing=True , func=lambda e: e.is_group))
async def tagall(event):
    if event.fwd_from:
        return
    mentions = "✅ آخرین افراد آنلاین گروه"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()
    
@bot.on(events.NewMessage(pattern=r'(tagadmins|تگ ادمین ها)', outgoing=True , func=lambda e: e.is_group))
async def tagadmins(event):
    if event.fwd_from:
        return
    mentions = "⚡️ تگ کردن ادمین ها"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter = ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()

@bot.on(events.NewMessage(pattern=r'\.check (.*)', outgoing=True))
async def reaction(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    link = "https://api-bot.site/check/Check.php?phone={}".format(input_str)
    req = requests.get(link)
    txt = "Ok {} | status : {} | Results : {}".format(input_str,req.json()['status'],req.json()['Results'])
    await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'(info|اطلاعات)', outgoing=True))
async def info(event):
    if event.fwd_from:
        return
    if event.is_reply:
        getMessage = await event.get_reply_message()
        get_id = getMessage.sender.id
    else:
        match = event.raw_text.split(' ')
        if len(match) == 2:
            get_id = int(match[1])
        else:
            get_id = event.chat_id
    full = await bot(GetFullUserRequest(get_id))
    first_name = full.user.first_name
    last_name = full.user.last_name
    username = full.user.username
    about = full.about
    phone = full.user.phone
    ir = pytz.timezone("Asia/Tehran")
    time = datetime.now(ir).strftime("ᴛɪᴍᴇ | %H:%M:%S")
    txt = "υѕer ιd : {}\nғιrѕт ɴαмe : {}\nlαѕт ɴαмe : {}\nυѕerɴαмe : {}\npнoɴe : {}\nвιo : {}\n{}".format(get_id,first_name,last_name,username,phone,about,time)
    await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'(status|وضعیت)', outgoing=True))
async def status(event):
    if event.fwd_from:
        return
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    largest_group_member_count = 0
    largest_group_with_admin = 0
    dialog: Dialog
    async for dialog in bot.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1
            elif entity.megagroup:
                groups += 1
                if entity.creator or entity.admin_rights:
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1
        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    txt = f"ѕтαтυѕ !"
    txt += f"\nᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs : {private_chats}"
    txt += f"\nʙᴏᴛs : {bots}"
    txt += f"\nɢʀᴏᴜᴘs : {groups}"
    txt += f"\nʙʀᴏᴀᴅᴄᴀsᴛ ᴄʜᴀɴɴᴇʟs : {broadcast_channels}"
    txt += f"\nᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘs : {admin_in_groups}"
    txt += f"\nᴄʀᴇᴀᴛᴏʀ ɪɴ ɢʀᴏᴜᴘs : {creator_in_groups}"
    txt += f"\nᴀᴅᴍɪɴ ɪɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄʜᴀɴɴᴇʟs : {admin_in_broadcast_channels}"
    txt += f"\nᴄʀᴇᴀᴛᴏʀ ɪɴ ᴄʜᴀɴɴᴇʟs : {creator_in_channels}"
    txt += f"\nᴜɴʀᴇᴀᴅ ᴍᴇɴᴛɪᴏɴs : {unread_mentions}"
    txt += f"\nᴜɴʀᴇᴀᴅ : {unread}"
    txt += f"\nʟᴀʀɢᴇsᴛ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ ᴄᴏᴜɴᴛ : {largest_group_member_count}"
    txt += f"\nʟᴀʀɢᴇsᴛ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ : {largest_group_with_admin}"
    await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'(sessions|نشست های فعال)', outgoing=True))
async def session(event):
    if event.fwd_from:
        return
    result = await bot(functions.account.GetAuthorizationsRequest())
    txt = f"sᴇssɪᴏɴs :\n\n"
    for i in result.authorizations:
        txt += f"ʜᴀsʜ : {i.hash}\nᴅᴇᴠɪᴄᴇ ᴍᴏᴅᴇʟ : {i.device_model}\nᴘʟᴀᴛғᴏʀᴍ : {i.platform}\nsʏsᴛᴇᴍ ᴠᴇʀsɪᴏɴ : {i.system_version}\nᴀᴘɪ ɪᴅ : {i.api_id}\nᴀᴘᴘ ɴᴀᴍᴇ : {i.app_name}\nᴀᴘᴘ ᴠᴇʀsɪᴏɴ : {i.app_version}\nᴅᴀᴛᴇ ᴄʀᴇᴀᴛᴇᴅ : {i.date_created}\nᴅᴀᴛᴇ ᴀᴄᴛɪᴠᴇ : {i.date_active}\nɪᴘ : {i.ip}\nᴄᴏᴜɴᴛʀʏ : {i.country}\n┄┅┈┉┅┉┈┅┄┄┅┈┉┅┉┈┅┄┄┅┈┉┅┉┈┅┄\n"
    await event.edit(txt)

@bot.on(events.NewMessage(pattern=r'(translate|مترجم)', outgoing=True , func=lambda e: e.is_reply))
async def translate(event):
    if event.fwd_from:
        return
    match = event.raw_text.split(' ')
    if len(match) == 2:
        lan = str(match[1])
    else:
        lan = "fa"
    getMessage = await event.get_reply_message()
    message = getMessage.raw_text
    try:
        translate = Translator().translate(message,lan)
        src = translate.src
        dest = translate.dest
        text = translate.text
        await event.edit(f"ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {src} ᴛᴏ {dest}\n\nᴛʀᴀɴsʟᴀᴛᴇᴅ ᴛᴇxᴛ : {text}")
        voice = gTTS(text = message , lang = src , slow = True)
        voice.save('file.mp3')
        await bot.send_file(event.chat_id, 'file.mp3' , voice_note = True , reply_to = event.message.id)
        os.remove('file.mp3')
    except Exception as e:
        await bot.send_message('me', f"ＥＲＲＯＲ :\n\n{e}")

@bot.on(events.NewMessage(pattern=r'(download|دانلود)', outgoing=True , func=lambda e: e.is_reply))
async def download(event):
    if event.fwd_from:
        return
    try:
        message = await event.get_reply_message()
        download = await bot.download_media(message)
        await bot.send_message('me',':)', file=download)
        os.remove(download)
    except Exception as e:
        await bot.send_message('me', f"ＥＲＲＯＲ :\n\n{e}")

@bot.on(events.NewMessage(outgoing=True))
async def mode(event):
    if event.fwd_from:
        return
    js = get("data.json")
    text = event.raw_text
    if js['hashtag'] == "on":
        new = text.replace(" ","_")
        await event.edit(f"#{new}")
    elif js['bold'] == "on":
        await event.edit(f"<b>{text}</b>", parse_mode = "HTML")
    elif js['italic'] == "on":
        await event.edit(f"<i>{text}</i>", parse_mode = "HTML")
    elif js['delete'] == "on":
        await event.edit(f"<del>{text}</del>", parse_mode = "HTML")
    elif js['code'] == "on":
        await event.edit(f"<code>{text}</code>", parse_mode = "HTML")
    elif js['underline'] == "on":
        await event.edit(f"<u>{text}</u>", parse_mode = "HTML")
    elif js['reverse'] == "on":
        await event.edit(text[::-1], parse_mode = "HTML")
    elif js['part'] == "on":
        if len(text) > 1:
            new = ""
            for add in text:
                new += add
                if add != " ":
                    await event.edit(new, parse_mode = "HTML")
    elif js['mention'] == "on":
        if event.is_reply:
            try:
                getMessage = await event.get_reply_message()
                get_id = getMessage.sender.id
                await event.edit(f"<a href ='tg://openmessage?user_id={get_id}'>{text}</a>", parse_mode = "HTML")
            except Exception as e:
                await bot.send_message('me', f"ＥＲＲＯＲ :\n\n{e}")

@bot.on(events.NewMessage(pattern=r'(hashtag|bold|italic|delete|code|underline|reverse|part|mention) (on|off)', outgoing=True))
async def editMode(event):
    if event.fwd_from:
        return
    match = event.raw_text.split(' ')
    js = get("data.json")
    js[match[0]] = str(match[1])
    put("data.json",js)
    mode = match[0].translate(match[0].maketrans("qwertyuiopasdfghjklzxcvbnm","ǫᴡᴇʀᴛʏᴜɪᴏᴘᴀsᴅғɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ"))
    await event.edit(f"⟩••• ᴛʜᴇ {mode} ᴍᴏᴅᴇ ɴᴏᴡ ɪs {match[1]}")

@bot.on(events.NewMessage(pattern=r'(typing|game|voice|video|sticker) (on|off)', outgoing=True))
async def editAction(event):
    if event.fwd_from:
        return
    match = event.raw_text.split(' ')
    js = get("data.json")
    js[match[0]] = str(match[1])
    put("data.json",js)
    action = match[0].translate(match[0].maketrans("qwertyuiopasdfghjklzxcvbnm","ǫᴡᴇʀᴛʏᴜɪᴏᴘᴀsᴅғɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ"))
    await event.edit(f"⟩••• ᴛʜᴇ {action} αcтιoɴ ɴᴏᴡ ɪs {match[1]}")

bot.start()
bot.parse_mode = 'markdown'
clock.start()
bot.run_until_disconnected()
asyncio.get_event_loop().run_forever()