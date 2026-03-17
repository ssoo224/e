import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.Ranks import isLockCommand


@Client.on_message(filters.text & filters.group, group=7)
def ranksCommandsHandler(c,m):
   k = r.get(f'{hmshelp}:botkey')
   Thread(target=ranks_reply_promote,args=(c,m,k)).start()
   

def ranks_reply_promote(c,m,k):
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
    if text == 'تعطيل الرفع':
      if not owner_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
      else:
        if r.get(f'{m.chat.id}:disableRanks:{hmshelp}'):
          return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الرفع معطل من قبل\n☆')
        else:
          r.set(f'{m.chat.id}:disableRanks:{hmshelp}', 1)
          return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الرفع\n☆')
    
    if text == 'تفعيل الرفع':
      if not owner_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
      else:
        if not r.get(f'{m.chat.id}:disableRanks:{hmshelp}'):
          return m.reply(f'「 {m.from_user.mention} 」\n{k} الرفع مفعل من قبل\n☆')
        else:
          r.delete(f'{m.chat.id}:disableRanks:{hmshelp}')
          return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الرفع\n☆')
    
    cid = m.chat.id
    
    if r.get(f'{m.chat.id}:disableRanks:{hmshelp}'):  return
    rank = get_rank(m.from_user.id, m.chat.id)
    if text.startswith('رفع ثانوي '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not devp_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المطور) بس')
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        
           
        if r.get(f'{id}:rankDEV2:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} المطور الثانوي من قبل\n☆')
        else:
          r.set(f'{id}:rankDEV2:{hmshelp}', 1)
          r.sadd(f'{hmshelp}DEV2', id)
          return m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار المطور الثانوي\n☆')
          if r.get(f'{id}:mute:{hmshelp}'):
            r.delete(f'{id}:mute:{hmshelp}')
            r.srem(f'listMUTE:{hmshelp}', id)
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    if text == 'رفع ثانوي' and m.reply_to_message and m.reply_to_message.from_user:
        if not devp_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المطور) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')        
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')           
        if r.get(f'{id}:rankDEV2:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} المطور الثانوي من قبل\n☆')
        else:
          r.set(f'{id}:rankDEV2:{hmshelp}', 1)
          r.sadd(f'{hmshelp}DEV2', id)
          return m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار المطور الثانوي\n☆')
          if r.get(f'{id}:mute:{hmshelp}'):
            r.delete(f'{id}:mute:{hmshelp}')
            r.srem(f'listMUTE:{hmshelp}', id)
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
          
    if text.startswith('رفع مطور '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return False
        if not dev2_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المطور الثانوي️ وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{id}:rankDEV:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مطور من قبل\n☆')
        else:
          r.set(f'{id}:rankDEV:{hmshelp}', 1)
          r.sadd(f'{hmshelp}DEV', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مطور\n☆')
          if r.get(f'{id}:mute:{hmshelp}'):
            r.delete(f'{id}:mute:{hmshelp}')
            r.srem(f'listMUTE:{hmshelp}', id)
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    if text == 'رفع مطور' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev2_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المطور الثانوي️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{id}:rankDEV:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مطور من قبل\n☆')
        else:
          r.set(f'{id}:rankDEV:{hmshelp}', 1)
          r.sadd(f'{hmshelp}DEV', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مطور\n☆')
          if r.get(f'{id}:mute:{hmshelp}'):
            r.delete(f'{id}:mute:{hmshelp}')
            r.srem(f'listMUTE:{hmshelp}', id)
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    cid = m.chat.id
    
    if text.startswith('رفع مالك اساسي '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not gowner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) بس')
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مالك اساسي من قبل\n☆')
        else:
          r.set(f'{cid}:rankGOWNER:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listGOWNER:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك اساسي\n☆')
          if r.get(f'{id}:mute:{hmshelp}'):
            r.delete(f'{id}:mute:{hmshelp}')
            r.srem(f'listMUTE:{hmshelp}', id)
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
          return 
    
    if text == 'رفع مالك اساسي' and m.reply_to_message and m.reply_to_message.from_user:
        if not gowner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص (المالك الاساسي وفوق) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention       
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مالك اساسي من قبل\n☆')
        else:
          r.set(f'{cid}:rankGOWNER:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listGOWNER:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك اساسي\n☆')
          if r.get(f'{id}:mute:{hmshelp}'):
            r.delete(f'{id}:mute:{hmshelp}')
            r.srem(f'listMUTE:{hmshelp}', id)
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
          return 
    
    if text.startswith('رفع مالك '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not gowner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مالك من قبل\n☆')
        else:
          r.set(f'{cid}:rankOWNER:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listOWNER:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    if text == 'رفع مالك' and m.reply_to_message and m.reply_to_message.from_user:
        if not gowner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مالك من قبل\n☆')
        else:
          r.set(f'{cid}:rankOWNER:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listOWNER:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    
    if text.startswith('رفع مدير '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not owner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if r.get(f'{cid}:rankMOD:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مدير من قبل\n☆')
        else:
          r.set(f'{cid}:rankMOD:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listMOD:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مدير\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    if text == 'رفع مدير' and m.reply_to_message and m.reply_to_message.from_user:
        if not owner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if r.get(f'{cid}:rankMOD:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مدير من قبل\n☆')
        else:
          r.set(f'{cid}:rankMOD:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listMOD:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مدير\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    if text.startswith('رفع ادمن '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not mod_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if r.get(f'{cid}:rankADMIN:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} ادمن من قبل\n☆')
        else:
          r.set(f'{cid}:rankADMIN:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listADMIN:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار ادمن\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    if text == 'رفع ادمن' and m.reply_to_message and m.reply_to_message.from_user:        
        if not mod_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if r.get(f'{cid}:rankADMIN:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} ادمن من قبل\n☆')
        else:
          r.set(f'{cid}:rankADMIN:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listADMIN:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار ادمن\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    if text.startswith('رفع مميز '):
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not admin_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
      else:
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if r.get(f'{cid}:rankPRE:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مميز من قبل\n☆')
        else:
          r.set(f'{cid}:rankPRE:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listPRE:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مميز\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
    
    if text == 'رفع مميز' and m.reply_to_message and m.reply_to_message.from_user:
      if not admin_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
      else:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{cid}:rankPRE:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مميز من قبل\n☆')
        else:
          r.set(f'{cid}:rankPRE:{id}{hmshelp}', 1)
          r.sadd(f'{cid}:listPRE:{hmshelp}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مميز\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{hmshelp}'):
            r.delete(f'{id}:mute:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:listMUTE:{hmshelp}', id)
          
    
    
    
@Client.on_message(filters.text & filters.group, group=8)
def ranksCommandsHandlerDemote(c,m):
   k = r.get(f'{hmshelp}:botkey')
   ranks_reply_demote(c,m,k)


def ranks_reply_demote(c,m,k):
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
    rank = get_rank(m.from_user.id, m.chat.id)
    cid = m.chat.id
    
    if text == 'تنزيل ثانوي' and m.reply_to_message and m.reply_to_message.from_user:
        if not devp_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المطور) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention     
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')           
        if not r.get(f'{id}:rankDEV2:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو المطور الثانوي\n☆')
        else:
          r.delete(f'{id}:rankDEV2:{hmshelp}')
          r.srem(f'{hmshelp}DEV2', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المطور الثانوي\n☆')
    
    if text.startswith('تنزيل مطور '):
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not devp_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المطور) بس')
      else:
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')           
        if not r.get(f'{id}:rankDEV2:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو المطور الثانوي\n☆')
        else:
          r.delete(f'{id}:rankDEV2:{hmshelp}')
          r.srem(f'{hmshelp}DEV2', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المطور الثانوي\n☆')
          
    if text == 'تنزيل مطور ثانوي'  and m.reply_to_message and m.reply_to_message.from_user:
        if not dev2_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المطور الثانوي️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if not r.get(f'{id}:rankDEV:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو المطورين من قبل\n☆')
        else:
          r.delete(f'{id}:rankDEV:{hmshelp}')
          r.srem(f'{hmshelp}DEV', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المطورين\n☆')
    
    if text.startswith('تنزيل مطور ثانوي '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not dev2_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المطور الثانوي️ وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if not r.get(f'{id}:rankDEV:{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو المطورين من قبل\n☆')
        else:
          r.delete(f'{id}:rankDEV:{hmshelp}')
          r.srem(f'{hmshelp}DEV', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المطورين\n☆')
    
    
    
    if text == 'تنزيل مالك اساسي' and m.reply_to_message and m.reply_to_message.from_user:
        if not gowner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص (المالك الاساسي وفوق) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if not r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مالك اساسي\n☆')
        else:
          r.delete(f'{cid}:rankGOWNER:{id}{hmshelp}')
          r.srem(f'{cid}:listGOWNER:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المالك الاساسي\n☆')
    
    if text.startswith('تنزيل مالك اساسي '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not gowner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص (المالك الاساسي وفوق) بس')
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if not r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مالك اساسي\n☆')
        else:
          r.delete(f'{cid}:rankGOWNER:{id}{hmshelp}')
          r.srem(f'{cid}:listGOWNER:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المالك الاساسي\n☆')
    
    
    if text.startswith('تنزيل مالك '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not gowner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')        
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''        
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')        
        if not r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مالك من قبل\n☆')
        else:
          r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
          r.srem(f'{cid}:listOWNER:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المالك \n☆')
    
    if text == 'تنزيل مالك' and m.reply_to_message and m.reply_to_message.from_user:    
        
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention     
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')        
        if not r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مالك من قبل\n☆')
        else:
          r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
          r.srem(f'{cid}:listOWNER:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المالك \n☆')

    if text.startswith('تنزيل مدير '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if not r.get(f'{cid}:rankMOD:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مدير من قبل\n☆')
        else:
          r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
          r.srem(f'{cid}:listMOD:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من رتبة المدير \n☆')
    
    if text == 'تنزيل مدير' and m.reply_to_message and m.reply_to_message.from_user:
        if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if not r.get(f'{cid}:rankMOD:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مدير من قبل\n☆')
        else:
          r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
          r.srem(f'{cid}:listMOD:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من رتبة المدير \n☆')
    
    if text.startswith('تنزيل ادمن '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not mod_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if not r.get(f'{cid}:rankADMIN:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو ادمن من قبل\n☆')
        else:
          r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
          r.srem(f'{cid}:listADMIN:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من رتبة الادمن \n☆')
    
    if text == 'تنزيل ادمن' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if not r.get(f'{cid}:rankADMIN:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو ادمن من قبل\n☆')
        else:
          r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
          r.srem(f'{cid}:listADMIN:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من رتبة الادمن \n☆')
    
    if text.startswith('تنزيل مميز '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not admin_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if not r.get(f'{cid}:rankPRE:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مميز من قبل\n☆')
        else:
          r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
          r.srem(f'{cid}:listPRE:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المميزين \n☆')
    
    if text == 'تنزيل مميز' and m.reply_to_message and m.reply_to_message.from_user:
        if not admin_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if not r.get(f'{cid}:rankPRE:{id}{hmshelp}'):
          return m.reply(f'「 {mention} 」\n{k} مو مميز من قبل\n☆')
        else:
          r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
          r.srem(f'{cid}:listPRE:{hmshelp}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المميزين \n☆')
    
    if text.startswith('تنزيل الكل '):
       if not '@' in text and not re.findall('[0-9]+', text):
          return 
       if not mod_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
       
       if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
       
       if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
       if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
       if devp_pls(m.from_user.id,m.chat.id):
          rank = get_rank(id,cid)
          if id == m.from_user.id:
             return m.reply(f'{k} مافيك تنزل نفسك')
          if not rank == 'عضو' and not id in [7115002714]:
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{id}:rankDEV2:{hmshelp}')
              r.srem(f'{hmshelp}DEV2', id)
              r.delete(f'{id}:rankDEV:{hmshelp}')
              r.srem(f'{hmshelp}DEV', id)
              r.delete(f'{cid}:rankGOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listGOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
              r.srem(f'{cid}:listMOD:{hmshelp}', id)
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714]:
              return m.reply(f'{k} مايمديك تستخدم الأمر على مبرمج السورس')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if dev2_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [7115002714]:
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{id}:rankDEV:{hmshelp}')
              r.srem(f'{hmshelp}DEV', id)
              r.delete(f'{cid}:rankGOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listGOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
              r.srem(f'{cid}:listMOD:{hmshelp}', id)
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')

       if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [7115002714] and not r.get(
               f'{id}:rankDEV2:{hmshelp}'):
           m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
           r.delete(f'{cid}:rankGOWNER:{id}{hmshelp}')
           r.srem(f'{cid}:listGOWNER:{hmshelp}', id)
           r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
           r.srem(f'{cid}:listOWNER:{hmshelp}', id)
           r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
           r.srem(f'{cid}:listMOD:{hmshelp}', id)
           r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
           r.srem(f'{cid}:listADMIN:{hmshelp}', id)
           r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
           r.srem(f'{cid}:listPRE:{hmshelp}', id)
           return
       if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or not r.get(
               f'{id}:rankDEV2:{hmshelp}'):
           return m.reply(f'{k} رتبته اعلى منك')
       else:
           return m.reply(f'{k} ماله رتبة')
       
       if gowner_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [7115002714] and not r.get(
                  f'{id}:rankDEV2:{hmshelp}') and not r.get(f'{id}:rankDEV:{hmshelp}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
              r.srem(f'{cid}:listMOD:{hmshelp}', id)
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or not r.get(
                  f'{id}:rankDEV2:{hmshelp}') or r.get(f'{id}:rankDEV:{hmshelp}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if owner_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [7115002714] and not r.get(
                  f'{id}:rankDEV2:{hmshelp}') and not r.get(f'{id}:rankDEV:{hmshelp}') and not r.get(
                  f'{cid}:rankGOWNER:{id}{hmshelp}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
              r.srem(f'{cid}:listMOD:{hmshelp}', id)
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or not r.get(
                  f'{id}:rankDEV2:{hmshelp}') or r.get(f'{id}:rankDEV:{hmshelp}') or r.get(
                  f'{cid}:rankGOWNER:{id}{hmshelp}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if mod_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [7115002714] and not r.get(
                  f'{id}:rankDEV2:{hmshelp}') and not r.get(f'{id}:rankDEV:{hmshelp}') and not r.get(
                  f'{cid}:rankGOWNER:{id}{hmshelp}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
              r.srem(f'{cid}:listMOD:{hmshelp}', id)
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or not r.get(
                  f'{id}:rankDEV2:{hmshelp}') or r.get(f'{id}:rankDEV:{hmshelp}') or r.get(
                  f'{cid}:rankGOWNER:{id}{hmshelp}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if admin_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [7115002714] and not r.get(
                  f'{id}:rankDEV2:{hmshelp}') and not r.get(f'{id}:rankDEV:{hmshelp}') and not r.get(
                  f'{cid}:rankGOWNER:{id}{hmshelp}') and not r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or not r.get(
                  f'{id}:rankDEV2:{hmshelp}') or r.get(f'{id}:rankDEV:{hmshelp}') or r.get(
                  f'{cid}:rankGOWNER:{id}{hmshelp}') or r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
    
    
    if text == 'تنزيل الكل' and m.reply_to_message and m.reply_to_message.from_user:
       if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
       
       id = m.reply_to_message.from_user.id
       mention= m.reply_to_message.from_user.mention
       
       if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
       if id == int(hmshelp):
           return m.reply('ركز حبيبي كيف انزل نفسي')
       if devp_pls(m.from_user.id,m.chat.id):
          rank = get_rank(id,cid)
          if id == m.from_user.id:
             return m.reply(f'{k} مافيك تنزل نفسك')
          if not rank == 'عضو' and not id in [7115002714]:
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{id}:rankDEV2:{hmshelp}')
              r.srem(f'{hmshelp}DEV2', id)
              r.delete(f'{id}:rankDEV:{hmshelp}')
              r.srem(f'{hmshelp}DEV', id)
              r.delete(f'{cid}:rankGOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listGOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
              r.srem(f'{cid}:listMOD:{hmshelp}', id)
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714]:
              return m.reply(f'{k} مايمديك تستخدم الأمر على مبرمج السورس')
          else:
             return m.reply(f'{k} ماله رتبة')
       
       if dev2_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [7115002714]:
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{id}:rankDEV:{hmshelp}')
              r.srem(f'{hmshelp}DEV', id)
              r.delete(f'{cid}:rankGOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listGOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
              r.srem(f'{cid}:listMOD:{hmshelp}', id)
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if dev_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [7115002714] and not r.get(
                  f'{id}:rankDEV2:{hmshelp}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankGOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listGOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
              r.srem(f'{cid}:listOWNER:{hmshelp}', id)
              r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
              r.srem(f'{cid}:listMOD:{hmshelp}', id)
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or not r.get(
                  f'{id}:rankDEV2:{hmshelp}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')

       if gowner_pls(m.from_user.id, m.chat.id):
           rank = get_rank(id, cid)
           if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [
               7115002714] and not r.get(f'{id}:rankDEV2:{hmshelp}') and not r.get(f'{id}:rankDEV:{hmshelp}'):
               m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
               r.delete(f'{cid}:rankOWNER:{id}{hmshelp}')
               r.srem(f'{cid}:listOWNER:{hmshelp}', id)
               r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
               r.srem(f'{cid}:listMOD:{hmshelp}', id)
               r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
               r.srem(f'{cid}:listADMIN:{hmshelp}', id)
               r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
               r.srem(f'{cid}:listPRE:{hmshelp}', id)
               return
           if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or not r.get(
                   f'{id}:rankDEV2:{hmshelp}') or r.get(f'{id}:rankDEV:{hmshelp}'):
               return m.reply(f'{k} رتبته اعلى منك')
           else:
               return m.reply(f'{k} ماله رتبة')
       
       if owner_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [7115002714] and not r.get(
                  f'{id}:rankDEV2:{hmshelp}') and not r.get(f'{id}:rankDEV:{hmshelp}') and not r.get(
                  f'{cid}:rankGOWNER:{id}{hmshelp}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankMOD:{id}{hmshelp}')
              r.srem(f'{cid}:listMOD:{hmshelp}', id)
              r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
              r.srem(f'{cid}:listADMIN:{hmshelp}', id)
              r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
              r.srem(f'{cid}:listPRE:{hmshelp}', id)
              return
          if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or not r.get(
                  f'{id}:rankDEV2:{hmshelp}') or r.get(f'{id}:rankDEV:{hmshelp}') or r.get(
                  f'{cid}:rankGOWNER:{id}{hmshelp}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')

       if mod_pls(m.from_user.id, m.chat.id):
           rank = get_rank(id, cid)
           if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [
               7115002714] and not r.get(f'{id}:rankDEV2:{hmshelp}') and not r.get(
                   f'{id}:rankDEV:{hmshelp}') and not r.get(f'{cid}:rankGOWNER:{id}{hmshelp}') and not r.get(
                   f'{cid}:rankOWNER:{id}{hmshelp}'):
               m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
               r.delete(f'{cid}:rankADMIN:{id}{hmshelp}')
               r.srem(f'{cid}:listADMIN:{hmshelp}', id)
               r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
               r.srem(f'{cid}:listPRE:{hmshelp}', id)
               return
           if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or not r.get(
                   f'{id}:rankDEV2:{hmshelp}') or r.get(f'{id}:rankDEV:{hmshelp}') or r.get(
                   f'{cid}:rankGOWNER:{id}{hmshelp}') or r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
               return m.reply(f'{k} رتبته اعلى منك')
           else:
               return m.reply(f'{k} ماله رتبة')

       if admin_pls(m.from_user.id, m.chat.id):
           rank = get_rank(id, cid)
           if not rank == 'عضو' and not id == int(r.get(f'{hmshelp}botowner')) and not id in [
               7115002714] and not r.get(f'{id}:rankDEV2:{hmshelp}') and not r.get(
                   f'{id}:rankDEV:{hmshelp}') and not r.get(f'{cid}:rankGOWNER:{id}{hmshelp}') and not r.get(
                   f'{cid}:rankOWNER:{id}{hmshelp}') and not r.get(f'{cid}:rankMOD:{id}{hmshelp}'):
               m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
               r.delete(f'{cid}:rankPRE:{id}{hmshelp}')
               r.srem(f'{cid}:listPRE:{hmshelp}', id)
               return
           if id in [7115002714, 7115002714] or id == int(r.get(f'{hmshelp}botowner')) or r.get(
                   f'{id}:rankDEV2:{hmshelp}') or r.get(f'{id}:rankDEV:{hmshelp}') or r.get(
                   f'{cid}:rankGOWNER:{id}{hmshelp}') or r.get(f'{cid}:rankOWNER:{id}{hmshelp}') or r.get(
                   f'{cid}:rankMOD:{id}{hmshelp}'):
               return m.reply(f'{k} رتبته اعلى منك')
           else:
               return m.reply(f'{k} ماله رتبة')