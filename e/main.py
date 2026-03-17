import time, redis, os, json, re, requests, asyncio
from pyrogram import Client, filters, idle
import yt_dlp  # إضافة مكتبة اليوت
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  # إضافة للأزرار

# إعداد Redis
r = redis.Redis('localhost', decode_responses=True)

# إنشاء/تحميل معلومات البوت
try:
    from information import *
    hmshelp = token.split(':')[0]
    r.set(f'{hmshelp}botowner', owner_id)
except Exception:
    with open('information.py', 'w+') as f:
        token = input('[+] Enter the bot token: ')
        hmshelp = token.split(':')[0]
        if not r.get(f'{hmshelp}botowner'):
            owner_id = int(input('[+] Enter SUDO ID: '))
            r.set(f'{hmshelp}botowner', owner_id)
        else:
            owner_id = int(r.get(f'{hmshelp}botowner'))
        f.write(f'token = "{token}"\nowner_id = {owner_id}')

# التأكد من وجود owner_id
if not r.get(f'{hmshelp}botowner'):
    owner_id = int(input('[+] Enter SUDO ID: '))
    r.set(f'{hmshelp}botowner', owner_id)
else:
    owner_id = int(r.get(f'{hmshelp}botowner'))

print('Database is being created...')

# إعداد config.py
to_config = f"""
import redis
r = redis.Redis('localhost', decode_responses=True)
token = '{token}'
hmshelp = token.split(':')[0]
sudo_id = {owner_id}
"""

# جلب username البوت
try:
    username = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]
except Exception:
    username = "UnknownBot"

to_config += f"\nbotUsername = '{username}'"
to_config += "\nfrom kvsqlite.sync import Client as DB"
to_config += "\nytdb = DB('ytdb.sqlite')"
to_config += "\nsounddb = DB('sounddb.sqlite')"
to_config += "\nwsdb = DB('wsdb.sqlite')"

with open('config.py', 'w+') as w:
    w.write(to_config)

print('Database is being sorted...')

# تعريف البوت
app = Client(
    f'{hmshelp}r3d',
    15263491,
    'f6cf6c2263f1e933f24d86bf02311467',
    bot_token=token,
    plugins={"root": "Plugins"},
)

# إعدادات عامة
if not r.get(f'{hmshelp}:botkey'):
    r.set(f'{hmshelp}:botkey', '⇜')

if not r.get(f'{hmshelp}botname'):
    r.set(f'{hmshelp}botname', 'همس')

if not r.get(f'{hmshelp}botchannel'):
    r.set(f'{hmshelp}botchannel', 'vn1bot')

# وظيفة البحث عن روابط
def Find(text):
    m = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(m, text)
    return [x[0] for x in url]

# ========== بداية كود اليوت (مضاف بالكامل) ==========

# إعدادات اليوت
DOWNLOADS_DIR = "downloads/youtube"
AUDIO_FORMAT = "mp3"
AUDIO_QUALITY = "192"
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 ميجابايت

# بصمة القناة
CHANNEL_NAME = "𝗦𝗰𝗼𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹"
CHANNEL_LINK = "https://t.me/unuez"
CHANNEL_BUTTON = InlineKeyboardMarkup([
    [InlineKeyboardButton("🎵 𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=CHANNEL_LINK)]
])

# إنشاء مجلد التحميلات
if not os.path.exists(DOWNLOADS_DIR):
    os.makedirs(DOWNLOADS_DIR)
    print("📁 تم إنشاء مجلد: downloads/youtube")

def clean_filename(title):
    """تنظيف اسم الملف"""
    cleaned = re.sub(r'[<>:"/\\|?*]', '', title)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned[:50].strip()

def search_youtube(query):
    """البحث في يوتيوب"""
    try:
        print(f"🔍 البحث عن: {query}")
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'extract_flat': True}) as ydl:
            search_results = ydl.extract_info(f"ytsearch1:{query}", download=False)
            if search_results and 'entries' in search_results and len(search_results['entries']) > 0:
                video = search_results['entries'][0]
                return {
                    'title': video.get('title', 'غير معروف'),
                    'link': f"https://www.youtube.com/watch?v={video.get('id', '')}",
                    'duration': video.get('duration_string', 'غير معروف'),
                    'channel': video.get('channel', 'غير معروف'),
                }
    except Exception as e:
        print(f"❌ خطأ بحث: {e}")
        return None

