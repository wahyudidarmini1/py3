# -*- coding: utf-8 -*-
import linepy
from linepy import *
from bs4 import BeautifulSoup
from datetime import datetime
#import json, time, random, tempfile, os, sys
#from gtts import gTTS
import time,random,sys,re,os,json,subprocess,threading,string,codecs,requests,tweepy,ctypes,urllib,tempfile,glob,shutil,unicodedata,urllib3
import html5lib
from gtts import gTTS
from googletrans import Translator
import logging
from threading import Thread

koplaxs = LineChannel(authToken='Esp2g4mSTvBR9IKjwjg5.7E95ZLqvL4PJdrLCOdm3Tq.g/c6HeoXTqmNbHmDrYn0+Z0hwPdhniLW7iSD/spcls0=')
#client.log("Auth Token : " + str(client.authToken))
channelboss = LineChannel(koplaxs) #Koplaxs
#client = LineClient() #untuk login qr in here
#client = LineClient(email='koplaxs1992@gmail.com', passwd='navy1992') #login email in here
client = LineClient(authToken='EsFEz4oGVmg2h9PtcDn6.w9BYAQTGAvGAkA1O6vuYzG.+qfsikiRYqtH4+4/WE0hA/FjmyssAk9HhiEygCAKgHA=')
#client.log("Auth Token : " + str(client.authToken))
channel = LineChannel(client) #Luffy
#client.log("Channel Access Token : " + str(channel.channelAccessToken))

k2 = LineClient(authToken='Es9Pv99GnW7NLY9AlXl9.gdzBS6/RQ+e0rHS8qtnvkq.kofQbK4ZcrgY4IVKTWYO7CMMTVaoFPthWXGHGmlwI5E=')
#k2.log("Auth Token : " + str(k2.authToken))
channel2 = LineChannel(k2) #Zoro
#k2.log("Channel Access Token : " + str(channel2.channelAccessToken))

k3 = LineClient(authToken='Esck4e72CrKt6si2nqU3.Y5ADuB5JChMEIGOjDMa/iW.NT0pMR5+zoJuHIXtqW2NvhH3Ce8uh/E15RxEyrkKr5E=')
#k3.log("Auth Token : " + str(k3.authToken))
channel3 = LineChannel(k3) #Sanji
#k3.log("Channel Access Token : " + str(channel3.channelAccessToken))

k4 = LineClient(authToken='EsFBO3jLf0wZ5dvyjxAf.7aUWl0wHMjrmRy8MZP4SFW.OVmszeK6An6DwrmZHelHyt8OWYr/S9XSai0JP0oCGko=')
#k4.log("Auth Token : " + str(k4.authToken))
channel4 = LineChannel(k4) #Ussop
#k4.log("Channel Access Token : " + str(channel4.channelAccessToken))

k5 = LineClient(authToken='EsgoKeRxrOZOB15Yjm33.9+8yAKSSYiX7/n/jkRW24W.gHDnMMb8UE4KbgJ8V6dDdaiJvi7NWQs9o8xoDXVmH9M=')
#k5.log("Auth Token : " + str(k5.authToken))
channel5 = LineChannel(k5) #Chooper
#k5.log("Channel Access Token : " + str(channel5.channelAccessToken))

k6 = LineClient(authToken='EsrHoOUl5n0mirHD6Ccf.EaAi18d1vBXlV8lcG/963W.0Fn/8sQP/S7ZS6K9R6GUH2GcItdcIP74tNC8yDx42pc=')
#k6.log("Auth Token : " + str(k6.authToken))
channel6 = LineChannel(k6) #Franky
#k6.log("Channel Access Token : " + str(channel6.channelAccessToken))

k7 = LineClient(authToken='EsAnjRIwbzAVEEDLw1Ne.rmbx1I8l5KdoGwmOJHBG3G.9oI5ZNoR/C1aK/921900JoAiBs+QXedk0++p/B31UC4=')
#k7.log("Auth Token : " + str(k7.authToken))
channel7 = LineChannel(k7) #Brook
#k7.log("Channel Access Token : " + str(channel7.channelAccessToken))

k8 = LineClient(authToken='EsvPrqumoRwj2ViKyiS4.H+383kQzMgR7vEEtYjb25a.vni7CAkcXkTosLKuDuJBSPe2lQCza6QKmoBxqDgBR6Y=')
#k8.log("Auth Token : " + str(k8.authToken))
channel8 = LineChannel(k8) #Nami
#k8.log("Channel Access Token : " + str(channel8.channelAccessToken))

k9 = LineClient(authToken='Es5wmAYapdgDRHaLC5x0.xVDZX1moRnRxb2NyFdZSma.qnQSxLHrdaTBQXjTwUX7hc+gFEl7iXwIQW6i3pM5Z58=')
#k9.log("Auth Token : " + str(k9.authToken))
channel9 = LineChannel(k9) #Robin
#k9.log("Channel Access Token : " + str(channel9.channelAccessToken))

k10 = LineClient(authToken='EsDn9l6ONhCN6lRFKoO9.7pqSa4Wu+XAr5+QQAiuV6q.x99UstYL9Yt3B91tV9ZwI34K6nwe8TvNzAMhDI/9pR8=')
#k10.log("Auth Token : " + str(k10.authToken))
channel10 = LineChannel(k10) #Jinbei
#k10.log("Channel Access Token : " + str(channel10.channelAccessToken))

cl = client

print ("بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ")

helpMessage ="""
════════════════
║ᴘᴏᴡᴇʀ║ʀᴀɴɢᴇʀ║ʜᴇʟᴘ
════════════════
║╠[👿]ᴘᴜʙʟɪᴄ ᴍᴇɴᴜ
║╠[👿]ᴀᴅᴍɪɴ ᴍᴇɴᴜ
║╠[👿]ᴏᴡɴᴇʀ ᴍᴇɴᴜ
╠═══════════════
║╠[👿]ᴄʀᴇᴀᴛᴏʀ :
║╠[👿]ᴏᴡɴᴇʀ1 :ғᴀᴅʟᴀɴ
║╠[👿]ᴏᴡɴᴇʀ2 :✰ќờᎮḽλẍֆ✰
║╠[👿]ᴏᴡɴᴇʀ3 :ᴘʀᴀs
╠═══════════════
║╠[👿]ᴠᴇʀsɪᴏɴ :
║╠[👿]ʙᴏᴛ : ᴘᴀsᴜᴋᴀɴ 1
║╠[👿]ᴊᴜᴍʟᴀʜ ʙᴏᴛ : 10 ʙᴏᴛ
║╠[👿]ʙᴏᴛ ᴠᴇʀsɪᴏɴ : 3.5
║╠[👿]sʏsᴛᴇᴍ : ᴘʏᴛʜᴏɴ 3
╠═══════════════
║╠[👿]ᴛʏᴘᴇ ʙᴏᴛ :
║╠[👿]ᴏɴᴇ ᴘɪᴇᴄᴇ
╠═══════════════
║╠[👿]ᴇᴅɪᴛᴇᴅ ʙʏ :
║╠[👿] 🇫​🇦​🇩​
║╠[👿] 🇦​🇷​🇴​🇪​🇱​
════════════════
"""

MOwner ="""
════════════════
║ᴘᴏᴡᴇʀ║ʀᴀɴɢᴇʀ║ᴏᴡɴᴇʀ
════════════════
║→ᴘᴇʀɪɴᴛᴀʜ ᴘʀᴏᴛᴇᴋsɪ←
║♣sᴛᴀᴛᴜs
║♣ᴘʀᴏᴛᴇᴄᴛ ᴋɪᴄᴋ ᴏɴ/ᴏғғ
║♣ᴘʀᴏᴛᴇᴄᴛ ϙʀ ᴏɴ/ᴏғғ
║♣ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏɴ/ᴏғғ
║♣ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ/ᴏғғ
║♣ɢʀᴏᴜᴘ ᴀᴅᴅ
║♣ɢʀᴏᴜᴘ ʀᴇᴍᴏᴠᴇ
║♣ᴘʀᴏᴛᴇᴄᴛʟɪsᴛ
║╔═════════════
║╠[👿]ʀᴇsᴘᴏɴ
║╠[👿]ᴄᴄᴛᴠ→ᴄɪᴅᴜᴋ
║╠[👿]sɪᴅᴇʀ ᴏɴ/ᴏғғ
║╠[👿]ᴛᴀɢ
║╠[👿]ᴍᴇ
║╠[👿]ɢɴ <Nama Group>
║╠[👿]ᴏᴡɴᴇʀ ᴀᴅᴅ: <Mid>
║╠[👿]ᴏᴡɴᴇʀ ʀᴇᴍᴏᴠᴇ: <Mid>
║╠[👿]ᴏᴡɴᴇʀʟɪsᴛ
║╠[👿]ᴀᴅᴍɪɴ ᴀᴅᴅ: <Mid>
║╠[👿]ᴀᴅᴍɪɴ ʀᴇᴍᴏᴠᴇ: <Mid>
║╠[👿]ᴀᴅᴍɪɴʟɪsᴛ
║╠[👿]sᴛᴀғғ ᴀᴅᴅ: <Mid>
║╠[👿]sᴛᴀғғ ʀᴇᴍᴏᴠᴇ: <Mid>
║╠[👿]sᴛᴀғғʟɪsᴛ
║╠[👿]ᴍɪᴅ @
║╠[👿]sᴘᴇᴇᴅ
║╠[👿]ʙᴀɴ
║╠[👿]ʙᴀɴ @
║╠[👿]ᴜɴʙᴀɴ
║╠[👿]ᴜɴʙᴀɴ @
║╠[👿]ᴄʟᴇᴀʀ ʙᴀɴ
║╠[👿]ʙᴀɴʟɪsᴛ
║╠[👿]ᴄʀᴇᴀᴛᴏʀ
║╠[👿]ᴄʀᴇᴀᴛᴏʀ²
║╠[👿]ʀᴜɴᴛɪᴍᴇ
║╠[👿]ʙᴄ <Text>
║╠[👿]ʙᴄ ɢʀᴏᴜᴘ <Text>
║╠[👿]ᴄᴇᴋ ᴍᴇᴍʙᴇʀ
║╠[👿]ᴄʀᴀsʜʜ
║╠[👿]ʙʟᴏᴄᴋ @
║╠[👿]ʙʟᴏᴄᴋʟɪsᴛ
║╠[👿]sᴘᴀᴍ ᴏɴ <Jumlah> <Text>
║╠[👿]ɪɴғᴏ ɢʀᴏᴜᴘ
║╠[👿]ʟɪsᴛ ɢʀᴏᴜᴘ
║╠[👿]ᴘᴘ @
║╠[👿]ᴅᴘ @
║╠[👿]ɴᴀᴍᴀ @
║╠[👿]ᴠɪᴅᴇᴏ @
║╠[👿]sᴛᴇᴀʟ ɢʀᴏᴜᴘ
║╠[👿]ʙᴜᴋᴀ/ᴛᴜᴛᴜᴘ ϙʀ
║╠[👿]ʟɪɴᴋ ɢʀᴏᴜᴘ
║╠[👿]ᴋɪʟʟ ʙᴀɴ
║╠[👿]ᴋɪᴄᴋ @
║╠[👿]ᴄᴏᴘʏ @
║╠[👿]ʙᴀᴄᴋᴜᴘ
║╚═════════════
║→ᴘᴇʀɪɴᴛᴀʜ ʜɪʙᴜʀᴀɴ←
║♥ᴍᴜsɪᴋ <Judul>
║♥ʟɪʀɪᴋ <Judul>
║♥ʏᴏᴜᴛᴜʙᴇ: <Judul>
║♥ғᴀᴄᴇʙᴏᴏᴋ <username>
║♥ɪɢ: <username>
║♥sᴀʏ <Terserah>
║♥ɪsᴀʏ <Terserah>
║♥jsᴀʏ <Terserah>
║♥ᴀsᴀʏ <Terserah>
║→ᴛᴀᴍʙᴀʜᴀɴ←
║♠ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ/ᴏғғ
║♠ᴀᴜᴛᴏ ᴀᴅᴅ ᴏɴ/ᴏғғ
║♠ᴄᴏɴᴛᴀᴄᴛ ᴏɴ/ᴏғғ
╠═══════════════
║╠[👿]ᴛʏᴘᴇ ʙᴏᴛ :
║╠[👿]ᴏɴᴇ ᴘɪᴇᴄᴇ
╠═══════════════
║╠[👿]EDITED BY :
║╠[👿] 🇫​🇦​🇩​
║╠[👿] 🇦​🇷​🇴​🇪​🇱​
════════════════
"""

