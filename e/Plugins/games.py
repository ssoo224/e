import random,re, time, akinator, string
from threading import Thread 
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.games import *
from helpers.Ranks import isLockCommand
import json
import random
import requests

users_demon = {}
def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100

def get_top(users):
   users = [tuple(i.items()) for i in users]
   top = sorted(users, key=lambda i: i[-1][-1], reverse=True)
   top = [dict(i) for i in top]
   return top

import requests
import html
import re
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import ChatAdminRequired
import redis

@Client.on_message(filters.group & ~filters.service)
async def filter_emoji(client: Client, m: Message):
    if r.get(f"{m.chat.id}:disableEmoji:{m.chat.id}"):
        return
    
    if not m.text and not m.caption:
        return
    
    entities = m.entities or m.caption_entities
    if not entities:
        return
    
    allowed_emojis = r.smembers(f"{m.chat.id}:allowedEmojis:{m.chat.id}")
    allowed_emojis = {int(emoji) for emoji in allowed_emojis} if allowed_emojis else set()
    
    for entity in entities:
        if entity.type == "custom_emoji":
            if entity.custom_emoji_id not in allowed_emojis:
                try:
                    await m.delete()
                    warn_msg = await m.reply(
                        f"{k} من「 {m.from_user.mention} 」\n{k} ممنوع استخدام الايموجي هذا\n☆"
                    )
                    await asyncio.sleep(5)
                    await warn_msg.delete()
                except ChatAdminRequired:
                    pass
                break

@Client.on_message(filters.text & filters.group, group=33)
def gamesHandler(c,m):
    k = r.get(f'{hmshelp}:botkey')
    channel = r.get(f'{hmshelp}:BotChannel') if r.get(f'{hmshelp}:BotChannel') else 'alwzaraa2'
    Thread(target=gamesFunc,args=(c,m,k,channel)).start()

@Client.on_message(filters.dice & filters.group, group=45)
def diceFunc(c,m):
   if r.get(f'{m.chat.id}:disableGames:{hmshelp}'):  return False
   if m.dice.emoji == "🎲":
     k = r.get(f'{hmshelp}:botkey')
     if m.dice.value == 6:
        time.sleep(3)
        ra = 100
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        return m.reply(f'''
صح عليك فزت **[بالنرد]({m.link})** ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
💸فلوسك: `{floos}` ريال
☆
''', disable_web_page_preview=True)
     else:
        time.sleep(3)
        return m.reply(f"{k} للأسف خسرت بالنرد")
   