async def download_audio(video_info):
    """تحميل الصوت"""
    try:
        safe_title = clean_filename(video_info['title'])
        filename = f"{safe_title}.{AUDIO_FORMAT}"
        filepath = os.path.join(DOWNLOADS_DIR, filename)
        
        if os.path.exists(filepath):
            return filepath, True
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': AUDIO_FORMAT,
                'preferredquality': AUDIO_QUALITY,
            }],
            'outtmpl': os.path.join(DOWNLOADS_DIR, f'{safe_title}.%(ext)s'),
            'quiet': True,
        }
        
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts).download([video_info['link']]))
        
        if os.path.exists(filepath):
            return filepath, True
        return None, False
    except Exception as e:
        return None, str(e)

@app.on_message(filters.text)
async def youtube_command(client, message):
    """معالجة أمر يوت"""
    try:
        text = message.text.strip()
        if not text.startswith('يوت'):
            return
        
        song_name = text[3:].strip()
        if not song_name:
            await message.reply_text("❌ اكتب اسم الاغنية بعد يوت", reply_markup=CHANNEL_BUTTON)
            return
        
        searching = await message.reply_text(f"🔍 جاري البحث عن: {song_name}")
        
        # بحث
        video_info = await asyncio.get_event_loop().run_in_executor(None, search_youtube, song_name)
        if not video_info:
            await searching.edit_text("❌ مافي نتائج للبحث", reply_markup=CHANNEL_BUTTON)
            return
        
        await searching.edit_text(
            f"✅ {video_info['title']}\n⏱️ {video_info['duration']}\n⬇️ جاري التحميل...",
            reply_markup=CHANNEL_BUTTON
        )
        
        # تحميل
        result = await download_audio(video_info)
        
        if isinstance(result, tuple) and result[1] is True:
            audio_file = result[0]
            
            if os.path.getsize(audio_file) > MAX_FILE_SIZE:
                await searching.edit_text("❌ الملف كبير جداً", reply_markup=CHANNEL_BUTTON)
                os.remove(audio_file)
                return
            
            await searching.delete()
            with open(audio_file, 'rb') as audio:
                await message.reply_audio(
                    audio=audio,
                    title=video_info['title'][:50],
                    performer=video_info['channel'],
                    reply_markup=CHANNEL_BUTTON
                )
            os.remove(audio_file)
        else:
            await searching.edit_text("❌ فشل التحميل", reply_markup=CHANNEL_BUTTON)
            
    except Exception as e:
        print(f"❌ خطأ يوت: {e}")
        try:
            await message.reply_text("❌ صار خطأ غير متوقع", reply_markup=CHANNEL_BUTTON)
        except:
            pass

# ========== نهاية كود اليوت ==========

# تحميل جميع الـ Plugins
print("📂 جاري تحميل الـ Plugins...")
try:
    import Plugins
    print("✅ تم تحميل جميع الـ Plugins بنجاح")
except Exception as e:
    print(f"⚠️ خطأ في تحميل الـ Plugins: {e}")

# تشغيل البوت
try:
    app.start()
except Exception as e:
    print(f"❌ فشل تشغيل البوت: {e}")
    exit()

print('🇸🇦 Bot is running. Send /start')

# إرسال رسالة للقناة DevGroup إذا موجودة
if r.get(f'DevGroup:{hmshelp}'):
    dev_group_id = int(r.get(f'DevGroup:{hmshelp}'))
    try:
        app.send_message(dev_group_id, "تم تشغيل البوت بنجاح ✔️")
    except:
        pass

# تشغيل idle للحفاظ على البوت شغال
idle()