import random, re, time, pytz, os, gtts, requests
import speech_recognition as sr
from pydub import AudioSegment
from hijri_converter import Hijri, Gregorian
from datetime import datetime
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.persianData import persianInformation
from .welcome_and_rules import *
from .games import *
from PIL import Image
from asyncio import run as RUN
from Python_ARQ import ARQ
from aiohttp import ClientSession

# from googletrans import Translator as googletranstr
from mutagen.mp3 import MP3 as mutagenMP3
# from main import TelegramBot

ARQ_API_KEY = "OZJRWV-SAURXD-PMBUKF-GMVSNS-ARQ"
ARQ_API_URL = "https://arq.hamker.dev"

# translator = googletranstr()


list_UwU = [
    "كس",
    "كسمك",
    "كسختك",
    "عير",
    "كسخالتك",
    "خرا بالله",
    "عير بالله",
    "كسخواتكم",
    "كحاب",
    "مناويج",
    "مناويج",
    "كحبه",
    "ابن الكحبه",
    "فرخ",
    "فروخ",
    "طيزك",
    "طيزختك",
    "كسمك",
    "يا ابن الخول",
    "المتناك",
    "شرموط",
    "شرموطه",
    "ابن الشرموطه",
    "ابن الخول",
    "ابن العرص",
    "منايك",
    "متناك",
    "ابن المتناكه",
    "زبك",
    "عرص",
    "زبي",
    "خول",
    "لبوه",
    "لباوي",
    "ابن اللبوه",
    "منيوك",
    "كسمكك",
    "متناكه",
    "يا عرص",
    "يا خول",
    "قحبه",
    "القحبه",
    "شراميط",
    "العلق",
    "العلوق",
    "العلقه",
    "كسمك",
    "يا ابن الخول",
    "المتناك",
    "شرموط",
    "شرموطه",
    "ابن الشرموطه",
    "ابن الخول",
    "االمنيوك",
    "كسمككك",
    "الشرموطه",
    "ابن العرث",
    "ابن الحيضانه",
    "زبك",
    "خول",
    "زبي",
    "قاحب",
]

list_Shiaa = [
    "يا علي",
    "يا حسين",
    "ياعلي",
    "ياحسين",
    "علي ولي الله",
    "عليا ولي الله",
    "عائشه زانيه",
    "عائشة زانية",
    "عائشة عاهرة",
    "عائشه عاهره",
    "خرب ربك",
    "خرب الله",
    "يلعن ربك",
    "يلعن الله",
    "يا عمر",
    "ياعمر",
    "يا محمد",
    "يامحمد",
    "زوجات الرسول",
    "عير بالسنة",
    "عير بالسنه",
    "خرب السنه",
    "خرا بالسنه",
    "خرب السنة",
    "خرا بالسنة",
    "والحسين",
    "والعباس",
    "وعلي",
    "والامام علي",
    "ربنا علي",
    "علي الله",
    "الله علي",
    "رب علي",
    "علي رب",
]


def Find(text):
    m = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(m, text)
    return [x[0] for x in url]


"""
         r.get(f'{m.chat.id}:mute:{hmshelp}')
         r.get(f'{m.chat.id}:lockJoin:{hmshelp}')
         r.get(f'{m.chat.id}:lockChannels:{hmshelp}')
         r.get(f'{m.chat.id}:lockEdit:{hmshelp}')
         r.get(f'{m.chat.id}:lockEditM:{hmshelp}')
         r.get(f'{m.chat.id}:lockVoice:{hmshelp}')
         r.get(f'{m.chat.id}:lockVideo:{hmshelp}')
         r.get(f'{m.chat.id}:lockNot:{hmshelp}')
         r.get(f'{m.chat.id}:lockPhoto:{hmshelp}')
         r.get(f'{m.chat.id}:lockStickers:{hmshelp}')
         r.get(f'{m.chat.id}:lockAnimations:{hmshelp}')
         r.get(f'{m.chat.id}:lockFiles:{hmshelp}')
         r.get(f'{m.chat.id}:lockPersian:{hmshelp}')
         r.get(f'{m.chat.id}:lockUrls:{hmshelp}')
         r.get(f'{m.chat.id}:lockHashtags:{hmshelp}')
         r.get(f'{m.chat.id}:lockMessages:{hmshelp}')
         r.get(f'{m.chat.id}:lockTags:{hmshelp}')
         r.get(f'{m.chat.id}:lockBots:{hmshelp}')
         r.get(f'{m.chat.id}:lockSpam:{hmshelp}')
         r.get(f'{m.chat.id}:lockInline:{hmshelp}')
         r.get(f'{m.chat.id}:lockForward:{hmshelp}')
         r.get(f'{m.chat.id}:lockAudios:{hmshelp}')
         r.get(f'{m.chat.id}:lockaddContacts:{hmshelp}')
         r.get(f'{m.chat.id}:lockSHTM:{hmshelp}')
"""

from pyrogram.errors import UserNotParticipant, FloodWait


@Client.on_message(filters.group, group=-1111111111111)
async def on_zbi(c: Client, m: Message):
    name = r.get(f"{hmshelp}:BotName") if r.get(f"{hmshelp}:BotName") else "ليو"
    text = m.text
    if text.startswith(f"{name} "):
        text = text.replace(f"{name} ", "")
    if r.get(f"{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}"):
        text = r.get(f"{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}")
    if r.get(f"Custom:{hmshelp}&text={text}"):
        text = r.get(f"Custom:{hmshelp}&text={text}")

    if r.get(f"inDontCheck:{hmshelp}"):
        return m.continue_propagation()

    if dev_pls(m.from_user.id, m.chat.id):
        return

    if (
        text.startswith("تفعيل ")
        or text.startswith("تعطيل ")
        or text.startswith("قفل ")
        or text.startswith("فتح ")
        or text == "ايدي"
        or text == "الاوامر"
    ):
        if r.get(f"forceChannel:{hmshelp}") and (
            not r.get(f"disableSubscribe:{hmshelp}")
        ):
            username = r.get(f"forceChannel:{hmshelp}").replace("@", "")
            not_member = False
            try:
                member = await c.get_chat_member(username, m.from_user.id)
            except FloodWait:
                return m.continue_propagation()
            except UserNotParticipant:
                await m.reply(
                    f"- انضم للقناة ( @{username} ) لتستطيع استخدام اوامر البوت",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "اضغط هنا", url="https://t.me/" + username
                                )
                            ]
                        ]
                    ),
                )
                r.set(f"inDontCheck:{hmshelp}", 1, ex=10)
                return m.stop_propagation()
            except Exception as e:
                print(e)
                return m.continue_propagation()

            if member.status in {
                enums.ChatMemberStatus.LEFT,
                enums.ChatMemberStatus.BANNED,
            } or member.status is None:
                not_member = True
            else:
                not_member = False

            if not_member:
                await m.reply(
                    f"- انضم للقناة ( @{username} ) لتستطيع استخدام اوامر البوت",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "اضغط هنا", url="https://t.me/" + username
                                )
                            ]
                        ]
                    ),
                )
                r.set(f"inDontCheck:{hmshelp}", ex=10)
                return m.stop_propagation()
            else:
                return m.continue_propagation()


@Client.on_message(filters.group, group=27)
def guardLocksResponse(c, m):
    k = r.get(f"{hmshelp}:botkey")
    channel = (
        r.get(f"{hmshelp}:BotChannel") if r.get(f"{hmshelp}:BotChannel") else "alwzaraa2"
    )
    Thread(target=guardResponseFunction, args=(c, m, k, channel)).start()


@Client.on_edited_message(filters.group, group=27)
def guardLocksResponse2(c, m):
    k = r.get(f"{hmshelp}:botkey")
    channel = (
        r.get(f"{hmshelp}:BotChannel") if r.get(f"{hmshelp}:BotChannel") else "alwzaraa2"
    )
    Thread(target=guardResponseFunction2, args=(c, m, k, channel)).start()


def guardResponseFunction2(c, m, k, channel):
    if not r.get(f"{m.chat.id}:enable:{hmshelp}"):
        return
    warner = """
「 {} 」
{} ممنوع {}
☆
"""
    warn = False
    reason = False

    if m.sender_chat:
        id = m.sender_chat.id
        mention = f"[{m.sender_chat.title}](t.me/{channel})"
    if m.from_user:
        id = m.from_user.id
        mention = m.from_user.mention

    if (
        r.get(f"{m.chat.id}:lockEdit:{hmshelp}")
        and m.text
        and not pre_pls(id, m.chat.id)
    ):
        m.delete()
        warn = True
        reason = "التعديل"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if (
        r.get(f"{m.chat.id}:lockEditM:{hmshelp}")
        and m.media
        and not pre_pls(id, m.chat.id)
    ):
        m.delete()
        warn = True
        reason = "تعديل الميديا"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )


def guardResponseFunction(c, m, k, channel):
    if not r.get(f"{m.chat.id}:enable:{hmshelp}"):
        return
    warner = """
「 {} 」
{} ممنوع {}
☆
"""
    warn = False
    reason = False

    if r.get(f"{m.chat.id}:lockNot:{hmshelp}") and m.service:
        m.delete()

    if (
        r.get(f"{m.chat.id}:lockaddContacts:{hmshelp}")
        and m.from_user
        and m.new_chat_members
    ):
        if pre_pls(m.from_user.id, m.chat.id):
            return
        for me in m.new_chat_members:
            if not me.id == m.from_user.id:
                warn = True
                mention = m.from_user.mention
                m.chat.ban_member(me.id)
                reason = "تضيف حد هنا"
                m.delete()
                if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}"):
                    return m.reply(
                        warner.format(mention, k, reason), disable_web_page_preview=True
                    )

    if m.sender_chat:
        id = m.sender_chat.id
        mention = f"[{m.sender_chat.title}](t.me/{channel})"
    if m.from_user:
        id = m.from_user.id
        mention = m.from_user.mention

    # print(id)

    if m.media:
        rep = m
        if rep.sticker:
            file_id = rep.sticker.file_id
        if rep.animation:
            file_id = rep.animation.file_id
        if rep.photo:
            file_id = rep.photo.file_id
        if rep.video:
            file_id = rep.video.file_id
        if rep.voice:
            file_id = rep.voice.file_id
        if rep.audio:
            file_id = rep.audio.file_id
        if rep.document:
            file_id = rep.document.file_id
        idd = file_id[-6:]
        if r.get(f"{idd}:NotAllow:{m.chat.id}{hmshelp}"):
            if not admin_pls(id, m.chat.id):
                return m.delete()

    if m.text and r.smembers(f"{m.chat.id}:NotAllowedListText:{hmshelp}"):
        if not admin_pls(id, m.chat.id):
            for word in r.smembers(f"{m.chat.id}:NotAllowedListText:{hmshelp}"):
                if word in m.text:
                    return m.delete()

    if r.get(f"{id}:mute:{m.chat.id}{hmshelp}") or r.get(f"{id}:mute:{hmshelp}"):
        return False

    if r.get(f"{m.chat.id}:mute:{hmshelp}") and not admin_pls(id, m.chat.id):
        m.delete()
        return False

    if pre_pls(id, m.chat.id):
        return False

    if r.get(f"{m.chat.id}:lockBots:{hmshelp}") and m.new_chat_members:
        for mem in m.new_chat_members:
            if mem.is_bot:
                return m.chat.ban_member(mem.id)

    if r.get(f"{m.chat.id}:lockJoin:{hmshelp}") and m.new_chat_members:
        for mem in m.new_chat_members:
            if not admin_pls(mem.id, m.chat.id):
                m.chat.ban_member(mem.id)
                m.chat.unban_member(mem.id)
                return False

    if r.get(f"{m.chat.id}:lockChannels:{hmshelp}") and m.sender_chat:
        if not m.sender_chat.id == m.chat.id:
            m.chat.ban_member(m.sender_chat.id)
            return False

    if r.get(f"{m.chat.id}:lockSpam:{hmshelp}"):
        if not r.get(f"{id}in_spam:{m.chat.id}{hmshelp}"):
            r.set(f"{id}in_spam:{m.chat.id}{hmshelp}", 1, ex=10)
        else:
            if int(r.get(f"{id}in_spam:{m.chat.id}{hmshelp}")) == 10:
                if m.from_user:
                    r.set(f"{id}:mute:{m.chat.id}{hmshelp}", 1)
                    r.sadd(f"{m.chat.id}:listMUTE:{hmshelp}", id)
                    r.delete(f"{id}in_spam:{m.chat.id}{hmshelp}")
                    return m.reply(
                        f"「 {mention} 」 \n{k} كتمتك يالبثر عشان تتعلم تكرر\n☆"
                    )

                if m.sender_chat:
                    m.chat.ban_member(m.sender_chat)
                    return m.reply(
                        f"「 {mention} 」 {k} حظرتك يالبثر عشان تتعلم تكرر\n☆"
                    )
            else:
                get = int(r.get(f"{id}in_spam:{m.chat.id}{hmshelp}"))
                r.set(f"{id}in_spam:{m.chat.id}{hmshelp}", get + 1, ex=10)

    if r.get(f"{m.chat.id}:lockInline:{hmshelp}") and m.via_bot:
        m.delete()
        warn = True
        reason = "ترسل انلاين"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockForward:{hmshelp}") and m.forward_date:
        m.delete()
        warn = True
        reason = "ترسل توجيه"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    """
  if r.get(f'{m.chat.id}:lockForward:{hmshelp}') and m.forward_from_chat:
     m.delete()
     warn = True
     reason = 'ترسل توجيه'
     if not r.get(f'{m.chat.id}:disableWarn:{hmshelp}') and not r.get(f'{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}'):
        r.set(f'{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}',1,ex=60)
        return m.reply(warner.format(mention,k,reason),disable_web_page_preview=True)
  """

    if r.get(f"{m.chat.id}:lockAudios:{hmshelp}") and m.audio:
        m.delete()
        warn = True
        reason = "ترسل صوت"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockVideo:{hmshelp}") and m.video:
        m.delete()
        warn = True
        reason = "ترسل فيديوهات"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockPhoto:{hmshelp}") and m.photo:
        m.delete()
        warn = True
        reason = "ترسل صور"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockStickers:{hmshelp}") and m.sticker:
        m.delete()
        warn = True
        reason = "ترسل ملصقات"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockAnimations:{hmshelp}") and m.animation:
        m.delete()
        warn = True
        reason = "ترسل متحركات"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockFiles:{hmshelp}") and m.document:
        m.delete()
        warn = True
        reason = "ترسل ملفات"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockPersian:{hmshelp}") and m.text:
        if "ه‍" in m.text or "ی" in m.text or "ک" in m.text or "چ" in m.text:
            m.delete()
            warn = True
            reason = "ترسل فارسي"
            if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}"):
                return m.reply(
                    warner.format(mention, k, reason), disable_web_page_preview=True
                )

    if r.get(f"{m.chat.id}:lockPersian:{hmshelp}") and m.caption:
        if "ه‍" in m.caption or "ی" in m.caption or "ک" in m.caption or "چ" in m.caption:
            m.delete()
            warn = True
            reason = "ترسل فارسي"
            if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}"):
                return m.reply(
                    warner.format(mention, k, reason), disable_web_page_preview=True
                )

    if (
        r.get(f"{m.chat.id}:lockUrls:{hmshelp}")
        and m.text
        and len(Find(m.text.html)) > 0
    ):
        m.delete()
        warn = True
        reason = "ترسل روابط"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if (
        r.get(f"{m.chat.id}:lockHashtags:{hmshelp}")
        and m.text
        and len(re.findall(r"#(\w+)", m.text)) > 0
    ):
        m.delete()
        warn = True
        reason = "ترسل هاشتاق"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockMessages:{hmshelp}") and m.text and len(m.text) > 150:
        m.delete()
        warn = True
        reason = "ترسل كلام كثير"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockVoice:{hmshelp}") and m.voice:
        m.delete()
        warn = True
        reason = "ترسل فويس"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(
        f"{m.chat.id}:lockTags:{hmshelp}"
    ) and '"type": "MessageEntityType.MENTION"' in str(m):
        m.delete()
        warn = True
        reason = "ترسل منشنات"
        if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
            f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockSHTM:{hmshelp}") and (m.caption or m.text):
        if m.caption:
            txt = m.caption
        if m.text:
            txt = m.text
        for a in list_UwU:
            if txt == a or f" {a} " in txt or a in txt:
                m.delete()
                warn = True
                reason = "السب هنا"
                if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}") and not r.get(
                    f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}"
                ):
                    r.set(f"{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
                    return m.reply(
                        warner.format(mention, k, reason), disable_web_page_preview=True
                    )

    """
  if r.get(f'{m.chat.id}:lockKFR:{hmshelp}') and (m.caption or m.text):
     if m.caption:
         txt = m.caption.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","").replace("ـ","").replace("َ","").replace("ٕ","").replace("ُ","").replace("ِ","").replace("ٰ","").replace("ٖ","").replace("ً","").replace("ّ","").replace("ٌ","").replace("ٍ","").replace("ْ","").replace("ٔ","").replace("'","").replace('"',"")
     if m.text:
         txt = m.text.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","").replace("ـ","").replace("َ","").replace("ٕ","").replace("ُ","").replace("ِ","").replace("ٰ","").replace("ٖ","").replace("ً","").replace("ّ","").replace("ٌ","").replace("ٍ","").replace("ْ","").replace("ٔ","").replace("'","").replace('"',"")
     for kfr in list_Shiaa:
         if kfr in txt:
            m.delete()
            warn = True
            reason = 'الكفر هنا'
            if not r.get(f'{m.chat.id}:disableWarn:{hmshelp}') and not r.get(f'{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}'):
                 r.set(f'{hmshelp}:inWARN:{m.from_user.id}{m.chat.id}',1,ex=60)
                 return m.reply(warner.format(mention,k,reason),disable_web_page_preview=True)
  """

    if r.get(f"{m.chat.id}:lockJoinPersian:{hmshelp}") and m.new_chat_members:
        if m.from_user.first_name:
            if (
                m.from_user.first_name in persianInformation["names"]
                or m.from_user.id in persianInformation["ids"]
                or "ه‍" in m.from_user.first_name
                or "ی" in m.from_user.first_name
                or "ک" in m.from_user.first_name
                or "چ" in m.from_user.first_name
                or "👙" in m.from_user.first_name
            ) and not pre_pls(m.from_user.id, m.chat.id):
                if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}"):
                    m.reply(
                        """
「 {} 」
{} تم حظره لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k)
                    )
                return c.ban_chat_member(m.chat.id, m.from_user.id)

        if m.from_user.last_name:
            if (
                m.from_user.last_name in persianInformation["last_names"]
                or m.from_user.id in persianInformation["ids"]
                or "ه‍" in m.from_user.last_name
                or "ی" in m.from_user.last_name
                or "ک" in m.from_user.last_name
                or "چ" in m.from_user.last_name
                or "👙" in m.from_user.last_name
            ) and not pre_pls(m.from_user.id, m.chat.id):
                if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}"):
                    m.reply(
                        """
「 {} 」
{} تم حظره لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k)
                    )
                return c.ban_chat_member(m.chat.id, m.from_user.id)

    if r.get(f"{m.chat.id}:enableVerify:{hmshelp}") and m.new_chat_members:
        for me in m.new_chat_members:
            if not pre_pls(me.id, m.chat.id):
                c.restrict_chat_member(
                    m.chat.id, me.id, ChatPermissions(can_send_messages=False)
                )
                get_random = get_for_verify(me)
                question = get_random["question"]
                reply_markup = get_random["key"]
                return m.reply(
                    f"{k} قيدناك عشان نتاكد انك شخص حقيقي مو زومبي\n\n{question}",
                    reply_markup=reply_markup,
                )

    if m.media and r.get(f"{m.chat.id}:lockNSFW:{hmshelp}"):
        print("nsfw scanner")
        if not admin_pls(id, m.chat.id):
            if m.sticker:
                id = m.sticker.thumbs[0].file_id
            if m.photo:
                id = m.photo.file_id
            if m.video:
                id = m.video.thumbs[0].file_id
            if m.animation:
                id = m.animation.thumbs[0].file_id
        file = c.download_media(id)
        Thread(target=scanR, args=(c, m, id, file)).start()