def gamesFunc(c,m,k,channel):
   text = m.text or ""
   if not r.get(f'{m.chat.id}:enable:{hmshelp}'):
       return
   if r.get(f'{m.from_user.id}:gbangames:{hmshelp}'):  return 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{hmshelp}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:mute:{hmshelp}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{hmshelp}'):  return 
   text = m.text
   name = r.get(f'{hmshelp}:BotName') if r.get(f'{hmshelp}:BotName') else 'فوق'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}'):
     text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}')
   if r.get(f'Custom:{hmshelp}&text={text}'):
     text = r.get(f'Custom:{hmshelp}&text={text}')
   if r.get(f'{m.chat.id}:disableGames:{hmshelp}'):  return
   
   if r.get(f'{m.from_user.id}:toTrans:{m.chat.id}{hmshelp}'):
      if not re.findall('[0-9]+', text): 
        r.delete(f'{m.from_user.id}:toTrans:{m.chat.id}{hmshelp}')
        return m.reply(f'{k} لازم يكون ارقام')
      acc_id = int(re.findall('[0-9]+', text)[0])
      acc_id_from = int(r.get(f'{m.from_user.id}:bankID'))
      if acc_id == acc_id_from:
        r.delete(f'{m.from_user.id}:toTrans:{m.chat.id}{hmshelp}')
        return m.reply(f'{k} مافيك تحول لنفسك')
      floos_to_trans = int(r.get(f'{m.from_user.id}:toTrans:{m.chat.id}{hmshelp}'))
      r.delete(f'{m.from_user.id}:toTrans:{m.chat.id}{hmshelp}')
      if not r.sismember('BankList', m.from_user.id):
        return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
      if not r.get(f'{m.from_user.id}:Floos'):
        floos = 0
      else:
        floos = int(r.get(f'{m.from_user.id}:Floos'))
      if floos_to_trans > floos:
        return m.reply(f'{k} فلوسك ماتكفي')
      else:
        if not r.get(f'{acc_id}:getAccBank'):
          return m.reply(f'{k} مافي حساب بنكي كذا')
        else:
          id_to = int(r.get(f'{acc_id}:getAccBank'))
          if not r.sismember('BankList', id_to):
            return m.reply(f'{k} ماعنده حساب بأي بنك')
          if r.get(f'{id_to}:bankName'):
            name_to = r.get(f'{id_to}:bankName')[:10]
          else:
            gett = c.get_users(int(r.get(f'{acc_id}:getAccBank')))
            name_to = gett.first_name[:10]
            r.set(f'{id_to}:bankName',name_to)
          if floos_to_trans == floos:
            r.delete(f'{m.from_user.id}:Floos')
          else:
            r.set(f'{m.from_user.id}:Floos',floos-floos_to_trans)
          bank_to = r.get(f'{id_to}:bankType')
          bank_from = r.get(f'{m.from_user.id}:bankType')
          name_from = r.get(f'{m.from_user.id}:bankName')[:10] or m.from_user.first_name[:10]
          mention_from = f'[{name_from}](tg://user?id={m.from_user.id})'
          mention_to = f'[{name_to}](tg://user?id={id_to})'
          if not r.get(f'{id_to}:Floos'):
            floos_to = 0
          else:
            floos_to = int(r.get(f'{id_to}:Floos'))
          txt = 'حوالة صادرة\n\nمن: {}\nحساب رقم: {}\nبنك: {}\nالى: {}\nحساب رقم: {}\nبنك: {}'.format(mention_from,acc_id_from,bank_from,mention_to,acc_id,bank_to)
          if bank_from != bank_to:
             floos_to_tran = int(floos_to_trans-floos_to_trans/10)
             txt += '\nخصمت 10% ضريبة بنك الى بنك'
             txt += f'\nالمبلغ: {floos_to_tran} ريال 💸'
          else:
             floos_to_tran = floos_to_trans
             txt += f'\nالمبلغ: {floos_to_tran} ريال 💸'
          r.set(f'{id_to}:Floos',floos_to+floos_to_tran)
          return m.reply(txt, disable_web_page_preview=True)

   if r.get(f'{m.from_user.id}:createBank:{m.chat.id}'):
     r.delete(f'{m.from_user.id}:createBank:{m.chat.id}')
     if r.get(f'{m.from_user.id}:bankID'):
       id = int(r.get(f'{m.from_user.id}:bankID'))
       floos_to_add = 0
     else:
       id = '4'
       floos_to_add = 2000
       for a in range(15):
         id += str(random.randint(1,9))
     if not r.get(f'{m.from_user.id}:Floos'):
       floos = 0
     else:
       floos = int(r.get(f'{m.from_user.id}:Floos'))
     '''
     if not text in ['الاهلي','راجحي', 'الانماء','عبد الفتاح السيسي']:
       return m.reply(f'{k} مافيه بنك بهالاسم')
     '''
   
   if text == "تفعيل الايموجي":
     if not mod_pls(m.from_user.id, m.chat.id):
         return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
     else:
         if r.get(f"{m.chat.id}:disableEmoji:{m.chat.id}"):
             r.delete(f"{m.chat.id}:disableEmoji:{m.chat.id}")
             return m.reply(
                 f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الايموجي\n☆"
                )
         else:
             return m.reply(
                 f"{k} من「 {m.from_user.mention} 」\n{k} الايموجي مفعل من قبل\n☆"
             )

   if text == "تعطيل الايموجي":
     if not mod_pls(m.from_user.id, m.chat.id):
         return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
     else:
         if not r.get(f"{m.chat.id}:disableEmoji:{m.chat.id}"):
             r.set(f"{m.chat.id}:disableEmoji:{m.chat.id}", 1)
             return m.reply(
                 f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الايموجي\n☆"
             )
         else:
             return m.reply(
                 f"{k} من「 {m.from_user.mention} 」\n{k} الايموجي معطل من قبل\n☆"
             )

   if text == "اضف ايموجي":
     if not mod_pls(m.from_user.id, m.chat.id):
         return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
     else:
         if not m.reply_to_message or not m.reply_to_message.entities:
             return m.reply(f"{k} يرجى الرد على رسالة تحتوي على الايموجي")
            
         emoji_id = None
         for entity in m.reply_to_message.entities:
             if entity.type == "custom_emoji":
                 emoji_id = entity.custom_emoji_id
                 break
            
         if emoji_id:
             r.sadd(f"{m.chat.id}:allowedEmojis:{m.chat.id}", emoji_id)
             return m.reply(
                 f"{k} من「 {m.from_user.mention} 」\n{k} ابشر اضفت الايموجي للقائمة\n☆"
             )
         else:
             return m.reply(f"{k} ما لقيت ايموجي في الرسالة")

   if text == "حذف ايموجي":
     if not mod_pls(m.from_user.id, m.chat.id):
         return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
     else:
         if not m.reply_to_message or not m.reply_to_message.entities:
             return m.reply(f"{k} يرجى الرد على رسالة تحتوي على الايموجي")
            
         emoji_id = None
         for entity in m.reply_to_message.entities:
             if entity.type == "custom_emoji":
                 emoji_id = entity.custom_emoji_id
                 break
            
         if emoji_id:
             r.srem(f"{m.chat.id}:allowedEmojis:{m.chat.id}", emoji_id)
             return m.reply(
                 f"{k} من「 {m.from_user.mention} 」\n{k} ابشر حذفت الايموجي من القائمة\n☆"
             )
         else:
             return m.reply(f"{k} ما لقيت ايموجي في الرسالة")
   
   if text == 'توب' or text == 'التوب':
     m.reply(f'{k} اهلين فيك في قوائم التوب\n\n• اختر التوب المراد الاطلاع عليه',
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('الفلوس 💸', callback_data=f'topfloos:{m.from_user.id}'),
         InlineKeyboardButton ('الحرامية 💰', callback_data=f'topzrf:{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹',url=f't.me/{channel}')
       ]
       ]
     ))
   
   if text == 'توب الفلوس':
     if not r.smembers('BankList'):
       return m.reply(f'{k} مافيه حسابات بالبنك')
     else:
       rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', url=f't.me/{channel}')]]
       )
       if r.get('BankTop'):
          text = r.get('BankTop')
          if not r.get(f'{m.from_user.id}:Floos'):
            floos = 0
          else:
            floos = int(r.get(f'{m.from_user.id}:Floos'))
          get = r.ttl('BankTop')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {floos:,} 💸 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          return m.reply(text, disable_web_page_preview=True,reply_markup=rep)
       else:
          users = []
          ccc = 0
          for user in r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if r.get(f'{id}:bankName'):
              name = r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = c.get_chat(id).first_name
                r.set(f'{id}:bankName',name)
              except:
                name = 'INVALID_NAME'
                r.set(f'{id}:bankName',name)
            if not r.get(f'{id}:Floos'):
              floos = 0
            else:
              floos = int(r.get(f'{id}:Floos'))
            users.append({'name':name, 'money':floos})
          top = get_top(users)
          text = 'توب 20 اغنى اشخاص:\n\n'
          count = 0
          for user in top:
            count += 1
            if count == 21:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'**{emoji}{floos:,}** 💸 l {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
          r.set('BankTop',text,ex=300)
          if not r.get(f'{m.from_user.id}:Floos'):
            floos_from_user = 0
          else:
            floos_from_user = int(r.get(f'{m.from_user.id}:Floos'))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {floos_from_user:,} 💸 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          get = r.ttl('BankTop')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          return m.reply(text,disable_web_page_preview=True,reply_markup=rep)
   
   
   if text == 'توب الحراميه' or text == 'توب الحرامية' or text == 'توب الزرف':
     if not r.smembers('BankList'):
       return m.reply(f'{k} مافيه حسابات بالبنك')
     else:
       rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', url=f't.me/{channel}')]]
       )
       if r.get('BankTopZRF'):
          text = r.get('BankTopZRF')
          if not r.get(f'{m.from_user.id}:Zrf'):
            zrf = 0
          else:
            zrf = int(r.get(f'{m.from_user.id}:Zrf'))
          get = r.ttl('BankTopZRF')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {zrf:,} 💰 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          return m.reply(text, disable_web_page_preview=True,reply_markup=rep)
       else:
          users = []
          ccc = 0
          for user in r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if r.get(f'{id}:bankName'):
              name = r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = c.get_chat(id).first_name
                r.set(f'{id}:bankName',name)
              except:
                name = 'INVALID_NAME'
                r.set(f'{id}:bankName',name)
            if not r.get(f'{id}:Zrf'):
              zrf = 0
            else:
              zrf = int(r.get(f'{id}:Zrf'))
            users.append({'name':name, 'money':zrf})
          top = get_top(users)
          text = 'توب 20 اكثر الحراميه زرفًا:\n\n'
          count = 0
          for user in top:
            count += 1
            if count == 21:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'**{emoji}{floos:,}** 💰 l⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
          r.set('BankTopZRF',text,ex=300)
          if not r.get(f'{m.from_user.id}:Zrf'):
            floos_from_user = 0
          else:
            floos_from_user = int(r.get(f'{m.from_user.id}:Zrf'))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {floos_from_user:,} 💰 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          get = r.ttl('BankTopZRF')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          m.reply(text,disable_web_page_preview=True,reply_markup=rep)
   
   if text == 'زواجات' or text == 'توب زواجات' or text == 'توب الزواجات':
     if not r.smembers(f'{m.chat.id}:zwag:{hmshelp}'):
        return m.reply(f'{k} محد متزوج بالقروب')
     else:
        #r.sadd(f'{m.chat.id}:zwag:{hmshelp}', f'{m.reply_to_message.from_user.id}--{m.from_user.id}&&floos={floos}')
        users = []
        ccc = 0
        for marriage in r.smembers(f'{m.chat.id}:zwag:{hmshelp}'):
           user_id_1 = int(marriage.split('--')[0])
           user_id_2 = int(marriage.split('--')[1].split('&&')[0])
           money = int(marriage.split('&&floos=')[1])
           ccc += 1
           if r.get(f'{user_id_1}:bankName'):
              name_1 = r.get(f'{user_id_1}:bankName')[:10]
           else:
              try:
                name_1 = c.get_chat(id).first_name[:10]
                r.set(f'{user_id_1}:bankName',name_1)
              except:
                name_1 = 'INVALID_NAME'
                r.set(f'{user_id_1}:bankName',name_1)
           if r.get(f'{user_id_2}:bankName'):
              name_2 = r.get(f'{user_id_2}:bankName')[:10]
           else:
              try:
                name_2 = c.get_chat(id).first_name[:10]
                r.set(f'{user_id_2}:bankName',name_2)
              except:
                name_2 = 'INVALID_NAME'
                r.set(f'{user_id_2}:bankName',name_2)
           users.append({'name_1':name_1, 'name_2':name_2,'money':money})
        top = get_top(users)
        text = 'توب 20 اغلى زواجات بالقروب:\n\n'
        count = 0
        for user in top:
          count += 1
          if count == 21:
            break 
          emoji = get_emoji_bank(count)
          money = user['money']
          name_1 = user['name_1']
          name_2 = user['name_2']
          text += f'**{emoji}**👫 ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name_1} 💕 {name_2} |\n**💸 {money:,}**\n'
        text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
        return m.reply(text, disable_web_page_preview=True)
           

   if text == 'تصفير التوب':
     if devp_pls(m.from_user.id,m.chat.id):
       if not r.get('BankTop'):
         return m.reply('اكتب توب الفلوس وارجع حاول')
       if not r.get('BankTopZRF'):
         return m.reply('اكتب توب الحراميه وارجع حاول')
       else:
         m.reply(f'{k} ابشر صفرت التوب')
         users = []
         ccc = 0
         for user in r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if r.get(f'{id}:bankName'):
              name = r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = c.get_chat(id).first_name
                r.set(f'{id}:bankName',name)
              except:
                name = 'INVALID_NAME'
                r.set(f'{id}:bankName',name)
            if not r.get(f'{id}:Zrf'):
              zrf = 0
            else:
              zrf = int(r.get(f'{id}:Zrf'))
            users.append({'name':name, 'money':zrf})
         top = get_top(users)
         text = ''
         count = 0
         for user in top:
            count += 1
            if count == 3:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'{emoji}{floos} 💰 l {name}\n'
         r.set(f'BankTopLastZrf',text)
         users = []
         ccc = 0
         for user in r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if r.get(f'{id}:bankName'):
              name = r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = c.get_chat(id).first_name
                r.set(f'{id}:bankName',name)
              except:
                name = 'INVALID_NAME'
                r.set(f'{id}:bankName',name)
            if not r.get(f'{id}:Floos'):
              floos = 0
            else:
              floos = int(r.get(f'{id}:Floos'))
         users.append({'name':name, 'money':floos})
         top = get_top(users)
         text = ''
         count = 0
         for user in top:
            count += 1
            if count == 3:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'**{emoji}{floos}** 💸 l {name}\n'
         r.set(f'BankTopLast',text)
         keys = r.keys('*:Floos')
         for a in keys:
           r.delete(a)
   
   if text == 'حسابي':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     else:
       card = r.get(f'{m.from_user.id}:bankCard')
       id = int(r.get(f'{m.from_user.id}:bankID'))
       bank = r.get(f'{m.from_user.id}:bankType')
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       if r.get(f'{m.from_user.id}:bankName'):
         name = r.get(f'{m.from_user.id}:bankName')
       else:
         name = m.from_user.first_name
       m.reply(f'''{k} الاسم ↢ ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
{k} الحساب ↢ `{id}`
{k} بنك ↢ ( {bank} )
{k} نوع ↢ ( {card} )
{k} الرصيد ↢ ( {floos} ريال 💸 )
☆''')
   
   if text == 'تقييم':
      if m.reply_to_message:
          target_user = m.reply_to_message.from_user 
      else:
          target_user = m.from_user  #
    
      target_id = target_user.id
    
      username = f"@{target_user.username}" if target_user.username else "لا يوجد"
      try:
          bio = c.get_chat(target_id).bio or "لا يوجد"
      except:
          bio = "لا يوجد"
    
      likes = int(r.get(f"user:{target_id}:likes") or 0)
      dislikes = int(r.get(f"user:{target_id}:dislikes") or 0)
      total = likes + dislikes
    
      if total == 0:
          rating_text = "لا يوجد تقييمات بعد"
      elif likes > dislikes:
          if (likes / total) >= 0.7:
              rating_text = "معشوق القروب 🥹💗"
          elif (likes / total) >= 0.5:
              rating_text = "حلو القروب 🥹🎉"
          else:
              rating_text = "نص نص 🙃"
      elif dislikes > likes:
          if (dislikes / total) >= 0.7:
              rating_text = "اخلاقه مو كويسه"
          elif (dislikes / total) >= 0.5:
              rating_text = "محد طايقك 🥲"
          else:
              rating_text = "مكروه 💔"
      else:
          rating_text = "ماشي حاله 🙆‍♂️"
    
      keyboard = InlineKeyboardMarkup([
          [
              InlineKeyboardButton(f"🤍 {likes}", callback_data=f"rate_like_{target_id}"),
              InlineKeyboardButton(f"👎 {dislikes}", callback_data=f"rate_dislike_{target_id}")
          ]
      ])
    
      return m.reply(
          f"``` ◈ تقييم المستخدم ◈```\n\n"
          f"𖡋 NaMe ⌯ {target_user.first_name}\n"
          f"𖡋 𝐔𝐒𝐄 ⌯ {username}\n"
          f"𖡋 𝐈𝐃 ⌯ `{target_id}`\n\n"
          f"𖡋 𝐔 ⌯ {rating_text}",
          reply_markup=keyboard
      )
   
   if text == 'المشاهير' or text == 'المشهورين':
      top_users_key = "daily_top_rated_users"
    
      if not r.exists(top_users_key):
        # نفس طريقة جلب البيانات المستخدمة في أمر التقييم
          all_user_ids = [key.split(':')[1] for key in r.keys("user:*:likes")]
          user_ratings = []
        
          for user_id in all_user_ids:
              likes = int(r.get(f"user:{user_id}:likes") or 0)
              dislikes = int(r.get(f"user:{user_id}:dislikes") or 0)
            
              if likes > 0:  # فقط المستخدمين الذين لديهم لايكات
                  user_ratings.append({
                      'user_id': user_id,
                      'likes': likes,
                      'dislikes': dislikes,
                      'total': likes + dislikes
                  })
        
        # الترتيب بنفس معايير أمر التقييم
          user_ratings.sort(key=lambda x: x['likes'], reverse=True)
          top_5 = user_ratings[:5]
        
        # تخزين البيانات بنفس الهيكل
          for user in top_5:
              r.zadd(top_users_key, {user['user_id']: user['likes']})
          r.expire(top_users_key, 86400)
    
    # جلب البيانات بنفس الطريقة
      top_users = []
      for user_id, likes in r.zrevrange(top_users_key, 0, 4, withscores=True):
          dislikes = int(r.get(f"user:{user_id}:dislikes") or 0)
          top_users.append({
              'user_id': user_id,
              'likes': int(likes),
              'dislikes': dislikes,
              'total': int(likes) + dislikes
          })
    
      if not top_users:
          return m.reply("لا يوجد مشاهير بعد!")
    
    # نفس نظام التقييم المستخدم في الأمر الآخر
      rank_emojis = {
          1: "🤴",
          2: "👑", 
          3: "⭐",
          4: "🌀",
          5: "💎"
      }
    
      message = "𓄼 قائمة المشاهير 𓄼\n\n"
    
      for rank, user in enumerate(top_users, 1):
          try:
              user_obj = c.get_users(int(user['user_id']))
              emoji = rank_emojis.get(rank, "✨")
            
            # نفس منطق التقييم
              if user['total'] == 0:
                  rating_text = "جديد"
              elif user['likes'] > user['dislikes']:
                  if (user['likes'] / user['total']) >= 0.7:
                      rating_text = "معشوق الجماهير 💗"
                  elif (user['likes'] / user['total']) >= 0.5:
                      rating_text = "محبوب 🎉"
                  else:
                      rating_text = "مقبول 🙃"
              else:
                  rating_text = "لديه نقاط سلبية 💔"
            
              message += (
                  f"{emoji} {user_obj.first_name} ⪧ {user['likes']} 🤍\n"
              )
            
          except Exception as e:
              print(f"Error processing user {user['user_id']}: {e}")
              continue
    
      message += "𓄼 يتم تحديث القائمة يومياً 𓄼"
      m.reply(message)
   
   if text == 'شراء تقييم':
      if not r.sismember('BankList', m.from_user.id):
          return m.reply(f'{k} ليس لديك حساب بنكي! أرسل "انشاء حساب بنكي" أولاً')

      floos = int(r.get(f'{m.from_user.id}:Floos') or 0)
    
      packages = [
          {"تقييمات": 5, "سعر": 25000, "نسبة": "50 لكل تقييم"},
          {"تقييمات": 15, "سعر": 60000, "نسبة": "40 لكل تقييم"}, 
          {"تقييمات": 30, "سعر": 102000, "نسبة": "35 لكل تقييم"},
          {"تقييمات": 50, "سعر": 150000, "نسبة": "30 لكل تقييم"}
      ]

      buttons = []
      for pkg in packages:
          buttons.append([
              InlineKeyboardButton(
                  f"{pkg['تقييمات']} --» {pkg['سعر']} ريال",
                  callback_data=f"buy_rate:{pkg['تقييمات']}:{pkg['سعر']}"
              )
          ])
    
      buttons.append([InlineKeyboardButton("إلغاء العملية", callback_data="cancel_rate_purchase")])

      return m.reply(
          f"𓂀 رصيدك الحالي: {floos} ريال 𓂀\n\n"
          "◈ اختر عدد التقييمات الذي تريد شرائه ◈\n", 
          reply_markup=InlineKeyboardMarkup(buttons)
      )

   if text == 'انشاء حساب بنكي':
      if r.sismember('BankList', m.from_user.id):
         bank = r.get(f'{m.from_user.id}:bankType')
         acc_id = int(r.get(f'{m.from_user.id}:bankID'))
         return m.reply(f'{k} عندك حساب في بنك {bank}\n\n{k} لتفاصيل اكثر اكتب\n{k} `حساب {acc_id}`')
      else:
            # إنشاء أزرار Inline لاختيار البنك
         keyboard = InlineKeyboardMarkup([
             [
                 InlineKeyboardButton("الاهلي", callback_data="create_bank_الاهلي"),
                 InlineKeyboardButton("راجحي", callback_data="create_bank_راجحي")
             ],
             [
                 InlineKeyboardButton("الانماء", callback_data="create_bank_الانماء")
             ]
         ])
         return m.reply(
             f'– عشان تسوي حساب لازم تختار بنك\n\n{k} اختر البنك من الأزرار أدناه:',
             reply_markup=keyboard
         )
   
   if text == 'مسح حسابي':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي')
     else:
       r.srem('BankList', m.from_user.id)
       m.reply(f'{k} تم حذف حسابك البنكي')
   
   if text == "الاعدادات":
     if not mod_pls(m.from_user.id, m.chat.id):
         return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
    
     settings = {
         "lockAudios": "الصوتيات",
         "lockVideo": "الفيديو",
         "lockVoice": "الصوت",
         "lockPhoto": "الصور",
         "mute": "الدردشة",
         "lockInline": "الانلاين",
         "lockForward": "التوجيه",
         "lockHashtags": "الهشتاق",
         "lockEdit": "التعديل",
         "lockStickers": "الملصقات",
         "lockFiles": "الملفات",
         "lockAnimations": "المتحركات",
         "lockUrls": "الروابط",
         "lockBots": "البوتات",
         "lockTags": "اليوزرات",
         "lockNot": "الاشعارات",
         "lockaddContacts": "الاضافة",
         "lockMessages": "الكلام الكثير",
         "lockSHTM": "السب",
         "lockSpam": "التكرار",
         "lockChannels": "القنوات",
         "lockEditM": "تعديل الميديا",
         "lockJoin": "الدخول",
         "lockPersian": "الفارسية",
         "lockJoinPersian": "دخول الإيراني",
         "lockNSFW": "الإباحي"
     }

     buttons = []
     temp_row = []
    
     for i, (key, name) in enumerate(settings.items(), 1):
         status = "🔴" if r.get(f"{m.chat.id}:{key}:{hmshelp}") else "🟢"
         temp_row.append(InlineKeyboardButton(
             f"{name} {status}",
             callback_data=f"settings_toggle_{key}"
         ))
        
         if i % 2 == 0 or i == len(settings):
             buttons.append(temp_row)
             temp_row = []
    
     buttons.append([InlineKeyboardButton("إغلاق القائمة", callback_data="settings_close")])
    
     m.reply(
         "⚙️ **إعدادات المجموعة**\n"
         "▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
         "🟢 = مفعل | 🔴 = معطل\n\n"
         "اضغط على الزر لتغيير حالته",
         reply_markup=InlineKeyboardMarkup(buttons)
     )
   
   if text.startswith('حساب ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
      acc_id = int(re.findall('[0-9]+', text)[0])
      if r.get(f'{acc_id}:getAccBank'):
         id = int(r.get(f'{acc_id}:getAccBank'))
         if r.get(f'{id}:bankName'):
           name = r.get(f'{id}:bankName')[:10]
         else:
           gett = c.get_users(int(r.get(f'{acc_id}:getAccBank')))
           name = gett.first_name
           r.set(f'{id}:bankName',name)
         bank = r.get(f'{id}:bankType')
         card = r.get(f'{id}:bankCard')
         if not r.get(f'{id}:Floos'):
           floos = 0
         else:
           floos = int(r.get(f'{id}:Floos'))
         m.reply(f'''
{k} الاسم ↢ ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
{k} الحساب ↢ `{acc_id}`
{k} بنك ↢ ( {bank} )
{k} نوع ↢ ( {card} )
{k} الرصيد ↢ ( `{floos}` ريال 💸 )
☆
''')
   
   if text.startswith('تحويل ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
      floos_to_trans = int(re.findall('[0-9]+', text)[0])
      if not r.get(f'{m.from_user.id}:Floos'):
        floos = 0
      else:
        floos = int(r.get(f'{m.from_user.id}:Floos'))
      if floos_to_trans < 200:
        return m.reply(f'{k} الحد الادنى المسموح هو 200 ريال')
      else:
        if floos_to_trans > floos:
          return m.reply(f'{k} فلوسك ماتكفي')
        if not r.sismember('BankList', m.from_user.id):
          return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
        else:
          r.set(f'{m.from_user.id}:toTrans:{m.chat.id}{hmshelp}',floos_to_trans, ex=600)
          return m.reply(f'{k} ارسل الحين رقم حساب البنكي الي تبي تحول له')      
      
   if text.startswith('حظ ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitHZ'):
       get = r.ttl(f'{m.from_user.id}:BankWaitHZ')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمديك تلعب لعبة الحظ الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       floos_to_hz = int(re.findall('[0-9]+', text)[0])
       if floos_to_hz == 0:
         return m.reply(f'{k} مايمدي تلعب بالصفر')
       if floos_to_hz > floos:
         return m.reply(f'{k} فلوسك ماتكفي')
       else:
         r.set(f'{m.from_user.id}:BankWaitHZ',1,ex=600)
         hzz = random.choice(['yes','no'])
         if hzz == 'yes':
           fls = floos_to_hz
           floos_com = floos+fls
           r.set(f'{m.from_user.id}:Floos', floos+fls)
           return m.reply(f'{k} مبروك فزت بالحظ !\n{k} فلوسك قبل ↢ ( **{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{floos_com}** ريال 💸 )')
         else:
           fls = floos-floos_to_hz
           if fls == 0:
              r.delete(f'{m.from_user.id}:Floos')
           else:
              r.set(f'{m.from_user.id}:Floos', fls)
           return m.reply(f'{k} للأسف خسرت بالحظ !\n{k} فلوسك قبل ↢ ( **{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{fls}** ريال 💸 )')
   
   
   if text == "حظ فلوسي":
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitHZ'):
       get = r.ttl(f'{m.from_user.id}:BankWaitHZ')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمديك تلعب لعبة الحظ الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       floos_to_hz = floos
       if floos_to_hz == 0:
         return m.reply(f'{k} مايمدي تلعب بالصفر')
       else:
         r.set(f'{m.from_user.id}:BankWaitHZ',1,ex=600)
         hzz = random.choice(['yes','no'])
         if hzz == 'yes':
           fls = floos_to_hz
           floos_com = floos+fls
           r.set(f'{m.from_user.id}:Floos', floos+fls)
           return m.reply(f'{k} مبروك فزت بالحظ !\n{k} فلوسك قبل ↢ ( **{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{floos_com}** ريال 💸 )')
         else:
           fls = floos-floos_to_hz
           if fls == 0:
              r.delete(f'{m.from_user.id}:Floos')
           else:
              r.set(f'{m.from_user.id}:Floos', fls)
           return m.reply(f'{k} للأسف خسرت بالحظ !\n{k} فلوسك قبل ↢ ( "**{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{fls}** ريال 💸 )')

   if text == 'عجله' or text == 'عجلة':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     else:
       if r.get(f'{m.from_user.id}:BankWait3JL'):
         get = r.ttl(f'{m.from_user.id}:BankWait3JL')
         wait = time.strftime('%M:%S', time.gmtime(get))
         return m.reply(f'{k} مايمديك تلعب عجلة الحين ! \n{k} تعال بعد {wait} دقيقة')
       else:
         r.set(f'{m.from_user.id}:BankWait3JL',1,ex=300)
         rep = m.reply(f'{k} حلف العجلة بعد ٣ ثواني',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('³',callback_data='None')]]))
         time.sleep(1)
         rep.edit_text(f'{k} حلف العجلة بعد ثانيتين',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('²',callback_data='None')]]))
         time.sleep(1)
         rep.edit_text(f'{k} حلف العجلة بعد ثانية',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('¹',callback_data='None')]]))
         time.sleep(1)
         emojis_3jl = [
         '💸','💸','💸','💸','💸','💸','💸',
         '💸','💸','💸','💸','💸','💸','💸',
         '⚡','⚡','⚡','⚡','⚡','⚡','⚡',
         '⚡','⚡','⚡','⚡','⚡','⚡','⚡',
         '💣','💣','💣','💣','💣','💣','💣',
         '💣','💣','💣','💣','💣','💣','💣',
         '🍒','🍒','🍒','🍒','🍒','🍒','🍒',
         '🍒','🍒','🍒','🍒','🍒','🍒','🍒',
         '💎','💎','💎','💎','💎','💎','💎',
         '💎','💎','💎','💎','💎','💎','💎'
         ]
         emoji1 = random.choice(emojis_3jl)
         emoji2 = random.choice(emojis_3jl)
         emoji3 = random.choice(emojis_3jl)
         reply_ma = InlineKeyboardMarkup (
           [
             [
               InlineKeyboardButton (emoji1, callback_data='None'),
               InlineKeyboardButton (emoji2, callback_data='None'),
               InlineKeyboardButton (emoji3, callback_data='None'),
             ],
             [
               InlineKeyboardButton ('🫦', url=f't.me/{channel}')
             ]
           ]
         )
         if emoji1 == emoji2 and emoji2 == emoji3:
            chance = random.choice([100000, 200000, 300000])
            if not r.get(f'{m.from_user.id}:Floos'):
              floos = 0
            else:
              floos = int(r.get(f'{m.from_user.id}:Floos'))
            rep.edit_text(f'{k} فزت بعجلة الحظ!\n\n{k} مبلغ الربح ( {chance} ريال 💸 )\n{k} فلوسك قبل ( `{floos}` ريال 💸 )\n{k} فلوسك الحين ( `{floos+chance}` ريال 💸 )',reply_markup=reply_ma)
            r.set(f'{m.from_user.id}:Floos', floos+chance)
         else:
            chance = random.randint(100,1000)
            if not r.get(f'{m.from_user.id}:Floos'):
              floos = 0
            else:
              floos = int(r.get(f'{m.from_user.id}:Floos'))
            rep.edit_text(f'{k} للأسف خسرت بعجلة الحظ!\n\n{k} خذ {chance} ريال عشان ماتصيح\n{k} فلوسك قبل ( `{floos}` ريال 💸 )\n{k} فلوسك الحين ( `{floos+chance}` ريال 💸 )',reply_markup=reply_ma)
            r.set(f'{m.from_user.id}:Floos', floos+chance)
           
   if text.startswith('استثمار ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitEST'):
       get = r.ttl(f'{m.from_user.id}:BankWaitEST')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمديك تستثمر الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       floos_to_est = int(re.findall('[0-9]+', text)[0])
       if floos_to_est == 0:
         return m.reply(f'{k} مايمدي تلعب بالصفر')
       if floos_to_est > floos:
         return m.reply(f'{k} فلوسك ماتكفي')
       if floos_to_est < 2000:
         return m.reply(f'{k} للأسف لازم تستثمر ب 2000 ريال عالأقل')
       else:
         r.set(f'{m.from_user.id}:BankWaitEST',1,ex=300)
         one = int(floos_to_est/random.randint(1,9))
         rb7 = int(is_what_percent_of(one,floos_to_est))
         r.set(f'{m.from_user.id}:Floos',floos+one)
         m.reply(f'''
{k}  استثمار ناجح!
{k} نسبة الربح ↢ {rb7}%
{k} مبلغ الربح ↢ ( `{one}` ريال )
{k} فلوسك صارت ↢ ( `{floos+one}` ريال 💸 )
''')
   
   if text == "استثمار فلوسي":
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitEST'):
       get = r.ttl(f'{m.from_user.id}:BankWaitEST')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمديك تستثمر الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       floos_to_est = floos
       if floos_to_est == 0:
         return m.reply(f'{k} مايمدي تستثمر بالصفر')
       if floos_to_est < 2000:
         return m.reply(f'{k} للأسف لازم تستثمر ب 2000 ريال عالأقل')
       else:
         r.set(f'{m.from_user.id}:BankWaitEST',1,ex=300)
         one = int(floos_to_est/random.randint(1,9))
         rb7 = int(is_what_percent_of(one,floos_to_est))
         r.set(f'{m.from_user.id}:Floos',floos+one)
         m.reply(f'''
{k}  استثمار ناجح!
{k} نسبة الربح ↢ {rb7}%
{k} مبلغ الربح ↢ ( `{one}` ريال )
{k} فلوسك صارت ↢ ( `{floos+one}` ريال 💸 )
''')
   
   if text == 'كنز':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitKNZ'):
       get = r.ttl(f'{m.from_user.id}:BankWaitKNZ')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} كنزك بينزل بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
          floos = 0
       else:
          floos = int(r.get(f'{m.from_user.id}:Floos'))
       knz = random.choice(knzs)
       money = knz['credit']
       name = knz['name']
       r.set(f'{m.from_user.id}:BankWaitKNZ',1, ex=600)
       r.set(f'{m.from_user.id}:Floos', floos+money)
       fls = floos+money
       return m.reply(f'اشعار ايداع {m.from_user.mention(m.from_user.first_name[:10])}⁪⁬⁪⁬⁮⁪⁬⁪\nالمبلغ: **{money}** ريال\nالكنز: {name}\nنوع العملية: ربح كنز\nرصيدك الحين: **{fls}** ريال 💸')

   if text == 'بخشيش':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitB5'):
       get = r.ttl(f'{m.from_user.id}:BankWaitB5')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمدي اعطيك بخشيش الحين\n{k} تعال بعد {wait} دقيقة')
     else:
       b5 = random.randint(5,1000)
       r.set(f'{m.from_user.id}:BankWaitB5',1, ex=300)
       if not r.get(f'{m.from_user.id}:Floos'):
          floos = 0
       else:
          floos = int(r.get(f'{m.from_user.id}:Floos'))
       r.set(f'{m.from_user.id}:Floos', floos+b5)
       m.reply(f'{k} دلعتك وعطيتك {b5} ريال 💸')
       
   if text == 'راتب':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWait'):
       get = r.ttl(f'{m.from_user.id}:BankWait')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} راتبك بينزل بعد {wait} دقيقة')
     else:
       job = random.choice(jobs)
       money = job['credit']
       name = job['name']
       r.set(f'{m.from_user.id}:BankWait',1, ex=300)
       if not r.get(f'{m.from_user.id}:Floos'):
          floos = 0
       else:
          floos = int(r.get(f'{m.from_user.id}:Floos'))
       r.set(f'{m.from_user.id}:Floos', floos+money)
       fls = floos+money
       m.reply(f'اشعار ايداع⁪⁬⁪⁬⁮⁪⁬⁪ {m.from_user.mention(m.from_user.first_name[:10])}\nالمبلغ: **{money}** ريال\nوظيفتك: {name}\nنوع العملية: اضافة راتب\nرصيدك الحين: **{fls}** ريال 💸')
   
   if text == 'زرف' and m.reply_to_message and m.reply_to_message.from_user:
     if m.reply_to_message.from_user.id == int(hmshelp):
       return m.reply('?')
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if not r.sismember('BankList', m.reply_to_message.from_user.id):
       return m.reply(f'{k} ماعنده حساب بنكي')
     if m.reply_to_message.from_user.id == m.from_user.id:
       return m.reply('تبي تزرف نفسك؟')
     if r.get(f'{m.from_user.id}:BankWaitZRF'):
       get = r.ttl(f'{m.from_user.id}:BankWaitZRF')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} يولد انحش الشرطة للحين تدور عنك\n{k} يمديك تزرف مره ثانيه بعد {wait}')
     if r.get(f'{m.reply_to_message.from_user.id}:BankWaitMZROF'):
       get = r.ttl(f'{m.reply_to_message.from_user.id}:BankWaitMZROF')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} ذا المسكين مزروف قبل شوي\n{k} يمديك تزرفه بعد {wait}')
     if not r.get(f'{m.reply_to_message.from_user.id}:Floos'):
       return m.reply(f'{k} مطفر مامعه ولا ريال')
     if int(r.get(f'{m.reply_to_message.from_user.id}:Floos')) < 2000:
       return m.reply(f'{k} مايمديك تزرفه لان فلوسه اقل من 2000 ريال')
     else:
       zrf = random.randint(50,1000)
       r.set(f'{m.from_user.id}:BankWaitZRF',1,ex=300)
       r.set(f'{m.reply_to_message.from_user.id}:BankWaitMZROF',1,ex=300)
       floos = int(r.get(f'{m.reply_to_message.from_user.id}:Floos'))
       r.set(f'{m.reply_to_message.from_user.id}:Floos',floos-zrf)
       m.reply(f'{k} خذ يالحرامي زرفته {zrf} ريال 💸')
       if not r.get(f'{m.from_user.id}:Floos'):
         floos_from_user = 0
       else:
         floos_from_user = int(r.get(f'{m.from_user.id}:Floos'))
       r.set(f'{m.from_user.id}:Floos',floos_from_user+zrf)
       r.sadd('BankZrf',m.from_user.id)
       if r.get(f'{m.from_user.id}:Zrf'):
          zrff = int(r.get(f'{m.from_user.id}:Zrf'))
       else:
          zrff = 0
       r.set(f'{m.from_user.id}:Zrf',zrff+zrf)
       try:
         c.send_message(
           m.reply_to_message.from_user.id,
           f'الحق الحق حلالك!!\nذا الحرامي {m.from_user.mention}\nسرق منك ( {zrf} ريال 💸 )\n༄',
           reply_markup=InlineKeyboardMarkup (
             [[
               InlineKeyboardButton (m.chat.title, url=m.link)
             ]]
           )
           )
       except:
         pass
       
  
   if text == 'تصفير البنك':
     if devp_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} متأكد تبي تصفر البنك ؟',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('اي', callback_data='yes:del:bank')],[InlineKeyboardButton ('لا', callback_data='no:del:bank')]]))
   
   if text == 'فلوسي':
     if not r.get(f'{m.from_user.id}:Floos'):
        m.reply(f'{k} ماعندك فلوس ارسل الالعاب وابدا جمع الفلوس')
     else:
        floos = int(r.get(f'{m.from_user.id}:Floos'))
        return m.reply(f'{k} فلوسك `{floos}` ريال 💸')
   
   if text == 'فلوس':
     if not m.reply_to_message:
       if not r.get(f'{m.from_user.id}:Floos'):
         return m.reply(f'{k} ماعندك فلوس ارسل الالعاب وابدا جمع الفلوس')
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       return m.reply(f'{k} فلوسك `{floos}` ريال 💸')
     else:
       if not r.get(f'{m.reply_to_message.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.reply_to_message.from_user.id}:Floos'))
       return m.reply(f'{k} فلوسه ↢ ( {floos} ريال 💸 )')
   
   if text.startswith('بيع فلوسي ') and len(text.split()) == 3 and re.findall('[0-9]+', text):
     if not r.get(f'{m.from_user.id}:Floos'):
        m.reply(f'{k} للاسف انت مطفر عندك 0 ريال')
     else:
        floos_to_sale = int(re.findall('[0-9]+', text)[0])
        floos = int(r.get(f'{m.from_user.id}:Floos'))
        if floos_to_sale == 0:
         return m.reply(f'{k} مايمدي تبيع صفر')
        if floos_to_sale > floos:
          return m.reply(f'{k} للاسف انت مطفر عندك {floos} ريال')
        if floos_to_sale == floos:
           r.delete(f'{m.from_user.id}:Floos')
        else:
           r.set(f'{m.from_user.id}:Floos',floos-floos_to_sale)
        get = int(r.get(f'{m.chat.id}:TotalMsgs:{m.from_user.id}{hmshelp}'))
        rsayl = floos_to_sale * 20
        r.set(f'{m.chat.id}:TotalMsgs:{m.from_user.id}{hmshelp}', get+rsayl)
        m.reply(f'{k} بعت ( {floos_to_sale} ريال 💸 ) من فلوسك\n{k} مجموع رسايلك الحين ( {get + rsayl} )\n☆')
   
   if text.startswith('اضف فلوس ') and len(text.split()) == 3 and re.findall('[0-9]+', text):
     if dev2_pls(m.from_user.id,m.chat.id):
       if m.reply_to_message and m.reply_to_message.from_user:
          floos_to_add = int(re.findall('[0-9]+', text)[0])
          if not r.get(f'{m.reply_to_message.from_user.id}:Floos'):
             r.set(f'{m.reply_to_message.from_user.id}:Floos',floos_to_add)
          else:
             floos = int(r.get(f'{m.reply_to_message.from_user.id}:Floos'))
             r.set(f'{m.reply_to_message.from_user.id}:Floos',floos_to_add+floos)
          m.reply(f'「 {m.reply_to_message.from_user.mention} 」\n{k} ضفت له ( {floos_to_add} ) ريال 💸')
   
   
   if text == 'انشاء اكواد':
      if devp_pls(m.from_user.id,m.chat.id):
         if r.get(f'{hmshelp}:codeWait'):
           t = r.ttl(f'{hmshelp}:codeWait')
           wait = time.strftime('%H:%M:%S', time.gmtime(t))
           return m.reply(f'{k} انشئت اكواد الكشط من شوي تعال بعد {wait}')
         else:
           txt = 'اكواد الكشط:\n'
           ccc = 1
           for none in range(10):
             code = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
             r.set(f'{code}:CodeBank:{hmshelp}',1,ex=7200)
             txt += f'{ccc} ) `{code}`\n'
             ccc += 1
           r.set(f'{hmshelp}:codeWait',1,ex=7200)
           txt += '\n~ الأكواد صالحة لساعتين فقط .'
           txt += '\n༄'
           return m.reply(txt)
   
   if text.startswith('كشط ') and len(text.split()) == 2:
     code = text.split()[1]
     if not r.get(f'{code}:CodeBank:{hmshelp}'):
       return m.reply(f'{k} الكود منتهي الصلاحيه او تابع لبوت ثاني')
     if r.get(f'{m.from_user.id}:BankWaitKSHT:{hmshelp}'):
       t = r.ttl(f'{m.from_user.id}:BankWaitKSHT:{hmshelp}')
       wait = time.strftime('%H:%M:%S', time.gmtime(t))
       return m.reply(f'{k} كشطت كود من شوي تعال بعد {wait}')
     else:
       r.delete(f'{code}:CodeBank:{hmshelp}')
     if not r.get(f'{m.from_user.id}:Floos'):
       floos_from_user = 0
     else:
       floos_from_user = int(r.get(f'{m.from_user.id}:Floos'))
     chance = random.choice([1000000000, 2000000000, 3000000000])
     r.set(f'{m.from_user.id}:Floos',floos_from_user+chance)
     m.reply(f'{k} مبرووووك 🏆\n{k} كشطت الكود واخذت ( {chance} ريال 💸 )\n{k} فلوسك قبل ( `{floos_from_user}` ريال 💸 )\n{k} فلوسك الحين ( `{floos_from_user+chance}` ريال 💸 )')
     r.set(f'{m.from_user.id}:BankWaitKSHT:{hmshelp}',1,ex=7200)
     if r.get(f'DevGroup:{hmshelp}'):
       alert = f'𖡋 𝐍𝐀𝐌𝐄 ⌯ {m.from_user.mention}\n𖡋 𝐈𝐃 ⌯ `{m.from_user.id}`\n\nكشط الكود `{code}` وأخذ {chance} ريال 💸'
       c.send_message(int(r.get(f'DevGroup:{hmshelp}')),alert)
   
   if text.startswith('زواج ') and re.findall('[0-9]+', text) and m.reply_to_message and m.reply_to_message.from_user and len(text.split()) == 2:
     if m.reply_to_message.from_user.id == c.me.id or m.reply_to_message.from_user.id == m.from_user.id:
       return m.reply('?')
     if m.reply_to_message.from_user.is_bot:
       return False
     if r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{hmshelp}'):
       getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{hmshelp}')))
       mention = getUser.mention
       return m.reply(f'「 {mention} 」 \n{k} تعاليييي زوجك بيخونك')
     if r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{hmshelp}'):
       getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{hmshelp}')))
       mention = getUser.mention
       return m.reply(f'「 {mention} 」 \n{k} تعال زوجتك بتخونك')
     if not r.get(f'{m.from_user.id}:Floos'):
       floos_from_user = 0
     else:
       floos_from_user = int(r.get(f'{m.from_user.id}:Floos'))
     floos = int(re.findall('[0-9]+', text)[0])
     if floos > floos_from_user:
       return m.reply('مطفر فلوسك ماتكفي')
     else:
       if r.get(f'{m.reply_to_message.from_user.id}:marriedWomen:{m.chat.id}{hmshelp}'):
         return m.reply('「 {} 」 \n{} مو سنقل دورلك غيرها\n༄'.format(m.reply_to_message.from_user.mention,k))
       if r.get(f'{m.reply_to_message.from_user.id}:marriedMan:{m.chat.id}{hmshelp}'):
         return m.reply('「 {} 」 \n{} مو سنقل دورلك غيره\n༄'.format(m.reply_to_message.from_user.mention,k))
       else:
         if floos < 50000:
           return m.reply('لازم المهر اقل شي 50 ألف ريال')
         else:
           if floos == floos_from_user:
             r.delete(f'{m.from_user.id}:Floos')
           else:
             r.set(f'{m.from_user.id}:Floos',floos_from_user-floos)
           r.set(f'{m.from_user.id}:marriedMan:{m.chat.id}{hmshelp}',m.reply_to_message.from_user.id)
           r.set(f'{m.reply_to_message.from_user.id}:marriedWomen:{m.chat.id}{hmshelp}',m.from_user.id)
           to_marry = '''
💒 وثيقة زواج

{k} 👰 العروس ↢ ( {one} )
{k} 🤵 العريس ↢ ( {two} )
'''
           to_marry += f'\n{k} 💸 المهر ↢ ( `{floos}` ريال )\n༄'
           r.set(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{hmshelp}',to_marry)
           r.set(f'{m.reply_to_message.from_user.id}:MARRYTEXT:{m.chat.id}{hmshelp}',to_marry)
           r.set(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{hmshelp}',floos)
           r.set(f'{m.reply_to_message.from_user.id}:MARRYMONEY:{m.chat.id}{hmshelp}',floos)
           r.sadd(f'{m.chat.id}:zwag:{hmshelp}', f'{m.reply_to_message.from_user.id}--{m.from_user.id}&&floos={floos}')
           return m.reply(f'''
{k} باركووو للعرسان 

{k} 👰 العروس ↢ ( {m.reply_to_message.from_user.mention} )
{k} 🤵 العريس ↢ ( {m.from_user.mention} )

{k} 💸 المهر ↢ ( `{floos}` ريال )
☆
''')
           
           
   if text == 'زواجي':
     if not r.get(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{hmshelp}'):
       return m.reply(f'{k} انت سنقل')
     else:
       if r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{hmshelp}'):
         getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{hmshelp}')))
         txt = r.get(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{hmshelp}').format(k=k,two=m.from_user.mention(m.from_user.first_name[:10]),one=getUser.mention(getUser.first_name[:10]))
         return m.reply(txt)
       if r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{hmshelp}'):
         getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{hmshelp}')))
         txt = r.get(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{hmshelp}').format(k=k,two=getUser.mention(getUser.first_name[:10]),one=m.from_user.mention(m.from_user.first_name[:10]))
         return m.reply(txt)         
   
   if text == "سورس" or text == "السورس":
    caption_text = "سورس 𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 لحماية الكروبات، ارفعه مشرف بالكروب واحميه"

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Aloush", url="https://t.me/I_e_e_l")],
        [InlineKeyboardButton("Channel Source", url="https://t.me/unuez")]
    ])

    try:
        channel_info = c.get_chat("@unuez")
        if hasattr(channel_info, 'photo') and channel_info.photo:
            return m.reply_photo(
                photo=channel_info.photo.big_file_id,
                caption=caption_text,
                reply_markup=buttons
            )
    except Exception as e:
        print(f"Error getting channel photo: {e}")

    try:
        return m.reply_photo(
            photo="https://t.me/unuez/photo",
            caption=caption_text,
            reply_markup=buttons
        )
    except Exception as e:
        print(f"Error using direct photo link: {e}")

    return m.reply(
        caption_text,
        reply_markup=buttons
    )

   if text.lower() in ["بوت", "هانكوك"]:
    try:
        photo_enabled = r.get(f'photo_status:{m.chat.id}') != 'disabled' if r.exists(f'photo_status:{m.chat.id}') else True
        
        reply_markup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Aloush ", url="t.me/I_e_e_l")
            ],
            [
                InlineKeyboardButton("Channel Source", url=f"https://t.me/unuez")
            ]
        ])
        
        if text.lower() == "بوت":
            bot_replies = [
                "ها حبيبي؟",
                "حبيبي اسمي هانكوك",
                "نعم؟",
                "تعال قولي وش تبي 😐",
                "البوت طفر منك"
            ]
            reply_text = random.choice(bot_replies)
        else:
            hms_replies = [
                "هانكوك موجوده، وش طلبك؟",
                "أحب النداء بأسمي ❤️",
                "أنا هانكوك، كيف أساعدك؟",
                "لك وش في كل شوي هانكوك",
                "هانكوك جتي"
            ]
            reply_text = random.choice(hms_replies)
        
        if photo_enabled:
            try:
                bot_user = c.get_users(botUsername)
                if hasattr(bot_user, 'photo') and bot_user.photo:
                    photo_file = c.download_media(bot_user.photo.big_file_id)
                    if photo_file:
                        return m.reply_photo(
                            photo=photo_file,
                            caption=reply_text,
                            reply_markup=reply_markup
                        )
            except Exception as photo_error:
                print(f"Failed to send photo: {photo_error}")
        
        return m.reply(
            text=reply_text,
            reply_markup=reply_markup
        )
        
    except Exception as main_error:
        print(f"Main error in bot response: {main_error}")
        # رد بديل في حالة حدوث خطأ جسيم
        return m.reply("حدث خطأ في معالجة طلبك، يرجى المحاولة لاحقاً")
   
   if text== 'طلاق' and r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{hmshelp}'):
     getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{hmshelp}')))
     floos = int(r.get(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{hmshelp}'))
     r.srem(f'{m.chat.id}:zwag:{hmshelp}', f'{getUser.id}--{m.from_user.id}&&floos={floos}')
     if not r.get(f'{getUser.id}:Floos'):
       floos_from_whife = 0
     else:
       floos_from_whife = int(r.get(f'{getUser.id}:Floos'))
     r.set(f'{getUser.id}:Floos', floos_from_whife+floos)
     r.delete(f'{m.from_user.id}:marriedMan:{m.chat.id}{hmshelp}')
     r.delete(f'{getUser.id}:marriedWomen:{m.chat.id}{hmshelp}')
     r.delete(f'{getUser.id}:MARRYTEXT:{m.chat.id}{hmshelp}')
     r.delete(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{hmshelp}')
     r.delete(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{hmshelp}')
     r.delete(f'{getUser.id}:MARRYMONEY:{m.chat.id}{hmshelp}')
     return m.reply(f'{k} طلقتك من 「 {getUser.mention} 」\n{k} ضفت ( {floos} ريال 💸 ) لفلوسها')
     
   
   if text== 'خلع' and r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{hmshelp}'):
     getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{hmshelp}')))
     floos = int(r.get(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{hmshelp}'))
     r.srem(f'{m.chat.id}:zwag:{hmshelp}', f'{m.from_user.id}--{getUser.id}&&floos={floos}')
     if not r.get(f'{getUser.id}:Floos'):
       floos_from_has = 0
     else:
       floos_from_has = int(r.get(f'{getUser.id}:Floos'))
     r.set(f'{getUser.id}:Floos', floos_from_has+floos)
     r.delete(f'{getUser.id}:marriedMan:{m.chat.id}{hmshelp}')
     r.delete(f'{m.from_user.id}:marriedWomen:{m.chat.id}{hmshelp}')
     r.delete(f'{getUser.id}:MARRYTEXT:{m.chat.id}{hmshelp}')
     r.delete(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{hmshelp}')
     r.delete(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{hmshelp}')
     r.delete(f'{getUser.id}:MARRYMONEY:{m.chat.id}{hmshelp}')
     return m.reply(f'{k} خلعتك من 「 {getUser.mention} 」\n{k} ورجعت له المهر ( {floos} ريال 💸 )')

   if text == 'كت' or text == 'تويت' or text == 'كت تويت':
      return m.reply(random.choice(cut))
   
   if text == 'جمل':
     gmla = random.choice(gomal)
     r.set(f'{m.chat.id}:game:{hmshelp}', gmla.replace(" '",""), ex=600)
     m.reply(f'الجملة ↢ ( {gmla} )\n{k} اكتبها بدون فواصل')
   
   if r.get(f'{m.chat.id}:gameEmoji:{hmshelp}'):
     if text == r.get(f'{m.chat.id}:gameEmoji:{hmshelp}'):
        ra = random.randint(1,5)
        t = r.ttl(f'{m.chat.id}:gameEmoji:{hmshelp}')
        timeo = f"{20 - int(t)}.{random.randint(1,9)}"
        r.delete(f'{m.chat.id}:gameEmoji:{hmshelp}')
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        return m.reply(f'''
صح عليك ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
⏰الوقت: {timeo} ثانية
💸فلوسك: {floos} ريال
☆
''')
   
   if r.get(f'{m.chat.id}:game5tm:{m.from_user.id}{hmshelp}'):
    try:
     if int(text) == r.get(f'{m.chat.id}:game5tm:{m.from_user.id}{hmshelp}'):
        ra = random.randint(1,5)
        t = r.ttl(f'{m.chat.id}:game5tm:{m.from_user.id}{hmshelp}')
        timeo = f"{600 - int(t)}.{random.randint(1,9)}"
        r.delete(f'{m.chat.id}:game5tm:{m.from_user.id}{hmshelp}')
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        return m.reply(f'''
صح عليك ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
⏰الوقت: {timeo} ثانية
💸فلوسك: {floos} ريال
☆
''')
     else:
        r.delete(f'{m.chat.id}:game5tm:{m.from_user.id}{hmshelp}')
        return m.reply(f'{k} اجابتك خطأ')
    except:
     pass

   if r.get(f'{m.chat.id}:game:{hmshelp}'):
     if text == r.get(f'{m.chat.id}:game:{hmshelp}'):
        ra = random.randint(1,5)
        t = r.ttl(f'{m.chat.id}:game:{hmshelp}')
        timeo = f"{600 - int(t)}.{random.randint(1,9)}"
        r.delete(f'{m.chat.id}:game:{hmshelp}')
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        m.reply(f'''
صح عليك ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
⏰الوقت: {timeo} ثانية
💸فلوسك: {floos} ريال
☆
''')
        return True
     
   
   if text == 'ترتيب':
     name = random.choice(trteep)
     name1 = name
     name = re.sub('سحور', 'س ر و ح', name)
     name = re.sub('سياره', 'ه ر س ي ا', name)
     name = re.sub('استقبال', 'ل ب ا ت ق س ا', name)
     name = re.sub('قنافه', 'ه ق ا ن ف', name)
     name = re.sub('ايفون', 'و ن ف ا', name)
     name = re.sub('بطاطس', 'ب ط ا ط س', name)
     name = re.sub('مطبخ', 'خ ب ط م', name)
     name = re.sub('كرستيانو', 'س ت ا ن و ك ر ي', name)
     name = re.sub('دجاجه', 'ج ج ا د ه', name)
     name = re.sub('مدرسه', 'ه م د ر س', name)
     name = re.sub('الوان', 'ن ا و ا ل', name)
     name = re.sub('غرفه', 'غ ه ر ف', name)
     name = re.sub('ثلاجه', 'ج ه ت ل ا', name)
     name = re.sub('قهوه', 'ه ق ه و', name)
     name = re.sub('سفينه', 'ه ن ف ي س', name)
     name = re.sub('مصر', 'ر م ص', name)
     name = re.sub('محطه', 'ه ط م ح', name)
     name = re.sub('طياره', 'ر ا ط ي ه', name)
     name = re.sub('رادار', 'ر ا ر ا د', name)
     name = re.sub('منزل', 'ن ز م ل', name)
     name = re.sub('مستشفى', 'ى ش س ف ت م', name)
     name = re.sub('كهرباء', 'ر ب ك ه ا ء', name)
     name = re.sub('تفاحه', 'ح ه ا ت ف', name)
     name = re.sub('اخطبوط', 'ط ب و ا خ ط', name)
     name = re.sub('سنترال', 'ن ر ت ل ا س', name)
     name = re.sub('فرنسا', 'ن ف ر س ا', name)
     name = re.sub('برتقاله', 'ر ت ق ب ا ه ل', name)
     name = re.sub('تفاح', 'ح ف ا ت', name)
     name = re.sub('مطرقه', 'ه ط م ر ق', name)
     name = re.sub('هريسه', 'س ه ر ي ه', name)
     name = re.sub('لبانه', 'ب ن ل ه ا', name)
     name = re.sub('شباك', 'ب ش ا ك', name)
     name = re.sub('باص', 'ص ا ب', name)
     name = re.sub('سمكه', 'ك س م ه', name)
     name = re.sub('ذباب', 'ب ا ب ذ', name)
     name = re.sub('تلفاز', 'ت ف ل ز ا', name)
     name = re.sub('حاسوب', 'س ا ح و ب', name)
     name = re.sub('انترنت', 'ا ت ن ر ن ت', name)
     name = re.sub('ساحه', 'ح ا ه س', name)
     name = re.sub('جسر', 'ر ج س', name)
     r.set(f'{m.chat.id}:game:{hmshelp}', name1,ex=600)
     m.reply(f'رتب ↢ {name}')
     return True
   
   if text == 'ايموجي':
      if r.get(f'{m.chat.id}:gameEmoji:{hmshelp}'):
        return m.reply(f'{k} معليش في لعبة ايموجي شغالة الحين حاول بعد 20 ثانية\n\n{k} في حال ماتبي تكملها ارسل سكب')
      ran = random.choice(emojis_pics)
      emoji = ran['emoji']
      photo = ran['photo']
      a = m.reply_photo(photo,caption='اسرع واحد يرسل الايموجي')
      r.delete(f'{m.chat.id}:game:{hmshelp}')
      time.sleep(3)
      r.set(f'{m.chat.id}:gameEmoji:{hmshelp}', emoji,ex=20)
      a.edit_media(media=InputMediaPhoto (media='https://telegra.ph/file/b53b14951a50d7f75c39e.jpg', caption='ارسل الايموجي الحين'))
      return True
   
   if text == 'سكب':
      if r.get(f'{m.chat.id}:gameEmoji:{hmshelp}'):
         r.delete(f'{m.chat.id}:gameEmoji:{hmshelp}')
         m.reply(f'{k} سكبت لعبه الايموجي')
         return True
   
   if text == 'انقليزي':
     name = random.choice(english)
     name1 = name
     name = re.sub("ذئب", "wolf", name)
     name = re.sub("معلومات", "information", name)
     name = re.sub("قنوات", "channels", name)
     name = re.sub("مجموعات", "groups", name)
     name = re.sub("كتاب", "book", name)
     name = re.sub("تفاحه", "apple", name)
     name = re.sub("مصر", "egypt", name)
     name = re.sub("فلوس", "money", name)
     name = re.sub("اعلم", "i know", name)
     name = re.sub("تمساح", "crocodile", name)
     name = re.sub("مختلف", "different", name)
     name = re.sub("ذكي", "intelligent", name)
     name = re.sub("كلب", "dog", name)
     name = re.sub("صقر", "falcon", name)
     name = re.sub("مشكله", "error", name)
     name = re.sub("كمبيوتر", "computer", name)
     name = re.sub("اصدقاء", "friends", name)
     name = re.sub("منضده", "table", name)
     r.set(f'{m.chat.id}:game:{hmshelp}', name1,ex=600)
     m.reply(f'اكتب معنى ↢ ( {name} )')
     return True
   
   if text == 'معاني':
     name = random.choice(m3any)
     name1 = name
     name = re.sub("قرد", "🐒", name)
     name = re.sub("دجاجه", "🐔", name)
     name = re.sub("بطريق", "🐧", name)
     name = re.sub("ضفدع", "🐸", name)
     name = re.sub("بومه", "🦉", name)
     name = re.sub("نحله", "🐝", name)
     name = re.sub("ديك", "🐓", name)
     name = re.sub("جمل", "🐫", name)
     name = re.sub("بقره", "🐄", name)
     name = re.sub("دولفين", "🐳", name)
     name = re.sub("تمساح", "🐊", name)
     name = re.sub("قرش", "🦈", name)
     name = re.sub("نمر", "🐅", name)
     name = re.sub("اخطبوط", "🐙", name)
     name = re.sub("سمكه", "🐟", name)
     name = re.sub("خفاش", "🦇", name)
     name = re.sub("اسد", "🦁", name)
     name = re.sub("فأر", "🐭", name)
     name = re.sub("ذئب", "🐺", name)
     name = re.sub("فراشه", "🦋", name)
     name = re.sub("عقرب", "🦂", name)
     name = re.sub("زرافه", "🦒", name)
     name = re.sub("قنفذ", "🦔", name)
     name = re.sub("تفاحه", "🍎", name)
     name = re.sub("باذنجان", "🍆", name)
     name = re.sub("قوس قزح", "🌈", name)
     name = re.sub("بزازه", "🍼", name)
     name = re.sub("بطيخ", "🍉", name)
     name = re.sub("وزه", "🦆", name)
     name = re.sub("كتكوت", "🐣", name)
     r.set(f'{m.chat.id}:game:{hmshelp}', name1,ex=600)
     m.reply(f'ايش معنى الايموجي ↢ ( {name} )')
     return True
   
   if text == 'احسب':
     name = random.choice(Maths)
     name1 = name
     name = re.sub("200", "250 - 50 = ?", name)
     name = re.sub("605", "655 - 50 = ?", name)
     name = re.sub("210", "247 - 37 = ?", name)
     name = re.sub("128", "168 - 40 = ?", name)
     name = re.sub("126", "202 - 76 = ?", name)
     name = re.sub("263", "31297 ÷ 119 = ?", name)
     name = re.sub("150", "246 - 96 = ?", name)
     name = re.sub("2000", "200 × 10 = ?", name)
     name = re.sub("40", "95 - 55 = ?", name)
     name = re.sub("242", "276 - 34 = ?", name)
     name = re.sub("14", "29 - 15 = ?", name)
     name = re.sub("13", "16 - 3 = ?", name)
     name = re.sub("1000", "956 + 44 = ?", name)
     name = re.sub("810", "767 + 43 = ?", name)
     name = re.sub("110", "77 + 33 = ?", name)
     name = re.sub("830", "745 + 85 = ?", name)
     name = re.sub("111", "66 + 45 = ?", name)
     name = re.sub("92", "61 + 31 = ?", name)
     name = re.sub("1110", "988 + 122 = ?", name)
     name = re.sub("6800", "85 × 80 = ?", name)
     name = re.sub("1554", "777 × 2 = ?", name)
     name = re.sub("920", "92 × 10 = ?", name)
     name = re.sub("1740", "87 × 20 = ?", name)
     name = re.sub("1140", "76 × 15 = ?", name)
     name = re.sub("1056", "88 × 12 = ?", name)
     name = re.sub("331", "243 + 88 = ?", name)
     name = re.sub("162", "250 - 88 = ?", name)
     name = re.sub("245", "290 - 45 = ?", name)
     name = re.sub("900", "975 - 75 = ?", name)
     name = re.sub("791", "878 - 87= ?", name)
     name = re.sub("0", "99 - 99 = ?", name)
     name = re.sub("57", "77 - 20 = ?", name)
     name = re.sub("220", "250 - 30 = ?", name)
     r.set(f'{m.chat.id}:game:{hmshelp}', name1,ex=600)
     m.reply(f'{name}')
     return True
   
   if text == 'عربي':
     name = random.choice(Arab)
     name1 = name
     name = re.sub("اناث", "انثى", name)
     name = re.sub("ثيران", "ثور", name)
     name = re.sub("دروس", "درس", name)
     name = re.sub("فحص", "فحوص", name)
     name = re.sub("رجال", "رجل", name)
     name = re.sub("كتب", "كتاب", name)
     name = re.sub("ضغوط", "ضغط", name)
     name = re.sub("صف", "صفوف", name)
     name = re.sub("عصفور", "عصافير", name)
     name = re.sub("لصوص", "لص", name)
     name = re.sub("تماسيح", "تمساح", name)
     name = re.sub("ملك", "ملوك", name)
     name = re.sub("فصل", "فصول", name)
     name = re.sub("كلاب", "كلب", name)
     name = re.sub("صقور", "صقر", name)
     name = re.sub("عقد", "عقود", name)
     name = re.sub("بحور", "بحر", name)
     name = re.sub("هاتف", "هواتف", name)
     name = re.sub("حدائق", "حديقه", name)
     name = re.sub("مسرح", "مسارح", name)
     name = re.sub("جرائم", "جريمة", name)
     name = re.sub("مدارس", "مدرسة", name)
     name = re.sub("منزل", "منازل", name)
     name = re.sub("كرسي", "كراسي", name)
     name = re.sub("مناطق", "منطقة", name)
     name = re.sub("بيوت", "بيت", name)
     name = re.sub("بنك", "بنوك", name)
     name = re.sub("علم", "علوم", name)
     name = re.sub("وظائف", "وظيفة", name)
     name = re.sub("طلاب", "طالب", name)
     name = re.sub("مراحل", "مرحلة", name)
     name = re.sub("فنانين", "فنان", name)
     name = re.sub("صواريخ", "صاروخ", name)
     r.set(f'{m.chat.id}:game:{hmshelp}', name1,ex=600)
     m.reply(f'اكتب جمع او مفرد ↢ ( {name} )')
     return True
   
   if text == 'كلمات':
     name = random.choice(words)
     '''
     name1 = name
     name = re.sub("ذئب", "ذئب", name)
     name = re.sub("معلومات", "معلومات", name)
     name = re.sub("قنوات", "قنوات", name)
     name = re.sub("مجموعات", "مجموعات", name)
     name = re.sub("كتاب", "كتاب", name)
     name = re.sub("تفاحه", "تفاحه", name)
     name = re.sub("مصر", "مصر", name)
     name = re.sub("فلوس", "فلوس", name)
     name = re.sub("اعلم", "اعلم", name)
     name = re.sub("تمساح", "تمساح", name)
     name = re.sub("مختلف", "مختلف", name)
     name = re.sub("ذكي", "ذكي", name)
     name = re.sub("كلب", "كلب", name)
     name = re.sub("صقر", "صقر", name)
     name = re.sub("مشكله", "مشكله", name)
     name = re.sub("كمبيوتر", "كمبيوتر", name)
     name = re.sub("اصدقاء", "اصدقاء", name)
     name = re.sub("منضده", "منضده", name)
     name = re.sub("سائق", "سائق", name)
     name = re.sub("جبل", "جبل", name)
     name = re.sub("مفتاح", "مفتاح", name)
     name = re.sub("يساوي", "يساوي", name)
     name = re.sub("انتبه", "انتبه", name)
     name = re.sub("موقد", "موقد", name)
     name = re.sub("مكتئب", "مكتئب", name)
     name = re.sub("انسان", "انسان", name)
     name = re.sub("ضفدع", "ضفدع", name)
     name = re.sub("عشق", "عشق", name)
     name = re.sub("منزل", "منزل", name)
     name = re.sub("طلاب", "طلاب", name)
     name = re.sub("فنان", "فنان", name)
     name = re.sub("صاروخ", "صاروخ", name)
     '''
     r.set(f'{m.chat.id}:game:{hmshelp}', name,ex=600)
     m.reply(f'الكلمة ↢ ( {name} )')
     return True

   if text == 'تفكيك':
     tfkeek = random.choice(trteep)
     name = ' '.join(a for a in tfkeek)
     r.set(f'{m.chat.id}:game:{hmshelp}', name,ex=600)
     m.reply(f'فكك ↢ ( {tfkeek} )')
     return True
   
   
   if text == 'عواصم':
     country=random.choice(countries)
     name = country['name']
     capital=country['capital']
     r.set(f'{m.chat.id}:game:{hmshelp}', capital,ex=600)
     m.reply(f'{k} ايش عاصمة {name} ؟')
     return True
   
   if text == 'اكمل':
     name = random.choice(mthal)
     name1 = name
     name = re.sub("اخوات", "لو قلبك مات متجيش على اتنين ... ", name)
     name = re.sub("زيهم", "اى ياعمهم اشتكيلك منهم تعمل ... ", name)
     name = re.sub("شمعتك", "دارى على ... تقيد", name)
     name = re.sub("داره", "من خرج من ... قل مقداره", name)
     name = re.sub("الوالدين", "رضا ... احسن من ابوك وامك", name)
     name = re.sub("الرءوس", "اذا تطاول الايدي تساوت ... ", name)
     name = re.sub("مرايه", "فى الوش ... وفى القفه سلايه", name)
     name = re.sub("حدو", "الشئ اللى يزيد عن ...  ينقلب لضدو", name)
     name = re.sub("رجالها", "مايجبها الا  ... ", name)
     name = re.sub("عدوك", "امشى عدل يحتار ... فيك", name)
     name = re.sub("الزبيب", "ضرب الحبيب زى اكل  ... ", name)
     name = re.sub("الغراب", "ياما جاب ...  لامه", name)
     name = re.sub("ماتو", "اللى اغتشو ... ", name)
     name = re.sub("اتمكن", "اتمسكن لحد ما ... ", name)
     name = re.sub("زجاج", "اللى بيتو من ... مايحدفش الناس بالطوب", name)
     name = re.sub("فار", "لو غاب القط العب يا ... ", name)
     name = re.sub("شهر", "امشي ... ولا تعدى نهر", name)
     name = re.sub("القتيل", "يقتل ... ويمشى فى جنازته", name)
     name = re.sub("الغطاس", "المايه تكدب ... ", name)
     name = re.sub("يكحلها", "جه ... عماها", name)
     name = re.sub("امه", "القرد فى عين ... غزال", name)
     r.set(f'{m.chat.id}:game:{hmshelp}', name1 ,ex=600)
     m.reply(f'اكمل ↢ ( {name} ؟ )')
     return True
   
   if text == 'احكام':
     if r.get(f'{m.chat.id}:AHKAMGAME:{hmshelp}'):
       return m.reply(f"{k} معليش في لعبة احكام شغالة الحين حاول بعد دقيقة")
     m.reply(f'''
{k} بدينا لعبة احكام واضفت اسمك 
{k} اللي يبي يلعب يرسل كلمة ( انا ) 

{k} اللي عليك انت صاحب اللعبة ترسل ( تم ) اذا اكتمل العدد
☆
''')
     r.delete(f'{m.chat.id}:ListAhkam:{hmshelp}')
     r.set(f'{m.chat.id}:AHKAMGAME:{hmshelp}',m.from_user.id,ex=120)
     r.sadd(f'{m.chat.id}:ListAhkam:{hmshelp}',m.from_user.id)
     return True
     
   if text == 'انا' and r.get(f'{m.chat.id}:AHKAMGAME:{hmshelp}'):
     if r.sismember(f'{m.chat.id}:ListAhkam:{hmshelp}',m.from_user.id):
       return m.reply(f"{k} اسمك موجود بالقائمة")
     else:
       m.reply(f"{k} ضفت اسمك للقائمة")
       r.sadd(f'{m.chat.id}:ListAhkam:{hmshelp}',m.from_user.id)
       return True
  
   if text == 'تم' and r.get(f'{m.chat.id}:AHKAMGAME:{hmshelp}') and m.from_user.id == int(r.get(f'{m.chat.id}:AHKAMGAME:{hmshelp}')):
     if len(r.smembers(f'{m.chat.id}:ListAhkam:{hmshelp}')) == 1:
       return m.reply(f"{k} مافيه لاعبين")
     else:
       ids = [elem for elem in r.smembers(f'{m.chat.id}:ListAhkam:{hmshelp}')]
       id = random.choice(ids)
       getUser = c.get_users(int(id))
       m.reply(f"{k} تم اختيار ( ⁪⁬⁪⁬{getUser.mention} ) للحكم عليه")
       r.delete(f'{m.chat.id}:ListAhkam:{hmshelp}')
       r.delete(f'{m.chat.id}:AHKAMGAME:{hmshelp}')
       return True
   
   
   if text == 'روليت':
     if r.get(f'{m.chat.id}:ROLETGAME:{hmshelp}'):
       return m.reply(f"{k} معليش في لعبة روليت شغالة الحين حاول بعد دقيقة")
     m.reply(f'''
{k} بدينا لعبة الروليت واضفت اسمك 
{k} اللي يبي يلعب يرسل كلمة ( انا ) 

{k} اللي عليك انت صاحب اللعبة ترسل ( تم ) اذا اكتمل العدد
☆
''')
     r.delete(f'{m.chat.id}:ListRolet:{hmshelp}')
     r.set(f'{m.chat.id}:ROLETGAME:{hmshelp}',m.from_user.id,ex=120)
     r.sadd(f'{m.chat.id}:ListRolet:{hmshelp}',m.from_user.id)
     return True
     
   if text == 'انا' and r.get(f'{m.chat.id}:ROLETGAME:{hmshelp}'):
     if r.sismember(f'{m.chat.id}:ListRolet:{hmshelp}',m.from_user.id):
       return m.reply(f"{k} اسمك موجود بالقائمة")
     else:
       m.reply(f"{k} ضفت اسمك للقائمة")
       r.sadd(f'{m.chat.id}:ListRolet:{hmshelp}',m.from_user.id)
       return True
  
   if text == 'تم' and r.get(f'{m.chat.id}:ROLETGAME:{hmshelp}') and m.from_user.id == int(r.get(f'{m.chat.id}:ROLETGAME:{hmshelp}')):
     if len(r.smembers(f'{m.chat.id}:ListRolet:{hmshelp}')) == 1:
       return m.reply(f"{k} مافيه لاعبين")
     else:
       ids = [elem for elem in r.smembers(f'{m.chat.id}:ListRolet:{hmshelp}')]
       id = random.choice(ids)
       getUser = c.get_users(int(id))
       m.reply(f"{k} مبروك اخترت اللاعب ( {getUser.mention} ) واخذ 3 مجوهرات")
       if not r.get(f'{getUser.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{getUser.id}:Floos'))
       r.set(f"{getUser.id}:Floos",floos+10)
       r.delete(f'{m.chat.id}:ListRolet:{hmshelp}')
       r.delete(f'{m.chat.id}:ROLETGAME:{hmshelp}')
       return True
       
  
   if text == 'خواتم':
     name = random.randint(1,6)
     r.set(f'{m.chat.id}:game5tm:{m.from_user.id}{hmshelp}', name ,ex=600)
     r.delete(f'{m.chat.id}:game:{hmshelp}')
     return m.reply('''
１    ２      ３     ４    ５     ６
  ↓     ↓      ↓     ↓     ↓     ↓
  ✋🏼 ‹› ✋🏼 ‹› ✋🏼 ‹› ✋🏼 ‹› ✋🏼 ‹› ✋🏼
  
  
⚘ اختار اليد اللي تتوقع فيها الخاتم
     ''')
   
   if text == 'اعلام':
     country=random.choice(countries_)
     name = country['name']
     flag=country['flag']
     r.set(f'{m.chat.id}:game:{hmshelp}', name,ex=600)
     m.reply_photo(flag, caption='ايش اسم الدولة ؟')
     return True
   
   if text == 'دين':
     dee = random.choice(deen)
     question = dee['question']
     answer = dee['answer']
     r.set(f'{m.chat.id}:game:{hmshelp}', answer ,ex=600)
     m.reply(question)
     return True
   
   if text == 'سيارات':
     car = random.choice(cars)
     brand = car["brand"]
     r.set(f'{m.chat.id}:game:{hmshelp}', brand ,ex=600)
     m.reply_photo(car['photo'], caption='وش اسم السيارة ؟')
     return True
   
   if text == 'ارقام':
     num = ''
     for a in range(random.randint(5,15)):
       num += str(random.randint(1,9))
     r.set(f'{m.chat.id}:game:{hmshelp}', num ,ex=600)
     m.reply(f'الرقم ↢ ( {num} )', protect_content=True)
     return True
     
   if text == 'انمي':
     anim = random.choice(anime)
     r.set(f'{m.chat.id}:game:{hmshelp}', anim['anime'] ,ex=600)
     m.reply_photo(anim['photo'], caption='ايش اسم شخصية الانمي ؟')
     return True
   
   if text == 'صور':
     ph = random.choice(pics)
     r.set(f'{m.chat.id}:game:{hmshelp}', ph['answer'] ,ex=600)
     if not ph['caption']:
       caption = 'وش الي فالصورة؟'
     else:
       caption = ph['caption']
     m.reply_photo(ph['photo'], caption=caption)
     return True
   
   if text == 'كرة قدم' or text == 'كره قدم':
     ph = random.choice(football)
     r.set(f'{m.chat.id}:game:{hmshelp}', ph['answer'] ,ex=600)
     if not ph['caption']:
       caption = 'وش اسم الاعب ؟'
     else:
       caption = ph['caption']
     m.reply_photo(ph['photo'], caption=caption)
     return True
   
   if text == 'تشفير':
     ph = random.choice(tashfeer)
     r.set(f'{m.chat.id}:game:{hmshelp}', ph['answer'] ,ex=600)
     if not ph['caption']:
       caption = 'فك التشفير ؟'
     else:
       caption = ph['caption']
     m.reply_photo(ph['photo'], caption=caption)
     return True
   
   if text == 'تركيب':
     name = random.choice(tarkeeb)
     name1 = name
     name = re.sub("اناث", "ا ن ا ث", name)
     name = re.sub("ثيران", "ث ي ر ا ن", name)
     name = re.sub("دروس", "د ر و س", name)
     name = re.sub("فحص", "ف ح ص", name)
     name = re.sub("رجال", "ر ج ا ل", name)
     name = re.sub("انستا", "ا ن س ت ا", name)
     name = re.sub("ضغوط", "ض غ و ط", name)
     name = re.sub("صف", "ص ف", name)
     name = re.sub("رجب", "ر ج ب", name)
     name = re.sub("اسد", "ا س د", name)
     name = re.sub("وقع", "و ق ع", name)
     name = re.sub("ملك", "م ل ك", name)
     name = re.sub("فصل", "ف ص ل", name)
     name = re.sub("كلاب", "ك ل ا ب", name)
     name = re.sub("صقور", "ص ق و ر", name)
     name = re.sub("عقد", "ع ق د", name)
     name = re.sub("بحور", "ب ح و ر", name)
     name = re.sub("هاتف", "ه ا ت ف", name)
     name = re.sub("حدائق", "ح د ا ئ ق", name)
     name = re.sub("مسرح", "م س ر ح", name)
     name = re.sub("جرائم", "ج ر ا ئ م", name)
     name = re.sub("مدارس", "م د ا ر س", name)
     name = re.sub("منزل", "م ن ز ل", name)
     name = re.sub("كرسي", "ك ر س ي", name)
     name = re.sub("مناطق", "م ن ا ط ق", name)
     name = re.sub("بيوت", "ب ي و ت", name)
     name = re.sub("بنك", "ب ن ك", name)
     name = re.sub("علم", "ع ل م", name)
     name = re.sub("وظائف", "و ظ ا ئ ف", name)
     name = re.sub("طلاب", "ط ل ا ب", name)
     name = re.sub("مراحل", "م ر ا ح ل", name)
     name = re.sub("فنانين", "ف ن ا ن ي ن", name)
     name = re.sub("صواريخ", "ص و ا ر ي خ", name)
     r.set(f'{m.chat.id}:game:{hmshelp}', name1,ex=600)
     m.reply(f'ركب ↢ ( {name} )')
   
   if text == "سكب ديمون":
    if m.from_user.id in users_demon:
        del users_demon[m.from_user.id]
        return m.reply("⇜ ابشر الغيت اللعبة")
    else:
        return m.reply("⇜ مافيه لعبة ديمون شغالة")
        
    if text == "تفعيل الذكاء الاصطناعي":
     if dev_pls(m.from_user.id, m.chat.id):
         r.set(f'{hmshelp}:ai_enabled', True)
         AI_ENABLED = True
         return m.reply("⇜ تم تفعيل الذكاء الاصطناعي")
     else:
         return m.reply("⇜ هذا الأمر يخص المطور فقط")

    if text == "تعطيل الذكاء الاصطناعي":
     if dev_pls(m.from_user.id, m.chat.id):
         r.set(f'{hmshelp}:ai_enabled', False)
         AI_ENABLED = False
         return m.reply("⇜ تم تعطيل الذكاء الاصطناعي")
     else:
         return m.reply("⇜ هذا الأمر يخص المطور فقط")
        
   if text == 'حجره' or text == 'حجرة':
     return m.reply('- اختار حجره / ورقة / مقص',reply_markup=InlineKeyboardMarkup (
     [
     [
       InlineKeyboardButton ('🪨', callback_data=f'RPS:rock++{m.from_user.id}'),
       InlineKeyboardButton ('📃', callback_data=f'RPS:paper++{m.from_user.id}'),
       InlineKeyboardButton ('✂️', callback_data=f'RPS:scissors++{m.from_user.id}'),
     ]
     ]
     ))
   
   if text == 'نرد':
     dice = c.send_dice(m.chat.id,"🎲",reply_to_message_id=m.id,
     reply_markup=InlineKeyboardMarkup (
       [[
         InlineKeyboardButton ("𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹",url=f"t.me/{channel}")
       ]]
     ))
     if dice.dice.value == 6:
        ra = 10
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        return m.reply(f'''
صح عليك فزت **[بالنرد]({dice.link})** ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
💸فلوسك: `{floos}` ريال
☆
''', disable_web_page_preview=True)
     else:
        return m.reply(f"{k} للأسف خسرت بالنرد")
       
   
   if text == 'ديمون':
     if m.from_user.id in users_demon:
        return m.reply("⇜ في لعبة ديمون شغالة استخدم امر <code>سكب ديمون</code>")
     else:
        return m.reply(f'''بوو 👻
انا ديمون 🧛🏻‍♀️ اقدر اعرف مين الشخصية الي فبالك !

- فكر بشخص واضغط بدء وجاوب على اسئلتي''',
     reply_markup=InlineKeyboardMarkup (
       [
       [
        InlineKeyboardButton ('بدء 🧛🏻‍♀️',callback_data=f'start_aki:{m.from_user.id}')
       ]
       ]
     ))


@Client.on_callback_query(filters.regex('aki'))
def akinatorHandler(c,m):
   channel = r.get(f'{hmshelp}:BotChannel') if r.get(f'{hmshelp}:BotChannel') else 'alwzaraa2'
   if m.data == f'start_aki:{m.from_user.id}':
    rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', url=f't.me/{channel}')]]
       )
    m.edit_message_text("⇜ جاري بدء اللعبة...",reply_markup=rep)
    aki= akinator.Akinator()
    q = aki.start_game(language="ar")
    users_demon.update({m.from_user.id:[aki,q]})
    return m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))
   if m.data == f'aki_c:n++{m.from_user.id}':
    users_demon[m.from_user.id][1] = users_demon[m.from_user.id][0].answer("n")
    if users_demon[m.from_user.id][0].progression >= 65:
        users_demon[m.from_user.id][0].win()
        str_to_send = users_demon[m.from_user.id][0].first_guess
        print(str_to_send)
        m.message.delete()
        rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', url=f't.me/{channel}')]]
         )
        try: c.send_photo(m.message.chat.id,str_to_send['absolute_picture_path'],caption=f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        except: c.send_message(m.message.chat.id,f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        del users_demon[m.from_user.id]
    else:
        return m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))
   if m.data == f'aki_c:y++{m.from_user.id}':
    users_demon[m.from_user.id][1] = users_demon[m.from_user.id][0].answer("y")
    if users_demon[m.from_user.id][0].progression >= 65:
        users_demon[m.from_user.id][0].win()
        str_to_send = users_demon[m.from_user.id][0].first_guess
        print(str_to_send)
        m.message.delete()
        rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', url=f't.me/{channel}')]]
         )
        try: c.send_photo(m.message.chat.id,str_to_send['absolute_picture_path'],caption=f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        except: c.send_message(m.message.chat.id,f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        del users_demon[m.from_user.id]
    else:
        return m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))
   if m.data == f'aki_c:p++{m.from_user.id}':
    users_demon[m.from_user.id][1] = users_demon[m.from_user.id][0].answer("p")
    if users_demon[m.from_user.id][0].progression >= 65:
        users_demon[m.from_user.id][0].win()
        str_to_send = users_demon[m.from_user.id][0].first_guess
        print(str_to_send)
        m.message.delete()
        rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('𝗦𝗰𝗼𝗥 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', url=f't.me/{channel}')]]
         )
        try: c.send_photo(m.message.chat.id,str_to_send['absolute_picture_path'],caption=f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        except: c.send_message(m.message.chat.id,f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        del users_demon[m.from_user.id]
    else:
        return m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))


