import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.Ranks import isLockCommand


@Client.on_message(filters.text & filters.group, group=34)
def funHandler(c,m):
    k = r.get(f'{hmshelp}:botkey')
    channel = r.get(f'{hmshelp}:BotChannel') if r.get(f'{hmshelp}:BotChannel') else 'alwzaraa2'
    Thread(target=funFunc,args=(c,m,k,channel)).start()
    
def funFunc(c,m,k,channel):
   if r.get(f'{m.chat.id}:disableFun:{hmshelp}'):  return 
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
   ################# CAKE #################
   if text == 'رفع كيك' or text == 'رفع كيكه' or text == 'رفع كيكة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:CakeList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} كيكه من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:CakeList:{m.chat.id}',id)
         r.set(f'{hmshelp}:CakeName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته كيكه 🍰\n☆')
   
   if text == 'تنزيل كيك' or text == 'تنزيل كيكه' or text == 'تنزيل كيكة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:CakeList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو كيكه من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:CakeList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:CakeName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من كيكه\n☆')
   
   if text == 'قائمه الكيك' or text == 'قائمة الكيك':
     if not r.smembers(f'{hmshelp}:CakeList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الكيك فاضية')
     else:
       txt = '- قائمة الكيك 🍰\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:CakeList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:CakeName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الكيك' or text == 'مسح قائمه الكيك':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:CakeList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الكيك فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الكيك')
         for cake in r.smembers(f'{hmshelp}:CakeList:{m.chat.id}'):
           r.srem(f'{hmshelp}:CakeList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:CakeName:{cake}')
           
   ################# CAKE #################
   
   ################# 3SL #################
   if text == 'رفع عسل':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:3SLList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} عسل من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:3SLList:{m.chat.id}',id)
         r.set(f'{hmshelp}:3SLName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته عسل 🍯\n☆')
   
   if text == 'تنزيل عسل':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:3SLList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو عسل من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:3SLList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:3SLName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من عسل\n☆')
   
   if text == 'قائمه العسل' or text == 'قائمة العسل':
     if not r.smembers(f'{hmshelp}:3SLList:{m.chat.id}'):
       return m.reply(f'{k} قائمة العسل فاضية')
     else:
       txt = '- قائمة العسل 🍯\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:3SLList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:3SLName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة العسل' or text == 'مسح قائمه العسل':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:3SLList:{m.chat.id}'):
         return m.reply(f'{k} قائمة العسل فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة العسل')
         for cake in r.smembers(f'{hmshelp}:3SLList:{m.chat.id}'):
           r.srem(f'{hmshelp}:3SLList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:3SLName:{cake}')

   ################# 3SL #################
   
   ################# ZQ #################
   if text == 'رفع نصاب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:ZQList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} نصاب من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:ZQList:{m.chat.id}',id)
         r.set(f'{hmshelp}:ZQName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته نصاب 💩\n☆')
   
   if text == 'تنزيل نصاب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:ZQList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو نصاب من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:ZQList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:ZQName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من نصاب\n☆')
   
   if text == 'قائمه النصابين' or text == 'قائمة النصابين':
     if not r.smembers(f'{hmshelp}:ZQList:{m.chat.id}'):
       return m.reply(f'{k} قائمة النصابين فاضية')
     else:
       txt = '- قائمة النصابين 💩\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:ZQList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:ZQName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة النصابين' or text == 'مسح قائمه النصابين':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:ZQList:{m.chat.id}'):
         return m.reply(f'{k} قائمة النصابين فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة النصابين')
         for cake in r.smembers(f'{hmshelp}:ZQList:{m.chat.id}'):
           r.srem(f'{hmshelp}:ZQList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:ZQName:{cake}')

   ################# ZQ #################
   
   ################# 7MR #################
   if text == 'رفع حمار':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:7MRList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} حمار من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:7MRList:{m.chat.id}',id)
         r.set(f'{hmshelp}:7MRName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته حمار 🦓\n☆')
   
   if text == 'تنزيل حمار':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:7MRList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو حمار من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:7MRList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:7MRName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من حمار\n☆')
   
   if text == 'قائمه الحمير' or text == 'قائمة الحمير':
     if not r.smembers(f'{hmshelp}:7MRList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الحمير فاضية')
     else:
       txt = '- قائمة الحمير 🦓\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:7MRList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:7MRName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الحمير' or text == 'مسح قائمه الحمير':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:7MRList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الحمير فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الحمير')
         for cake in r.smembers(f'{hmshelp}:7MRList:{m.chat.id}'):
           r.srem(f'{hmshelp}:7MRList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:7MRName:{cake}')

   ################# 7MR #################
   
   ################# COW #################
   if text == 'رفع بقرة' or text == 'رفع بقره':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:COWList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} بقرة من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:COWList:{m.chat.id}',id)
         r.set(f'{hmshelp}:COWName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته بقرة 🐄\n☆')
   
   if text == 'تنزيل بقرة' or text == 'تنزيل بقره':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:COWList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو بقرة من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:COWList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:COWName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من بقرة\n☆')
   
   if text == 'قائمه البقر' or text == 'قائمة البقر':
     if not r.smembers(f'{hmshelp}:COWList:{m.chat.id}'):
       return m.reply(f'{k} قائمة البقر فاضية')
     else:
       txt = '- قائمة البقر 🐄\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:COWList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:COWName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة البقر' or text == 'مسح قائمه البقر':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:COWList:{m.chat.id}'):
         return m.reply(f'{k} قائمة البقر فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة البقر')
         for cake in r.smembers(f'{hmshelp}:COWList:{m.chat.id}'):
           r.srem(f'{hmshelp}:COWList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:COWName:{cake}')

   ################# COW #################
   
   ################# DOG #################
   if text == 'رفع كلب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:DOGList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} كلب من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:DOGList:{m.chat.id}',id)
         r.set(f'{hmshelp}:DOGName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته كلب 🐩\n☆')
   
   if text == 'تنزيل كلب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:DOGList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو كلب من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:DOGList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:DOGName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من كلب\n☆')
   
   if text == 'قائمه الكلاب' or text == 'قائمة الكلاب':
     if not r.smembers(f'{hmshelp}:DOGList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الكلاب فاضية')
     else:
       txt = '- قائمة الكلاب 🐩\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:DOGList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:DOGName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الكلاب' or text == 'مسح قائمه الكلاب':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:DOGList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الكلاب فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الكلاب')
         for cake in r.smembers(f'{hmshelp}:DOGList:{m.chat.id}'):
           r.srem(f'{hmshelp}:DOGList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:DOGName:{cake}')

   ################# DOG #################
   
   ################# MON #################
   if text == 'رفع قرد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:MONList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} قرد من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:MONList:{m.chat.id}',id)
         r.set(f'{hmshelp}:MONName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته قرد 🐒\n☆')
   
   if text == 'تنزيل قرد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:MONList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو قرد من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:MONList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:MONName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من قرد\n☆')
   
   if text == 'قائمه القرود' or text == 'قائمة القرود':
     if not r.smembers(f'{hmshelp}:MONList:{m.chat.id}'):
       return m.reply(f'{k} قائمة القرود فاضية')
     else:
       txt = '- قائمة القرود 🐒\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:MONList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:MONName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة القرود' or text == 'مسح قائمه القرود':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:MONList:{m.chat.id}'):
         return m.reply(f'{k} قائمة القرود فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة القرود')
         for cake in r.smembers(f'{hmshelp}:MONList:{m.chat.id}'):
           r.srem(f'{hmshelp}:MONList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:MONName:{cake}')

   ################# MON #################
   
   ################# TES #################
   if text == 'رفع تيس':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:TESList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تيس من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:TESList:{m.chat.id}',id)
         r.set(f'{hmshelp}:TESName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته تيس 🐐\n☆')
   
   if text == 'تنزيل تيس':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:TESList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو تيس من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:TESList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:TESName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من تيس\n☆')
   
   if text == 'قائمه التيس' or text == 'قائمة التيس':
     if not r.smembers(f'{hmshelp}:TESList:{m.chat.id}'):
       return m.reply(f'{k} قائمة التيوس فاضية')
     else:
       txt = '- قائمة التيوس 🐐\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:TESList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:TESName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة التيس' or text == 'مسح قائمه التيس':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:TESList:{m.chat.id}'):
         return m.reply(f'{k} قائمة التيوس فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة التيوس')
         for cake in r.smembers(f'{hmshelp}:TESList:{m.chat.id}'):
           r.srem(f'{hmshelp}:TESList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:TESName:{cake}')

   ################# TES #################
   
   
   ################# TOR #################
   if text == 'رفع ثور':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:TORList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ثور من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:TORList:{m.chat.id}',id)
         r.set(f'{hmshelp}:TORName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته ثور 🐂\n☆')
   
   if text == 'تنزيل ثور':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:TORList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو ثور من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:TORList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:TORName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من ثور\n༄')
   
   if text == 'قائمه الثور' or text == 'قائمة الثور':
     if not r.smembers(f'{hmshelp}:TORList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الثور فاضية')
     else:
       txt = '- قائمة الثور 🐂\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:TORList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:TORName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الثور' or text == 'مسح قائمه الثور':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:TORList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الثور فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الثور')
         for cake in r.smembers(f'{hmshelp}:TORList:{m.chat.id}'):
           r.srem(f'{hmshelp}:TORList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:TORName:{cake}')

   ################# TOR #################
   
   
   ################# B3S #################
   if text == 'رفع هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:B3SList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} هكر من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:B3SList:{m.chat.id}',id)
         r.set(f'{hmshelp}:B3SName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته هكر 🏅\n☆')
   
   if text == 'تنزيل هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:B3SList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو هكر من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:B3SList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:B3SName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من هكر\n☆')
   
   if text == 'قائمه الهكر' or text == 'قائمة الهكر':
     if not r.smembers(f'{hmshelp}:B3SList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الهكر فاضية')
     else:
       txt = '- قائمة الهكر 🏅\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:B3SList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:B3SName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الهكر' or text == 'مسح قائمه الهكر':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:B3SList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الهكر فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الهكر')
         for cake in r.smembers(f'{hmshelp}:B3SList:{m.chat.id}'):
           r.srem(f'{hmshelp}:B3SList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:B3SName:{cake}')

   ################# B3S #################
   
   ################# DJJ #################
   if text == 'رفع دجاجه' or text == 'رفع دجاجة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:DJJList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} دجاجه من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:DJJList:{m.chat.id}',id)
         r.set(f'{hmshelp}:DJJName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته دجاجه 🐓\n☆')
   
   if text == 'تنزيل دجاجه' or text == 'تنزيل دجاجة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:DJJList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو دجاجه من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:DJJList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:DJJName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من دجاجه\n☆')
   
   if text == 'قائمه الدجاج' or text == 'قائمة الدجاج':
     if not r.smembers(f'{hmshelp}:DJJList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الدجاج فاضية')
     else:
       txt = '- قائمة الدجاج 🐓\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:DJJList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:DJJName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الدجاج' or text == 'مسح قائمه الدجاج':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:DJJList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الدجاج فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الدجاج')
         for cake in r.smembers(f'{hmshelp}:DJJList:{m.chat.id}'):
           r.srem(f'{hmshelp}:DJJList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:DJJName:{cake}')

   ################# DJJ #################
   
   ################# HTF #################
   if text == 'رفع ملكه':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:HTFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ملكه من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:HTFList:{m.chat.id}',id)
         r.set(f'{hmshelp}:HTFName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته ملكه 🧱\n☆')
   
   if text == 'تنزيل ملكه':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:HTFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو ملكه من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:HTFList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:HTFName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من ملكه\n☆')
   
   if text == 'قائمه الهطوف' or text == 'قائمة الهطوف':
     if not r.smembers(f'{hmshelp}:HTFList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الهطوف فاضية')
     else:
       txt = '- قائمة الهطوف 🧱\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:HTFList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:HTFName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الهطوف' or text == 'مسح قائمه الهطوف':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:HTFList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الهطوف فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الهطوف')
         for cake in r.smembers(f'{hmshelp}:HTFList:{m.chat.id}'):
           r.srem(f'{hmshelp}:HTFList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:HTFName:{cake}')

   ################# HTF #################
   
   ################# SYD #################
   if text == 'رفع صياد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:SYDList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} صياد من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:SYDList:{m.chat.id}',id)
         r.set(f'{hmshelp}:SYDName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته صياد 🔫\n☆')
   
   if text == 'تنزيل صياد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:SYDList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو صياد من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:SYDList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:SYDName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من صياد\n☆')
   
   if text == 'قائمه الصيادين' or text == 'قائمة الصيادين':
     if not r.smembers(f'{hmshelp}:SYDList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الصيادين فاضية')
     else:
       txt = '- قائمة الصيادين 🔫\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:SYDList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:SYDName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الصيادين' or text == 'مسح قائمه الصيادين':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:SYDList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الصيادين فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الصيادين')
         for cake in r.smembers(f'{hmshelp}:SYDList:{m.chat.id}'):
           r.srem(f'{hmshelp}:SYDList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:SYDName:{cake}')

   ################# SYD #################
   
   ################# 5RF #################
   if text == 'رفع خروف':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:5RFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} خروف من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:5RFList:{m.chat.id}',id)
         r.set(f'{hmshelp}:5RFName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته خروف 🐏\n☆')
   
   if text == 'تنزيل خروف':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:5RFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو خروف من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:5RFList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:5RFName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من خروف\n☆')
   
   if text == 'قائمه الخرفان' or text == 'قائمة الخرفان':
     if not r.smembers(f'{hmshelp}:5RFList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الخرفان فاضية')
     else:
       txt = '- قائمة الخرفان 🐏\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:5RFList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:5RFName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الخرفان' or text == 'مسح قائمه الخرفان':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:5RFList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الخرفان فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الخرفان')
         for cake in r.smembers(f'{hmshelp}:5RFList:{m.chat.id}'):
           r.srem(f'{hmshelp}:5RFList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:5RFName:{cake}')

   ################# 5RF #################
   
   ################# TEZ #################
   if text == 'رفع هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{hmshelp}:TEZList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} هكر من قبل\n☆')
       else:
         r.sadd(f'{hmshelp}:TEZList:{m.chat.id}',id)
         r.set(f'{hmshelp}:TEZName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته هكر ♕\n☆')
   
   if text == 'تنزيل هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{hmshelp}:TEZList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو هكر من قبل\n☆')
       else:
         r.srem(f'{hmshelp}:TEZList:{m.chat.id}',id)
         r.delete(f'{hmshelp}:TEZName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من هكر\n☆')
   
   if text == 'قائمه هكر' or text == 'قائمة هكر':
     if not r.smembers(f'{hmshelp}:TEZList:{m.chat.id}'):
       return m.reply(f'{k} قائمة هكر فاضية')
     else:
       txt = '- قائمة هكر ♕\n'
       count = 1
       for cake in r.smembers(f'{hmshelp}:TEZList:{m.chat.id}'):
          mention = r.get(f'{hmshelp}:TEZName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة هكر' or text == 'مسح قائمه هكر':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{hmshelp}:TEZList:{m.chat.id}'):
         return m.reply(f'{k} قائمة هكر فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة هكر')
         for cake in r.smembers(f'{hmshelp}:TEZList:{m.chat.id}'):
           r.srem(f'{hmshelp}:TEZList:{m.chat.id}',int(cake))
           r.delete(f'{hmshelp}:TEZName:{cake}')

   ################# TEZ #################
   
   ################# 🔮 #################
   
   if text == 'رفع بقلبي' and m.reply_to_message:
     return m.reply('{} رفعته لقلبك\n{} اللهم حسد 😔'.format(k,k))
   
   if text == 'تنزيل من قلبي' and m.reply_to_message:
     return m.reply('اح اح ماتوصل')
   