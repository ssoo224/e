import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.Ranks import isLockCommand


@Client.on_message(filters.text & filters.group, group=35)
def customrankHandler(c,m):
    k = r.get(f'{hmshelp}:botkey')
    channel = r.get(f'{hmshelp}:BotChannel') if r.get(f'{hmshelp}:BotChannel') else 'alwzaraa2'
    Thread(target=customRankFunc,args=(c,m,k,channel)).start()
    
def customRankFunc(c,m,k,channel):
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
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if text == 'الغاء':
     if r.get(f'{m.from_user.id}:addRank2:{m.chat.id}{hmshelp}') or r.get(f'{m.from_user.id}:addRank:{m.chat.id}{hmshelp}') or r.get(f'{m.from_user.id}:delRank:{m.chat.id}{hmshelp}'):
        m.reply(f'{k} من عيوني لغيت كل شي يخص الرتب')
        r.delete(f'{m.from_user.id}:addRank:{m.chat.id}{hmshelp}')
        r.delete(f'{m.from_user.id}:delRank:{m.chat.id}{hmshelp}')
        r.delete(f'{m.from_user.id}:addRank2:{m.chat.id}{hmshelp}')
   
   if r.get(f'{m.from_user.id}:addRank2:{m.chat.id}{hmshelp}') and mod_pls(m.from_user.id,m.chat.id) and len(m.text) <= 20:
     rank = r.get(f'{m.from_user.id}:addRank2:{m.chat.id}{hmshelp}')
     r.delete(f'{m.from_user.id}:addRank2:{m.chat.id}{hmshelp}')
     if rank == 'مالك اساسي':
       if r.get(f'{m.chat.id}:RankGowner:{hmshelp}'):
         rrr = r.get(f'{m.chat.id}:RankGowner:{hmshelp}')
         r.srem(f'{m.chat.id}:ranklist:{hmshelp}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankGowner:{hmshelp}')
       r.set(f'{m.chat.id}:RankGowner:{hmshelp}',m.text)
     if rank == 'مالك':
       if r.get(f'{m.chat.id}:RankOwner:{hmshelp}'):
         rrr = r.get(f'{m.chat.id}:RankOwner:{hmshelp}')
         r.srem(f'{m.chat.id}:ranklist:{hmshelp}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankOwner:{hmshelp}')
       r.set(f'{m.chat.id}:RankOwner:{hmshelp}',m.text)
     if rank == 'مدير':
       if r.get(f'{m.chat.id}:RankMod:{hmshelp}'):
         rrr = r.get(f'{m.chat.id}:RankMod:{hmshelp}')
         r.srem(f'{m.chat.id}:ranklist:{hmshelp}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankMod:{hmshelp}')     
       r.set(f'{m.chat.id}:RankMod:{hmshelp}',m.text)
     if rank == 'ادمن':
       if r.get(f'{m.chat.id}:RankAdm:{hmshelp}'):
         rrr = r.get(f'{m.chat.id}:RankAdm:{hmshelp}')
         r.srem(f'{m.chat.id}:ranklist:{hmshelp}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankAdm:{hmshelp}')     
       r.set(f'{m.chat.id}:RankAdm:{hmshelp}',m.text)
     if rank == 'مميز':
       if r.get(f'{m.chat.id}:RankPre:{hmshelp}'):
         rrr = r.get(f'{m.chat.id}:RankPre:{hmshelp}')
         r.srem(f'{m.chat.id}:ranklist:{hmshelp}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankPre:{hmshelp}')     
       r.set(f'{m.chat.id}:RankPre:{hmshelp}',m.text)
     if rank == 'عضو':
       if r.get(f'{m.chat.id}:RankMem:{hmshelp}'):
         rrr = r.get(f'{m.chat.id}:RankMem:{hmshelp}')
         r.srem(f'{m.chat.id}:ranklist:{hmshelp}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankMem:{hmshelp}')     
       r.set(f'{m.chat.id}:RankMem:{hmshelp}',m.text)
     r.sadd(f'{m.chat.id}:ranklist:{hmshelp}',f'{rank}&&newr={m.text}')  
     return m.reply(f'{k} تم غيرت الرتبه الى ( {m.text} )')
       
   
   if r.get(f'{m.from_user.id}:addRank:{m.chat.id}{hmshelp}') and mod_pls(m.from_user.id,m.chat.id):
     r.delete(f'{m.from_user.id}:addRank:{m.chat.id}{hmshelp}')
     if not m.text in ['مالك اساسي','مالك','مدير','ادمن','مميز','عضو']:
       return m.reply(f'{k} ركز! الرتبه اللي كتبتها مو موجوده')
     else:
       r.set(f'{m.from_user.id}:addRank2:{m.chat.id}{hmshelp}',m.text,ex=600)
       return m.reply(f'{k} حلو الحين ارسل الرتبه الجديدة')
   
   if r.get(f'{m.from_user.id}:delRank:{m.chat.id}{hmshelp}') and mod_pls(m.from_user.id,m.chat.id):
     r.delete(f'{m.from_user.id}:delRank:{m.chat.id}{hmshelp}')
     if not m.text in ['مالك اساسي','مالك','مدير','ادمن','مميز','عضو']:
       return m.reply(f'{k} مافي رتبه زي كذا لازم تكتب الرتبه الاساسيه مثال مالك اساسي مو {m.text[:20]}')
     else:
       rank = m.text
       if rank == 'مالك اساسي':
         rank2 = r.get(f'{m.chat.id}:RankGowner:{hmshelp}')
         r.delete(f'{m.chat.id}:RankGowner:{hmshelp}')
       if rank == 'مالك':
         rank2 = r.get(f'{m.chat.id}:RankOwner:{hmshelp}')
         r.delete(f'{m.chat.id}:RankOwner:{hmshelp}')
       if rank == 'مدير':
         rank2 = r.get(f'{m.chat.id}:RankMod:{hmshelp}')
         r.delete(f'{m.chat.id}:RankMod:{hmshelp}')
       if rank == 'ادمن':
         rank2 = r.get(f'{m.chat.id}:RankAdm:{hmshelp}')
         r.delete(f'{m.chat.id}:RankAdm:{hmshelp}')
       if rank == 'مميز':
         rank2 = r.get(f'{m.chat.id}:RankPre:{hmshelp}')
         r.delete(f'{m.chat.id}:RankPre:{hmshelp}')
       if rank == 'عضو':
         rank2 = r.get(f'{m.chat.id}:RankMem:{hmshelp}')
         r.delete(f'{m.chat.id}:RankMem:{hmshelp}')
       r.srem(f'{m.chat.id}:ranklist:{hmshelp}',f'{rank}&&newr={rank2}')
       return m.reply(f'{k} مسحت رتبه ( {rank2} )')
   
   if text == 'مسح الرتب':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       if not r.smembers(f'{m.chat.id}:ranklist:{hmshelp}'):
         return m.reply(f'{k} مافيه رتب مضافة')
       else:
         m.reply(f'{k} مسحت كل الرتب المضافة')
         r.delete(f'{m.chat.id}:RankGowner:{hmshelp}')
         r.delete(f'{m.chat.id}:RankOwner:{hmshelp}')
         r.delete(f'{m.chat.id}:RankMod:{hmshelp}')
         r.delete(f'{m.chat.id}:RankAdm:{hmshelp}')
         r.delete(f'{m.chat.id}:RankPre:{hmshelp}')
         r.delete(f'{m.chat.id}:RankMem:{hmshelp}')
         return r.delete(f'{m.chat.id}:ranklist:{hmshelp}')
   
   if text == 'قائمه الرتب' or text == 'قائمة الرتب':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       if not r.smembers(f'{m.chat.id}:ranklist:{hmshelp}'):
         return m.reply(f'{k} مافيه رتب مضافة')
       else:
         txt = 'قائمة الرتب:\n'
         count = 1
         for rrr in r.smembers(f'{m.chat.id}:ranklist:{hmshelp}'):
            rank = rrr.split('&&newr=')
            txt += f'{count}) {rank[0]} ~ ( {rank[1]} )\n'
            count += 1
         txt += '\n☆'
         return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح رتبه' or text == 'مسح رتبة':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.from_user.id}:delRank:{m.chat.id}{hmshelp}',1,ex=600)
       return m.reply(f'{k} ارسل اسم الرتبه اللي تبي تمسحها الحين')
   
   if text == 'تغيير رتبه' or text == 'تغيير رتبة':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.from_user.id}:addRank:{m.chat.id}{hmshelp}',1,ex=600)
       return m.reply(f'''
{k} ارسل الرتبه اللي تبي تغييرها

{k} مالك اساسي
{k} مالك
{k} مدير
{k} ادمن
{k} مميز
{k} عضو
☆''')