@Client.on_callback_query(filters.regex('^create_bank_'))
async def handle_bank_selection(c, query):
    bank_type = query.data.split('_')[2]
    m = query.message
    user_id = query.from_user.id
    
    if r.sismember('BankList', user_id):
        bank = r.get(f'{user_id}:bankType')
        acc_id = int(r.get(f'{user_id}:bankID'))
        await query.answer(f'لديك حساب بالفعل في بنك {bank}', show_alert=True)
        return
    
    id = random.randint(1111111, 9999999)
    card = random.choice(['الاهلي كارد','الراجحي كارد','الإنماء كارد','مدى كارد'])
    floos = 1000
    floos_to_add = random.randint(500, 5000)
    
    r.set(f'{user_id}:bankType', bank_type)
    r.set(f'{user_id}:bankID', int(id))
    r.set(f'{user_id}:bankCard', card)
    r.sadd('BankList', user_id)
    r.set(f'{id}:getAccBank', user_id)
    fff = floos + floos_to_add
    r.set(f'{user_id}:Floos', fff)
    r.set(f'{user_id}:bankName', query.from_user.first_name)
    
    await query.message.edit_text(
        f'• وسوينا لك حساب في بنك {bank_type}\n\n'
        f'⌯ رقم حسابك ↢ ( `{id}` )\n'
        f'⌯ نوع البطاقة ↢ ( {card} )\n'
        f'⌯ فلوسك ↢ ( {fff} ريال 💸 )'
    )
    
    if r.get(f'DevGroup:{hmshelp}'):
        await c.send_message(
            int(r.get(f'DevGroup:{hmshelp}')),
            f' ⟨ {query.from_user.mention()} ⟩\n'
            f'{k} سوى حساب بالبنك\n'
            f'{k} رقم حسابه ( `{id}` )'
        )
    
    await query.answer(f'تم إنشاء حساب في بنك {bank_type}')

