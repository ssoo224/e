import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from pyrogram.errors import *
from config import *
from helpers.Ranks import *
from helpers.Ranks import isLockCommand
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.text & filters.group, group=14)
def mutesHandler(c,m):
    k = r.get(f'{hmshelp}:botkey')
    Thread(target=mute_func,args=(c,m,k)).start()
    
def mute_func(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{hmshelp}'):  return
   if r.get(f'{m.chat.id}:mute:{hmshelp}') and not admin_pls(m.from_user.id,m.chat.id):  return 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}'):  return 
   if r.get(f'{m.from_user.id}:mute:{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{hmshelp}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{hmshelp}'):  return 
   text = m.text
   name = r.get(f'{hmshelp}:BotName') if r.get(f'{hmshelp}:BotName') else 'هانكوك'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}')
   if r.get(f'Custom:{hmshelp}&text={text}'):
       text = r.get(f'Custom:{hmshelp}&text={text}')
   
   if isLockCommand(m.from_user.id, m.chat.id, text): return

   if text == 'كتم' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if not mod_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        if id == m.from_user.id:
           return m.reply('شفيك تبي تنزل نفسك')
        if pre_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مكتوم من قبل\n☆')
        else:
          r.set(f'{id}:mute:{m.chat.id}{hmshelp}', 1)
          r.sadd(f'{m.chat.id}:listMUTE:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} كتمته\n☆')
   
   if re.match("^كتم عام (.*?)$", text) and len(text.split()) ==  3:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المطور وفوق ) بس')      
      user = text.split()[2]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         return m.reply(f'{k} مافيه يوزر كذا')
      if dev_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
      if r.get(f'{id}:mute:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مكتوم عام من قبل\n☆')
      else:
          r.set(f'{id}:mute:{hmshelp}', 1)
          r.sadd(f'listMUTE:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} كتمته عام\n☆')

   if re.match("^تحذير (.*)?$", text) or (text == 'تحذير' and m.reply_to_message):
       if not mod_pls(m.from_user.id, m.chat.id):
           return m.reply(f"{k} هذا الأمر يخص (المدير وفوق) فقط")

       if m.reply_to_message:
           warned_user = m.reply_to_message.from_user
       else:
           parts = text.split()
           if len(parts) < 2:
               return m.reply("حدد المستخدم بالرد أو بيوزر/آيدي")
           identifier = parts[1]
           try:
               warned_user = c.get_chat(identifier)
           except:
               return m.reply("لم أتمكن من العثور على المستخدم")

       user_id = warned_user.id
       mention = f"[{warned_user.first_name}](tg://user?id={user_id})"

       if mod_pls(user_id, m.chat.id):
           rank = get_rank(user_id, m.chat.id)
           return m.reply(f"{k} لا يمكن تحذير {rank}.")

       key_warn = f"{m.chat.id}:{user_id}:warns:{hmshelp}"
       warns = int(r.get(key_warn) or 0) + 1
       r.set(key_warn, warns)

       if warns >= 3:
           if not mod_pls(user_id, m.chat.id):
               r.set(f'{user_id}:mute:{m.chat.id}{hmshelp}', 1)
               r.sadd(f'{m.chat.id}:listMUTE:{hmshelp}', user_id)
               keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("إلغاء الكتم", callback_data=f'unmute_{user_id}')]])
               return m.reply(
                   f"{mention}\n{k} تم كتمه بسبب تراكم 3 تحذيرات",
                   reply_markup=keyboard
               )

       keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("مسح التحذيرات", callback_data=f'clear_warns_{user_id}')]])
       return m.reply(
           f"⚠️ {mention}\n{k} تم تحذيره\nعدد التحذيرات: {warns}/3",
           reply_markup=keyboard
       )

   if re.match("^كتم (.*?)$", text) and len(text.split()) == 2:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not admin_pls(m.from_user.id,m.chat.id):
         return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
      user = text.split()[1]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         return m.reply(f'{k} مافيه يوزر كذا')
      if id == m.from_user.id:
        return m.reply('شفيك تبي تنزل نفسك')
      if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
         return m.reply(f'「 {mention} 」\n{k} مكتوم من قبل\n☆')
      if pre_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
      r.set(f'{id}:mute:{m.chat.id}{hmshelp}', 1)
      r.sadd(f'{m.chat.id}:listMUTE:{hmshelp}', id)
      return m.reply(f'「 {mention} 」\n{k} كتمته\n☆')
   
   if text == 'الغاء الكتم' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if not admin_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
        if not r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مكتوم قبل\n☆')
        else:
          r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
          r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} ابشر الغيت كتمه\n༄')
   
   if re.match("^مسح تحذيرات (.*)?$", text) or (text == 'مسح تحذيرات' and m.reply_to_message):
      if not mod_pls(m.from_user.id, m.chat.id):
          return m.reply(f"{k} هذا الأمر يخص (المدير وفوق) فقط")

      if m.reply_to_message:
          target_user = m.reply_to_message.from_user
      else:
          parts = text.split()
          if len(parts) < 2:
              return m.reply("حدد المستخدم بالرد أو بيوزر/آيدي")
          try:
              target_user = c.get_chat(parts[1])
          except:
              return m.reply("لم أتمكن من العثور على المستخدم")

      r.delete(f"{m.chat.id}:{target_user.id}:warns:{hmshelp}")
      return m.reply(f"✅ تم مسح تحذيرات {target_user.mention}")
   
   if re.match("^الغاء الكتم العام (.*?)$", text) and len(text.split()) ==  4:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( المطور الثانوي وفوق ) بس')
      user = text.split()[3]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f"{k} مافيه مستخدم كذا")
         mention = f'[{id}](tg://user?id={id})'
      if not r.get(f'{id}:mute:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مكتوم عام من قبل\n☆')
      else:
          r.delete(f'{id}:mute:{hmshelp}')
          r.srem(f'listMUTE:{hmshelp}',id)
          return m.reply(f'「 {mention} 」\n{k} لغيت كتمته عام\n☆')

   if re.match("^الغاء الكتم (.*?)$", text) and len(text.split()) ==  3:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not mod_pls(m.from_user.id,m.chat.id):
         return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
      user = text.split()[2]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f"{k} مافيه مستخدم كذا")
         mention = f'[{id}](tg://user?id={id})'
      if not r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
         return m.reply(f'「 {mention} 」\n{k} مو مكتوم من قبل\n☆')
      r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
      r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
      return m.reply(f'「 {mention} 」\n{k} أبشر الغيت كتمه\n☆')
   
   if re.match("^حظر عام (.*?)$", text) and len(text.split()) ==  3:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المطور وفوق ) بس')      
      user = text.split()[2]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         return m.reply(f'{k} مافيه يوزر كذا')
      if dev_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'{k} هييه مايمديك تحظر {rank} يورع!')
      if r.get(f'{id}:gban:{hmshelp}'):
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} محظور عام من قبل\n☆')
      else:
          r.set(f'{id}:gban:{hmshelp}', 1)
          r.sadd(f'listGBAN:{hmshelp}', id)
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} حظرته عام\n☆')
   
   if re.match("^حظر عام من الالعاب (.*?)$", text) and len(text.split()) ==  5:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( المطور الثانوي وفوق ) بس')
      user = text.split()[4]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         return m.reply(f'{k} مافيه يوزر كذا')
      if dev_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'{k} هييه مايمديك تحظر {rank} يورع!')
      if r.get(f'{id}:gbangames:{hmshelp}'):
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} محظور من الالعاب من قبل\n☆')
      else:
          r.set(f'{id}:gbangames:{hmshelp}', 1)
          r.sadd(f'listGBANGAMES:{hmshelp}', id)
          r.delete(f'{id}:Floos')
          r.srem("BankList",id)
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} حظرته عام من الالعاب\n☆')
   
   if re.match("^الغاء الحظر العام من الالعاب (.*?)$", text) and len(text.split()) ==  6:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( المطور الثانوي وفوق ) بس')
      user = text.split()[5]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f"{k} مافيه مستخدم كذا")
         mention = f'[{id}](tg://user?id={id})'
      if not r.get(f'{id}:gbangames:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو محظور من الالعاب من قبل\n☆')
      else:
          r.delete(f'{id}:gbangames:{hmshelp}')
          r.srem(f'listGBANGAMES:{hmshelp}',id)
          return m.reply(f'「 {mention} 」\n{k} لغيت حظره من الالعاب عام\n☆')

   if re.match("^الغاء الحظر العام (.*?)$", text) and len(text.split()) ==  4:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( المطور الثانوي وفوق ) بس')
      user = text.split()[3]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f"{k} مافيه مستخدم كذا")
         mention = f'[{id}](tg://user?id={id})'
      if not r.get(f'{id}:gban:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو محظور عام من قبل\n☆')
      else:
          r.delete(f'{id}:gban:{hmshelp}')
          r.srem(f'listGBAN:{hmshelp}',id)
          return m.reply(f'「 {mention} 」\n{k} لغيت حظره عام\n☆')