def scanR(c, m, id, file):
    RUN(scan4(c, m, id, file))


async def scan4(c, m, id, file):
    session = ClientSession()
    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)
    resp = await arq.nsfw_scan(file=file)
    if resp.result.is_nsfw:
        print("xNSFW")
        await m.delete()
        k = r.get(f"{hmshelp}:botkey")
        await m.reply(
            f"「 {m.from_user.mention} 」\n{k} تم حذف رسالتك لإحتوائها على محتوى إباحي .\n☆"
        )
    os.remove(file)
    await session.close()


def get_for_verify(me):
    for_verify = [
        {
            "question": "ماهو الحيوان الذي ينتهي اسمه بحرف الباء ؟",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("فأر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("وشق", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("بشار الأسد", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("حمار", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("كلب", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("قطة", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "ماهي عاصمة فرنسا؟",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("دمشق", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الرياض", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("باريس", callback_data=f"yes:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("الكويت", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("القاهرة", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ماشا والدب", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "نادي يبدأ بحرف الباء :",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("برشلونا", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("الهلال", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("النصر", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("الزمالك", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ريال مدريد", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("مانشستر", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "دولة يبدأ اسمها بحرف التاء :",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("قطر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("امريكا", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("سوريا", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("مصر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الصين", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("تركيا", callback_data=f"yes:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اختر هذا الايموجي - 🤑 -",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🍭", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🤑", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("🏆", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("🌀", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🪨", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("💎", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اختر هذا الايموجي - 🔓 -",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🏆", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("💎", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🙄", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("💸", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("💣", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🔓", callback_data=f"yes:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اختر هذا الايموجي - 🌠 -",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☄️", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🙈", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🦄", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("🌠", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("🌈", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🧑‍💻", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "ماهي عاصمة سوريا",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("دمشق", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("دير الزور", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ادلب", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("ليو ميسي", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الرياض", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("مزة فيلات", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "ماهي عملة الولايات المتحدة الأمريكية",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("الروبية", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الجنيه", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الليرة", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("الدولار", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("الدينار", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الين", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اسم مذكر يبدأ بحرف ز",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("زيد", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("علي", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("محمد", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("عمر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("المريخ", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("احمد", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اسم مؤنث ينتهي بحرف ي",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("لورين", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ماجدة", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("علياء", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("أماني", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("فرح", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("أمل", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اسم مؤنث يبدأ بحرف أ",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("لورين", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ماجدة", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("علياء", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("أمل", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("فرح", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("يمنى", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "الأسبوع كم يوم؟",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("1", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("2", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("3", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("4", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("5", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("6", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("7", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("8", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("9", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
    ]
    return random.choice(for_verify)


@Client.on_chat_join_request(filters.group, group=100)
def antiPersian(c, m):
    if r.get(f"{m.chat.id}:lockJoinPersian:{hmshelp}"):
        k = r.get(f"{hmshelp}:botkey")
        if not pre_pls(m.from_user.id, m.chat.id):
            if m.from_user.first_name:
                if (
                    m.from_user.first_name in persianInformation["names"]
                    or m.from_user.id in persianInformation["ids"]
                    or "ه‍" in m.from_user.first_name
                    or "ی" in m.from_user.first_name
                    or "ک" in m.from_user.first_name
                    or "چ" in m.from_user.first_name
                    or "👙" in m.from_user.first_name
                ):
                    c.decline_chat_join_request(m.chat.id, m.from_user.id)
                    if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}"):
                        c.send_message(
                            m.chat.id,
                            """
「 {} 」
{} تم رفض طلب انضمامه لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k),
                        )
                    return True
            if m.from_user.last_name:
                if (
                    m.from_user.last_name in persianInformation["last_names"]
                    or m.from_user.id in persianInformation["ids"]
                    or "ه‍" in m.from_user.last_name
                    or "ی" in m.from_user.last_name
                    or "ک" in m.from_user.last_name
                    or "چ" in m.from_user.last_name
                    or "👙" in m.from_user.last_name
                ):
                    c.decline_chat_join_request(m.chat.id, m.from_user.id)
                    if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}"):
                        c.send_message(
                            m.chat.id,
                            """
「 {} 」
{} تم رفض طلب انضمامه لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k),
                        )
                    return True


@Client.on_message(filters.group & filters.text, group=28)
def guardCommandsHandler(c, m):
    k = r.get(f"{hmshelp}:botkey")
    channel = (
        r.get(f"{hmshelp}:BotChannel") if r.get(f"{hmshelp}:BotChannel") else "alwzaraa2"
    )
    Thread(target=guardCommands, args=(c, m, k, channel)).start()


def guardCommands(c, m, k, channel):
    if not r.get(f"{m.chat.id}:enable:{hmshelp}"):
        return False
    if r.get(f"{m.chat.id}:mute:{hmshelp}") and not admin_pls(
        m.from_user.id, m.chat.id
    ):
        return False
    if r.get(f"{m.from_user.id}:mute:{m.chat.id}{hmshelp}"):
        return False
    if r.get(f"{m.from_user.id}:mute:{hmshelp}"):
        return False
    if r.get(f"{m.chat.id}:addCustom:{m.from_user.id}{hmshelp}"):
        return False
    if r.get(f"{m.chat.id}addCustomG:{m.from_user.id}{hmshelp}"):
        return False
    if r.get(f"{m.chat.id}:delCustom:{m.from_user.id}{hmshelp}") or r.get(
        f"{m.chat.id}:delCustomG:{m.from_user.id}{hmshelp}"
    ):
        return False
    text = m.text
    name = r.get(f"{hmshelp}:BotName") if r.get(f"{hmshelp}:BotName") else "ليو"
    if text.startswith(f"{name} "):
        text = text.replace(f"{name} ", "")
    if r.get(f"{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}"):
        text = r.get(f"{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}")
    if r.get(f"Custom:{hmshelp}&text={text}"):
        text = r.get(f"Custom:{hmshelp}&text={text}")
    if isLockCommand(m.from_user.id, m.chat.id, text):
        return
    Open = """
{} من 「 {} 」
{} ابشر فتحت {}
☆
"""
    Openn = """
{} من 「 {} 」
{} {} مفتوح من قبل
☆
"""
    Openn2 = """
{} من 「 {} 」
{} {} مفتوحة من قبل
☆
"""

    lock = """
{} من 「 {} 」
{} ابشر قفلت {}
☆
"""

    lockn = """
{} من 「 {} 」
{} {} مقفل من قبل
☆
"""
    locknn = """
{} من 「 {} 」
{} {} مقفلة من قبل
☆
"""
    
    if text == "الساعة" or text == "الساعة" or text == "الوقت":
        TIME_ZONE = "Asia/Riyadh"
        ZONE = pytz.timezone(TIME_ZONE)
        TIME = datetime.now(ZONE)
        clock = TIME.strftime("%I:%M %p")
        return m.reply(f"{k} الساعة ( {clock} )")

    if text == "القوانين":
        if r.get(f"{m.chat.id}:CustomRules:{hmshelp}"):
            rules = r.get(f"{m.chat.id}:CustomRules:{hmshelp}")
        else:
            rules = f"""{k} ممنوع نشر الروابط
{k} ممنوع التكلم او نشر صور اباحيه
{k} ممنوع اعاده توجيه
{k} ممنوع العنصرية بكل انواعها
{k} الرجاء احترام المدراء والادمنيه"""
        return m.reply(rules, disable_web_page_preview=True)

    if text == "التاريخ":
        b = Hijri.today().isoformat()
        a = b.split("-")
        year = int(a[0])
        month = int(a[1])
        day = int(a[2])
        hijri = Hijri(year, month, day)
        hijri_date = str(b).replace("-", "/")
        hijri_month = hijri.month_name("ar")

        b = Gregorian.today().isoformat()
        a = b.split("-")
        year = int(a[0])
        month = int(a[1])
        day = int(a[2])
        geo = Gregorian(year, month, day)
        geo_date = str(b).replace("-", "/")
        geo_month = geo.month_name("en")[:3]

        return m.reply(f"""
التاريخ:
{k} هجري ↢ {hijri_date} {hijri_month}
{k} ميلادي ↢ {geo_date} {geo_month}
""")

    if text == "المالك":
        owner = None
        for mm in m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
            if mm.status == ChatMemberStatus.OWNER:
                owner = mm.user
                break
        if owner:
            if owner.is_deleted:
                m.reply("حساب المالك محذوف")
            else:
                owner_username = owner.username if owner.username else owner.id
                caption = f"• Owner ☆ ↦ {owner.mention}\n\n"
                caption += f"• Owner User ↦ @{owner_username}"
                if owner.photo:
                    file_id = owner.photo.big_file_id
                    photo_path = c.download_media(file_id)
                    button = InlineKeyboardMarkup(
                        [[InlineKeyboardButton(owner.first_name, user_id=owner.id)]]
                    )
                    m.reply_photo(
                        photo=photo_path, caption=caption, reply_markup=button
                    )
                    os.remove(photo_path)
                else:
                    button = InlineKeyboardMarkup(
                        [[InlineKeyboardButton(owner.first_name, user_id=owner.id)]]
                    )
                    m.reply(caption, reply_markup=button)

    if text == "اطردني":
        if r.get(f"{m.chat.id}:enableKickMe:{hmshelp}"):
            get = m.chat.get_member(m.from_user.id)
            if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                return m.reply(f"{k} ممنوع طرد الحلوين")
            if admin_pls(m.from_user.id, m.chat.id):
                return m.reply(f"{k} ممنوع طرد الحلوين")
            else:
                m.reply(
                    f"طردتك يانفسية , وارسلت لك الرابط خاص تقدر ترجع متى مابغيت يامعقد"
                )
                m.chat.ban_member(m.from_user.id)
                time.sleep(0.5)
                c.unban_chat_member(m.chat.id, m.from_user.id)
                link = c.get_chat(m.chat.id).invite_link
                try:
                    c.send_message(
                        m.from_user.id,
                        f"{k} حبيبي النفسية رابط القروب الي طردتك منه: {link}",
                    )
                except:
                    pass
                return False

    if text == "الرابط":
        if not r.get(f"{m.chat.id}:disableLINK:{hmshelp}"):
            link = c.get_chat(m.chat.id).invite_link
            return m.reply(f"[{m.chat.title}]({link})", disable_web_page_preview=True)

    if text == "انشاء رابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        link = c.get_chat(m.chat.id).invite_link
        c.revoke_chat_invite_link(m.chat.id, link)
        return m.reply(f'{k} ابشر سويت رابط جديد ارسل "الرابط"')

    if text.startswith("@all"):
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        if r.get(f"{m.chat.id}:disableALL:{hmshelp}"):
            return m.reply("المنشن معطل")
        if r.get(f"{m.chat.id}:inMention:{hmshelp}"):
            return False
        if r.get(f"{m.chat.id}:inMentionWAIT:{hmshelp}"):
            get = r.ttl(f"{m.chat.id}:inMentionWAIT:{hmshelp}")
            tm = time.strftime("%M:%S", time.gmtime(get))
            return m.reply(f"{k} سويت منشن من شوي تعال بعد {tm}")
        else:
            if len(text.split()) > 1:
                reason = text.split(None, 1)[1]
            else:
                reason = ""
            users_list = []
            r.set(f"{m.chat.id}:inMention:{hmshelp}", 1)
            m.reply(f"{k} بسوي منشن يحلو ، اذا تبي توقفه ارسل `/Cancel` او `ايقاف`")
            for mm in m.chat.get_members(limit=150):
                if mm.user and not mm.user.is_deleted and not mm.user.is_bot:
                    users_list.append(mm.user.mention)
            final_list = [users_list[x : x + 5] for x in range(0, len(users_list), 5)]
            ftext = f"{reason}\n\n"
            for a in final_list:
                for i in a:
                    if not r.get(f"{m.chat.id}:inMention:{hmshelp}"):
                        return False
                    ftext += f"{i} , "
                c.send_message(m.chat.id, ftext)
                ftext = f"{reason}\n\n"
            r.delete(f"{m.chat.id}:inMention:{hmshelp}")
            r.set(f"{m.chat.id}:inMentionWAIT:{hmshelp}", 1, ex=1200)

    if text.lower() == "/cancel" or text == "ايقاف":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:inMention:{hmshelp}"):
                return m.reply(f"{k} مو قاعده اسوي منشن ركز")
            else:
                r.delete(f"{m.chat.id}:inMention:{hmshelp}")
                return m.reply("ابشر وقفت المنشن")

    if text == "منشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        return m.reply("استخدم امر\n@all مع الكلام")

    if text == "تعطيل المنشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableALL:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} المشن معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableALL:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت المنشن\n☆"
                )

    if text == "تفعيل المنشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableALL:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} المنشن مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableALL:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت المنشن\n☆"
                )

    if text == "تعطيل الترحيب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableWelcome:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترحيب معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableWelcome:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الترحيب\n☆"
                )

    if text == "تعطيل الترحيب بالصورة" or text == "تعطيل الترحيب بالصورة":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableWelcomep:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترحيب بالصورة من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableWelcomep:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الترحيب بالصورة\n☆"
                )

    if text == "تفعيل الترحيب بالصورة" or text == "تفعيل الترحيب بالصورة":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableWelcomep:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترحيب بالصورة مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableWelcomep:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الترحيب بالصورة\n☆"
                )

    if text == "تعطيل الرابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableLINK:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الرابط معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableLINK:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الرابط\n☆"
                )

    if text == "تفعيل الرابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableLINK:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الرابط مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableLINK:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الرابط\n☆"
                )

    if text == "تعطيل البايو":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableBio:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} البايو معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableBio:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت البايو\n☆"
                )

    if text == "تفعيل البايو":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableBio:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} البايو مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableBio:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت البايو\n☆"
                )

    if text == "تعطيل اطردني":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:enableKickMe:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} اطردني معطل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:enableKickMe:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت اطردني\n☆"
                )

    if text == "تفعيل اطردني":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:enableKickMe:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} اطردني مفعل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:enableKickMe:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت اطردني\n☆"
                )

    if text == "تعطيل التحقق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:enableVerify:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التحقق معطل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:enableVerify:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التحقق\n☆"
                )

    if text == "تفعيل التحقق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:enableVerify:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التحقق مفعل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:enableVerify:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التحقق\n☆"
                )

    if (
        (text == "شيكول" or text == "ترجم")
        and m.reply_to_message
        and m.reply_to_message.voice
    ):
        if m.reply_to_message.voice.file_size > 20971520:
            return m.reply("حجمه اكثر من ٢٠ ميجابايت، توكل")
        id = random.randint(99, 1000)
        voice = m.reply_to_message.download(f"./zaid{id}.wav")
        s = sr.Recognizer()
        sound = AudioSegment.from_ogg(voice)
        wav_file = sound.export(voice, format="wav")
        with sr.AudioFile(wav_file) as src:
            audio_source = s.record(src)
        try:
            text = s.recognize_google(audio_source, language="ar-SA")
        except Exception as e:
            print(e)
            os.remove(f"zaid{id}.wav")
            return m.reply("عجزت افهم وش يقول ")
        os.remove(f"zaid{id}.wav")
        return m.reply(f"يقول : {text}")

    if (
        (text == "zaid" or text == "زوز")
        and m.reply_to_message
        and m.reply_to_message.voice
        and m.from_user.id == 6168217372
    ):
        if m.reply_to_message.voice.file_size > 20971520:
            return m.reply("حجمه اكثر من ٢٠ ميجابايت، توكل")
        id = random.randint(99, 1000)
        voice = m.reply_to_message.download(f"./zaid{id}.wav")
        s = sr.Recognizer()
        sound = AudioSegment.from_ogg(voice)
        wav_file = sound.export(voice, format="wav")
        with sr.AudioFile(wav_file) as src:
            audio_source = s.record(src)
        try:
            text = s.recognize_google(audio_source, language="en-US")
        except Exception as e:
            print(e)
            os.remove(f"zaid{id}.wav")
            return m.reply("عجزت افهم وش يقول ")
        os.remove(f"zaid{id}.wav")
        return m.reply(f"يقول : {text}")

    if text.startswith("منع "):
        if mod_pls(m.from_user.id, m.chat.id):
            noice = text.split(None, 1)[1]
            if r.sismember(f"{m.chat.id}:NotAllowedListText:{hmshelp}", noice):
                return m.reply(
                    f"{k} الكلمة ( {noice} ) موجودة بقائمة المنع",
                    disable_web_page_preview=True,
                )
            else:
                r.sadd(f"{m.chat.id}:NotAllowedListText:{hmshelp}", noice)
                return m.reply(
                    f"{k} الكلمة ( {noice} ) اضفتها الى قائمة المنع",
                    disable_web_page_preview=True,
                )

    if text.startswith("الغاء منع ") and len(text.split()) > 2:
        if mod_pls(m.from_user.id, m.chat.id):
            noice = text.split(None, 2)[2]
            if not r.sismember(f"{m.chat.id}:NotAllowedListText:{hmshelp}", noice):
                return m.reply(
                    f"{k} الكلمة ( {noice} ) مو مضافة بقائمة المنع",
                    disable_web_page_preview=True,
                )
            else:
                r.srem(f"{m.chat.id}:NotAllowedListText:{hmshelp}", noice)
                return m.reply(
                    f"{k} ابشر مسحت ( {noice} ) من قائمة المنع",
                    disable_web_page_preview=True,
                )

    if text == "منع" and m.reply_to_message and m.reply_to_message.media:
        if mod_pls(m.from_user.id, m.chat.id):
            rep = m.reply_to_message
            if rep.sticker:
                file_id = rep.sticker.file_id
                type = "sticker"
            if rep.animation:
                file_id = rep.animation.file_id
                type = "animation"
            if rep.photo:
                file_id = rep.photo.file_id
                type = "photo"
            if rep.video:
                file_id = rep.photo.file_id
                type = "video"
            if rep.voice:
                file_id = rep.voice.file_id
                type = "voice"
            if rep.audio:
                file_id = rep.audio.file_id
                type = "audio"
            if rep.document:
                file_id = rep.document.file_id
                type = "document"

            id = file_id[-6:]
            if r.get(f"{id}:NotAllow:{m.chat.id}{hmshelp}"):
                return m.reply(f"{k} موجودة بقائمة المنع")
            else:
                r.set(f"{id}:NotAllow:{m.chat.id}{hmshelp}", 1)
                r.sadd(
                    f"{m.chat.id}:NotAllowedList:{hmshelp}",
                    f"file={id}&by={m.from_user.id}&type={type}&file_id={file_id}",
                )
                return m.reply(f"{k} واضفناها لقائمة المنع")

    if text == "الغاء منع" and m.reply_to_message and m.reply_to_message.media:
        if mod_pls(m.from_user.id, m.chat.id):
            rep = m.reply_to_message
            if rep.sticker:
                file_id = rep.sticker.file_id
                type = "sticker"
            if rep.animation:
                file_id = rep.animation.file_id
                type = "animation"
            if rep.photo:
                file_id = rep.photo.file_id
                type = "photo"
            if rep.video:
                file_id = rep.photo.file_id
                type = "video"
            if rep.voice:
                file_id = rep.voice.file_id
                type = "voice"
            if rep.audio:
                file_id = rep.audio.file_id
                type = "audio"
            if rep.document:
                file_id = rep.document.file_id
                type = "document"

            id = file_id[-6:]
            if not r.get(f"{id}:NotAllow:{m.chat.id}{hmshelp}"):
                return m.reply(f"{k} مو موجودة بقائمة المنع")
            else:
                r.delete(f"{id}:NotAllow:{m.chat.id}{hmshelp}")
                r.srem(
                    f"{m.chat.id}:NotAllowedList:{hmshelp}",
                    f"file={id}&by={m.from_user.id}&type={type}&file_id={file_id}",
                )
                return m.reply(f"{k} ابشر شلتها من قائمة المنع")

    if text == "منع" and m.reply_to_message and not m.reply_to_message.media:
        if mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} المنع بالرد فقط للوسائط")

    if text == "صلاحياته" and m.reply_to_message and m.reply_to_message.from_user:
        if not (owner_pls(m.from_user.id, m.chat.id) or dev_pls(m.from_user.id, m.chat.id)):
            return m.reply(f"{k} هذا الأمر يخص ( المالك أو المطور الأساسي ) فقط")
        
        target_user = m.reply_to_message.from_user
        get_member = m.chat.get_member(target_user.id)
        
        if not get_member.privileges:
            return m.reply("هذا المستخدم ليس مشرفاً")
        
        permissions = [
            ("حذف الرسائل", "can_delete_messages"),
            ("حظر الأعضاء", "can_restrict_members"),
            ("تثبيت الرسائل", "can_pin_messages"),
            ("دعوة المستخدمين", "can_invite_users"),
            ("تغيير المعلومات", "can_change_info"),
            ("إدارة المكالمات", "can_manage_video_chats"),
            ("رفع مشرفين", "can_promote_members")
        ]
        
        buttons = []
        for perm, key in permissions:
            current_status = getattr(get_member.privileges, key, False)
            buttons.append([
                InlineKeyboardButton(
                    f"{perm} {'✅' if current_status else '❌'}", 
                    callback_data=f"edit_perm_{key}_{target_user.id}"
                )
            ])
        
        buttons.append([
            InlineKeyboardButton("حفظ التعديلات", callback_data=f"save_perms_{target_user.id}"),
            InlineKeyboardButton("إلغاء", callback_data=f"cancel_perms_{target_user.id}")
        ])
        
        m.reply(
            f"⚙️ صلاحيات المشرف: {target_user.mention}\n\n"
            "▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
            "اضغط على الصلاحية لتغيير حالتها",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    if text == "قائمة المنع" or text == "قائمة المنع":
        text1 = "الكلمات الممنوعة:\n"
        text2 = "الوسائط الممنوعة:\n"
        count = 1
        count2 = 1
        if mod_pls(m.from_user.id, m.chat.id):
            if not r.smembers(
                f"{m.chat.id}:NotAllowedListText:{hmshelp}"
            ) and not r.smembers(f"{m.chat.id}:NotAllowedList:{hmshelp}"):
                return m.reply(f"{k} مافي شي ممنوع")
            else:
                if not r.smembers(f"{m.chat.id}:NotAllowedListText:{hmshelp}"):
                    text1 += "لايوجد"
                else:
                    for a in r.smembers(f"{m.chat.id}:NotAllowedListText:{hmshelp}"):
                        text1 += f"{count} - {a}\n"
                        count += 1
                if not r.smembers(f"{m.chat.id}:NotAllowedList:{hmshelp}"):
                    text2 += "لايوجد"
                else:
                    for a in r.smembers(f"{m.chat.id}:NotAllowedList:{hmshelp}"):
                        g = a
                        id = g.split("file=")[1].split("&")[0]
                        by = g.split("by=")[1].split("&")[0]
                        type = g.split("type=")[1].split("&")[0]
                        text2 += (
                            f"{count2} - (`{id}`) ࿓ ( [{type}](tg://user?id={by}) )\n"
                        )
                return m.reply(f"{text1}\n{text2}", disable_web_page_preview=True)

    if text == "مسح قائمة المنع" or text == "مسح قائمة المنع":
        if mod_pls(m.from_user.id, m.chat.id):
            if not r.smembers(
                f"{m.chat.id}:NotAllowedListText:{hmshelp}"
            ) and not r.smembers(f"{m.chat.id}:NotAllowedList:{hmshelp}"):
                return m.reply(f"{k} مافي شي ممنوع")
            else:
                if r.smembers(f"{m.chat.id}:NotAllowedListText:{hmshelp}"):
                    r.delete(f"{m.chat.id}:NotAllowedListText:{hmshelp}")
                if r.smembers(f"{m.chat.id}:NotAllowedList:{hmshelp}"):
                    for a in r.smembers(f"{m.chat.id}:NotAllowedList:{hmshelp}"):
                        file_id = a.split("file=")[1].split("&by=")[0]
                        r.delete(f"{file_id}:NotAllow:{m.chat.id}{hmshelp}")
                r.delete(f"{m.chat.id}:NotAllowedList:{hmshelp}")
                return m.reply(f"{k} ابشر مسحت قائمة المنع")

    if text == "قفل الكل":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if (
                r.get(f"{m.chat.id}:mute:{hmshelp}")
                and r.get(f"{m.chat.id}:lockEdit:{hmshelp}")
                and r.get(f"{m.chat.id}:lockEditM:{hmshelp}")
                and r.get(f"{m.chat.id}:lockVoice:{hmshelp}")
                and r.get(f"{m.chat.id}:lockVideo:{hmshelp}")
                and r.get(f"{m.chat.id}:lockNot:{hmshelp}")
                and r.get(f"{m.chat.id}:lockPhoto:{hmshelp}")
                and r.get(f"{m.chat.id}:lockPersian:{hmshelp}")
                and r.get(f"{m.chat.id}:lockStickers:{hmshelp}")
                and r.get(f"{m.chat.id}:lockFiles:{hmshelp}")
                and r.get(f"{m.chat.id}:lockAnimations:{hmshelp}")
                and r.get(f"{m.chat.id}:lockUrls:{hmshelp}")
                and r.get(f"{m.chat.id}:lockHashtags:{hmshelp}")
                and r.get(f"{m.chat.id}:lockBots:{hmshelp}")
                and r.get(f"{m.chat.id}:lockTags:{hmshelp}")
                and r.get(f"{m.chat.id}:lockMessages:{hmshelp}")
                and r.get(f"{m.chat.id}:lockSpam:{hmshelp}")
                and r.get(f"{m.chat.id}:lockForward:{hmshelp}")
                and r.get(f"{m.chat.id}:lockSHTM:{hmshelp}")
                and r.get(f"{m.chat.id}:lockaddContacts:{hmshelp}")
                and r.get(f"{m.chat.id}:lockAudios:{hmshelp}")
                and r.get(f"{m.chat.id}:lockChannels:{hmshelp}")
                and r.get(f"{m.chat.id}:lockJoin:{hmshelp}")
                and r.get(f"{m.chat.id}:lockInline:{hmshelp}")
                and r.get(f"{m.chat.id}:lockNSFW:{hmshelp}")
            ):
                return m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} كل شي مقفل يالطيب!\n☆"
                )
            else:
                m.reply(f"{k} من 「 {m.from_user.mention} 」 \n{k} ابشر قفلت كل شي\n☆")
                r.set(f"{m.chat.id}:mute:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockJoin:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockChannels:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockEdit:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockEditM:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockVoice:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockVideo:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockNot:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockPhoto:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockStickers:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockAnimations:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockFiles:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockPersian:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockUrls:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockHashtags:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockMessages:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockTags:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockBots:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockSpam:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockInline:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockForward:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockAudios:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockaddContacts:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockSHTM:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockNSFW:{hmshelp}", 1)
                return False

    if text == "فتح الكل":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if (
                not r.get(f"{m.chat.id}:mute:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockEdit:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockEditM:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockVoice:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockVideo:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockNot:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockPhoto:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockPersian:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockStickers:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockFiles:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockAnimations:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockUrls:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockHashtags:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockBots:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockTags:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockMessages:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockSpam:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockForward:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockSHTM:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockaddContacts:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockAudios:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockChannels:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockJoin:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockInline:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockNSFW:{hmshelp}")
            ):
                return m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} كل شي مفتوح يالطيب!\n☆"
                )
            else:
                m.reply(f"{k} من 「 {m.from_user.mention} 」 \n{k} ابشر فتحت كل شي\n☆")
                r.delete(f"{m.chat.id}:mute:{hmshelp}")
                r.delete(f"{m.chat.id}:lockJoin:{hmshelp}")
                r.delete(f"{m.chat.id}:lockChannels:{hmshelp}")
                r.delete(f"{m.chat.id}:lockEdit:{hmshelp}")
                r.delete(f"{m.chat.id}:lockEditM:{hmshelp}")
                r.delete(f"{m.chat.id}:lockVoice:{hmshelp}")
                r.delete(f"{m.chat.id}:lockVideo:{hmshelp}")
                r.delete(f"{m.chat.id}:lockNot:{hmshelp}")
                r.delete(f"{m.chat.id}:lockPhoto:{hmshelp}")
                r.delete(f"{m.chat.id}:lockStickers:{hmshelp}")
                r.delete(f"{m.chat.id}:lockAnimations:{hmshelp}")
                r.delete(f"{m.chat.id}:lockFiles:{hmshelp}")
                r.delete(f"{m.chat.id}:lockPersian:{hmshelp}")
                r.delete(f"{m.chat.id}:lockUrls:{hmshelp}")
                r.delete(f"{m.chat.id}:lockHashtags:{hmshelp}")
                r.delete(f"{m.chat.id}:lockMessages:{hmshelp}")
                r.delete(f"{m.chat.id}:lockTags:{hmshelp}")
                r.delete(f"{m.chat.id}:lockBots:{hmshelp}")
                r.delete(f"{m.chat.id}:lockSpam:{hmshelp}")
                r.delete(f"{m.chat.id}:lockInline:{hmshelp}")
                r.delete(f"{m.chat.id}:lockForward:{hmshelp}")
                r.delete(f"{m.chat.id}:lockAudios:{hmshelp}")
                r.delete(f"{m.chat.id}:lockaddContacts:{hmshelp}")
                r.delete(f"{m.chat.id}:lockSHTM:{hmshelp}")
                r.delete(f"{m.chat.id}:lockKFR:{hmshelp}")
                r.delete(f"{m.chat.id}:lockNSFW:{hmshelp}")
                return False

    if text == "تفعيل الحماية" or text == "تفعيل الحمايه":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المالك وفوق ) بس")
        else:
            if (
                r.get(f"{m.chat.id}:lockEditM:{hmshelp}")
                and r.get(f"{m.chat.id}:lockVoice:{hmshelp}")
                and r.get(f"{m.chat.id}:lockVideo:{hmshelp}")
                and r.get(f"{m.chat.id}:lockPhoto:{hmshelp}")
                and r.get(f"{m.chat.id}:lockPersian:{hmshelp}")
                and r.get(f"{m.chat.id}:lockStickers:{hmshelp}")
                and r.get(f"{m.chat.id}:lockFiles:{hmshelp}")
                and r.get(f"{m.chat.id}:lockAnimations:{hmshelp}")
                and r.get(f"{m.chat.id}:lockUrls:{hmshelp}")
                and r.get(f"{m.chat.id}:lockTags:{hmshelp}")
                and r.get(f"{m.chat.id}:lockMessages:{hmshelp}")
                and r.get(f"{m.chat.id}:lockSpam:{hmshelp}")
                and r.get(f"{m.chat.id}:lockForward:{hmshelp}")
                and r.get(f"{m.chat.id}:lockSHTM:{hmshelp}")
                and r.get(f"{m.chat.id}:lockAudios:{hmshelp}")
                and r.get(f"{m.chat.id}:lockChannels:{hmshelp}")
                and r.get(f"{m.chat.id}:lockNSFW:{hmshelp}")
            ):
                return m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} الحماية مفعله من قبل\n☆"
                )
            else:
                m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} ابشر فعلت الحمايه\n☆"
                )

                r.set(f"{m.chat.id}:lockChannels:{hmshelp}", 1)
                r.delete(f"{m.chat.id}:disableWarn:{hmshelp}")
                r.set(f"{m.chat.id}:lockVoice:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockVideo:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockPhoto:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockStickers:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockAnimations:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockFiles:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockPersian:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockUrls:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockTags:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockSpam:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockForward:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockAudios:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockSHTM:{hmshelp}", 1)
                r.set(f"{m.chat.id}:lockNSFW:{hmshelp}", 1)
                return False

    if text == "تعطيل الحماية" or text == "تعطيل الحمايه":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المالك وفوق ) بس")
        else:
            if (
                r.get(f"{m.chat.id}:lockEditM:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockVoice:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockVideo:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockPhoto:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockPersian:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockStickers:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockFiles:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockAnimations:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockUrls:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockTags:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockMessages:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockSpam:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockForward:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockSHTM:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockAudios:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockChannels:{hmshelp}")
                and not r.get(f"{m.chat.id}:lockNSFW:{hmshelp}")
            ):
                return m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} الحماية معطله من قبل\n☆"
                )
            else:
                m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} ابشر عطلت الحمايه\n☆"
                )

                r.delete(f"{m.chat.id}:lockChannels:{hmshelp}")
                r.delete(f"{m.chat.id}:lockVoice:{hmshelp}")
                r.delete(f"{m.chat.id}:lockVideo:{hmshelp}")
                r.delete(f"{m.chat.id}:lockPhoto:{hmshelp}")
                r.delete(f"{m.chat.id}:lockStickers:{hmshelp}")
                r.delete(f"{m.chat.id}:lockAnimations:{hmshelp}")
                r.delete(f"{m.chat.id}:lockFiles:{hmshelp}")
                r.delete(f"{m.chat.id}:lockPersian:{hmshelp}")
                r.delete(f"{m.chat.id}:lockUrls:{hmshelp}")
                r.delete(f"{m.chat.id}:lockTags:{hmshelp}")
                r.delete(f"{m.chat.id}:lockSpam:{hmshelp}")
                r.delete(f"{m.chat.id}:lockForward:{hmshelp}")
                r.delete(f"{m.chat.id}:lockAudios:{hmshelp}")
                r.delete(f"{m.chat.id}:lockSHTM:{hmshelp}")
                r.delete(f"{m.chat.id}:lockNSFW:{hmshelp}")
                return False

    if text == "قفل الدردشة" or text == "قفل الدردشه" or text == "قفل الشات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:mute:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الشات"))
            else:
                r.set(f"{m.chat.id}:mute:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الشات"))

    if text == "فتح الدردشة" or text == "فتح الدردشه" or text == "فتح الشات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:mute:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الشات"))
            else:
                r.delete(f"{m.chat.id}:mute:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الشات"))

    if text == "قفل التعديل":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockEdit:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "التعديل"))
            else:
                r.set(f"{m.chat.id}:lockEdit:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "التعديل"))

    if text == "فتح التعديل":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockEdit:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "التعديل"))
            else:
                r.delete(f"{m.chat.id}:lockEdit:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "التعديل"))

    if text == "قفل تعديل الميديا":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockEditM:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "تعديل الميديا"))
            else:
                r.set(f"{m.chat.id}:lockEditM:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "تعديل الميديا"))

    if text == "فتح تعديل الميديا":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockEditM:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "تعديل الميديا"))
            else:
                r.delete(f"{m.chat.id}:lockEditM:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "تعديل الميديا"))

    if text == "قفل الفويسات" or text == "قفل البصمات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockVoice:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الفويس"))
            else:
                r.set(f"{m.chat.id}:lockVoice:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الفويس"))

    if text == "فتح الفويسات" or text == "فتح البصمات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockVoice:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الفويس"))
            else:
                r.delete(f"{m.chat.id}:lockVoice:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الفويس"))

    if text == "قفل الفيديو" or text == "قفل الفيديوهات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockVideo:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الفيديو"))
            else:
                r.set(f"{m.chat.id}:lockVideo:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الفيديو"))

    if text == "فتح الفيديو" or text == "فتح الفيديوهات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockVideo:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الفيديو"))
            else:
                r.delete(f"{m.chat.id}:lockVideo:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الفيديو"))

    if text == "قفل الاشعارات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockNot:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الاشعارات"))
            else:
                r.set(f"{m.chat.id}:lockNot:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الاشعارات"))

    if text == "فتح الاشعارات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockNot:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الاشعارات"))
            else:
                r.delete(f"{m.chat.id}:lockNot:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الاشعارات"))

    if text == "قفل الصور":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockPhoto:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الصور"))
            else:
                r.set(f"{m.chat.id}:lockPhoto:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الصور"))

    if text == "فتح الصور":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockPhoto:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الصور"))
            else:
                r.delete(f"{m.chat.id}:lockPhoto:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الصور"))

    if text == "قفل الملصقات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockStickers:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الملصقات"))
            else:
                r.set(f"{m.chat.id}:lockStickers:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الملصقات"))

    if text == "فتح الملصقات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockStickers:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الملصقات"))
            else:
                r.delete(f"{m.chat.id}:lockStickers:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الملصقات"))

    if text == "قفل الفارسيه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockPersian:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الفارسيه"))
            else:
                r.set(f"{m.chat.id}:lockPersian:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الفارسيه"))

    if text == "فتح الفارسيه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockPersian:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الفارسيه"))
            else:
                r.delete(f"{m.chat.id}:lockPersian:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الفارسيه"))

    if text == "قفل الملفات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockFiles:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الملفات"))
            else:
                r.set(f"{m.chat.id}:lockFiles:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الملفات"))

    if text == "فتح الملفات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockFiles:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الملفات"))
            else:
                r.delete(f"{m.chat.id}:lockFiles:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الملفات"))

    if text == "قفل المتحركات" or text == "قفل المتحركه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockAnimations:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "المتحركات"))
            else:
                r.set(f"{m.chat.id}:lockAnimations:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "المتحركات"))

    if text == "فتح المتحركات" or text == "فتح المتحركه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockAnimations:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "المتحركات"))
            else:
                r.delete(f"{m.chat.id}:lockAnimations:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "المتحركات"))

    if text == "قفل الروابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockUrls:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الروابط"))
            else:
                r.set(f"{m.chat.id}:lockUrls:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الروابط"))

    if text == "فتح الروابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockUrls:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الروابط"))
            else:
                r.delete(f"{m.chat.id}:lockUrls:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الروابط"))

    if text == "قفل الهشتاق" or text == "قفل الهاشتاق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockHashtags:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الهاشتاق"))
            else:
                r.set(f"{m.chat.id}:lockHashtags:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الهاشتاق"))

    if text == "فتح الهشتاق" or text == "فتح الهاشتاق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockHashtags:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الهاشتاق"))
            else:
                r.delete(f"{m.chat.id}:lockHashtags:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الهاشتاق"))

    if text == "قفل البوتات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockBots:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "البوتات"))
            else:
                r.set(f"{m.chat.id}:lockBots:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "البوتات"))

    if text == "فتح البوتات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockBots:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "البوتات"))
            else:
                r.delete(f"{m.chat.id}:lockBots:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "البوتات"))

    if text == "قفل اليوزرات" or text == "قفل المنشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockTags:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "اليوزرات"))
            else:
                r.set(f"{m.chat.id}:lockTags:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "اليوزرات"))

    if text == "فتح اليوزرات" or text == "فتح المنشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockTags:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "اليوزرات"))
            else:
                r.delete(f"{m.chat.id}:lockTags:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "اليوزرات"))

    """
   if text == 'قفل الكفر' or text == 'قفل الشيعه' or text == 'قفل الشيعة':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if r.get(f'{m.chat.id}:lockKFR:{hmshelp}'):
         return m.reply(locknn.format(k,m.from_user.mention,k,'الكفر'))
       else:
         r.set(f'{m.chat.id}:lockKFR:{hmshelp}',1)
         return m.reply(lock.format(k,m.from_user.mention,k,'الكفر'))

   if text == 'فتح الكفر' or text == 'فتح الشيعه' or text == 'فتح الشيعة':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.get(f'{m.chat.id}:lockKFR:{hmshelp}'):
         return m.reply(Openn2.format(k,m.from_user.mention,k,'الكفر'))
       else:
         r.delete(f'{m.chat.id}:lockKFR:{hmshelp}')
         return m.reply(Open.format(k,m.from_user.mention,k,'الكفر'))
   """

    if text == "قفل الإباحي" or text == "قفل الاباحي":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المالك وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockNSFW:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الإباحي"))
            else:
                r.set(f"{m.chat.id}:lockNSFW:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الإباحي"))

    if text == "فتح الإباحي" or text == "فتح الاباحي":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المالك وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockNSFW:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "االإباحي"))
            else:
                r.delete(f"{m.chat.id}:lockNSFW:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الإباحي"))

    if text == "قفل الكلام الكثير" or text == "قفل الكلايش":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockMessages:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الكلام الكثير"))
            else:
                r.set(f"{m.chat.id}:lockMessages:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الكلام الكثير"))

    if text == "فتح الكلام الكثير" or text == "فتح الكلايش":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockMessages:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الكلام الكثير"))
            else:
                r.delete(f"{m.chat.id}:lockMessages:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الكلام الكثير"))

    if text == "قفل التكرار":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockSpam:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "التكرار"))
            else:
                r.set(f"{m.chat.id}:lockSpam:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "التكرار"))

    if text == "فتح التكرار":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockSpam:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "التكرار"))
            else:
                r.delete(f"{m.chat.id}:lockSpam:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "التكرار"))

    if text == "قفل التوجيه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockForward:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "التوجيه"))
            else:
                r.set(f"{m.chat.id}:lockForward:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "التوجيه"))

    if text == "فتح التوجيه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockForward:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "التوجيه"))
            else:
                r.delete(f"{m.chat.id}:lockForward:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "التوجيه"))

    if text == "قفل الانلاين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockInline:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الانلاين"))
            else:
                r.set(f"{m.chat.id}:lockInline:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الانلاين"))

    if text == "فتح الانلاين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockInline:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الانلاين"))
            else:
                r.delete(f"{m.chat.id}:lockInline:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الانلاين"))

    if text == "قفل السب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockSHTM:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "السب"))
            else:
                r.set(f"{m.chat.id}:lockSHTM:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "السب"))

    if text == "فتح السب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockSHTM:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "السب"))
            else:
                r.delete(f"{m.chat.id}:lockSHTM:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "السب"))

    if text == "قفل الاضافه" or text == "قفل الاضافة" or text == "قفل الجهات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockaddContacts:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الاضافه"))
            else:
                r.set(f"{m.chat.id}:lockaddContacts:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الاضافه"))

    if text == "فتح الاضافه" or text == "فتح الاضافة" or text == "فتح الجهات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockaddContacts:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الاضافه"))
            else:
                r.delete(f"{m.chat.id}:lockaddContacts:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الاضافه"))

    if text == "قفل دخول البوتات" or text == "قفل الوهمي" or text == "قفل الايراني":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockJoinPersian:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "دخول البوتات"))
            else:
                r.set(f"{m.chat.id}:lockJoinPersian:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "دخول البوتات"))

    if text == "فتح دخول البوتات" or text == "فتح الوهمي" or text == "فتح الايراني":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockJoinPersian:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "دخول البوتات"))
            else:
                r.delete(f"{m.chat.id}:lockJoinPersian:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "دخول البوتات"))

    if text == "قفل الصوت":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockAudios:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الصوت"))
            else:
                r.set(f"{m.chat.id}:lockAudios:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الصوت"))

    if text == "فتح الصوت":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockAudios:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الصوت"))
            else:
                r.delete(f"{m.chat.id}:lockAudios:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الصوت"))

    if text == "قفل القنوات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockChannels:{hmshelp}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "القنوات"))
            else:
                r.set(f"{m.chat.id}:lockChannels:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "القنوات"))

    if text == "فتح القنوات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockChannels:{hmshelp}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "القنوات"))
            else:
                r.delete(f"{m.chat.id}:lockChannels:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "القنوات"))

    if text == "قفل الدخول":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockJoin:{hmshelp}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الدخول"))
            else:
                r.set(f"{m.chat.id}:lockJoin:{hmshelp}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الدخول"))

    if text == "فتح الدخول":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockJoin:{hmshelp}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الدخول"))
            else:
                r.delete(f"{m.chat.id}:lockJoin:{hmshelp}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الدخول"))

    if text == "تعطيل التحذير":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableWarn:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التحذير معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableWarn:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التحذير\n☆"
                )

    if text == "تفعيل التحذير":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableWarn:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التحذير مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableWarn:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التحذير\n☆"
                )

    if text == "تعطيل الهمسة":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableWHISPER:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الهمسة معطله من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableWHISPER:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الهمسة\n☆"
                )

    if text == "تفعيل الهمسة":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableWHISPER:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الهمسة مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableWHISPER:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الهمسة\n☆"
                )

    if text == "تعطيل التيك":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableTik:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التيك معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableTik:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التيك\n☆"
                )

    if text == "تفعيل التيك":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableTik:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التيك مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableTik:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التيك\n☆"
                )


    if text == "تعطيل الالعاب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableGames:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الالعاب معطله من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableGames:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الالعاب\n☆"
                )

    if text == "تفعيل الالعاب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableGames:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الالعاب مفعله من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableGames:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الالعاب\n☆"
                )

    if text == "تعطيل الترجمة" or text == "تعطيل الترجمه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableTrans:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترجمه معطله من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableTrans:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الترجمه\n☆"
                )

    if text == "تفعيل الترجمة" or text == "تفعيل الترجمه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableTrans:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترجمه مفعله من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableTrans:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الترجمه\n☆"
                )

    if text == "تعطيل التسلية" or text == "تعطيل التسلية":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableFun:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التسلية معطله من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableFun:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التسلية\n☆"
                )

    if text == "تفعيل التسلية" or text == "تفعيل التسلية":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableFun:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التسلية مفعله من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableFun:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التسلية\n☆"
                )

    if text == "تعطيل الاشتراك":
        if not dev2_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المطور وفوق ) بس")
        else:
            if r.get(f"disableSubscribe:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الاشتراك الاجباري معطل من قبل\n☆"
                )
            else:
                r.set(f"disableSubscribe:{hmshelp}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الاشتراك الاجباري\n☆"
                )

    if text == "قناة الاشتراك":
        if not dev2_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المطور وفوق ) بس")
        ch = r.get(f"forceChannel:{hmshelp}") or "مافي قناة"
        return m.reply(f"{k} قناة الاشتراك هي ( {ch} )")

    if text.startswith("وضع قناة @"):
        if not dev2_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المطور وفوق ) بس")
        username = text.split("@")[1]
        try:
            chat = c.get_chat(username)
        except:
            return m.reply(f"{k} حدث خطأ")
        r.set(f"forceChannel:{hmshelp}", "@" + username)
        return m.reply(f"{k} تم تعيين القناة بنجاح")

    if text == "تفعيل الاشتراك":
        if not dev2_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المطور وفوق ) بس")
        else:
            if not r.get(f"disableSubscribe:{hmshelp}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الاشتراك الاجباري مفعل من قبل\n☆"
                )
            else:
                r.delete(f"disableSubscribe:{hmshelp}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الاشتراك الاجباري\n☆"
                )

    if (
        text == "/ar"
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not r.get(f"{m.chat.id}:disableTrans:{hmshelp}"):
            text = m.reply_to_message.text or m.reply_to_message.caption
            translation = requests.get(
                f"https://hozory.com/translate/?target=ar&text={text}"
            ).json()["result"]["translate"]
            m.reply(f"`{translation}`")

    if (
        text == "/en"
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not r.get(f"{m.chat.id}:disableTrans:{hmshelp}"):
            text = m.reply_to_message.text or m.reply_to_message.caption
            translation = requests.get(
                f"https://hozory.com/translate/?target=en&text={text}"
            ).json()["result"]["translate"]
            m.reply(f"`{translation}`")

    if (
        text == "ترجمه"
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not r.get(f"{m.chat.id}:disableTrans:{hmshelp}"):
            text = m.reply_to_message.text or m.reply_to_message.caption
            en = requests.get(
                f"https://hozory.com/translate/?target=en&text={text}"
            ).json()["result"]["translate"]
            ar = requests.get(
                f"https://hozory.com/translate/?target=ar&text={text}"
            ).json()["result"]["translate"]
            ru = requests.get(
                f"https://hozory.com/translate/?target=ru&text={text}"
            ).json()["result"]["translate"]
            zh = requests.get(
                f"https://hozory.com/translate/?target=zh&text={text}"
            ).json()["result"]["translate"]
            fr = requests.get(
                f"https://hozory.com/translate/?target=fr&text={text}"
            ).json()["result"]["translate"]
            du = requests.get(
                f"https://hozory.com/translate/?target=nl&text={text}"
            ).json()["result"]["translate"]
            tr = requests.get(
                f"https://hozory.com/translate/?target=tr&text={text}"
            ).json()["result"]["translate"]
            txt = f"🇷🇺 : \n {ru}\n\n🇨🇳 : \n {zh}\n\n🇫🇷 :\n {fr}\n\n🇩🇪 :\n {du}\n\n🇹🇷 : \n{tr}"
            return m.reply(txt)

    if (
        text.startswith("ترجمه ")
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not r.get(f"{m.chat.id}:disableTrans:{hmshelp}"):
            lang = text.split()[1]
            text = m.reply_to_message.text or m.reply_to_message.caption
            translation = requests.get(
                f"https://hozory.com/translate/?target={lang}&text={text}"
            ).json()["result"]["translate"]
            m.reply(f"`{translation}`")

    if text == "ابلاغ" and m.reply_to_message:
        text = f"{k} تم ابلاغ المشرفين"
        cc = 0
        for mm in c.get_chat_members(
            m.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            if not mm.user.is_deleted and not mm.user.is_bot:
                cc += 1
                text += f"[⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮](tg://user?id={mm.user.id})"
        if cc == 0:
            return False
        return m.reply(
            text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⚠️", callback_data="delAdminMSG")]]
            ),
        )

    if text == "المقيدين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            co = 0
            cc = 1
            text = "المقيدين:\n\n"
            for mm in c.get_chat_members(
                m.chat.id, filter=ChatMembersFilter.RESTRICTED
            ):
                if co == 100:
                    break
                if not mm.user.is_deleted:
                    co += 1
                    user = (
                        f"@{mm.user.username}"
                        if mm.user.username
                        else f"[@{channel}](tg://user?id={mm.user.id})"
                    )
                    text += f"{cc} ➣ {user} ☆ ( `{mm.user.id}` )\n"
                    cc += 1
            text += "☆"
            if co == 0:
                return m.reply(f"{k} مافيه مقيديين")
            else:
                return m.reply(text)

    if text == "مسح المقيدين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            co = 0
            for mm in c.get_chat_members(
                m.chat.id, filter=ChatMembersFilter.RESTRICTED
            ):
                co += 1
                c.restrict_chat_member(
                    m.chat.id,
                    mm.user.id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_send_polls=True,
                        can_invite_users=True,
                        can_add_web_page_previews=True,
                        can_change_info=True,
                        can_pin_messages=True,
                    ),
                )
            if co == 0:
                return m.reply(f"{k} مافيه مقيديين")
            else:
                return m.reply(f"{k} ابشر مسحت ( {co} ) من المقيدين")

    if text == "تثبيت" and m.reply_to_message:
        if mod_pls(m.from_user.id, m.chat.id):
            m.reply_to_message.pin(disable_notification=False)
            m.reply(f"{k} ابشر ثبتت الرسالة ")

    if text == "الغاء التثبيت" and m.reply_to_message:
        if mod_pls(m.from_user.id, m.chat.id):
            m.reply_to_message.unpin()
            m.reply(f"{k} ابشر لغيت تثبيت الرسالة ")

    if text.startswith("تقييد ") and len(text.split()) == 2:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                user = int(text.split()[1])
            except:
                user = text.split()[1].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if m.from_user.id == get.user.id:
                    return m.reply("شفيك تبي تنزل نفسك")
                if pre_pls(get.user.id, m.chat.id):
                    rank = get_rank(get.user.id, m.chat.id)
                    return m.reply(f"{k} هييه مايمديك تقييد {rank} ياورع!")
                if get.status == ChatMemberStatus.RESTRICTED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} مقيد من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            c.restrict_chat_member(
                m.chat.id, get.user.id, ChatPermissions(can_send_messages=False)
            )
            return m.reply(f"「 {get.user.mention} 」 \n{k} قييدته\n☆")

    if text == "تقييد" and m.reply_to_message and m.reply_to_message.from_user:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            if m.from_user.id == m.reply_to_message.from_user.id:
                return m.reply("شفيك تبي تنزل نفسك")
            get = m.chat.get_member(m.reply_to_message.from_user.id)
            if pre_pls(m.reply_to_message.from_user.id, m.chat.id):
                rank = get_rank(m.reply_to_message.from_user.id, m.chat.id)
                return m.reply(f"{k} هييه مايمديك تقييد {rank} ياورع!")
            if get.status == ChatMemberStatus.RESTRICTED:
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」 \n{k} مقيد من قبل\n☆"
                )
            c.restrict_chat_member(
                m.chat.id,
                m.reply_to_message.from_user.id,
                ChatPermissions(can_send_messages=False),
            )
            return m.reply(
                f"「 {m.reply_to_message.from_user.mention} 」 \n{k} قييدته\n☆"
            )

    if (
        text.startswith("الغاء تقييد ")
        or text.startswith("الغاء التقييد ")
        and len(text.split()) == 3
    ):
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")
        else:
            try:
                user = int(text.split()[2])
            except:
                user = text.split()[2].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if not get.status == ChatMemberStatus.RESTRICTED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} مو مقيد من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            c.restrict_chat_member(
                m.chat.id,
                get.user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_invite_users=True,
                    can_add_web_page_previews=True,
                    can_change_info=True,
                    can_pin_messages=True,
                ),
            )
            return m.reply(f"「 {get.user.mention} 」 \n{k} ابشر الغيت تقييده\n☆")

    if (
        text == "الغاء تقييد"
        or text == "الغاء التقييد"
        and m.reply_to_message
        and m.reply_to_message.from_user
    ):
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")
        else:
            get = m.chat.get_member(m.reply_to_message.from_user.id)
            if not get.status == ChatMemberStatus.RESTRICTED:
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」 \n{k} مو مقيد من قبل\n☆"
                )
            c.restrict_chat_member(
                m.chat.id,
                m.reply_to_message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_invite_users=True,
                    can_add_web_page_previews=True,
                    can_change_info=True,
                    can_pin_messages=True,
                ),
            )
            return m.reply(
                f"「 {m.reply_to_message.from_user.mention} 」 \n{k} ابشر الغيت تقييده\n☆"
            )

    if text == "المحظورين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            co = 0
            cc = 1
            text = "المحظورين:\n\n"
            for mm in c.get_chat_members(m.chat.id, filter=ChatMembersFilter.BANNED):
                if co == 100:
                    break
                if mm.user:
                    if not mm.user.is_deleted:
                        co += 1
                        user = (
                            f"@{mm.user.username}"
                            if mm.user.username
                            else f"[@{channel}](tg://user?id={mm.user.id})"
                        )
                        text += f"{cc} ➣ {user} ☆ ( `{mm.user.id}` )\n"
                        cc += 1
                if mm.chat:
                    co += 1
                    user = f"@{mm.chat.username}"
                    text += f"{cc} ➣ {user} ☆ (`{mm.chat.id}`)\n"
                    cc += 1
            text += "☆"
            if co == 0:
                return m.reply(f"{k} مافيه محظورين")
            else:
                return m.reply(text)

    if text == "مسح المحظورين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")
        else:
            co = 0
            for mm in c.get_chat_members(m.chat.id, filter=ChatMembersFilter.BANNED):
                if mm.user:
                    co += 1
                    c.unban_chat_member(m.chat.id, mm.user.id)
                if mm.chat:
                    co += 1
                    c.unban_chat_member(m.chat.id, mm.chat.id)
            if co == 0:
                return m.reply(f"{k} مافيه محظورين")
            else:
                return m.reply(f"{k} ابشر مسحت ( {co} ) من المحظورين")

    if text.startswith("حظر ") and len(text.split()) == 2:
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                user = int(text.split()[1])
            except:
                user = text.split()[1].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if m.from_user.id == get.user.id:
                    return m.reply("شفيك تبي تنزل نفسك")
                if pre_pls(get.user.id, m.chat.id):
                    rank = get_rank(get.user.id, m.chat.id)
                    return m.reply(f"{k} هييه مايمديك تحظر {rank} ياورع!")
                if get.status == ChatMemberStatus.BANNED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} محظور من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            m.chat.ban_member(get.user.id)
            return m.reply(f"「 {get.user.mention} 」 \n{k} حظرته\n☆")

    if text == "حظر" and m.reply_to_message and m.reply_to_message.from_user:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            if m.from_user.id == m.reply_to_message.from_user.id:
                return m.reply("شفيك تبي تنزل نفسك")
            get = m.chat.get_member(m.reply_to_message.from_user.id)
            if pre_pls(m.reply_to_message.from_user.id, m.chat.id):
                rank = get_rank(m.reply_to_message.from_user.id, m.chat.id)
                return m.reply(f"{k} هييه مايمديك تحظر {rank} ياورع!")
            if get.status == ChatMemberStatus.BANNED:
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」 \n{k} محظور من قبل\n☆"
                )
            m.chat.ban_member(m.reply_to_message.from_user.id)
            return m.reply(
                f"「 {m.reply_to_message.from_user.mention} 」 \n{k} حظرته\n☆"
            )

    if text == "طرد البوتات":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك وفوق ) بس")
        else:
            co = 0
            for mm in m.chat.get_members(filter=ChatMembersFilter.BOTS):
                try:
                    m.chat.ban_member(mm.user.id)
                    co += 1
                except:
                    pass
            if co == 0:
                return m.reply(f"{k} مافيه بوتات")
            else:
                return m.reply(f"{k} ابشر حظر ( {co} ) بوت")

    if text.startswith("طرد ") and len(text.split()) == 2:
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")
        else:
            try:
                user = int(text.split()[1])
            except:
                user = text.split()[1].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if m.from_user.id == get.user.id:
                    return m.reply("شفيك تبي تنزل نفسك")
                if pre_pls(get.user.id, m.chat.id):
                    rank = get_rank(get.user.id, m.chat.id)
                    return m.reply(f"{k} هييه مايمديك تطرد {rank} ياورع!")
                if get.status == ChatMemberStatus.BANNED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} مطرود من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            m.chat.ban_member(get.user.id)
            m.chat.unban_member(get.user.id)
            return m.reply(f"「 {get.user.mention} 」 \n{k} طردته\n☆")

    if text == "همسة" and m.reply_to_message and m.reply_to_message.from_user:
        if r.get(f"{m.chat.id}:disableWHISPER:{hmshelp}"):
            return m.reply(f"{k} الهمسة معطله")
        user_id = m.reply_to_message.from_user.id
        if user_id == m.from_user.id:
            return m.reply(f"{k} مافيك تهمس لنفسك ياغبي")
        else:
            import uuid

            id = str(uuid.uuid4())[:6]
            a = m.reply(
                f"{k} تم تحديد الهمسة الى [ {m.reply_to_message.from_user.mention} ]\n\n~ اضغط على الزر بالاسفل لارسال الهمسة",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                f"ارسال الهمسة",
                                url=f"t.me/{c.me.username}?start=hmsa{id}",
                            )
                        ]
                    ]
                ),
            )
            data = {
                "from": m.from_user.id,
                "to": user_id,
                "chat": m.chat.id,
                "id": a.id,
            }
            # wsdb.set(str(id), data)
            wsdb.setex(key=id, ttl=3600, value=data)
            return True

    if text == "تعطيل التنظيف":
        if not gowner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس")
        else:
            if not r.hget(hmshelp + str(m.chat.id), "ena-clean"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التنظيف معطل من قبل\n☆"
                )
            else:
                r.hdel(hmshelp + str(m.chat.id), "ena-clean")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التنظيف\n☆"
                )

    if text == "تفعيل التنظيف":
        if not gowner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس")
        else:
            if r.hget(hmshelp + str(m.chat.id), "ena-clean"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التنظيف مفعل من قبل\n☆"
                )
            else:
                r.hset(hmshelp + str(m.chat.id), "ena-clean", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التنظيف\n☆"
                )

    if re.search("^وضع وقت التنظيف [0-9]+$", text):
        if not gowner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس")
        else:
            secs = int(text.split()[3])
            if secs > 3600 or secs < 60:
                return m.reply(
                    f"{k} عليك تحديد وقت التنظيف بالثواني من 60 الى 3600 ثانية"
                )
            else:
                r.hset(hmshelp + str(m.chat.id), "clean-secs", secs)
                return m.reply(f"{k} تم تعيين وقت التنظيف ( {secs} ) ثانية")

    if text == "وقت التنظيف":
        if not gowner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس")
        else:
            secs = r.hget(hmshelp + str(m.chat.id), "clean-secs") or "60"
            return m.reply(f"`{secs}`")

    if text == "طرد" and m.reply_to_message and m.reply_to_message.from_user:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                if m.from_user.id == m.reply_to_message.from_user.id:
                    return m.reply("شفيك تبي تنزل نفسك")
                get = m.chat.get_member(m.reply_to_message.from_user.id)
                if pre_pls(m.reply_to_message.from_user.id, m.chat.id):
                    rank = get_rank(m.reply_to_message.from_user.id, m.chat.id)
                    return m.reply(f"{k} هييه مايمديك تطرد {rank} ياورع!")
                if get.status == ChatMemberStatus.BANNED:
                    return m.reply(
                        f"「 {m.reply_to_message.from_user.mention} 」 \n{k} مطرود من قبل\n☆"
                    )
                m.chat.ban_member(m.reply_to_message.from_user.id)
                m.reply(f"「 {m.reply_to_message.from_user.mention} 」 \n{k} طردته\n☆")
                return m.chat.unban_member(m.reply_to_message.from_user.id)
            except:
                return m.reply(f"{k} العضو مو بالمجموعة")

    if (
        text.startswith("رفع الحظر ")
        or text.startswith("الغاء الحظر ")
        and len(text.split()) == 3
    ):
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                user = int(text.split()[2])
            except:
                user = text.split()[2].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if not get.status == ChatMemberStatus.BANNED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} مو محظور من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            m.chat.unban_member(get.user.id)
            return m.reply(f"「 {get.user.mention} 」 \n{k} ابشر الغيت حظره\n☆")

    if (
        text == "رفع الحظر"
        or text == "الغاء الحظر"
        and m.reply_to_message
        and m.reply_to_message.from_user
    ):
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                get = m.chat.get_member(m.reply_to_message.from_user.id)
                if not get.status == ChatMemberStatus.BANNED:
                    return m.reply(
                        f"「 {m.reply_to_message.from_user.mention} 」 \n{k} مو محظور من قبل\n☆"
                    )
                m.chat.unban_member(m.reply_to_message.from_user.id)
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」 \n{k} ابشر الغيت حظره\n☆"
                )
            except:
                return m.reply(f"{k} العضو مو بالمجموعة")

    if text.startswith("رفع القيود ") and len(text.split()) == 3:
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                user = int(text.split()[2])
            except:
                user = text.split()[2].replace("@", "")
            co = 0
            text = ""
            try:
                get = m.chat.get_member(user)
                if get.status == ChatMemberStatus.BANNED:
                    m.chat.unban_member(get.user.id)
                    text += "حظر\n"
                    co += 1
                if get.status == ChatMemberStatus.RESTRICTED:
                    c.restrict_chat_member(
                        m.chat.id,
                        get.user.id,
                        ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_other_messages=True,
                            can_send_polls=True,
                            can_invite_users=True,
                            can_add_web_page_previews=True,
                            can_change_info=True,
                            can_pin_messages=True,
                        ),
                    )
                    text += "تقييد\n"
                    co += 1
                if r.get(f"{get.user.id}:mute:{m.chat.id}{hmshelp}"):
                    r.delete(f"{get.user.id}:mute:{m.chat.id}{hmshelp}")
                    r.srem(f"{m.chat.id}:listMUTE:{hmshelp}", get.user.id)
                    text += "كتم\n"
                    co += 1
                if co > 0:
                    return m.reply(f"رفعت القيود التالية:\n{text}\n☆")
                else:
                    return m.reply(f"「 {get.user.mention} 」\n{k} ماله قيود من قبل\n☆")

            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            m.chat.unban_member(get.user.id)
            return m.reply(f"「 {get.user.mention} 」 \n{k} ابشر الغيت حظره\n☆")

    if text == "رفع القيود" and m.reply_to_message and m.reply_to_message.from_user:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                text = ""
                co = 0
                get = m.chat.get_member(m.reply_to_message.from_user.id)
                if get.status == ChatMemberStatus.BANNED:
                    m.chat.unban_member(get.user.id)
                    text += "حظر\n"
                    co += 1
                if get.status == ChatMemberStatus.RESTRICTED:
                    c.restrict_chat_member(
                        m.chat.id,
                        get.user.id,
                        ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_other_messages=True,
                            can_send_polls=True,
                            can_invite_users=True,
                            can_add_web_page_previews=True,
                            can_change_info=True,
                            can_pin_messages=True,
                        ),
                    )
                    text += "تقييد\n"
                    co += 1
                if r.get(f"{get.user.id}:mute:{m.chat.id}{hmshelp}"):
                    r.delete(f"{get.user.id}:mute:{m.chat.id}{hmshelp}")
                    r.srem(f"{m.chat.id}:listMUTE:{hmshelp}", get.user.id)
                    text += "كتم\n"
                    co += 1
                if co > 0:
                    return m.reply(f"رفعت القيود التالية:\n{text}\n☆")
                else:
                    return m.reply(f"「 {get.user.mention} 」\n{k} ماله قيود من قبل\n☆")
            except:
                return m.reply(f"{k} العضو مو بالمجموعة")

    if text == "كشف البوتات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            co = 0
            text = "بوتات المجموعة:\n\n"
            cc = 1
            for mm in m.chat.get_members(filter=ChatMembersFilter.BOTS):
                if co == 100:
                    break
                text += f"{cc}) {mm.user.mention}"
                if mm.status == ChatMemberStatus.ADMINISTRATOR:
                    text += "👑"
                text += "\n"
                cc += 1
                co += 1
            text += "☆"
            if co == 0:
                return m.reply(f"{k} مافيه بوتات")
            else:
                return m.reply(text)

    if text == "مين ضافني":
        get = m.chat.get_member(m.from_user.id).invited_by
        if not get:
            return m.reply(f"{k} محد ضافك")
        else:
            return m.reply(get.mention)

    if text == "بايو عشوائي":
        return m.reply(f"{k} تحت الصيانة")

    if text == "مسح" and m.reply_to_message:
        if admin_pls(m.from_user.id, m.chat.id):
            m.reply_to_message.delete()
            m.delete()
        else:
            m.delete()

    if (
        text.startswith("مسح ")
        and len(text.split()) == 2
        and re.findall("[0-9]+", text)
    ):
        count = int(re.findall("[0-9]+", text)[0])
        if not admin_pls(m.from_user.id, m.chat.id):
            return m.delete()
        else:
            if count > 400:
                return m.reply(f"{k} اختار من 1 الى 400")
            else:
                for msg in range(m.id, m.id - count, -1):
                    try:
                        c.delete_messages(m.chat.id, msg)
                    except:
                        pass

    if text == "تنزيل مشرف" and m.reply_to_message and m.reply_to_message.from_user:
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك وفوق ) بس")
        else:
            try:
                c.promote_chat_member(
                    m.chat.id,
                    m.reply_to_message.from_user.id,
                    privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=False,
                        can_restrict_members=False,
                        can_promote_members=False,
                        can_pin_messages=False,
                        can_change_info=False,
                        can_invite_users=False,
                    ),
                )
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」\n{k} نزلته من الاشراف"
                )
            except:
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」\n{k} مو انا الي رفعته او ماعندي صلاحيات"
                )

    if text == "رفع مشرف" and m.reply_to_message and m.reply_to_message.from_user:
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك وفوق ) بس")
        
        get = m.chat.get_member(c.me.id)
        priv = get.privileges
        if not all([
            priv.can_manage_chat,
            priv.can_delete_messages,
            priv.can_restrict_members,
            priv.can_pin_messages,
            priv.can_invite_users,
            priv.can_change_info,
            priv.can_promote_members
        ]):
            return m.reply("هات كل الصلاحيات بعدين سولف")
        
        target_user = m.reply_to_message.from_user
        r.set(f"promote_temp:{m.chat.id}:{m.from_user.id}", target_user.id, ex=600)
        
        # أزرار الصلاحيات
        permissions = [
            ("حذف الرسائل", "can_delete_messages"),
            ("حظر الأعضاء", "can_restrict_members"),
            ("تثبيت الرسائل", "can_pin_messages"),
            ("دعوة المستخدمين", "can_invite_users"),
            ("تغيير المعلومات", "can_change_info"),
            ("إدارة المكالمات", "can_manage_video_chats"),
            ("رفع مشرفين", "can_promote_members")
        ]
        
        buttons = []
        for perm, key in permissions:
            buttons.append([
                InlineKeyboardButton(
                    f"{perm} ❌", 
                    callback_data=f"promote_toggle_{key}_{target_user.id}"
                )
            ])
        
        buttons.append([
            InlineKeyboardButton("✅ تأكيد الرفع", callback_data=f"promote_confirm_{target_user.id}"),
            InlineKeyboardButton("❌ إلغاء", callback_data=f"promote_cancel_{target_user.id}")
        ])
        
        m.reply(
            f"⚙️ صلاحيات المشرف: {target_user.mention}\n"
            "▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
            "اضغط على الصلاحية لتغيير حالتها:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    if text == "مسح قائمة التثبيت":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            c.unpin_all_chat_messages(m.chat.id)
            return m.reply(f"{k} ابشر مسحت قائمة التثبيت")

    if (
        text == "الاوامر"
        or text.lower() == "/commands"
        or text.lower() == f"/commands@{botUsername.lower()}"
    ):
        if admin_pls(m.from_user.id, m.chat.id):
            channel = (
                r.get(f"{hmshelp}:BotChannel")
                if r.get(f"{hmshelp}:BotChannel")
                else "alwzaraa2"
            )
            return m.reply(
                f"{k} مرحبا بك في اوامر التحكم في بوت  هانكوك  \n\n~ اعرف اوامر التحكم عن طريق الازرار الموجودة بالاسفل",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "م1", callback_data=f"commands1:{m.from_user.id}"
                            ),
                            InlineKeyboardButton(
                                "م2", callback_data=f"commands2:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "م3", callback_data=f"commands3:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                            ),
                            InlineKeyboardButton(
                                "التسلية", callback_data=f"commands5:{m.from_user.id}"
                            ),
                        ],
                        [
                            
                            InlineKeyboardButton(
                                "البنك", callback_data=f"commands7:{m.from_user.id}"
                            ),
                            InlineKeyboardButton(
                                "زواج", callback_data=f"commands8:{m.from_user.id}"
                            ),
                        ],
                    ]
                ),
            )
        else:
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")


