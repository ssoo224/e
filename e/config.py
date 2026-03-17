
import redis
r = redis.Redis('localhost', decode_responses=True)
token = '8650990801:AAFnanKsGXF7D9_znW9sxMtHzZXYD8Nb6Fg'
hmshelp = token.split(':')[0]
sudo_id = 7115002714

botUsername = 'cvetuwbot'
from kvsqlite.sync import Client as DB
ytdb = DB('ytdb.sqlite')
sounddb = DB('sounddb.sqlite')
wsdb = DB('wsdb.sqlite')