@Client.on_message(filters.group, group=15)
def muteResponse(c,m):
    del_formutes(c,m)
    
def del_formutes(c,m):
   if r.get(f'{m.from_user.id}:gban:{hmshelp}'):
     try:
        m.chat.ban_member(m.from_user.id)
     except:
        m.delete()
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}') or r.get(f'{m.from_user.id}:mute:{hmshelp}'):
     try:
       m.delete()
     except FloodWait as x:
       time.sleep(x.value)
     except Exception:
       pass

@Client.on_message(filters.text & filters.group, group=16)
def mutesHandlerG(c,m):
    k = r.get(f'{hmshelp}:botkey')
    Thread(target=mute_funcg,args=(c,m,k)).start()
    
    
def mute_funcg(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{hmshelp}'):  return
   if r.get(f'{m.chat.id}:mute:{hmshelp}') and not admin_pls(m.from_user.id,m.chat.id):  return 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}'):  return 
   if r.get(f'{m.from_user.id}:mute:{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{hmshelp}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{hmshelp}'):  return 
   text = m.text
   name = r.get(f'{hmshelp}:BotName') if r.get(f'{hmshelp}:BotName') else 'هانكوك'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}')
   if r.get(f'Custom:{hmshelp}&text={text}'):
       text = r.get(f'Custom:{hmshelp}&text={text}')
       
   if text == 'كتم عام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الأمر يخص ( المطور الثانوي وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if r.get(f'{id}:mute:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مكتوم عام من قبل\n☆')
        else:
          r.set(f'{id}:mute:{hmshelp}', 1)
          r.sadd(f'listMUTE:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} كتمته عام\n☆')
      
   if text == 'حظر عام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الأمر يخص ( المطور الثانوي وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تحظر {rank} يورع')
        if r.get(f'{id}:gban:{hmshelp}'):
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} محظور عام من قبل\n☆')
        else:
          r.set(f'{id}:gban:{hmshelp}', 1)
          r.sadd(f'listGBAN:{hmshelp}', id)
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} حظرته عام\n☆')
   
   if text == 'حظر عام من الالعاب' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المطور وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تحظر {rank} يورع!')
        if r.get(f'{id}:gbangames:{hmshelp}'):
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} محظور من الالعاب من قبل\n☆')
        else:
          r.set(f'{id}:gbangames:{hmshelp}', 1)
          r.sadd(f'listGBANGAMES:{hmshelp}', id)
          r.delete(f'{id}:Floos')
          r.srem("BankList",id)
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} حظرته عام من الالعاب\n☆')

   if text == 'الغاء الكتم العام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المطور وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if not r.get(f'{id}:mute:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مكتوم عام من قبل\n☆')
        else:
          r.delete(f'{id}:mute:{hmshelp}')
          r.srem(f'listMUTE:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} لغيت كتمته عام\n☆')
   
   if text == 'الغاء الحظر العام من الالعاب' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الأمر يخص ( المطور الثانوي وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if not r.get(f'{id}:gbangames:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو محظور من الالعاب من قبل\n☆')
        else:
          r.delete(f'{id}:gbangames:{hmshelp}')
          r.srem(f'listGBANGAMES:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} لغيت حظره من الالعاب\n☆')

   if text == 'الغاء الحظر العام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الأمر يخص ( المطور الثانوي وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if not r.get(f'{id}:gban:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو محظور عام من قبل\n☆')
        else:
          r.delete(f'{id}:gban:{hmshelp}')
          r.srem(f'listGBAN:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} لغيت حظره عام\n☆')