@Client.on_callback_query(filters.regex(r'^rate_(like|dislike)_(\d+)$'))
async def handle_rating(c, query):
    try:
        action = query.data.split('_')[1]
        target_id = int(query.data.split('_')[2])
        voter_id = query.from_user.id
        
        if voter_id == target_id:
            await query.answer("لا يمكنك تقييم نفسك", show_alert=True)
            return
        
        vote_key = f"user:{target_id}:voter:{voter_id}"
        if r.get(vote_key):
            await query.answer("لقد قمت بالتقييم مسبقاً", show_alert=True)
            return
        
        rate_key = f"user:{target_id}:{action}s"
        r.incr(rate_key)
        r.set(vote_key, "1", ex=604800)
        
        likes = int(r.get(f"user:{target_id}:likes") or 0)
        dislikes = int(r.get(f"user:{target_id}:dislikes") or 0)
        
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(f"🤍 {likes}", callback_data=f"rate_like_{target_id}"),
                InlineKeyboardButton(f"👎 {dislikes}", callback_data=f"rate_dislike_{target_id}")
            ]
        ])
        
        await query.message.edit_reply_markup(reply_markup=keyboard)
        await query.answer("تم تسجيل تقييمك بنجاح ✅")
        
    except Exception as e:
        print(f"Error in rating system: {e}")
        await query.answer("حدث خطأ أثناء التقييم", show_alert=True)