@Client.on_callback_query(group=1)
def CallbackQueryHandler(c, m):
    channel = (
        r.get(f"{hmshelp}:BotChannel") if r.get(f"{hmshelp}:BotChannel") else "alwzaraa2"
    )
    Thread(target=CallbackQueryResponse, args=(c, m, channel)).start()


def CallbackQueryResponse(c, m, channel):
    k = r.get(f"{hmshelp}:botkey")
    if m.data == f"commands1:{m.from_user.id}":
        m.edit_message_text(
            f"""
❨ اوامر الرفع والتنزيل ❩

⌯ رفع ↣ ↢ تنزيل مشرف
⌯ رفع ↣ ↢ تنزيل مالك اساسي
⌯ رفع ↣ ↢ تنزيل مالك
⌯ رفع ↣ ↢ تنزيل مدير
⌯ رفع ↣ ↢ تنزيل ادمن
⌯ رفع ↣ ↢ تنزيل مميز
⌯ تنزيل الكل  ↢ بالرد  ↢ لتنزيل الشخص من جميع رتبة
⌯ مسح الكل  ↢ بدون رد  ↢ لتنزيل كل رتب المجموعة

❨ اوامر المسح ❩

⌯ مسح المالكيين
⌯ مسح المدراء
⌯ مسح الادمنيه
⌯ مسح المميزين
⌯ مسح المحظورين
⌯ مسح المكتومين
⌯ مسح قائمة المنع
⌯ مسح رتبة
⌯ مسح الرتب
⌯ مسح الردود
⌯ مسح الاوامر
⌯ مسح + العدد
⌯ مسح بالرد
⌯ مسح الترحيب
⌯ مسح قائمة التثبيت

❨ اوامر الطرد الحظر الكتم ❩

⌯ حظر ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ طرد ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ كتم ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ تقيد ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ الغاء الحظر ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ الغاء الكتم ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ الغاء التقييد ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ رفع القيود ↢ لحذف الكتم,الحظر,التقييد
⌯ منع الكلمة
⌯ منع بالرد على متحركة او ستيكر
⌯ الغاء منع الكلمة
⌯ طرد البوتات
⌯ كشف البوتات

❨ اوامر النطق ❩

⌯ شيكول + بالرد على فويس لترجمة المحتوى

❨ اوامر اخرى ❩

⌯ الرابط
⌯ انشاء رابط
⌯ بايو
⌯ بايو عشوائي
⌯ ايدي
⌯ الانشاء
⌯ افتاري
⌯ افتار + باليوزر او الرد
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("م1 ‣", callback_data="None"),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسلية", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],

                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands2:{m.from_user.id}":
        m.edit_message_text(
            f"""
❨ اوامر الوضع ❩

⌯ وضع ترحيب
⌯ وضع قوانين
⌯ تغيير رتبة
⌯ تغيير امر

❨ اوامر رؤية الاعدادات ❩

⌯ المطورين
⌯ المالكيين الاساسيين
⌯ المالكيين
⌯ الادمنيه
⌯ المدراء
⌯ المشرفين
⌯ المميزين
⌯ القوانين
⌯ قائمة المنع
⌯ المكتومين
⌯ المطور
⌯ الاعدادت
⌯ المجموعة
⌯ الساعة
⌯ التاريخ
⌯ صلاحياتي
⌯ لقبي
⌯ صلاحياته + بالرد
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("م2 ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسلية", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],

                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands3:{m.from_user.id}":
        m.edit_message_text(
            f"""
❨ اوامر الردود ❩

⌯ الردود ↢ تشوف كل الردود المضافة
⌯ الردود المتعدده ↢ تشوف كل الردود المتعدده المضافة
⌯ اضف رد ↢ عشان تضيف رد
⌯ اضف رد متعدد ↢ عشان تضيف أكثر من رد
⌯ اضف رد متعدد ↢ خاص بالاعضاء
⌯ مسح رد ↢ عشان تمسح الرد
⌯ مسح رد متعدد ↢ عشان تمسح رد متعدد
⌯ مسح ردي ↢ عشان تمسح ردك اذا كان بردود الأعضاء
⌯ مسح الردود ↢ تمسح كل الردود
⌯ مسح الردود المتعدده ↢ عشان تمسح كل الردود المتعدده
⌯ الرد + كلمة الرد
-

❨ اوامر القفل والفتح بالمسح ❩

⌯ قفل ↣ ↢ فتح  التعديل
⌯ قفل ↣ ↢ فتح  الفويسات
⌯ قفل ↣ ↢ فتح  الفيديو
⌯ قفل ↣ ↢ فتح  الـصــور
⌯ قفل ↣ ↢ فتح  الملصقات
⌯ قفل ↣ ↢ فتح  الدخول
⌯ قفل ↣ ↢ فتح  الفارسية
⌯ قفل ↣ ↢ فتح  الملفات
⌯ قفل ↣ ↢ فتح  المتحركات
⌯ قفل ↣ ↢ فتح  تعديل الميديا
⌯ قفل ↣ ↢ فتح  تعديل الميديا بالتقييد
⌯ قفل ↣ ↢ فتح  الدردشه
⌯ قفل ↣ ↢ فتح  الروابط
⌯ قفل ↣ ↢ فتح  الهشتاق
⌯ قفل ↣ ↢ فتح  البوتات
⌯ قفل ↣ ↢ فتح  اليوزرات
⌯ قفل ↣ ↢ فتح  الاشعارات
⌯ قفل ↣ ↢ فتح  الكلام الكثير
⌯ قفل ↣ ↢ فتح  التكرار
⌯ قفل ↣ ↢ فتح  التوجيه
⌯ قفل ↣ ↢ فتح  الانلاين
⌯ قفل ↣ ↢ فتح  الجهات
⌯ قفل ↣ ↢ فتح  الــكـــل
⌯ قفل ↣ ↢ فتح  السب
⌯ قفل ↣ ↢ فتح  الاضافه
⌯ قفل ↣ ↢ فتح  الصوت
⌯ قفل ↣ ↢ فتح  القنوات
⌯ قفل ↣ ↢ فتح الايراني
⌯ قفل ↣ ↢ فتح الإباحي

❨ اوامر التفعيل والتعطيل ❩

⌯ تفعيل ↣ ↢ تعطيل الترحيب
⌯ تفعيل ↣ ↢ تعطيل الترحيب بالصورة
⌯ تفعيل ↣ ↢ تعطيل الردود
⌯ تفعيل ↣ ↢ تعطيل ردود الاعضاء
⌯ تفعيل ↣ ↢ تعطيل الايدي
⌯ تفعيل ↣ ↢ تعطيل الرابط
⌯ تفعيل ↣ ↢ تعطيل اطردني
⌯ تفعيل ↣ ↢ تعطيل الحماية
⌯ تفعيل ↣ ↢ تعطيل المنشن
⌯ تفعيل ↣ ↢ تعطيل التحقق
⌯ تفعيل ↣ ↢ تعطيل ردود المطور
⌯ تفعيل ↣ ↢ تعطيل التحذير
⌯ تفعيل ↣ ↢ تعطيل البايو
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("م3 ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسلية", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],

                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands4:{m.from_user.id}":
        m.edit_message_text(
            """
☤ تفعيل الالعاب
☤ تعطيل الالعاب
    ╼╾
✽ جمل
✽ كلمات
✽ اغاني
✽ دين
✽ عربي
✽ اكمل
✽ صور
✽ كت تويت
✽ مؤقت
✽ اعلام
✽ معاني
✽ تخمين
✽ احكام
✽ ارقام
✽ احسب
✽ خواتم
✽ انقليزي
✽ ترتيب
✽ انمي
✽ تركيب
✽ تفكيك
✽ عواصم
✽ روليت
✽ سيارات
✽ ايموجي
✽ حجرة
✽ تشفير
✽ كره قدم
✽ ديمون
✽ تقييم
╼╾
❖ فلوسي ↼ عشان تشوف فلوسك
❖ بيع فلوسي + العدد ↼ للأستبدال
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("الالعاب ‣", callback_data="None"),
                        InlineKeyboardButton(
                            "التسلية", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],

                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands5:{m.from_user.id}":
        m.edit_message_text(
            f"""
🍰 ⌯ رفع ↣ ↢ تنزيل كيكة
🍯 ⌯ رفع ↣ ↢ تنزيل عسل
💩 ⌯ رفع ↣ ↢ تنزيل زربة
🦓 ⌯ رفع ↣ ↢ تنزيل حمار
🐄 ⌯ رفع ↣ ↢ تنزيل بقرة
🐩 ⌯ رفع ↣ ↢ تنزيل كلب
🐒 ⌯ رفع ↣ ↢ تنزيل قرد
🐐 ⌯ رفع ↣ ↢ تنزيل تيس
🐂 ⌯ رفع ↣ ↢ تنزيل ثور
🏅 ⌯ رفع ↣ ↢ تنزيل هكر
🐓 ⌯ رفع ↣ ↢ تنزيل دجاجة
🧱 ⌯ رفع ↣ ↢ تنزيل ملكة
🔫 ⌯ رفع ↣ ↢ تنزيل صياد
🐏 ⌯ رفع ↣ ↢ تنزيل خاروف
❤️ ⌯ رفع لقلبي ↣ ↢ تنزيل من قلبي

⌯ قائمة الكيك
⌯ قائمة العسل
⌯ قائمة الزربة
⌯ قائمة الحمير
⌯ قائمة البقر
⌯ قائمة الكلاب
⌯ قائمة القرود
⌯ قائمة التيس
⌯ قائمة الثور
⌯ قائمة الهكر
⌯ قائمة الدجاج
⌯ قائمة الهطوف
⌯ قائمة الصيادين
⌯ قائمة الخرفان
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("التسلية ‣", callback_data="None"),
                    ],

                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands6:{m.from_user.id}":
        m.edit_message_text(
            """
⚘ طريقة استخدام الذكاء الاصطناعي

هانكوك + الكلمه

مثال :- هانكوك كيف حالك
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسلية", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands7:{m.from_user.id}":
        m.edit_message_text(
            """
✜ اوامر البنك

⌯ انشاء حساب بنكي  ↢ تسوي حساب وتقدر تحول فلوس مع مزايا ثانيه

⌯ مسح حساب بنكي  ↢ تلغي حسابك البنكي

⌯ تحويل ↢ تطلب رقم حساب الشخص وتحول له فلوس

⌯ حسابي  ↢ يطلع لك رقم حسابك عشان تعطيه للشخص اللي بيحول لك

⌯ فلوسي ↢ يعلمك كم فلوسك

⌯ راتب ↢ يعطيك راتبك كل ٥ دقيقة

⌯ بخشيش ↢ يعطيك بخشيش كل ٥ دقايق

⌯ زرف ↢ تزرف فلوس اشخاص كل ٥ دقايق

⌯ كنز ↢ يعطيك كنز كل ١٠ دقايق

⌯ استثمار ↢ تستثمر بالمبلغ اللي تبيه مع نسبة ربح مضمونه من ١٪؜ الى ١٥٪؜ ( او استثمار فلوسي )

⌯ حظ ↢ تلعبها بأي مبلغ ياتدبله ياتخسره انت وحظك ( او حظ فلوسي )

⌯ عجلة ↢ تلعب عجلة الحظ ولو تشابهو ال ٣ ايموجيات تكسب من ١٠٠ الف لحد ٣٠٠ الف انت وحظك

⌯ توب الفلوس ↢ يطلع توب اكثر ناس معهم فلوس بكل القروبات

⌯ توب الحرامية ↢ يطلع لك اكثر ناس زرفوا
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسلية", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],

                    [
                        InlineKeyboardButton("البنك ‣", callback_data="None"),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands8:{m.from_user.id}":
        m.edit_message_text(
            """
✜ اوامر الزواج

⌯ زواج  ↢ تكتبه بالرد على رسالة شخص مع المهر ويزوجك

⌯ زواجي  ↢ يطلع وثيقة زواجك اذا متزوج

⌯ طلاق ↢ يطلقك اذا متزوج

⌯ خلع  ↢ يخلع زوجك ويرجع له المهر

⌯ زواجات ↢ يطلع اغلى الزواجات بالقروب
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسلية", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],

                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("زواج ‣", callback_data="None"),
                    ],
                ]
            ),
        )
        return

    if m.data == "delAdminMSG":
        if str(m.from_user.id) in m.message.text.html:
            return m.message.delete()

    if m.data == f"yes:{m.from_user.id}":
        try:
            c.restrict_chat_member(
                m.message.chat.id,
                m.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_invite_users=True,
                    can_add_web_page_previews=True,
                    can_change_info=True,
                    can_pin_messages=True,
                ),
            )
        except:
            return False
        m.edit_message_text(
            f"""
{k} تم التحقق منك وطلعت مو زومبي
{k} الحين تقدر تسولف بالقروب
☆
""",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            ),
        )

    if m.data == f"no:{m.from_user.id}":
        return m.edit_message_text(
            f"""
{k} للأسف طلعت زومبي 🧟‍♀️
{k} مالك غير تنطر حد من المشرفين يجي يتوسطلك
☆
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "رفع التقييد والسماح",
                            callback_data=f"yesVER:{m.from_user.id}",
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "طرد", callback_data=f"noVER:{m.from_user.id}"
                        )
                    ],
                ]
            ),
        )

    if m.data.startswith("yesVER"):
        user_id = int(m.data.split(":")[1])
        if not admin_pls(m.from_user.id, m.message.chat.id):
            return m.answer(f"{k} هذا الزر يخص ( الادمن وفوق ) بس", show_alert=True)
        else:
            m.edit_message_text(f"{k} توسطلك واحد من الادمن ورفعت عنك القيود")
            try:
                c.restrict_chat_member(
                    m.message.chat.id,
                    user_id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_send_polls=True,
                        can_invite_users=True,
                        can_add_web_page_previews=True,
                        can_change_info=True,
                        can_pin_messages=True,
                    ),
                )
            except:
                return False

    if m.data.startswith("noVER"):
        user_id = int(m.data.split(":")[1])
        if not admin_pls(m.from_user.id, m.message.chat.id):
            return m.answer(f"{k} هذا الزر يخص ( الادمن وفوق ) بس", show_alert=True)
        else:
            m.edit_message_text(f"{k} انقلع برا القروب يلا")
            try:
                m.message.chat.ban_member(user_id)
                m.message.chat.unban_member(user_id)
            except:
                pass

    if m.data == "yes:del:bank":
        if not devp_pls(m.from_user.id, m.message.chat.id):
            return m.answer("تعجبني ثقتك")
        else:
            m.edit_message_text("ابشر صفرت البنك")
            keys = r.keys("*:Floos")
            for a in keys:
                r.delete(a)
            for a in r.keys("*:BankWait"):
                r.delete(a)
            for a in r.keys("*:BankWaitB5"):
                r.delete(a)
            for a in r.keys("*:BankWaitZRF"):
                r.delete(a)
            for a in r.keys("*:BankWaitEST"):
                r.delete(a)
            for a in r.keys("*:BankWaitHZ"):
                r.delete(a)
            for a in r.keys("*:BankWait3JL"):
                r.delete(a)
            for a in r.keys("*:Zrf"):
                r.delete(a)
            r.delete("BankTop")
            r.delete("BankTopZRF")
            return True

    if m.data == "no:del:bank":
        if not devp_pls(m.from_user.id, m.message.chat.id):
            return m.answer("تعجبني ثقتك")
        else:
            m.message.delete()

    if m.data == f"topfloos:{m.from_user.id}":
        if not r.smembers("BankList"):
            return m.answer(f"{k} مافيه حسابات بالبنك", show_alert=True)
        else:
            rep = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("‣ 💸", callback_data="None"),
                        InlineKeyboardButton(
                            "توب الحرامية 💰", callback_data=f"topzrf:{m.from_user.id}"
                        ),
                    ],
                    [InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")],
                ]
            )
            if r.get("BankTop"):
                text = r.get("BankTop")
                if not r.get(f"{m.from_user.id}:Floos"):
                    floos = 0
                else:
                    floos = int(r.get(f"{m.from_user.id}:Floos"))
                get = r.ttl("BankTop")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {floos:,} 💸 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                return m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )
            else:
                users = []
                ccc = 0
                for user in r.smembers("BankList"):
                    ccc += 1
                    id = int(user)
                    if r.get(f"{id}:bankName"):
                        name = r.get(f"{id}:bankName")[:10]
                    else:
                        try:
                            name = c.get_chat(id).first_name
                            r.set(f"{id}:bankName", name)
                        except:
                            name = "INVALID_NAME"
                            r.set(f"{id}:bankName", name)
                    if not r.get(f"{id}:Floos"):
                        floos = 0
                    else:
                        floos = int(r.get(f"{id}:Floos"))
                    users.append({"name": name, "money": floos})
                top = get_top(users)
                text = "توب 20 اغنى اشخاص:\n\n"
                count = 0
                for user in top:
                    count += 1
                    if count == 21:
                        break
                    emoji = get_emoji_bank(count)
                    floos = user["money"]
                    name = user["name"]
                    text += f'**{emoji}{floos:,}** 💸 l {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
                r.set("BankTop", text, ex=300)
                if not r.get(f"{m.from_user.id}:Floos"):
                    floos_from_user = 0
                else:
                    floos_from_user = int(r.get(f"{m.from_user.id}:Floos"))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {floos_from_user:,} 💸 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                get = r.ttl("BankTop")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )

    if m.data == f"topzrf:{m.from_user.id}":
        if not r.smembers("BankList"):
            return m.answer(f"{k} مافيه حسابات بالبنك", show_alert=True)
        else:
            rep = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "توب الفلوس 💸", callback_data=f"topfloos:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("‣ 💰", callback_data="None"),
                    ],
                    [InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")],
                ]
            )
            if r.get("BankTopZRF"):
                text = r.get("BankTopZRF")
                if not r.get(f"{m.from_user.id}:Zrf"):
                    zrf = 0
                else:
                    zrf = int(r.get(f"{m.from_user.id}:Zrf"))
                get = r.ttl("BankTopZRF")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {zrf:,} 💰 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                return m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )
            else:
                users = []
                ccc = 0
                for user in r.smembers("BankList"):
                    ccc += 1
                    id = int(user)
                    if r.get(f"{id}:bankName"):
                        name = r.get(f"{id}:bankName")[:10]
                    else:
                        try:
                            name = c.get_chat(id).first_name
                            r.set(f"{id}:bankName", name)
                        except:
                            name = "INVALID_NAME"
                            r.set(f"{id}:bankName", name)
                    if not r.get(f"{id}:Zrf"):
                        pass
                    else:
                        zrf = int(r.get(f"{id}:Zrf"))
                        users.append({"name": name, "money": zrf})
                top = get_top(users)
                text = "توب 20 اكثر الحرامية زرفًا:\n\n"
                count = 0
                for user in top:
                    count += 1
                    if count == 21:
                        break
                    emoji = get_emoji_bank(count)
                    floos = user["money"]
                    name = user["name"]
                    text += f'**{emoji}{floos}** 💰 l {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
                r.set("BankTopZRF", text, ex=300)
                if not r.get(f"{m.from_user.id}:Zrf"):
                    floos_from_user = 0
                else:
                    floos_from_user = int(r.get(f"{m.from_user.id}:Zrf"))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {floos_from_user} 💰 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                get = r.ttl("BankTopZRF")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )

    """
   if m.data == f'toplast:{m.from_user.id}':
     if not r.get(f'BankTopLast') and not r.get(f'BankTopLastZrf'):
       return m.answer(f'{k} مافي توب اسبوع الي فات',show_alert=True)
     else:
       text = 'توب أوائل الأسبوع الي راح:\n'
       text += r.get(f'BankTopLast')
       text += '\n\nتوب حرامية الاسبوع اللي راح:\n'
       text += r.get(f'BankTopLastZrf')
       text += '\n༄'
       rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', url=f't.me/{channel}')]]
       )
       m.edit_message_text(text, disable_web_page_preview=True,reply_markup=rep)
   """

    name = r.get(f"{hmshelp}:BotName") if r.get(f"{hmshelp}:BotName") else "رعد"
    if m.data == f"RPS:rock++{m.from_user.id}":
        RPS = ["paper", "scissors", "rock"]
        kk = random.choice(RPS)
        if kk == "scissors":
            if r.get(f"{m.from_user.id}:Floos"):
                get = int(r.get(f"{m.from_user.id}:Floos"))
                r.set(f"{m.from_user.id}:Floos", get + 1)
            else:
                r.set(f"{m.from_user.id}:Floos", 1)
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 🪨
أنا: ✂️

النتيجة: ⁪⁬⁪⁬ 🏆 {m.from_user.first_name}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

        if kk == "paper":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 🪨
أنا: 📃

النتيجة: ⁪⁬⁪⁬ 🏆️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )
        if kk == "rock":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 🪨
أنا: 🪨

النتيجة: ⁪⁬⁪⁬ ⚖️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

    if m.data == f"gowner+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(hmshelp + f"locks-{m.message.chat.id}", command, 0)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للمالك الاساسي وفوق فقط"
            )

    if m.data == f"owner+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(hmshelp + f"locks-{m.message.chat.id}", command, 1)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للمالك وفوق فقط"
            )

    if m.data == f"mod+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(hmshelp + f"locks-{m.message.chat.id}", command, 2)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للمدير وفوق فقط"
            )

    if m.data == f"admin+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(hmshelp + f"locks-{m.message.chat.id}", command, 3)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للادمن وفوق فقط"
            )

    if m.data == f"pre+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(hmshelp + f"locks-{m.message.chat.id}", command, 4)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للمميز وفوق فقط"
            )

    if m.data == f"RPS:paper++{m.from_user.id}":
        RPS = ["paper", "scissors", "rock"]
        kk = random.choice(RPS)
        if kk == "rock":
            if r.get(f"{m.from_user.id}:Floos"):
                get = int(r.get(f"{m.from_user.id}:Floos"))
                r.set(f"{m.from_user.id}:Floos", get + 1)
            else:
                r.set(f"{m.from_user.id}:Floos", 1)
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 📃
أنا: 🪨

النتيجة: ⁪⁬⁪⁬ 🏆 {m.from_user.first_name}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

        if kk == "scissors":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 📃
أنا: ✂️

النتيجة: ⁪⁬⁪⁬ 🏆️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )
        if kk == "paper":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 📃
أنا: 📃

النتيجة: ⁪⁬⁪⁬ ⚖️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

    if m.data == f"RPS:scissors++{m.from_user.id}":
        RPS = ["paper", "scissors", "rock"]
        kk = random.choice(RPS)
        if kk == "paper":
            if r.get(f"{m.from_user.id}:Floos"):
                get = int(r.get(f"{m.from_user.id}:Floos"))
                r.set(f"{m.from_user.id}:Floos", get + 1)
            else:
                r.set(f"{m.from_user.id}:Floos", 1)
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: ✂️
أنا: 📃

النتيجة: ⁪⁬⁪⁬ 🏆 {m.from_user.first_name}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

        if kk == "rock":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: ✂️
أنا: 🪨

النتيجة: ⁪⁬⁪⁬ 🏆️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )
        if kk == "scissors":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: ✂️
أنا: ✂️

النتيجة: ⁪⁬⁪⁬ ⚖️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )
            
@Client.on_callback_query(filters.regex(r'^promote_toggle_(.*?)_(\d+)$'))
async def toggle_promote_permission(c, query):
    try:
        parts = query.data.split('_')
        permission_key = '_'.join(parts[2:-1])  # يأخذ كل الأجزاء بين toggle والآيدي
        target_id = int(parts[-1])  # الآيدي هو آخر جزء
        
        chat_id = query.message.chat.id
        user_id = query.from_user.id
        
        if not owner_pls(user_id, chat_id):
            await query.answer("⛔ ليس لديك صلاحية", show_alert=True)
            return
        
        # تبديل الحالة في الذاكرة المؤقتة
        temp_key = f"promote_perms:{chat_id}:{user_id}:{target_id}"
        current_perms = eval(r.get(temp_key) or "{}") if r.exists(temp_key) else {}
        
        # تبديل الحالة الحالية
        current_perms[permission_key] = not current_perms.get(permission_key, False)
        r.set(temp_key, str(current_perms), ex=600)
        
        # تحديث نص الزر
        perm_name = {
            'can_delete_messages': 'حذف الرسائل',
            'can_restrict_members': 'حظر الأعضاء',
            'can_pin_messages': 'تثبيت الرسائل',
            'can_invite_users': 'دعوة المستخدمين',
            'can_change_info': 'تغيير المعلومات',
            'can_manage_video_chats': 'إدارة المكالمات',
            'can_promote_members': 'رفع مشرفين'
        }.get(permission_key, permission_key)
        
        # إنشاء لوحة المفاتيح الجديدة
        new_keyboard = []
        for row in query.message.reply_markup.inline_keyboard:
            new_row = []
            for btn in row:
                if btn.callback_data == query.data:
                    new_btn = InlineKeyboardButton(
                        f"{perm_name} {'✅' if current_perms[permission_key] else '❌'}",
                        callback_data=btn.callback_data
                    )
                    new_row.append(new_btn)
                else:
                    new_row.append(btn)
            new_keyboard.append(new_row)
        
        await query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
        await query.answer(f"تم {'تفعيل' if current_perms[permission_key] else 'تعطيل'} الصلاحية")
        
    except Exception as e:
        print(f"Error in toggle permission: {e}")
        await query.answer("⚠️ حدث خطأ!", show_alert=True)

@Client.on_callback_query(filters.regex(r'^promote_confirm_(\d+)$'))
async def confirm_promotion(c, query):
    try:
        target_id = int(query.data.split('_')[2])
        chat_id = query.message.chat.id
        user_id = query.from_user.id
        
        if not owner_pls(user_id, chat_id):
            await query.answer("⛔ ليس لديك صلاحية", show_alert=True)
            return
        
        # جلب الصلاحيات المحددة
        temp_key = f"promote_perms:{chat_id}:{user_id}:{target_id}"
        if not r.exists(temp_key):
            await query.answer("⚠️ لم يتم تحديد أي صلاحيات!", show_alert=True)
            return
            
        perms = eval(r.get(temp_key))
        
        # تطبيق الصلاحيات
        await c.promote_chat_member(
            chat_id,
            target_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=perms.get('can_delete_messages', False),
                can_restrict_members=perms.get('can_restrict_members', False),
                can_pin_messages=perms.get('can_pin_messages', False),
                can_invite_users=perms.get('can_invite_users', False),
                can_change_info=perms.get('can_change_info', False),
                can_manage_video_chats=perms.get('can_manage_video_chats', False),
                can_promote_members=perms.get('can_promote_members', False)
            )
        )
        
        # تخزين بيانات المشرف
        r.set(f"{chat_id}:rankADMIN:{target_id}{hmshelp}", 1)
        r.sadd(f"{chat_id}:listADMIN:{hmshelp}", target_id)
        
        # تنظيف البيانات المؤقتة
        r.delete(temp_key)
        r.delete(f"promote_temp:{chat_id}:{user_id}")
        
        target_user = await c.get_users(target_id)
        await query.message.edit_text(
            f"✅ تم رفع {target_user.mention} مشرفاً بنجاح\n"
            f"▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
            f"الصلاحيات الممنوحة:\n"
            f"- حذف الرسائل: {'✅' if perms.get('can_delete_messages') else '❌'}\n"
            f"- حظر الأعضاء: {'✅' if perms.get('can_restrict_members') else '❌'}\n"
            f"- تثبيت الرسائل: {'✅' if perms.get('can_pin_messages') else '❌'}\n"
            f"- دعوة المستخدمين: {'✅' if perms.get('can_invite_users') else '❌'}\n"
            f"- تغيير المعلومات: {'✅' if perms.get('can_change_info') else '❌'}\n"
            f"- إدارة المكالمات: {'✅' if perms.get('can_manage_video_chats') else '❌'}\n"
            f"- رفع مشرفين: {'✅' if perms.get('can_promote_members') else '❌'}"
        )
        
    except Exception as e:
        print(f"Error in confirm promotion: {e}")
        await query.answer("⚠️ حدث خطأ أثناء الرفع!", show_alert=True)

@Client.on_callback_query(filters.regex(r'^promote_cancel_(\d+)$'))
async def cancel_promotion(c, query):
    try:
        target_id = int(query.data.split('_')[2])
        chat_id = query.message.chat.id
        user_id = query.from_user.id
        
        if not owner_pls(user_id, chat_id):
            await query.answer("⛔ ليس لديك صلاحية", show_alert=True)
            return
        
        # تنظيف البيانات المؤقتة
        r.delete(f"promote_perms:{chat_id}:{user_id}:{target_id}")
        r.delete(f"promote_temp:{chat_id}:{user_id}")
        
        await query.message.edit_text("❌ تم إلغاء عملية الرفع")
        
    except Exception as e:
        print(f"Error in cancel promotion: {e}")
        await query.answer("⚠️ حدث خطأ أثناء الإلغاء!", show_alert=True)

@Client.on_callback_query(filters.regex(r'^edit_perm_(.*?)_(\d+)$'))
async def edit_permission(c, query):
    try:
        permission_key = query.data.split('_')[2]
        target_id = int(query.data.split('_')[3])
        chat_id = query.message.chat.id
        
        if not (owner_pls(query.from_user.id, chat_id) or dev_pls(query.from_user.id, chat_id)):
            await query.answer("⛔ ليس لديك صلاحية", show_alert=True)
            return
        
        # حفظ التعديلات المؤقتة
        temp_key = f"temp_perms:{chat_id}:{target_id}"
        current_perms = eval(r.get(temp_key) or "{}") if r.exists(temp_key) else {}
        
        # تبديل الحالة الحالية
        current_perms[permission_key] = not current_perms.get(permission_key, False)
        r.set(temp_key, str(current_perms), ex=600)
        
        # تحديث الزر
        for row in query.message.reply_markup.inline_keyboard:
            for btn in row:
                if btn.callback_data == query.data:
                    perm_name = permission_key.split('_')[-1]
                    new_status = '✅' if current_perms[permission_key] else '❌'
                    btn.text = f"{perm_name} {new_status}"
                    break
        
        await query.message.edit_reply_markup(
            reply_markup=query.message.reply_markup
        )
        await query.answer(f"تم {'تفعيل' if current_perms[permission_key] else 'تعطيل'} الصلاحية")
        
    except Exception as e:
        print(f"Error in edit permission: {e}")
        await query.answer("⚠️ حدث خطأ!", show_alert=True)

@Client.on_callback_query(filters.regex(r'^save_perms_(\d+)$'))
async def save_permissions(c, query):
    try:
        target_id = int(query.data.split('_')[2])
        chat_id = query.message.chat.id
        
        if not (owner_pls(query.from_user.id, chat_id) or dev_pls(query.from_user.id, chat_id)):
            await query.answer("⛔ ليس لديك صلاحية", show_alert=True)
            return
        
        # جلب التعديلات المؤقتة
        temp_key = f"temp_perms:{chat_id}:{target_id}"
        if not r.exists(temp_key):
            await query.answer("⚠️ لم تقم بأي تعديلات!", show_alert=True)
            return
            
        perms = eval(r.get(temp_key))
        
        # جلب الصلاحيات الحالية
        get_member = await c.get_chat_member(chat_id, target_id)
        current_priv = get_member.privileges
        
        # تطبيق التعديلات
        await c.promote_chat_member(
            chat_id,
            target_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=perms.get('can_delete_messages', current_priv.can_delete_messages),
                can_restrict_members=perms.get('can_restrict_members', current_priv.can_restrict_members),
                can_pin_messages=perms.get('can_pin_messages', current_priv.can_pin_messages),
                can_invite_users=perms.get('can_invite_users', current_priv.can_invite_users),
                can_change_info=perms.get('can_change_info', current_priv.can_change_info),
                can_manage_video_chats=perms.get('can_manage_video_chats', current_priv.can_manage_video_chats),
                can_promote_members=perms.get('can_promote_members', current_priv.can_promote_members)
            )
        )
        
        # تنظيف البيانات المؤقتة
        r.delete(temp_key)
        
        target_user = await c.get_users(target_id)
        await query.message.edit_text(
            f"✅ تم تحديث صلاحيات {target_user.mention} بنجاح\n"
            f"▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
            f"الصلاحيات الجديدة:\n"
            f"- حذف الرسائل: {'✅' if perms.get('can_delete_messages', current_priv.can_delete_messages) else '❌'}\n"
            f"- حظر الأعضاء: {'✅' if perms.get('can_restrict_members', current_priv.can_restrict_members) else '❌'}\n"
            f"- تثبيت الرسائل: {'✅' if perms.get('can_pin_messages', current_priv.can_pin_messages) else '❌'}\n"
            f"- دعوة المستخدمين: {'✅' if perms.get('can_invite_users', current_priv.can_invite_users) else '❌'}\n"
            f"- تغيير المعلومات: {'✅' if perms.get('can_change_info', current_priv.can_change_info) else '❌'}\n"
            f"- إدارة المكالمات: {'✅' if perms.get('can_manage_video_chats', current_priv.can_manage_video_chats) else '❌'}\n"
            f"- رفع مشرفين: {'✅' if perms.get('can_promote_members', current_priv.can_promote_members) else '❌'}"
        )
        
    except Exception as e:
        print(f"Error in save permissions: {e}")
        await query.answer("⚠️ حدث خطأ أثناء الحفظ!", show_alert=True)

@Client.on_callback_query(filters.regex(r'^cancel_perms_(\d+)$'))
async def cancel_permissions(c, query):
    try:
        target_id = int(query.data.split('_')[2])
        chat_id = query.message.chat.id
        
        if not (owner_pls(query.from_user.id, chat_id) or dev_pls(query.from_user.id, chat_id)):
            await query.answer("⛔ ليس لديك صلاحية", show_alert=True)
            return
        
        # تنظيف البيانات المؤقتة
        r.delete(f"temp_perms:{chat_id}:{target_id}")
        
        await query.message.edit_text("❌ تم إلغاء التعديلات")
        
    except Exception as e:
        print(f"Error in cancel permissions: {e}")
        await query.answer("⚠️ حدث خطأ أثناء الإلغاء!", show_alert=True)
        
@Client.on_chat_member_updated()
async def monitor_admin_behavior(client, chat_member_updated):
    if (chat_member_updated.old_chat_member 
        and chat_member_updated.old_chat_member.status == ChatMemberStatus.MEMBER
        and chat_member_updated.new_chat_member 
        and chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED):
        
        kicking_admin = chat_member_updated.from_user
        
        if kicking_admin and await is_admin_or_owner(client, kicking_admin.id, chat_member_updated.chat.id):
            kicked_user = chat_member_updated.new_chat_member.user
            
            try:
                await client.promote_chat_member(
                    chat_member_updated.chat.id,
                    kicking_admin.id,
                    can_manage_chat=False,
                    can_delete_messages=False,
                    can_manage_video_chats=False,
                    can_restrict_members=False,
                    can_promote_members=False,
                    can_change_info=False,
                    can_post_messages=False,
                    can_edit_messages=False,
                    can_pin_messages=False,
                    can_invite_users=False
                )
                
                notification = f"""
⌯ تنبيه: إساءة استخدام الصلاحيات
⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯
⌯ المشرف : {kicking_admin.mention}
⌯ قام بطرد العضو: {kicked_user.mention}

⌯ تم إزالة صلاحياته تلقائياً
⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯
⌯ المجموعة: {chat_member_updated.chat.title}"""
                
                await client.send_message(
                    chat_member_updated.chat.id,
                    notification
                )
                
                r.delete(f"{chat_member_updated.chat.id}:rankADMIN:{kicking_admin.id}{hmshelp}")
                r.srem(f"{chat_member_updated.chat.id}:listADMIN:{hmshelp}", kicking_admin.id)
                
            except Exception as e:
                print(f"حدث خطأ أثناء معاقبة المشرف: {e}")