import random, re, time, os, sys
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *


@Client.on_message(filters.text & filters.group, group=36)
def replaceCode(c,m):
    k = r.get(f'{hmshelp}:botkey')
    channel = r.get(f'{hmshelp}:BotChannel') if r.get(f'{hmshelp}:BotChannel') else 'alwzaraa2'
    Thread(target=raplaceCodefunc,args=(c,m,k,channel)).start()
    
def raplaceCodefunc(c,m,k,channel):
   if not r.get(f'{m.chat.id}:enable:{hmshelp}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}'):  return 
   if r.get(f'{m.from_user.id}:mute:{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{hmshelp}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{hmshelp}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:mute:{hmshelp}') and not admin_pls(m.from_user.id,m.chat.id):  return  
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{hmshelp}'):  return 
   text = m.text
   name = r.get(f'{hmshelp}:BotName') if r.get(f'{hmshelp}:BotName') else 'هانكوك'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}')
   if r.get(f'Custom:{hmshelp}&text={text}'):
       text = r.get(f'Custom:{hmshelp}&text={text}')
       
   '''
   if text == 'الملفات':
     if m.from_user.id == 80595335:
        text = '——— ملفات السورس ———'
        a = os.listdir('Plugins')
        a.sort()
        count = 1
        for file in a:
          if file.endswith('.py'):
            text += f'\n{count}) `{file}`'
            count += 1
        text += f'\n——— @{channel} ———'
        return m.reply(text, disable_web_page_preview=True)
   '''
   if r.get(f'{m.chat.id}:replace:{m.from_user.id}{hmshelp}') or r.get(f'{m.chat.id}:replace2:{m.from_user.id}{hmshelp}') or r.get(f'{m.chat.id}:replace3:{m.from_user.id}{hmshelp}'):
     if text == 'الغاء':
       r.delete(f'{m.chat.id}:replace:{m.from_user.id}{hmshelp}')
       r.delete(f'{m.chat.id}:replace2:{m.from_user.id}{hmshelp}')
       r.delete(f'{m.chat.id}:replace3:{m.from_user.id}{hmshelp}')
       return m.reply(f'{k} من عيوني لغيت استبدال كلمة ')
      
   if text == 'استبدال كلمه' or text == 'استبدال كلمة':
      if not devp_pls(m.from_user.id,m.chat.id):
         return m.reply(f'{k} هذا الأمر يخص ( مبرمج السورس ) بس')
      else:
         r.set(f'{m.chat.id}:replace:{m.from_user.id}{hmshelp}',1,ex=600)
         return m.reply(f'{k} ارسل الكلمة القديمة الآن')
   
   if r.get(f'{m.chat.id}:replace:{m.from_user.id}{hmshelp}') and devp_pls(m.from_user.id,m.chat.id):
      r.set(f'{m.chat.id}:replace2:{m.from_user.id}{hmshelp}',m.text,ex=600)
      r.delete(f'{m.chat.id}:replace:{m.from_user.id}{hmshelp}')
      return m.reply(f'{k} ارسل الكلمة الجديدة الحين')
   
   if r.get(f'{m.chat.id}:replace2:{m.from_user.id}{hmshelp}') and devp_pls(m.from_user.id,m.chat.id):
      txt = r.get(f'{m.chat.id}:replace2:{m.from_user.id}{hmshelp}')
      r.delete(f'{m.chat.id}:replace2:{m.from_user.id}{hmshelp}')
      r.set(f'{m.chat.id}:replace3:{m.from_user.id}{hmshelp}',f'{txt}&&new&&{m.text}',ex=600)
      a = os.listdir('Plugins')
      a.sort()
      txt = f'{k} ارسل اسم الملف الي تبي تعدل فيه الحين:'
      count = 1
      txt += '\n\n——— ملفات السورس ———'
      for file in a:
          if file.endswith('.py'):
            txt += f'\n{count}) `{file}`'
            count += 1
      txt += f'\n——— @{channel} ———'
      return m.reply(txt)
   
   if r.get(f'{m.chat.id}:replace3:{m.from_user.id}{hmshelp}') and devp_pls(m.from_user.id,m.chat.id) and m.text in os.listdir('Plugins'):
      mm = m.reply(f'{k} جاري تعديل الملف')
      get = r.get(f'{m.chat.id}:replace3:{m.from_user.id}{hmshelp}')
      old = get.split('&&new&&')[0]
      new = get.split('&&new&&')[1]
      r.delete(f'{m.chat.id}:replace3:{m.from_user.id}{hmshelp}')
      with open(f'Plugins/{m.text}','r') as Read:
         old_confing = Read.read()
         mm.edit(f'{k} تم فتح الملف وقرائته')
      with open(f'Plugins/{m.text}','w+') as Write:
         mm.edit(f'{k} تم فتح الملف جاري كتابة الكود مع استبدال الكلمة')
         Write.write(old_confing.replace(old,new))
      mm.edit(f'{k} تم فتح الملف `{m.text}` وتعديله\n{k} تم استبدال الكلمة القديمة ( {old} ) بالكلمة الجديدة ( {new} )')
      python = sys.executable
      os.execl(python, python, *sys.argv)
      
      
      
      
      
   