@Client.on_callback_query(filters.regex(r'^buy_rate:(\d+):(\d+)$'))
async def process_rating_purchase(c, query):
    user_id = query.from_user.id
    _, count, price = query.data.split(':')
    count, price = int(count), int(price)

    if not r.sismember('BankList', user_id):
        return await query.answer("الحساب البنكي غير موجود", show_alert=True)

    current_balance = int(r.get(f'{user_id}:Floos') or 0)
    
    if current_balance < price:
        return await query.answer(f"رصيدك غير كافي المبلغ المطلوب : {price} ريال", show_alert=True)

    try:
        new_balance = current_balance - price
        r.set(f'{user_id}:Floos', new_balance)
        
        current_ratings = int(r.get(f'user:{user_id}:likes') or 0)
        r.set(f'user:{user_id}:likes', current_ratings + count)
        
        await query.message.edit_text(
            f" **تمت عملية الشراء**\n\n"
            f"• عدد التقييمات : {count}\n\n"
            f"• المبلغ المخصوم : {price} ريال\n"
            f"• الرصيد الجديد: {new_balance} ريال\n\n"
            f"يمكنك رؤية التقييمات الجديدة بأمر `تقييم`"
        )
        
    except Exception as e:
        print(f"خطأ في عملية الشراء: {e}")
        await query.answer("حدث خطأ أثناء المعالجة", show_alert=True)

