import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.Ranks import isLockCommand


@Client.on_message(filters.text & filters.group, group=13)
def delRanksHandler(c,m):
    k = r.get(f'{hmshelp}:botkey')
    Thread(target=del_ranks_func,args=(c,m,k)).start()
    

def del_ranks_func(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{hmshelp}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:mute:{hmshelp}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{hmshelp}'):  return 
   
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{hmshelp}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{hmshelp}'):  return 
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
   id = m.from_user.id
   cid = m.chat.id
   demoted = '''{} ابشر عيني {}
{} مسحت ( {} ) من {} 
☆
'''
   if text == 'مسح قائمه المطورين':
      if not devp_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( المطورين ) بس')
      else:
        if not r.smembers(f'{hmshelp}DEV2'):
          return m.reply(f'{k} مافيه قائمة المطورين الثانويين')
        else:
          count = 0
          for dev2 in r.smembers(f'{hmshelp}DEV2'):
             r.srem(f'{hmshelp}DEV2', int(dev2))
             r.delete(f'{int(dev2)}:rankDEV2:{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'قائمة Dev'))
   
   if text == 'مسح قائمه المطورين الثانويين':
      if not dev2_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المطورين الثانويين وفوق ) بس')
      else:
        if not r.smembers(f'{hmshelp}DEV'):
          return m.reply(f'{k} مافيه قائمة مطورين ثانويين')
        else:
          count = 0
          for dev in r.smembers(f'{hmshelp}DEV'):
             r.srem(f'{hmshelp}DEV', int(dev))
             r.delete(f'{int(dev)}:rankDEV:{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'قائمة MY'))
   
   if text == 'مسح المالكين الاساسيين':
      if not dev_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( مالك القروب وفوق) بس')
      else:
        if not r.smembers(f'{cid}:listGOWNER:{hmshelp}'):
          return m.reply(f'{k} مافيه مالكين اساسيين')
        else:
          count = 0
          for gowner in r.smembers(f'{cid}:listGOWNER:{hmshelp}'):
             r.srem(f'{cid}:listGOWNER:{hmshelp}', int(gowner))
             r.delete(f'{cid}:rankGOWNER:{int(gowner)}{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المالكين الاساسيين'))
   
   if text == 'مسح المالكين':
      if not gowner_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listOWNER:{hmshelp}'):
          return m.reply(f'{k} مافيه مالكين ')
        else:
          count = 0
          for owner in r.smembers(f'{cid}:listOWNER:{hmshelp}'):
             r.srem(f'{cid}:listOWNER:{hmshelp}', int(owner))
             r.delete(f'{cid}:rankOWNER:{int(owner)}{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المالكين'))
   
   if text == 'مسح المدراء':
      if not owner_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المالك وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listMOD:{hmshelp}'):
          return m.reply(f'{k} مافيه مدراء')
        else:
          count = 0
          for MOD in r.smembers(f'{cid}:listMOD:{hmshelp}'):
             r.srem(f'{cid}:listMOD:{hmshelp}', int(MOD))
             r.delete(f'{cid}:rankMOD:{int(MOD)}{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المدراء'))
   
   if text == 'مسح الادمنيه' or text == 'مسح الادمن':
      if not mod_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listADMIN:{hmshelp}'):
          return m.reply(f'{k} مافيه ادمن')
        else:
          count = 0
          for ADM in r.smembers(f'{cid}:listADMIN:{hmshelp}'):
             r.srem(f'{cid}:listADMIN:{hmshelp}', int(ADM))
             r.delete(f'{cid}:rankADMIN:{int(ADM)}{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'الادمن'))
   
   if text == 'مسح المميزين':
      if not mod_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listPRE:{hmshelp}'):
          return m.reply(f'{k} مافيه مميزين')
        else:
          count = 0
          for MOD in r.smembers(f'{cid}:listPRE:{hmshelp}'):
             r.srem(f'{cid}:listPRE:{hmshelp}', int(MOD))
             r.delete(f'{cid}:rankPRE:{int(MOD)}{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المميزين'))
   
   if text == 'مسح المكتومين':
      if not mod_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listMUTE:{hmshelp}'):
          return m.reply(f'{k} مافيه مكتومين')
        else:
          count = 0
          for MOD in r.smembers(f'{cid}:listMUTE:{hmshelp}'):
             try:
               mod = int(MOD)
             except:
               mod = MOD
             r.srem(f'{cid}:listMUTE:{hmshelp}', mod)
             r.delete(f'{mod}:mute:{cid}{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المكتومين'))
   
   if text == 'مسح المكتومين عام':
      if not dev_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( المالكين وفوق ) بس')
      else:
        if not r.smembers(f'listMUTE:{hmshelp}'):
          return m.reply(f'{k} مافيه مكتومين عام')
        else:
          count = 0
          for MOD in r.smembers(f'listMUTE:{hmshelp}'):
             r.srem(f'listMUTE:{hmshelp}', int(MOD))
             r.delete(f'{int(MOD)}:mute:{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المكتومين عام'))
   
   if text == 'مسح المحظورين عام':
      if not dev_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( المالكين وفوق ) بس')
      else:
        if not r.smembers(f'listGBAN:{hmshelp}'):
          return m.reply(f'{k} مافيه حمير محظورين')
        else:
          count = 0
          for MOD in r.smembers(f'listGBAN:{hmshelp}'):
             r.srem(f'listGBAN:{hmshelp}', int(MOD))
             r.delete(f'{int(MOD)}:gban:{hmshelp}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'الحمير المحظورين عام'))
          
             
       
   
   