MAdmin = """
════════════════
║ᴘᴏᴡᴇʀ║ʀᴀɴɢᴇʀ║ᴀᴅᴍɪɴ
════════════════
║╠[👿]sᴛᴀᴛᴜs
║╠[👿]ʀᴇsᴘᴏɴ
║╠[👿]ᴄᴄᴛᴠ→ᴄɪᴅᴜᴋ
║╠[👿]sɪᴅᴇʀ ᴏɴ
║╠[👿]ᴛᴀɢ
║╠[👿]ᴍᴇ
║╠[👿]ɢɴ <Nama Group>
║╠[👿]sᴘᴇᴇᴅ
║╠[👿]ʙᴀɴʟɪsᴛ
║╠[👿]ᴄʀᴇᴀᴛᴏʀ
║╠[👿]ᴄʀᴇᴀᴛᴏʀ²
║╠[👿]ʀᴜɴᴛɪᴍᴇ
║╠[👿]ɪɴғᴏ ɢʀᴏᴜᴘ
║╠[👿]ᴘᴘ @
║╠[👿]ᴅᴘ @
║╠[👿]ɴᴀᴍᴀ @
║╠[👿]ᴠɪᴅᴇᴏ @
║╠[👿]sᴛᴇᴀʟ ɢʀᴏᴜᴘ
║╠[👿]ʙᴜᴋᴀ/ᴛᴜᴛᴜᴘ ϙʀ
║╠[👿]ʟɪɴᴋ ɢʀᴏᴜᴘ
║╠[👿]ᴋɪᴄᴋ @
║╚════════════
║→ᴘᴇʀɪɴᴛᴀʜ ʜɪʙᴜʀᴀɴ←
║♥ᴍᴜsɪᴋ <Judul>
║♥ʟɪʀɪᴋ <Judul>
║♥ʏᴏᴜᴛᴜʙᴇ: <Judul>
║♥ғᴀᴄᴇʙᴏᴏᴋ <username>
║♥ɪɢ: <username>
║♥sᴀʏ <Terserah>
║♥ɪsᴀʏ <Terserah>
║♥Jsᴀʏ <Terserah>
║♥Asᴀʏ <Terserah>
╠═══════════════
║╠[👿]ᴛʏᴘᴇ ʙᴏᴛ :
║╠[👿]ᴏɴᴇ ᴘɪᴇᴄᴇ
╠═══════════════
║╠[👿]ᴇᴅɪᴛᴇᴅ ʙʏ :
║╠[👿]🇫​🇦​🇩​
║╠[👿] 🇦​🇷​🇴​🇪​🇱​
════════════════
"""

MPublic = """
════════════════
║POWER║RANGER║PUBLIC
════════════════
║╠[👿]Me
║╠[👿]Creator1
║╠[👿]Creator2
║╠[👿]Creator3
║╠[👿]Runtime
║╠[👿]Apakah <tanya>
║╠[👿]Welcome
╠═══════════════
║╠[👿]TYPE BOT :
║╠[👿]ONE PIECE
╠═══════════════
║╠[👿]EDITED BY :
║╠[👿] Fad
║╠[👿] 😛
════════════════
"""
poll = LinePoll(client)
poll2 = LinePoll(k2)
poll3 = LinePoll(k3)
poll4 = LinePoll(k4)
poll5 = LinePoll(k5)
poll6 = LinePoll(k6)
poll7 = LinePoll(k7)
poll8 = LinePoll(k8)
poll9 = LinePoll(k9)
poll10 = LinePoll(k10)
pollboss = LinePoll(koplaxs)

KAC=[cl,k2,k3,k4,k5,k6,k7,k8,k9,k10]
mid = cl.getProfile().mid
mid2 = k2.getProfile().mid
mid3 = k3.getProfile().mid
mid4 = k4.getProfile().mid
mid5 = k5.getProfile().mid
mid6 = k6.getProfile().mid
mid7 = k7.getProfile().mid
mid8 = k8.getProfile().mid
mid9 = k9.getProfile().mid
mid10 = k10.getProfile().mid
midkoplaxs = koplaxs.getProfile().mid

Bots=[mid,mid2,mid3,mid4,mid5,mid6,mid7,mid8,mid9,mid10]
owner=["u1112a364f49ad61d6ca5ec5bc9d6d375","ued156c86ffa56024c0acba16f7889e6d","u88cd7ee9fd691d6306e5e19be5d16f69"] 
admin=[
  "u1112a364f49ad61d6ca5ec5bc9d6d375", #Fadlan
  "u61e7226d767ed789511ddaecafdc9e62", #Kak Fyfy
  "ubfb4ddb05b6d5a05215083404887ab85", #Bg Aroel
  "uff311a7f8eb86f0bdac17beb82626137"] ##Bg Ressa
  #"", #Crz
  #"", #Blue
  #""] #Admin Event
staff=[
  "u1b109c6de9d2eaec4e82195eda37d2e9", #Vera
  "u400b0b0dbdcafbd8720cd513df757c7e", #Nita
  "u660460365abd4a2ff3191b025831c64f", #Vitri
  "ua4dba8a4b5e291b62aef9192999ffd70", #Vira
  "u8f8179e37a1c9da4fc36853b3fc7c9ec", #Lion
  "ud6f594e283cccf71d35e247e0a0c35cc"] #Bunda

groupList=[
    "c483ce06d735c647d124d987517b93c04", #Power Rangers
    "c3454bc445d166960b8a1089c4747e882", #VROne
    "c25f3bae6ef89374c1e1d64307972f2cc"] #Goblin Hunter Team
    #"", #Pasukan 1
    #"", #CSCI
    #""] #Event1

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
≫ P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉  ≪

Ready:

≫ Bot Protect ≪
≫ SelfBot ≪
≫ VPS Google Clouds ≪

ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆ ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ ☆
☆ P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉  ☆


Minat? Silahkan PM!
Idline: http://line.me/ti/p/~4dlantobing""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    'pap':{},
    'likeOn':{},
    'Leave':{},    
    "Sider":{},
    "BlGroup":{},
    "commentLike":"🌟Autolike By 🌟\n✰Fadlan✰\nP҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ",
    "winvite" :True,
    "winvite2" :True,
    "winvite3" :True,
    "winvite4" :True,
    "winvite5" :True,
    "winvite6" :True,
    "winvite7" :True,
    "winvite8" :True,
    "winvite9" :True,
    "winvite10" :True,
    "wblacklist":False,
    "dblacklist":False,
    "pname":{},
    "pro_name":{},
    "Protectgr":True,
    "Protectcancl":True,
    "Protectcancel":True,
    "Protectkick":True,
    "atjointicket":True
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

contact = cl.getProfile()
restoreprofile = cl.getProfile()
restoreprofile.displayName = contact.displayName
restoreprofile.statusMessage = contact.statusMessage                        
restoreprofile.pictureStatus = contact.pictureStatus

contact = cl.getProfile() 
backup = cl.getProfile() 
backup.displayName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
      
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
  
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
    
def mention(self, to, nama):
        aa = ""
        bb = ""
        strt = int(0)
        akh = int(0)
        nm = nama
        myid = self.talk.getProfile().mid
        if myid in nm:    
            nm.remove(myid)
        for mm in nm:
          akh = akh + 6
          aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
          strt = strt + 7
          akh = akh + 1
          bb += "@nrik \n"
        aa = (aa[:int(len(aa)-1)])
        text = bb
        try:
            msg = Message()
            msg.to = to
            msg.text = text
            msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}'}
            msg.contentType = 0
            self.talk.sendMessage(0, msg)
        except Exception as error:
           print(error, 'def Mention')
           
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print (error)

#while True:
  #try:
    #ops=poll.trace(threading=True)
    #ops=poll2.trace(threading=True)
    #ops=poll3.trace(threading=True)
    #ops=poll4.trace(threading=True)
    #ops=poll5.trace(threading=True)
    #ops=poll6.trace(threading=True)
    #ops=poll7.trace(threading=True)
    #ops=poll8.trace(threading=True)
    #ops=poll9.trace(threading=True)
    #ops=poll10.trace(threading=True)
    #if ops != None:
      #for op in ops:
def bot(op):
        
        if op.type == 26:
          msg = op.message
          text = msg.text
          msg_id = msg.id
          receiver = msg.to
          sender = msg._from
          try:
            if msg.contentType == 16:
              if wait['likeOn'] == True:
                url = msg.contentMetadata["postEndUrl"]
                cl.likePost(url[25:58], url[66:], likeType=1005)
                k2.likePost(url[25:58], url[66:], likeType=1002)
                k3.likePost(url[25:58], url[66:], likeType=1004)
                k4.likePost(url[25:58], url[66:], likeType=1003)
                k5.likePost(url[25:58], url[66:], likeType=1001)
                k6.likePost(url[25:58], url[66:], likeType=1001)
                k7.likePost(url[25:58], url[66:], likeType=1001)
                k8.likePost(url[25:58], url[66:], likeType=1001)
                k9.likePost(url[25:58], url[66:], likeType=1001)
                k10.likePost(url[25:58], url[66:], likeType=1001)
                cl.createComment(url[25:58], url[66:], wait["commentLike"])
                cl.createComment(url[25:58], url[66:], wait["commentLike"])
                k2.sendText(msg.to,"Like Success")                     
                k3.createComment(url[25:58], url[66:], wait["commentLike"])
                k4.createComment(url[25:58], url[66:], wait["commentLike"])
                k5.createComment(url[25:58], url[66:], wait["commentLike"])
                k6.createComment(url[25:58], url[66:], wait["commentLike"])
                k7.createComment(url[25:58], url[66:], wait["commentLike"])
                k8.createComment(url[25:58], url[66:], wait["commentLike"])
                k9.createComment(url[25:58], url[66:], wait["commentLike"])
                k10.createComment(url[25:58], url[66:], wait["commentLike"])
                wait['likeOn'] = False
              
            elif msg.contentType == 13:
              if wait["winvite"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = cl.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      cl.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      cl.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        cl.inviteIntoGroup(msg.to,[target])
                        cl.sendText(msg.to,"Already Invited Boss 💋: \n➡" + _name)
                        wait["winvite"] = False
                        break
                      except:
                        try:
                          cl.findAndAddContactsByMid(invite)
                          cl.inviteIntoGroup(op.param1,[invite])
                          wait["winvite"] = False
                        except:
                          try:
                            cl.findAndAddContactsByMid(invite)
                            cl.inviteIntoGroup(op.param1,[invite])
                            wait["winvite"] = False
                            cl.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              cl.findAndAddContactsByMid(invite)
                              cl.inviteIntoGroup(op.param1,[invite])
                              wait["winvite"] = False
                              cl.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              cl.sendText(msg.to,"Negative, Error detected")
                              wait["winvite"] = False
                              break
              elif wait["winvite2"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = k2.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      k2.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      k2.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      k2.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        k2.findAndAddContactsByMid(target)
                        k2.inviteIntoGroup(msg.to,[target])
                        k2.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite2"] = False
                        break
                      except:
                        try:
                          k2.findAndAddContactsByMid(invite)
                          k2.inviteIntoGroup(op.param1,[invite])
                          wait["winvite2"] = False
                        except:
                          try:
                            k2.findAndAddContactsByMid(invite)
                            k2.inviteIntoGroup(op.param1,[invite])
                            wait["winvite2"] = False
                            k2.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              k2.findAndAddContactsByMid(invite)
                              k2.inviteIntoGroup(op.param1,[invite])
                              wait["winvite2"] = False
                              k2.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              k2.sendText(msg.to,"Negative, Error detected")
                              wait["winvite2"] = False
                              break
              elif wait["winvite3"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = k3.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      k3.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      k3.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      k3.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        k3.findAndAddContactsByMid(target)
                        k3.inviteIntoGroup(msg.to,[target])
                        k3.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite3"] = False
                        break
                      except:
                        try:
                          k3.findAndAddContactsByMid(invite)
                          k3.inviteIntoGroup(op.param1,[invite])
                          wait["winvite3"] = False
                        except:
                          try:
                            k3.findAndAddContactsByMid(invite)
                            k3.inviteIntoGroup(op.param1,[invite])
                            wait["winvite3"] = False
                            k3.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              k3.findAndAddContactsByMid(invite)
                              k3.inviteIntoGroup(op.param1,[invite])
                              wait["winvite3"] = False
                              k3.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              k3.sendText(msg.to,"Negative, Error detected")
                              wait["winvite3"] = False
                              break
              elif wait["winvite4"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = k4.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      k4.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      k4.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      k4.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        k4.findAndAddContactsByMid(target)
                        k4.inviteIntoGroup(msg.to,[target])
                        k4.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite4"] = False
                        break
                      except:
                        try:
                          k4.findAndAddContactsByMid(invite)
                          k4.inviteIntoGroup(op.param1,[invite])
                          wait["winvite4"] = False
                        except:
                          try:
                            k4.findAndAddContactsByMid(invite)
                            k4.inviteIntoGroup(op.param1,[invite])
                            wait["winvite4"] = False
                            k4.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              k4.findAndAddContactsByMid(invite)
                              k4.inviteIntoGroup(op.param1,[invite])
                              wait["winvite4"] = False
                              k4.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              k4.sendText(msg.to,"Negative, Error detected")
                              wait["winvite4"] = False
                              break
              elif wait["winvite5"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = k5.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      k5.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      k5.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      k5.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        k5.findAndAddContactsByMid(target)
                        k5.inviteIntoGroup(msg.to,[target])
                        k5.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite5"] = False
                        break
                      except:
                        try:
                          k5.findAndAddContactsByMid(invite)
                          k5.inviteIntoGroup(op.param1,[invite])
                          wait["winvite5"] = False
                        except:
                          try:
                            k5.findAndAddContactsByMid(invite)
                            k5.inviteIntoGroup(op.param1,[invite])
                            wait["winvite5"] = False
                            k5.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              k5.findAndAddContactsByMid(invite)
                              k5.inviteIntoGroup(op.param1,[invite])
                              wait["winvite5"] = False
                              k5.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              k5.sendText(msg.to,"Negative, Error detected")
                              wait["winvite5"] = False
                              break
              elif wait["winvite6"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = k6.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      k6.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      k6.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      k6.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        k6.findAndAddContactsByMid(target)
                        k6.inviteIntoGroup(msg.to,[target])
                        k6.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite6"] = False
                        break
                      except:
                        try:
                          k6.findAndAddContactsByMid(invite)
                          k6.inviteIntoGroup(op.param1,[invite])
                          wait["winvite6"] = False
                        except:
                          try:
                            k6.findAndAddContactsByMid(invite)
                            k6.inviteIntoGroup(op.param1,[invite])
                            wait["winvite6"] = False
                            k6.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              k6.findAndAddContactsByMid(invite)
                              k6.inviteIntoGroup(op.param1,[invite])
                              wait["winvite6"] = False
                              k6.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              k6.sendText(msg.to,"Negative, Error detected")
                              wait["winvite6"] = False
                              break
              
              elif wait["winvite7"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = k7.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      k7.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      k7.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      k7.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        k7.findAndAddContactsByMid(target)
                        k7.inviteIntoGroup(msg.to,[target])
                        k7.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite7"] = False
                        break
                      except:
                        try:
                          k7.findAndAddContactsByMid(invite)
                          k7.inviteIntoGroup(op.param1,[invite])
                          wait["winvite7"] = False
                        except:
                          try:
                            k7.findAndAddContactsByMid(invite)
                            k7.inviteIntoGroup(op.param1,[invite])
                            wait["winvite7"] = False
                            k7.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              k7.findAndAddContactsByMid(invite)
                              k7.inviteIntoGroup(op.param1,[invite])
                              wait["winvite7"] = False
                              k7.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              k7.sendText(msg.to,"Negative, Error detected")
                              wait["winvite7"] = False
                              break
              
              elif wait["winvite8"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = k8.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      k8.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      k8.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      k8.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        k8.findAndAddContactsByMid(target)
                        k8.inviteIntoGroup(msg.to,[target])
                        k8.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite8"] = False
                        break
                      except:
                        try:
                          k8.findAndAddContactsByMid(invite)
                          k8.inviteIntoGroup(op.param1,[invite])
                          wait["winvite8"] = False
                        except:
                          try:
                            k8.findAndAddContactsByMid(invite)
                            k8.inviteIntoGroup(op.param1,[invite])
                            wait["winvite8"] = False
                            k8.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              k8.findAndAddContactsByMid(invite)
                              k8.inviteIntoGroup(op.param1,[invite])
                              wait["winvite8"] = False
                              k8.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              k8.sendText(msg.to,"Negative, Error detected")
                              wait["winvite8"] = False
                              break
              
              elif wait["winvite9"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = k9.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      k9.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      k9.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      k9.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        k9.findAndAddContactsByMid(target)
                        k9.inviteIntoGroup(msg.to,[target])
                        k9.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite9"] = False
                        break
                      except:
                        try:
                          k9.findAndAddContactsByMid(invite)
                          k9.inviteIntoGroup(op.param1,[invite])
                          wait["winvite9"] = False
                        except:
                          try:
                            k9.findAndAddContactsByMid(invite)
                            k9.inviteIntoGroup(op.param1,[invite])
                            wait["winvite9"] = False
                            k9.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              k9.findAndAddContactsByMid(invite)
                              k9.inviteIntoGroup(op.param1,[invite])
                              wait["winvite9"] = False
                              k9.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              k9.sendText(msg.to,"Negative, Error detected")
                              wait["winvite9"] = False
                              break
              
              elif wait["winvite10"] == True:
                #if msg._from in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = k10.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      k10.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      k10.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      k10.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        k10.findAndAddContactsByMid(target)
                        k10.inviteIntoGroup(msg.to,[target])
                        k10.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite10"] = False
                        break
                      except:
                        try:
                          k10.findAndAddContactsByMid(invite)
                          k10.inviteIntoGroup(op.param1,[invite])
                          wait["winvite10"] = False
                        except:
                          try:
                            k10.findAndAddContactsByMid(invite)
                            k10.inviteIntoGroup(op.param1,[invite])
                            wait["winvite10"] = False
                            k10.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              k10.findAndAddContactsByMid(invite)
                              k10.inviteIntoGroup(op.param1,[invite])
                              wait["winvite10"] = False
                              k10.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              k10.sendText(msg.to,"Negative, Error detected")
                              wait["winvite10"] = False
                              break
                              
              elif wait["wblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  cl.sendText(msg.to,"already")
                  wait["wblack"] = False
                else:
                  wait["commentBlack"][msg.contentMetadata["mid"]] = True
                  wait["wblack"] = False
                  cl.sendText(msg.to,"decided not to comment")
                  
              elif wait["dblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  del wait["commentBlack"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  wait["dblack"] = False
                else:
                  wait["dblack"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  
              elif wait["wblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  cl.sendText(msg.to,"already")
                  wait["wblacklist"] = False
                else:
                  wait["blacklist"][msg.contentMetadata["mid"]] = True
                  wait["wblacklist"] = False
                  cl.sendText(msg.to,"aded")
                  
              elif wait["dblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  del wait["blacklist"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  wait["dblacklist"] = False
                else:
                  wait["dblacklist"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  
              elif wait["contact"] == True:
                msg.contentType = 0
                cl.sendText(msg.to,msg.contentMetadata["mid"])
                if 'displayName' in msg.contentMetadata:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    pass
                else:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    pass
            
            elif msg.contentType == 0:
              if msg.text in ["Help","help","Key"]:
              #if msg._from in owner:
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,helpMessage)
                else:
                  cl.sendText(msg.to,helpMessage)
                    
              elif msg.text in ["Admin menu","admin menu"]:
                if msg._from in admin:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,MAdmin)
                  else:
                    cl.sendText(msg.to,MAdmin)
                else:
                  cl.sendText(msg.to,"This Command Only For Admin & Owner")
                    
              elif msg.text in ["Public menu","public menu"]:
                #if msg._from in owner:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,MPublic)
                  else:
                    cl.sendText(msg.to,MPublic)
                    
              elif msg.text in ["Owner menu","owner menu"]:
                if msg._from in owner:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,MOwner)
                  else:
                    cl.sendText(msg.to,MOwner)
                else:
                  cl.sendText(msg.to,"This Command Only For Owner")
                    
              elif "Group add " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("Group add ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                  else:
                    if gid in groupList:
                      cl.sendText(msg.to,"This Group Already in Protect List Boss")
                      #pass
                    else:
                      groupList.append(gid)
                      cl.sendText(msg.to,"Group Added to Protect List")
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")
                
              elif "Group remove " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("Group remove ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                  else:
                    if gid in groupList:
                      groupList.remove(gid)
                      cl.sendText(msg.to,"Group Deleted From Protect List")
                    else:
                      cl.sendText(msg.to,"This Group Not in Protect List Boss")
                      #pass
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")
                
              elif "Protectlist" in msg.text:
                if msg._from in admin:
                  if groupList == []:
                    cl.sendText(msg.to,"Protect List is empty")
                  else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = "╔════════════════\n║⭐Group On Protected⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                    for mi_d in groupList:
                      mc += "║[★]" + cl.getGroup(mi_d).name + "\n"
                    cl.sendText(msg.to,mc)
                    
              elif "Admin add: " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("Admin add: ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid Mid")
                  else:
                    if gid in admin:
                      cl.sendText(msg.to,"Makhluk Ini Sudah Jadi Admin Boss")
                      #pass
                    else:
                      admin.append(gid)
                      cl.sendText(msg.to,"Added to Admin List")
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")
                
              elif "Owner add: " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("Owner add: ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid Mid")
                  else:
                    if gid in owner:
                      cl.sendText(msg.to,"Makhluk Ini Sudah Jadi Owner Boss")
                      #pass
                    else:
                      owner.append(gid)
                      cl.sendText(msg.to,"Added to Owner List")
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")
                  
              elif "Staff add: " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("Staff add: ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid Mid")
                  else:
                    if gid in staff:
                      cl.sendText(msg.to,"Makhluk Ini Sudah Jadi Staff Boss")
                      #pass
                    else:
                      staff.append(gid)
                      cl.sendText(msg.to,"Added to Staff List")
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")
                  
              elif "Staff remove: " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("Staff remove: ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid Mid")
                  else:
                    if gid in staff:
                      staff.remove(gid)
                      cl.sendText(msg.to,"Deleted From Staff List")
                    else:
                      cl.sendText(msg.to,"This Person Not in Staff List Boss")
                      #pass
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")

              elif "Friend add: " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("Friend add: ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid Mid")
                  else:
                    for cmin in gid:
                      try:
                        cl.getContact(cmin)
                        cl.findAndAddContactsByMid(cmin)
                        k2.findAndAddContactsByMid(cmin)
                        k3.findAndAddContactsByMid(cmin)
                        k4.findAndAddContactsByMid(cmin)
                        k5.findAndAddContactsByMid(cmin)
                        k6.findAndAddContactsByMid(cmin)
                        k7.findAndAddContactsByMid(cmin)
                        k8.findAndAddContactsByMid(cmin)
                        k9.findAndAddContactsByMid(cmin)
                        k10.findAndAddContactsByMid(cmin)
                        cl.sendText(msg.to,"Added As Friends")
                      except:
                        random.choice(KAC).findAndAddContactsByMid(cmin)
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")

              elif "Admin remove: " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("Admin remove: ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid Mid")
                  else:
                    if gid in admin:
                      admin.remove(gid)
                      cl.sendText(msg.to,"Deleted From Admin List")
                    else:
                      cl.sendText(msg.to,"This Person Not in Admin List Boss")
                      #pass
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")

              elif "Owner remove: " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("Owner remove: ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid Mid")
                  else:
                    if gid in owner:
                      owner.remove(gid)
                      cl.sendText(msg.to,"Deleted From Owner List")
                    else:
                      cl.sendText(msg.to,"This Person Not in Owner List Boss")
                      #pass
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")

              elif "Staff remove @" in msg.text:
                if msg._from in owner:
                  _name = msg.text.replace("Staff remove @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Orangnya ga ada Lagi Colli")
                  else:
                    for target in targets:
                      try:
                        staff.remove(target)
                        cl.sendText(msg.to,"staff Deleted")
                      except:
                        pass
                else:
                  cl.sendText(msg.to,"You Are Not My Boss !!!")
                  cl.sendText(msg.to,"Command Denied")

              elif msg.text in ["Adminlist","adminlist"]:
                if admin == []:
                  cl.sendText(msg.to,"The Adminlist is empty")
                else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "╔══════════════\n║👑 Admin P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉  Bot 👑\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in admin:
                    mc += "║[★]" + cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)

              elif msg.text in ["Ownerlist","ownerlist"]:
                if owner == []:
                  cl.sendText(msg.to,"The Owner is empty")
                else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════\n║👑 Owner P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉  Bot 👑\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in owner:
                    mc += "║[★]" + cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)

              elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                  cl.sendText(msg.to,"The Owner is empty")
                else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════\n║👥 Staff P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉  Bot 👥\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in staff:
                    mc += "║[★]" + cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)

              elif msg.text in ["Me","me","ME"]:
                middd = "Name : " +cl.getContact(msg._from).displayName + "\nMid : " +msg._from
                cl.sendText(msg.to,middd)

              elif "Gn " in msg.text:
                if msg._from in admin:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                  else:
                    cl.sendText(msg.to,"It can't be used besides the group.")

              elif msg.text in ["Contact On","Contact on","contact on"]:
                if msg._from in owner:
                  if wait["contact"] == True:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                      cl.sendText(msg.to,"done")
              elif msg.text in ["Contact Off","Contact off","contact off"]:
                if msg._from in owner:
                  if wait["contact"] == False:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text in ["Join on","Auto join on"]:
                if msg._from in owner:
                  if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"already on")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"already on")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text in ["Join off","Auto join off"]:
                if msg._from in owner:
                  if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"already off")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"already off")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text in ["Protect kick on","protect kick on"]:
                if msg._from in owner:
                  if wait["ProtectKick"] == True:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Protect Kickers On")
                    else:
                      cl.sendText(msg.to,"Done")
                  else:
                    wait["ProtectKick"] = True
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Udah On Njir\nPikun Lu")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text in ["Protect kick off","protect kick off"]:
                if msg._from in owner:
                  if wait["ProtectKick"] == False:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Protect Kickers Off")
                    else:
                      cl.sendText(msg.to,"Done")
                  else:
                    wait["ProtectKick"] = False
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Udah Off Njir\nPikun Lu")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text == "Cctv":
                if msg._from in admin:
                  cl.sendText(msg.to, "Mencari CCTV...")
                  try:
                    del wait2['readPoint'][msg.to]
                    del wait2['readMember'][msg.to]
                  except:
                    pass
                  now2 = datetime.now()
                  wait2['readPoint'][msg.to] = msg.id
                  wait2['readMember'][msg.to] = ""
                  wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                  wait2['ROM'][msg.to] = {}

              elif msg.text == "Ciduk":
                if msg._from in admin:
                  if msg.to in wait2['readPoint']:
                      if wait2["ROM"][msg.to].items() == []:
                          chiya = ""
                      else:
                          chiya = ""
                          for rom in wait2["ROM"][msg.to].items():
                              #print rom
                              chiya += rom[1] + "\n"

                      cl.sendText(msg.to, "||Dilihat Oleh||%s\n\n||By : P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ||\n\n>Pelaku CCTV<\n%sAwas Yang CCTV Bintitan\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                  else:
                      cl.sendText(msg.to, "Ketik Cctv Dulu Njir\nBaru Ketik Ciduk\nDasar Pikun ♪")
          #----------------Fungsi Join Group Start-----------------------#
              elif msg.text in ["Tag","Tagall"]:
                if msg._from in admin:
                  group = client.getGroup(receiver)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                  if jml <= 100:
                    client.mention(receiver, nama)
                  if jml > 100 and jml < 200:
                    for i in range(0, 100):
                      nm1 += [nama[i]]
                    client.mention(receiver, nm1)
                    for j in range(101, len(nama)):
                      nm2 += [nama[j]]
                    client.mention(receiver, nm2)
                  if jml > 200 and jml < 300:
                    for i in range(0, 100):
                      nm1 += [nama[i]]
                    client.mention(receiver, nm1)
                    for j in range(101, 200):
                      nm2 += [nama[j]]
                    client.mention(receiver, nm2)
                    for k in range(201, len(nama)):
                      nm3 += [nama[k]]
                    client.mention(receiver, nm3)
                  if jml > 300 and jml < 400:
                    for i in range(0, 100):
                      nm1 += [nama[i]]
                    client.mention(receiver, nm1)
                    for j in range(101, 200):
                      nm2 += [nama[j]]
                    client.mention(receiver, nm2)
                    for k in range(201, len(nama)):
                      nm3 += [nama[k]]
                    client.mention(receiver, nm3)
                    for l in range(301, len(nama)):
                      nm4 += [nama[l]]
                    client.mention(receiver, nm4)
                  if jml > 400 and jml < 501:
                    for i in range(0, 100):
                      nm1 += [nama[i]]
                    client.mention(receiver, nm1)
                    for j in range(101, 200):
                      nm2 += [nama[j]]
                    client.mention(receiver, nm2)
                    for k in range(201, len(nama)):
                      nm3 += [nama[k]]
                    client.mention(receiver, nm3)
                    for l in range(301, len(nama)):
                      nm4 += [nama[l]]
                    client.mention(receiver, nm4)
                    for m in range(401, len(nama)):
                      nm5 += [nama[m]]
                    client.mention(receiver, nm5)             
                  client.sendText(receiver, "Jumlah Members :"+str(jml))
                else:
                  client.sendText(receiver, "Perintah Ini Cuma Buat Admin & Owner Njiir\nTablo Lu 😂😂😂")

              elif "Mid @" in msg.text:
                if msg._from in owner:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      cl.sendText(msg.to, g.mid)
                    else:
                      pass

              elif msg.text in ["Speed","Sp","sp"]:
                if msg._from in admin:
                  start = time.time()
                  cl.sendText(msg.to, "Menghitung Duit...")
                  elapsed_time = time.time() - start
                  cl.sendText(msg.to, "%sDetik" % (elapsed_time))
        #-------------Fungsi Speedbot Finish---------------------#
        #-------------Fungsi Banned Send Contact Start------------------#
              elif msg.text in ["Ban"]:
                if msg._from in owner:
                  wait["wblacklist"] = True
                  cl.sendText(msg.to,"Kirim Kontaknya")
                  #kc.sendText(msg.to,"Kirim contact")
              elif msg.text in ["Unban"]:
                if msg._from in owner:
                  wait["dblacklist"] = True
                  cl.sendText(msg.to,"Kirim Kontaknya")
                  #kc.sendText(msg.to,"Kirim contact")

              elif msg.text in ["Cancel","cancel"]:
                if msg._from in admin:
                  if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    if X.invitee is not None:
                      gInviMids = [contact.mid for contact in X.invitee]
                      random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                      if wait["lang"] == "JP":
                        cl.sendText(msg.to,"No one is inviting")
                      else:
                        cl.sendText(msg.to,"Sorry, nobody absent")
                  else:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                      cl.sendText(msg.to,"Not for use less than group")
                else:
                  cl.sendText(msg.to,"This Command Only For Admin & Owner")

              elif msg.text in ["Buka qr","Open qr"]:
                if msg._from in admin:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"QR Sudah Dibuka")
                    else:
                      cl.sendText(msg.to,"QR Udah Kebuka Njir")
                  else:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                      cl.sendText(msg.to,"Not for use less than group")

              elif msg.text in ["Tutup qr","close qr"]:
                if msg._from in admin:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"QR Sudah Di Tutup")
                    else:
                      cl.sendText(msg.to,"QR Udah Ketutup Njir")
                  else:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                      cl.sendText(msg.to,"Not for use less than group")

              elif msg.text in ["Protect cancel on","protect cancel on"]:
                if msg._from in owner:
                  if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Yang Cancel Invitan Ane Kick")
                    else:
                      cl.sendText(msg.to,"Done")
                  else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Udah On Njir")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text in ["Protect cancel off","protect cancel off"]:
                if msg._from in owner:
                  if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Yang Cancel Invitan Ga Ane Kick")
                    else:
                      cl.sendText(msg.to,"Done")
                  else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Udah Off Njir")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text in ["Protect invite on","Invite on"]:
                if msg._from in owner:
                  if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Cancel All Invitation On")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Udah On Njir")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text in ["Protect invite off","Invite off"]:
                if msg._from in owner:
                  if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Cancel All Invitation Off")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Udah Off Njir")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text in ["Protect qr on","protect qr on"]:
                if msg._from in owner:
                  if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Protect QR On")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Udah On Njir")
                    else:
                      cl.sendText(msg.to,"done")

              elif msg.text in ["Protect qr off","protect qr off"]:
                if msg._from in owner:
                  if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Protect QR Off")
                    else:
                      cl.sendText(msg.to,"Done")
                  else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Udah Off Njir")
                    else:
                      cl.sendText(msg.to,"Done")

              elif msg.text in ["Leave on","Auto leave:on"]:
                if msg._from in owner:
                  if wait["Leave"] == True:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"already on")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["Leave"] = True
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"done")
                    else:
                      cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")

              elif msg.text in ["Leave off","Auto leave:off"]:
                if msg._from in owner:
                  if wait["Leave"] == False:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"already off")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["Leave"] = False
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"done")
                    else:
                      cl.sendText(msg.to,"already")

              elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if msg._from in owner:
                  if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"already on")
                    else:
                      cl.sendText(msg.to,"Done")
                  else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Done")
                    else:
                      cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
              elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if msg._from in owner:
                  if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"already off")
                    else:
                      cl.sendText(msg.to,"done")
                  else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"done")
                    else:
                      cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")

              elif msg.text in ["Status","Set"]:
                if msg._from in admin:
                  md = "╔═══════════════\n║       ⭐Protection Status⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  if wait["Protectgr"] == True: md+="║[•]Protect QR Enable\n"
                  else: md+="║[•]Protect QR Disable\n"
                  if wait["Protectcancl"] == True: md+="║[•]Protect Invite Enable\n"
                  else: md+="║[•]Protect Invite Disable\n"
                  if wait["Protectcancel"] == True: md+="║[•]Protect Cancel Enable\n"
                  else: md+="║[•]Protect Cancel Disable\n"
                  if wait["Protectkick"] == True: md+="║[•]Protect Kick Enable\n"
                  else: md+="║[•]Protect Kick Disable\n"
                  if wait["contact"] == True: md+="║[•]Contact ✔\n"
                  else: md+="║[•]Contact ❌\n"
                  if wait["autoJoin"] == True: md+="║[•]Auto Join ✔\n"
                  else: md +="║[•]Auto Join ❌\n"
                  if wait["Leave"] == True: md+="║[•]Auto Leave ✔\n"
                  else: md +="║[•]Auto Leave ❌\n"
                  if wait["Sider"] == True: md+="║[•]Auto Sider ✔\n"
                  else:md+="║[•]Auto Sider ❌\n"
                  #if wait["autoCancel"]["on"] == True:md+="║[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                  #else: md+="║[•]Group Cancel [Off]\n"
                  #if wait["leaveRoom"] == True: md+="║[•]Auto Leave ✔\n"
                  #else: md+="║[•]Auto Leave ✖\n"
                  #if wait["timeline"] == True: md+="║[•]Share ✔\n"
                  #else: md+="║[•]Share ✖\n"
                  if wait["autoAdd"] == True: md+="║[•]Auto Add ✔\n"
                  else: md+="║[•]Auto Add ❌\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n║   ⭐P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n╚═══════════════"
                  cl.sendText(msg.to,md)
                else:
                  cl.sendText(msg.to,"This Command Only For Admin & Owner")
        #-------------Fungsi Banned Send Contact Finish------------------#
              elif msg.text in ["Link group"]:
                if msg._from in admin:
                  if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventedJoinByTicket == True:
                      x.preventedJoinByTicket = False
                      cl.updateGroup(x)
                      gurl = cl.reissueGroupTicket(msg.to)
                      cl.sendText(msg.to,"line://ti/g/" + gurl)
                  else:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                      cl.sendText(msg.to,"Not for use less than group")

              elif "/invitemeto: " in msg.text:
                if msg._from in owner:
                  gid = msg.text.replace("/invitemeto: ","")
                  if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                  else:
                    try:
                      cl.findAndAddContactsByMid(msg._from)
                      cl.inviteIntoGroup(gid,[msg._from])
                    except:
                      try:
                        k2.findAndAddContactsByMid(msg._from)
                        k2.inviteIntoGroup(gid,[msg._from])
                      except:
                        try:
                          k3.findAndAddContactsByMid(msg._from)
                          k3.inviteIntoGroup(gid,[msg._from])
                        except:
                          try:
                            k4.findAndAddContactsByMid(msg._from)
                            k4.inviteIntoGroup(gid,[msg._from])
                          except:
                            try:
                              k5.findAndAddContactsByMid(msg._from)
                              k5.inviteIntoGroup(gid,[msg._from])
                            except:
                              try:
                                random.choice(KAC).findAndAddContactsByMid(msg._from)
                                random.choice(KAC).inviteIntoGroup(gid,[msg._from])
                              except:
                                cl.sendText(msg.to,"Mungkin kami tidak di dalaam grup itu")

              elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u1112a364f49ad61d6ca5ec5bc9d6d375'}
                cl.sendText(msg.to,"======================")
                cl.sendText(msg)
                cl.sendText(msg.to,"==||Fadlan||==")
                cl.sendText(msg.to,"======================")

              elif msg.text in ["Creator2","Owner2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ued156c86ffa56024c0acba16f7889e6d'}
                cl.sendText(msg.to,"======================")
                cl.sendText(msg)
                cl.sendText(msg.to,"==||Hanavy Koplaxs||==")
                cl.sendText(msg.to,"======================")

              elif msg.text in ["Creator3","Owner3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u88cd7ee9fd691d6306e5e19be5d16f69'}
                cl.sendText(msg.to,"======================")
                cl.sendText(msg)
                cl.sendText(msg.to,"=======||PRAS||======")
                cl.sendText(msg.to,"======================")
                #cl.sendImageWithURL("http://oi64.tinypic.com/x2oua8.jpg")

              elif msg.text in ["In","Masuk","Bot in"]:
                if msg._from in owner:
                  G = cl.getGroup(msg.to)
                  #ginfo = cl.getGroup(msg.to)
                  G.preventedJoinByTicket = False
                  cl.updateGroup(G)
                  invsend = 0
                  Ticket = cl.reissueGroupTicket(msg.to)
                  k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  G = cl.getGroup(msg.to)
                  G.preventedJoinByTicket = True
                  cl.updateGroup(G)
                  
              elif msg.text in ["In3","Masuk3","Bot in3"]:
                if msg._from in owner:
                  G = koplaxs.getGroup(msg.to)
                  #ginfo = cl.getGroup(msg.to)
                  G.preventedJoinByTicket = False
                  koplaxs.updateGroup(G)
                  invsend = 0
                  Ticket = koplaxs.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                  time.sleep(0.00001)
                  G = koplaxs.getGroup(msg.to)
                  G.preventedJoinByTicket = True
                  koplaxs.updateGroup(G)

              elif msg.text in ["Keluar","Get out","Out"]:
                if msg._from in owner:
                  if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                      k10.leaveGroup(msg.to)
                      k9.leaveGroup(msg.to)
                      k8.leaveGroup(msg.to)
                      k7.leaveGroup(msg.to)
                      k6.leaveGroup(msg.to)
                      k5.leaveGroup(msg.to)
                      k4.leaveGroup(msg.to)
                      k3.leaveGroup(msg.to)
                      k2.leaveGroup(msg.to)
                      cl.leaveGroup(msg.to)
                    except:
                      pass

              elif msg.text in ["Pulang"]:
                if msg._from in owner:
                  if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                      k10.leaveGroup(msg.to)
                      k9.leaveGroup(msg.to)
                      k8.leaveGroup(msg.to)
                      k7.leaveGroup(msg.to)
                      k6.leaveGroup(msg.to)
                      k5.leaveGroup(msg.to)
                      k4.leaveGroup(msg.to)
                      k3.leaveGroup(msg.to)
                      k2.leaveGroup(msg.to)
                    except:
                      pass
        #-------------Fungsi Bannlist Start------------------#          
              elif msg.text in ["Banlist"]:
                if msg._from in admin:
                  if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Gak Ada Yang Di Blacklist")
                  else:
                    cl.sendText(msg.to,"↓↓Blacklist↓↓")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                      mc += "→" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

              elif msg.text.lower() == 'Runtime':
                if msg._from in admin:
                  eltime = time.time() - mulai
                  van = "Bot Sudah Berjalan Selama\n "+waktu(eltime)
                  cl.sendText(msg.to,van)

              elif msg.text in ["Cek member","Member"]:
                if msg._from in admin:
                  kontak = cl.getGroup(msg.to)
                  group = kontak.members
                  num=1
                  msgs="═════════List Member═════════-"
                  for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                  msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                  cl.sendText(msg.to, msgs)

              elif msg.text.lower() == 'crashh':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u1112a364f49ad61d6ca5ec5bc9d6d375',"}
                cl.sendMessage(msg)

              elif "Block @" in msg.text:
                if msg.toType == 2:
                  print ("[block] OK")
                  _name = msg.text.replace("Block @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to, "Not Found...")
                  else:
                    for target in targets:
                      try:
                        cl.blockContact(target)
                        cl.sendText(msg.to, "Success block contact~")
                      except Exception as e:
                        print (e)

              elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                  msgs+="\n%i. %s" % (num, ids.displayName)
                  num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)

              elif msg.text in ["My BCA"]:
                if msg._from in admin:
                  cl.sendText(msg.to, "No Rekening : 7015274646\nAtas Nama : Achmad Hanafi\nJenis Bank : Bank BCA")

              elif msg.text in ["My HP"]:
                if msg._from in admin:
                  cl.sendText(msg.to, "089663427204")

              elif "Spam " in msg.text:
                if msg._from in owner:
                  txt = msg.text.split(" ")
                  jmlh = int(txt[2])
                  teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                  tulisan = jmlh * (teks+"\n")
                  #Keke cantik <3
                  if txt[1] == "on":
                    if jmlh <= 500:
                      for x in range(jmlh):
                        cl.sendText(msg.to, teks)
                    else:
                      cl.sendText(msg.to, "Out of range! ")
                  elif txt[1] == "off":
                    if jmlh <= 900:
                      cl.sendText(msg.to, tulisan)
                    else:
                      cl.sendText(msg.to, "Out of range! ")

              elif "Info group" == msg.text:
                if msg.toType == 2:
                  if msg._from in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                      gCreator = ginfo.creator.displayName
                    except:
                      gCreator = "Error"
                    if wait["lang"] == "JP":
                      if ginfo.invitee is None:
                        sinvitee = "0"
                      else:
                        sinvitee = str(len(ginfo.invitee))
                      if ginfo.preventedJoinByTicket == True:
                        QR = "Close"
                      else:
                        QR = "Open"
                      cl.sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Status Link Group]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                    else:
                      cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Status Link Group]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                  else:
                    if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                      cl.sendText(msg.to,"Not for use less than group")

              elif msg.text in ["List group","List Group"]:
                if msg._from in owner:
                  gids = cl.getGroupIdsJoined()
                  h = ""
                  for i in gids:
                    #####gn = cl.getGroup(i).name
                    h += "[★]%s Member\n" % (cl.getGroup(i).name   + "👉" + str(len(cl.getGroup(i).members)))
                  cl.sendText(msg.to,"===========[List Group]==========\n"+ h +"Total Group :" + str(len(gids)))

              elif msg.text in ["Kill ban"]:
                if msg._from in owner:
                  if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                      matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                      cl.sendText(msg.to,"Selamat tinggal")
                      cl.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                      pass
                    for jj in matched_list:
                      try:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        print (msg.to,[jj])
                      except:
                        pass

              elif "Ban " in msg.text:
                if msg._from in owner:
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                    except:
                      pass

              elif "Unban @" in msg.text:
                if msg._from in owner:
                  if msg.toType == 2:
                    #print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                      if _nametarget == g.displayName:
                        targets.append(g.mid)
                    if targets == []:
                      cl.sendText(msg.to,"Tidak Ditemukan.....")
                      #kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                      for target in targets:
                        try:
                          del wait["blacklist"][target]
                          f=codecs.open('st2__b.json','w','utf-8')
                          json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                          cl.sendText(msg.to,"Akun Bersih Kembali")
                        except:
                          cl.sendText(msg.to,"Error")

              elif msg.text in ["Clear ban"]:
                if msg._from in owner:
                  wait["blacklist"] = {}
                  cl.sendText(msg.to,"Succes Clear Blacklist")

              elif ("Kick " in msg.text):
                if msg._from in owner:
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"] [0] ["M"]
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    cl.kickoutFromGroup(msg.to,[target])

              elif "Copy @" in msg.text:
                if msg._from in owner:
                  _name = msg.text.replace("Copy @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    sendMessage(msg.to, "Not Found...")
                  else:
                    for target in targets:
                      try:
                        cl.cloneContactProfile(target)
                        cl.sendText(msg.to, "Success Copy profile ~")
                      except Exception as e:
                        print (e)

              elif msg.text in ["Backup","backup"]:
                if msg._from in owner:
                  try:
                    cl.updateProfileAttribute(8, backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "backup done")
                  except Exception as e:
                    cl.sendText(msg.to, str (e))

              elif "Bc group " in msg.text:
                if msg._from in owner:
                  bctxt = msg.text.replace("Bc group ","")
                  a = cl.getGroupIdsJoined()
                  for taf in a:
                    cl.sendText(taf, (bctxt))

              elif "Say " in msg.text:
                if msg._from in admin:
                  say = msg.text.replace("Say ","")
                  lang = 'id'
                  tts = gTTS(text=say, lang=lang)
                  tts.save("hasil.mp3")
                  cl.sendAudio(msg.to,"hasil.mp3")

              elif "Jsay " in msg.text:
                if msg._from in admin:
                  say = msg.text.replace("Jsay ","")
                  lang = 'ja'
                  tts = gTTS(text=say, lang=lang)
                  tts.save("hasil.mp3")
                  cl.sendAudio(msg.to,"hasil.mp3")

              elif "Isay " in msg.text:
                if msg._from in admin:
                  say = msg.text.replace("Isay ","")
                  lang = 'en'
                  tts = gTTS(text=say, lang=lang)
                  tts.save("hasil.mp3")
                  cl.sendAudio(msg.to,"hasil.mp3")

              elif "Asay " in msg.text:
                if msg._from in admin:
                  say = msg.text.replace("Asay ","")
                  lang = 'ar'
                  tts = gTTS(text=say, lang=lang)
                  tts.save("hasil.mp3")
                  cl.sendAudio(msg.to,"hasil.mp3")

              elif 'Lirik ' in msg.text.lower():
                if msg._from in owner:  
                  try:
                    songname = msg.text.lower().replace('Lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                      hasil = 'Lyric Song ('
                      hasil += song[0]
                      hasil += ')\n\n'
                      hasil += song[5]
                      cl.sendText(msg.to, hasil)
                  except Exception as wak:
                     cl.sendText(msg.to, str(wak))

              elif "Youtube: " in msg.text:
                if msg._from in admin:
                  query = msg.text.replace("Youtube: ","")
                  cl.sendText(msg.to, "Searching...")
                  with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'https://www.youtube.com/results'
                    params = {'search_query':query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    loop = 1
                    for a in soup.select('.yt-lockup-title > a[title]'):
                      if '&list=' not in a['href']:
                        if loop == 0:
                          cl.sendText(msg.to, a['title']+'\nhttps://www.youtube.com'+a['href'])
                          break
                        else:
                          loop = loop - 1
              elif 'Music ' in msg.text.lower():
                if msg._from in owner:
                  try:
                    songname = msg.text.lower().replace('Music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                      hasil = 'This is Your Music\n'
                      hasil += 'Judul : ' + song[0]
                      hasil += '\nDurasi : ' + song[1]
                      hasil += '\nLink Download : ' + song[4]
                    cl.sendText(msg.to, hasil)
                    cl.sendText(msg.to, "Please Wait for audio...")
                    cl.sendAudioWithURL(msg.to, song[3])
                  except Exception as njer:
                    cl.sendText(msg.to, str(njer))

              elif 'Musik ' in msg.text.lower():
                if msg._from in owner:  
                  try:
                    songname = msg.text.lower().replace('Musik ','')
                    params = {'songname': songname}
                    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                      hasil = 'This is Your Music\n'
                      hasil += 'Judul : ' + song[0]
                      hasil += '\nDurasi : ' + song[1]
                      hasil += '\nLink Download : ' + song[4]
                      cl.sendText(msg.to, hasil)
                      cl.sendText(msg.to, "Please Wait for audio...")
                      cl.sendAudioWithURL(msg.to, song[4])
                  except Exception as njer:
                      cl.sendText(msg.to, str(njer))

              elif "Dp " in msg.text:
                if msg._from in owner:
                  try:
                    key = eval(msg.contentMetadata["MENTION"])
                    u = key["MENTIONEES"][0]["M"]
                    a = channel.getProfileCoverURL(mid=u)
                    client.sendImageWithURL(receiver, a)
                  except Exception as e:
                    client.sendText(receiver, str(e))
                    
              elif 'Like ' in text.lower():
                if msg._from in owner:
                  try:
                    typel = [1001,1002,1003,1004,1005,1006]
                    key = eval(msg.contentMetadata["MENTION"])
                    u = key["MENTIONEES"][0]["M"]
                    a = client.getContact(u).mid
                    s = client.getContact(u).displayName
                    hasil = channel.getHomeProfile(mid=a)
                    st = hasil['result']['feeds']
                    for i in range(len(st)):
                      test = st[i]
                      result = test['post']['postInfo']['postId']
                      channel.like(str(sender), str(result), likeType=random.choice(typel))
                      channel.comment(str(sender), str(result), 'Auto Like by Fadlan')
                    client.sendText(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                  except Exception as e:
                    client.sendText(receiver, str(e))
                    
              elif "Groupid " in text.lower():
                if msg._from in owner:
                  try:
                    gname=text.replace("Groupid ","")
                    x=cl.getGroupIdsByName(gname)
                    #print("[COMMAND]GET GROUP ID EXECUTED\n")
                    cl.sendMessage(receiver,str(x))
                  except Exception as e:
                    cl.sendMessage(receiver,str(e))
                                    
              elif "Stealgroup" in msg.text:
                if msg._from in owner:
                  group = cl.getGroup(msg.to)
                  cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + group.pictureStatus)

              elif "Pp @" in msg.text:
                if msg._from in owner:
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  targets = []
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  if targets == []:
                    cl.sendText(msg.to,"Kontak tidak ditemukan,mungkin kontak yg dituju tidak mempunyai muka")
                  else:
                    for target in targets:
                      try:
                        contact = cl.getContact(target)
                        path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(msg.to, path)
                      except Exception as e:
                        raise e

              elif "Nama @" in msg.text:
                if msg._from in owner:
                  _name = msg.text.replace("Nama @","")
                  _nametarget = _name.rstrip(" ")
                  gs = cl.getGroup(msg.to)
                  for h in gs.members:
                    if _nametarget == h.displayName:
                      cl.sendText(msg.to,"[DisplayName]:\n" + h.displayName )
                    else:
                      pass

              elif "Video @" in msg.text:
                #print "[Command]dp executing"
                _name = msg.text.replace("Video @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                  if _nametarget == g.displayName:
                    targets.append(g.mid)
                if targets == []:
                  cl.sendText(msg.to,"Contact not found")
                else:
                  for target in targets:
                    try:
                      contact = cl.getContact(target)
                      path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                      cl.sendVideoWithURL(msg.to, path)
                    except Exception as e:
                      raise e

              elif "Ig: " in msg.text:
                if msg._from in owner:
                  cari = msg.text.replace("Ig: ","")
                  try:
                    response = requests.get("https://www.instagram.com/"+cari+"?__a=1")
                    data = response.json()
                    namaIG = str(data['user']['full_name'])
                    bioIG = str(data['user']['biography'])
                    mediaIG = str(data['user']['media']['count'])
                    verifIG = str(data['user']['is_verified'])
                    usernameIG = str(data['user']['username'])
                    followerIG = str(data['user']['followed_by']['count'])
                    profileIG = data['user']['profile_pic_url_hd']
                    privateIG = str(data['user']['is_private'])
                    followIG = str(data['user']['follows']['count'])
                    text = "==============================\n[Name] : "+namaIG+"\n[Biography] :\n"+bioIG+"\n[Follower] : "+followerIG+"\n[Following] : "+followIG+"\n[Media] : "+mediaIG+"\n[Verified] :"+verifIG+"\n[Private] : "+privateIG+"\n[Username] : "+usernameIG+"\n=============================="
                    cl.sendImageWithURL(msg.to, profileIG)
                    cl.sendText(msg.to, str(text))
                  except Exception as e:
                    cl.sendText(msg.to, str(e))

              elif "Facebook " in msg.text:
                if msg._from in owner:
                  a = msg.text.replace("Facebook ","")
                  b = urllib.quote(a)
                  cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                  cl.sendText(msg.to, "https://www.facebook.com" + b)
                  cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")

              elif "Bc " in msg.text:
                if msg._from in owner:
                  bctxt = msg.text.replace("Bc ","")
                  a = cl.getGroupIdsJoined()
                  a = k2.getGroupIdsJoined()
                  a = k3.getGroupIdsJoined()
                  a = k4.getGroupIdsJoined()
                  a = k5.getGroupIdsJoined()
                  a = k6.getGroupIdsJoined()
                  a = k7.getGroupIdsJoined()
                  a = k8.getGroupIdsJoined()
                  a = k9.getGroupIdsJoined()
                  a = k10.getGroupIdsJoined()
                  for taf in a:
                    cl.sendText(taf, (bctxt))
                    k2.sendText(taf, (bctxt))
                    k3.sendText(taf, (bctxt))
                    k4.sendText(taf, (bctxt))
                    k5.sendText(taf, (bctxt))
                    k6.sendText(taf, (bctxt))
                    k7.sendText(taf, (bctxt))
                    k8.sendText(taf, (bctxt))
                    k9.sendText(taf, (bctxt))
                    k10.sendText(taf, (bctxt))

              elif "Lbc " in msg.text:
                if msg._from in owner:
                  bctxt = msg.text.replace("Lbc ","")
                  a = cl.getGroupIdsJoined()
                  for taf in a:
                    cl.sendText(taf, (bctxt))

              elif msg.text in ["Absen","Rname","Absen dulu","Respon"]:
                if msg._from in admin:
                  cl.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")
                  k2.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")
                  k3.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")
                  k4.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")
                  k5.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")
                  k6.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")
                  k7.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")
                  k8.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")
                  k9.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")
                  k10.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ")

              elif msg.text in ["Invite"]:
                if msg._from in owner:
                  wait["winvite"] = True
                  cl.sendText(msg.to,"Share contact boss 😎")
                  
              elif msg.text in ["2invite"]:
                if msg._from in owner:
                  wait["winvite2"] = True
                  k2.sendText(msg.to,"Share contact boss 😎")
                
              elif msg.text in ["3invite"]:
                if msg._from in owner:
                  wait["winvite3"] = True
                  k3.sendText(msg.to,"Share contact boss 😎")
                
              elif msg.text in ["4invite"]:
                if msg._from in owner:
                  wait["winvite4"] = True
                  k4.sendText(msg.to,"Share contact boss 😎")
                
              elif msg.text in ["5invite"]:
                if msg._from in owner:
                  wait["winvite5"] = True
                  k5.sendText(msg.to,"Share contact boss 😎")
                
              elif msg.text in ["6invite"]:
                if msg._from in owner:
                  wait["winvite6"] = True
                  k6.sendText(msg.to,"Share contact boss 😎")
                
              elif msg.text in ["7invite"]:
                if msg._from in owner:
                  wait["winvite7"] = True
                  k7.sendText(msg.to,"Share contact boss 😎")
                
              elif msg.text in ["8invite"]:
                if msg._from in owner:
                  wait["winvite8"] = True
                  k8.sendText(msg.to,"Share contact boss 😎")
                
              elif msg.text in ["9invite"]:
                if msg._from in owner:
                  wait["winvite9"] = True
                  k9.sendText(msg.to,"Share contact boss 😎")
                
              elif msg.text in ["10invite"]:
                if msg._from in owner:
                  wait["winvite10"] = True
                  k10.sendText(msg.to,"Share contact boss 😎")

              elif msg.text in ["Ban"]:
                if msg._from in owner:
                  wait["wblacklist"] = True
                  cl.sendText(msg.to,"Send Contact")

              elif msg.text in ["Unban"]:
                if msg._from in owner:
                  wait["dblacklist"] = True
                  cl.sendText(msg.to,"Send Contact")

              elif msg.text in ["One piece","OP"]:
                if msg._from in owner:
                  cl.sendImageWithURL(msg.to,"http://oi64.tinypic.com/106xa1j.jpg")
                  cl.sendImageWithURL(msg.to,"http://oi63.tinypic.com/125rms0.jpg")
                  cl.sendImageWithURL(msg.to,"http://oi68.tinypic.com/kb8tae.jpg")
                  cl.sendImageWithURL(msg.to,"http://oi63.tinypic.com/69oy2v.jpg")
                  cl.sendImageWithURL(msg.to,"http://oi66.tinypic.com/10dxtp1.jpg")
                  cl.sendImageWithURL(msg.to,"http://oi65.tinypic.com/2ds4y78.jpg")
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': 'uc9363b5a4bfacd981c3e3c082bc4d5ef'}
                  cl.sendMessage(msg)
                  cl.sendText(msg.to,"Thats Logos Team Us\n☆ P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉  ☆")

              elif msg.text in ["1pap"]:
                if msg._from in admin:
                  cl.sendImageWithURL(msg.to,"http://oi63.tinypic.com/2q86pw2.jpg")
              elif msg.text in ["2pap"]:
                if msg._from in admin:
                  k2.sendImageWithURL(msg.to,"http://oi65.tinypic.com/4zu808.jpg")
              elif msg.text in ["3pap"]:
                if msg._from in admin:
                  k3.sendImageWithURL(msg.to,"http://oi64.tinypic.com/iykifn.jpg")
              elif msg.text in ["4pap"]:
                if msg._from in admin:
                  k4.sendImageWithURL(msg.to,"http://oi66.tinypic.com/2vwcp3q.jpg")
              elif msg.text in ["5pap"]:
                if msg._from in admin:
                  k5.sendImageWithURL(msg.to,"http://oi66.tinypic.com/344xsle.jpg")
              elif msg.text in ["6pap"]:
                if msg._from in admin:
                  k6.sendImageWithURL(msg.to,"http://oi66.tinypic.com/539wzq.jpg")
              elif msg.text in ["7pap"]:
                if msg._from in admin:
                  k7.sendImageWithURL(msg.to,"http://oi66.tinypic.com/1sz1vc.jpg")
              elif msg.text in ["8pap"]:
                if msg._from in admin:
                  k8.sendImageWithURL(msg.to,"http://oi68.tinypic.com/154d4pt.jpg")
              elif msg.text in ["9pap"]:
                if msg._from in admin:
                  k9.sendImageWithURL(msg.to,"http://oi65.tinypic.com/21314rs.jpg")
              elif msg.text in ["10pap"]:
                if msg._from in admin:
                  k10.sendImageWithURL(msg.to,"http://oi67.tinypic.com/ptbeq.jpg")

              elif msg.text in ["Remove all chat"]:
                if msg._from in owner:
                  cl.sendText(msg.to,"Starting Remove All Chat...")
                  cl.removeAllMessages(op.param2)
                  k2.removeAllMessages(op.param2)
                  k3.removeAllMessages(op.param2)
                  k4.removeAllMessages(op.param2)
                  k5.removeAllMessages(op.param2)
                  k6.removeAllMessages(op.param2)
                  k7.removeAllMessages(op.param2)
                  k8.removeAllMessages(op.param2)
                  k9.removeAllMessages(op.param2)
                  k10.removeAllMessages(op.param2)
                  cl.sendText(msg.to,"All Chat In Bots Removed")

              elif "Yuhuuu" in msg.text:
                if msg._from in owner:
                  if msg.toType == 2:
                    #print "Ratain"
                    _name = msg.text.replace("Yuhuuu","")
                    gs = cl.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    gs = k6.getGroup(msg.to)
                    gs = k7.getGroup(msg.to)
                    gs = k8.getGroup(msg.to)
                    gs = k9.getGroup(msg.to)
                    gs = k10.getGroup(msg.to)
                    cl.sendText(msg.to,"Hello Kk")
                    k2.sendText(msg.to,"P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉  Team Mau Bersih² Group Sampah Nih")
                    k3.sendText(msg.to,"Karna Ini Group Sampah Jadi Mau Di Bersihin Dulu Yah\n★Jangan Baper...\n★Jangan Nangis\n★Jangan Cengeng\nBawa Enjoy Aja Kawan♪")
                    k4.sendText(msg.to,"★Inget Baik² Nih Logo Team War Kami★\n\n★★★P҉ o҉ w҉ e҉ r҉  R҉ a҉ n҉ g҉ e҉ r҉ s҉ ★★★")
                    k5.sendImageWithURL(msg.to,"http://oi67.tinypic.com/j5a0wl.jpg")
                    k6.sendImageWithURL(msg.to,"http://oi65.tinypic.com/2m5ndac.jpg")
                    k7.sendImageWithURL(msg.to,"http://oi66.tinypic.com/xpoiet.jpg")
                    k8.sendImageWithURL(msg.to,"http://oi65.tinypic.com/29eorc3.jpg")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': 'uc9363b5a4bfacd981c3e3c082bc4d5ef'}
                    k9.sendMessage(msg)
                    k10.sendText(msg.to,"This My Team WAR")
                    targets = []
                    for g in gs.members:
                      if _name in g.displayName:
                        targets.append(g.mid)
                    if targets == []:
                      cl.sendText(msg.to,"Not found")
                    else:
                      for target in targets:
                        if target in admin:
                          pass
                        elif target in Bots:
                          pass
                        elif target in staff:
                          pass
                        else:
                          try:
                            klist=[cl,k2,k3,k4,k5,k6,k7,k8,k9,k10]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[target])
                            #print (msg.to,[g.mid])
                          except:
                            try:
                              cl.kickoutFromGroup(msg.to,[target])
                            except:
                              try:
                                k2.kickoutFromGroup(msg.to,[target])
                              except:
                                try:
                                  k3.kickoutFromGroup(msg.to,[target])
                                except:
                                  try:
                                    k4.kickoutFromGroup(msg.to,[target])
                                  except:
                                    try:
                                      k5.kickoutFromGroup(msg.to,[target])
                                    except:
                                      try:
                                        k6.kickoutFromGroup(msg.to,[target])
                                      except:
                                        try:
                                          k7.kickoutFromGroup(msg.to,[target])
                                        except:
                                          try:
                                            k8.kickoutFromGroup(msg.to,[target])
                                          except:
                                            try:
                                              k9.kickoutFromGroup(msg.to,[target])
                                            except:
                                              try:
                                                k10.kickoutFromGroup(msg.to,[target])
                                              except:
                                                random.choice(KAC).kickoutFromGroup(msg.to,[target])

              elif msg.text in[".qrp on",".kick on","kick on","Kick on","Ready op","Ready Op","Fvck","fvck","Fuck","fuck",".kickall","!kickall"]:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Cieee Kickers!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                    wait["blacklist"][msg._from] = True
                    #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  except:
                    cl.sendText(msg.to,"Bye Bitch")

              elif msg.text in ["Kontol","kontol","Memek","memek","Kntl","kntl","Kntol","kntol"]:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")

              elif "Kontol" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")
              elif "kontol" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")
              elif "Memek" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")
              elif "memek" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")

              elif "Ngentot" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")
              elif "ngentot" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")
              elif "Bangsat" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Kasar !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")
              elif "bangsat" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Kasar !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")
              elif "Kntol" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")
              elif "kntol" in msg.text:
                if msg._from in admin:
                  pass
                else:
                  try:
                    cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                  except:
                    cl.sendText(msg.to,"Bye Bitch")

              elif "Ban group " in msg.text:
                grp = msg.text.replace("Ban group ","")
                gid = cl.getGroupIdsJoined()
                if msg._from in owner:
                  for i in gid:
                    h = cl.getGroup(i).name
                  if h == grp:
                    wait["BlGroup"][i]=True
                    cl.sendText(msg.to, "Success Ban Group : "+grp)
                  else:
                    pass
                else:
                  cl.sendText(msg.to, "Just For Owner")

              elif msg.text in ["Group ban","List group ban"]:
                if msg._from in admin:
                  if wait["BlGroup"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada")
                  else:
                    mc = ""
                    for gid in wait["BlGroup"]:
                      mc += "-> " +cl.getGroup(gid).name + "\n"
                    random.choice(KAC).sendText(msg.to,"===[Ban Group]===\n"+mc)
                else:
                  cl.sendText(msg.to, "Just For Admin")

              elif msg.text in ["Group remove ban "]:
                if msg._from in owner:
                  ng = msg.text.replace("Group remove ban ","")
                  for gid in wait["BlGroup"]:
                    if cl.getGroup(gid).name == ng:
                      del wait["BlGroup"][gid]
                      cl.sendText(msg.to, "Success del ban "+ng)
                    else:
                      pass
                else:
                  cl.sendText(msg.to, "Just For Owner")

              elif "Sider on" in msg.text:
                if msg._from in admin:
                  try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                  except:
                    pass
                  cctv['point'][msg.to] = msg.id
                  cctv['sidermem'][msg.to] = ""
                  cctv['cyduk'][msg.to]=True
                  wait["Sider"] = True
                  cl.sendText(msg.to,"Siap On Cek Sider")

              elif "Sider off" in msg.text:
                if msg._from in admin:
                  if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off")
                  else:
                    cl.sendText(msg.to, "Heh Belom Di Set")

              elif msg.text in ["Auto like"]:
                if msg._from in owner:
                  wait["likeOn"] = True
                  cl.sendText(msg.to,"Shere Post Yang Mau Di Like Boss!")

              elif "Kedip: " in msg.text:
                if msg._from in owner:
                  txt = msg.text.replace("Kedip: ", "")
                  cl.kedapkedip(msg.to,txt)
                  #print "[Command] Kedapkedip"

              elif "Apakah " in msg.text:
                apk = msg.text.replace("Apakah ","")
                rnd = ["Ya","Tidak","Enggak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

              elif "Profile " in msg.text:
                if msg._from in admin:
                  key = eval(msg.contentMetadata["MENTION"])
                  key1 = key["MENTIONEES"][0]["M"]
                  contact = cl.getContact(key1)
                  cu = cl.channel.getCover(key1)
                  path = str(cu)
                  image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                  try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                  except:
                    pass

              elif "Info " in msg.text:
                if msg._from in admin:
                  key = eval(msg.contentMetadata["MENTION"])
                  key1 = key["MENTIONEES"][0]["M"]
                  contact = cl.getContact(key1)
                  cu = cl.channel.getCover(key1)
                  try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                  except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))

              elif "Bio " in msg.text:
                if msg._from in admin:
                  key = eval(msg.contentMetadata["MENTION"])
                  key1 = key["MENTIONEES"][0]["M"]
                  contact = cl.getContact(key1)
                  cu = cl.channel.getCover(key1)
                  try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                  except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)

              elif msg.text in ["Kalender","Time","Waktu"]:
                if msg._from in admin:
                  timeNow = datetime.now()
                  timeHours = datetime.strftime(timeNow,"(%H:%M)")
                  day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                  hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                  bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                  inihari = datetime.today()
                  hr = inihari.strftime('%A')
                  bln = inihari.strftime('%m')
                  for i in range(len(day)):
                      if hr == day[i]: hasil = hari[i]
                  for k in range(0, len(bulan)):
                      if bln == str(k): bln = bulan[k-1]
                  rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                  cl.sendText(msg.to, rst)

              elif "Namelock on" in msg.text:
                if msg._from in admin:
                  if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                  else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
              elif "Namelock off" in msg.text:
                if msg._from in admin:
                  if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                  else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")

              elif msg.text in ["Welcome"]:
                random.choice(KAC).sendText(msg.to,"Selamat Datang di Group Kami 👥👥 \nJangan Lupa Jalan² Ke note Yah Ka\nSemoga Betah")

          except Exception as e:
            client.log("[SEND_MESSAGE] ERROR : " + str(e))
            
        elif op.type == 13:
          if op.param3 in mid:
            cl.getGroup(op.param1)
            cl.acceptGroupInvitation(op.param1)
        
        elif op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                k2.findAndAddContactsByMid(op.param1)
                k3.findAndAddContactsByMid(op.param1)
                k4.findAndAddContactsByMid(op.param1)
                k5.findAndAddContactsByMid(op.param1)
                k6.findAndAddContactsByMid(op.param1)
                k7.findAndAddContactsByMid(op.param1)
                k8.findAndAddContactsByMid(op.param1)
                k9.findAndAddContactsByMid(op.param1)
                k10.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
            else:
              pass
          
        elif op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = k2.getGroup(op.param1)
                        except:
                            try:
                                G = k3.getGroup(op.param1)
                            except:
                                try:
                                    G = k4.getGroup(op.param1)
                                except:
                                    try:
                                        G = k5.getGroup(op.param1)
                                    except:
                                        try:
                                            G = random.choice(KAC).getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            k2.updateGroup(G)
                        except:
                            try:
                                k3.updateGroup(G)
                            except:
                                try:
                                    k4.updateGroup(G)
                                except:
                                    try:
                                        k5.updateGroup(G)
                                    except:
                                        try:
                                            random.choice(KAC).updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in Bots:
                      pass
                    elif op.param2 in admin:
                      pass
                    elif op.param2 in staff:
                      pass
                    else:
                        try:
                            random.chpice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                random.chpice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    random.chpice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        random.chpice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group name lock")
                                        random.choice(KAC).sendText(op.param1,"Dikunci Pe'a")
                                        random.choice(KAC).sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
                
        elif op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param1 not in groupList:
              cl.sendText(op.param1,"This Group Not In Protect List\nWe Will Ignored Anything!!!\nPlease Contact My Owner")
            else:
              group = random.choice(KAC).getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in staff:
                pass
              else:
                  try:
                    random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                    random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "Who do you want to invite  ??? \nYou Are Not Our Admin, So We Cancel it.\nPlease Contact Admin/Owner")
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                  except:
                    random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
          else:
            pass
                    
        elif op.type == 13: #Jika Blacklist Di Invite
          if wait["Protectcancl"] == True:
            if op.param3 in wait["blacklist"] == True:
              #if wait["blacklist"][op.param3] == True:
              if op.param1 not in groupList:
                cl.sendText(op.param1,"This Group Not In Protect List\nWe Will Ignored Anything!!!\nPlease Contact My Owner")
              else:
                if op.param2 in Bots:
                  pass
                elif op.param2 in admin:
                  pass
                elif op.param2 in staff:
                  pass
                else:
                  try:
                    random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param3).displayName + " On Blacklist Boss\nWe Will Cancel Invitation")
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  except:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
              pass
                
        elif op.type == 11:
          if wait["Protectgr"] == True:
            if op.param1 not in groupList:
              cl.sendText(op.param1,"This Group Not In Protect List\nWe Will Ignored Anything!!!\nPlease Contact My Owner")
            else:
              #if random.choice(KAC).getGroup(op.param1).preventedJoinByTicket == False:
                if op.param2 in Bots:
                  pass
                elif op.param2 in admin:
                  pass
                elif op.param2 in staff:
                  pass
                else:
                  try:
                    random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Dont Playing Link Group Bro")
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    #random.choice(KAC).updateGroup(G)
                    random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "We Enter Into Blacklist Boss")
                    wait["blacklist"][op.param2] = True
                  except:
                    G.preventedJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    #random.choice(KAC).updateGroup(G)
                    wait["blacklist"][op.param2] = True
          else:
            pass
                
        elif op.type == 32:
          if wait["Protectcancel"] == True:
            if op.param1 not in groupList:
              cl.sendText(op.param1,"This Group Not In Protect List\nWe Will Ignored Anything!!!\nPlease Contact My Owner")
            else:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in staff:
                pass
              else:
                try:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Canceled Invitation")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
          else:
            pass
                
        elif op.type == 19: #Member Ke Kick
          if op.param1 not in groupList:
            cl.sendText(op.param1,"This Group Not In Protect List\nWe Will Ignored Anything!!!\nPlease Contact My Owner")
          else:
            if wait["Protectkick"] == True:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in staff:
                pass
              else:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  wait["blacklist"][op.param2] = True
            else:
              pass
            
        elif op.type == 19:
          if op.param3 in mid:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                k8.kickoutFromGroup(op.param1,[op.param2])
                G = k8.getGroup(op.param1)
                G.preventedJoinByTicket = False
                #k8.updateGroup(G)
                Ticket = k8.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k8.getGroup(op.param1)
                G.preventedJoinByTicket = True
                #k8.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                #random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                #random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                  
          elif op.param3 in mid2:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                cl.kickoutFromGroup(op.param1,[op.param2])
                G = cl.getGroup(op.param1)
                G.preventedJoinByTicket = False
                #cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = cl.getGroup(op.param1)
                G.preventedJoinByTicket = True
                #cl.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                #random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                
          elif op.param3 in mid3:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                k4.kickoutFromGroup(op.param1,[op.param2])
                G = k4.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k4.updateGroup(G)
                Ticket = k4.reissueGroupTicket(op.param1)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k4.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k4.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                  
          elif op.param3 in mid4:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                k5.kickoutFromGroup(op.param1,[op.param2])
                G = k5.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k5.updateGroup(G)
                Ticket = k5.reissueGroupTicket(op.param1)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k5.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k5.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                  
          elif op.param3 in mid5:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                k6.kickoutFromGroup(op.param1,[op.param2])
                G = k6.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k6.updateGroup(G)
                Ticket = k6.reissueGroupTicket(op.param1)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k6.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k6.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                  
          elif op.param3 in mid6:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                k7.kickoutFromGroup(op.param1,[op.param2])
                G = k7.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k7.updateGroup(G)
                Ticket = k7.reissueGroupTicket(op.param1)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k7.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k7.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                  
          elif op.param3 in mid7:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                k2.kickoutFromGroup(op.param1,[op.param2])
                G = k2.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k2.updateGroup(G)
                Ticket = k2.reissueGroupTicket(op.param1)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k2.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k2.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                  
          elif op.param3 in mid8:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                k9.kickoutFromGroup(op.param1,[op.param2])
                G = k9.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k9.updateGroup(G)
                Ticket = k9.reissueGroupTicket(op.param1)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k9.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k9.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                  
          elif op.param3 in mid9:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                k10.kickoutFromGroup(op.param1,[op.param2])
                G = k10.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k10.updateGroup(G)
                Ticket = k10.reissueGroupTicket(op.param1)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k10.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k10.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                  
          elif op.param3 in mid10:
            if op.param2 in owner:
              pass
            elif op.param2 in Bots:
              pass
            else:
              try:
                k3.kickoutFromGroup(op.param1,[op.param2])
                G = k3.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k3.updateGroup(G)
                Ticket = k3.reissueGroupTicket(op.param1)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k3.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k3.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                
          elif op.param3 in midkoplaxs:
            try:
              cl.kickoutFromGroup(op.param1,[op.param2])
              G = cl.getGroup(op.param1)
              G.preventedJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              koplaxs.acceptGroupInvitationByTicket(op.param1,Ticket)
              G = cl.getGroup(op.param1)
              G.preventedJoinByTicket = True
              cl.updateGroup(G)
              wait["blacklist"][op.param2] = True
            except:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              G = random.choice(KAC).getGroup(op.param1)
              G.preventedJoinByTicket = False
              random.choice(KAC).updateGroup(G)
              Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
              koplaxs.acceptGroupInvitationByTicket(op.param1,Ticket)
              G = random.choice(KAC).getGroup(op.param1)
              G.preventedJoinByTicket = True
              random.choice(KAC).updateGroup(G)
              wait["blacklist"][op.param2] = True
                
        #elif op.type == 19: #Admin Ke Kick
          elif op.param3 in admin:
            if op.param1 not in groupList:
              cl.sendText(op.param1,"This Group Not In Protect List\nWe Will Ignored Anything!!!\nPlease Contact My Owner")
            else:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              else:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(op.param1,[op.param3])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(op.param1,[op.param3])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                  
          elif op.param3 in staff: #Staff Ke Kick
            if op.param1 not in groupList:
              cl.sendText(op.param1,"This Group Not In Protect List\nWe Will Ignored Anything!!!\nPlease Contact My Owner")
            else:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in owner:
                pass
              else:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(op.param1,[op.param3])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(op.param1,[op.param3])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#------------------------
        if op.type == 59:
            print (op)
        
        if op.type == 55:
          try:
            group_id = op.param1
            user_id=op.param2
            subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
          except Exception as e:
              print (e)
            
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            Name = k2.getContact(op.param2).displayName
                            Name = k3.getContact(op.param2).displayName
                            Name = k4.getContact(op.param2).displayName
                            Name = k5.getContact(op.param2).displayName
                            Name = k6.getContact(op.param2).displayName
                            Name = k7.getContact(op.param2).displayName
                            Name = k8.getContact(op.param2).displayName
                            Name = k9.getContact(op.param2).displayName
                            Name = k10.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        random.choice(KAC).sendText(op.param1, "Woy " + "☞ " + nick[0] + " ☜" + "\nDasar Cicitipi\nAku Doain Bintitan   ")
                                    else:
                                        random.choice(KAC).sendText(op.param1, "Woy " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Cicitipi. . .\nChat Woy (-__-)   ")
                                else:
                                    random.choice(KAC).sendText(op.param1, "Jiahahaha " + "☞ " + Name + " ☜" + "\nNgapain Cicitipi Doang???\nGa Gaul Lu ga Mau Chat\nPasti Temennya Dikit ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
        else:
            pass
        #poll.setRevision(op.revision)
        
        
  #except Exception as e:
      #client.log("[SINGLE_TRACE] ERROR : " + str(e))
      
def clPoll():
  while True:
    try:
      ops=poll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll.setRevision(op.revision)
        
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
        
def k2Poll():
  while True:
    try:
      ops=poll2.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll2.setRevision(op.revision)
          
    except Exception as e:
        k2.log("[SINGLE_TRACE] ERROR : " + str(e))
          
def k3Poll():
  while True:
    try:
      ops=poll3.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll3.setRevision(op.revision)
          
    except Exception as e:
        k3.log("[SINGLE_TRACE] ERROR : " + str(e))

def k4Poll():
  while True:
    try:
      ops=poll4.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll4.setRevision(op.revision)
          
    except Exception as e:
        k4.log("[SINGLE_TRACE] ERROR : " + str(e))

def k5Poll():
  while True:
    try:
      ops=poll5.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll5.setRevision(op.revision)
          
    except Exception as e:
        k5.log("[SINGLE_TRACE] ERROR : " + str(e))
          
def k6Poll():
  while True:
    try:
      ops=poll6.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll6.setRevision(op.revision)
          
    except Exception as e:
        k6.log("[SINGLE_TRACE] ERROR : " + str(e))

def k7Poll():
  while True:
    try:
      ops=poll7.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll7.setRevision(op.revision)
          
    except Exception as e:
        k7.log("[SINGLE_TRACE] ERROR : " + str(e))

def k8Poll():
  while True:
    try:
      ops=poll8.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll8.setRevision(op.revision)
          
    except Exception as e:
        k8.log("[SINGLE_TRACE] ERROR : " + str(e))

def k9Poll():
  while True:
    try:
      ops=poll9.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll9.setRevision(op.revision)
          
    except Exception as e:
        k9.log("[SINGLE_TRACE] ERROR : " + str(e))

def k10Poll():
  while True:
    try:
      ops=poll10.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          poll10.setRevision(op.revision)
          
    except Exception as e:
        k10.log("[SINGLE_TRACE] ERROR : " + str(e))

def bossPoll():
  while True:
    try:
      ops=pollboss.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          pollboss.setRevision(op.revision)
          
    except Exception as e:
        koplaxs.log("[SINGLE_TRACE] ERROR : " + str(e))
        
print("Sukses Menjalankan Semua Bot\n")
Thread(target=clPoll).start()