@Client.on_callback_query(filters.regex('^cancel_rate_purchase$'))
async def cancel_purchase(c, query):
    await query.message.edit_text("تم إلغاء عملية الشراء")

@Client.on_callback_query(filters.regex(r'^settings_toggle_(.*)$'))
async def handle_settings_toggle(c, query):
    try:
        setting_key = query.data.split('_')[2]
        chat_id = query.message.chat.id
        user_id = query.from_user.id
        
        if not mod_pls(user_id, chat_id):
            await query.answer("❌ ليس لديك صلاحية!", show_alert=True)
            return
        
        current = r.get(f"{chat_id}:{setting_key}:{hmshelp}")
        new_status = not current
        
        if new_status:
            r.set(f"{chat_id}:{setting_key}:{hmshelp}", "on")
        else:
            r.delete(f"{chat_id}:{setting_key}:{hmshelp}")
        
        # تحديث الزر مباشرة
        for row in query.message.reply_markup.inline_keyboard:
            for btn in row:
                if btn.callback_data == query.data:
                    btn.text = btn.text.replace("🔴", "🟢") if current else btn.text.replace("🟢", "🔴")
                    break
        
        await query.message.edit_reply_markup(
            reply_markup=query.message.reply_markup
        )
        await query.answer(f"تم {'قفل' if new_status else 'فتح'} الإعداد")
        
    except Exception as e:
        print(f"Error in toggle: {e}")
        await query.answer("❌ حدث خطأ!", show_alert=True)

@Client.on_callback_query(filters.regex('^settings_close$'))
async def handle_settings_close(c, query):
    try:
        await query.message.delete()
    except:
        await query.answer("❌ لا يمكن حذف الرسالة!", show_alert=True)

def get_emoji_bank(count):
  if count == 1:
     return '🥇 ) '
  if count == 2:
     return '🥈 ) '
  if count == 3:
     return '🥉 ) '
  else:
     return f' {count}  ) '
     
     