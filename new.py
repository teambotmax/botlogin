# BOT LOGIN BY KHIE
# </> NOOB CODER 2K16
from linepy import *
from akad.ttypes import Message
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from KhieBots.thrift.protocol import TCompactProtocol
from KhieBots.thrift.transport import THttpClient
from KhieBots.ttypes import LoginRequest
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from tmp.MySplit import *
from zalgo import zalgoname
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import LineService
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
#=====================================================================
khie = LINE()
#=======================================================
waitOpen = codecs.open("wait.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
tokenOpen = codecs.open("toket.json","r","utf-8")
premiumOpen = codecs.open("user.json","r","utf-8")
#=====================================================================
#=====================================================================
khieProfile = khie.getProfile()
khieSettings = khie.getSettings()
khiePoll = OEPoll(khie)
khieMID = khie.getProfile().mid
#=====================================================================
#=====================================================================
loop = asyncio.get_event_loop()
admin =["u79a6284e9ef959e88784874c6b662c9a"]
myAdmin = ["u79a6284e9ef959e88784874c6b662c9a"]
botStart = time.time()
msg_dict = {}
temp_flood = {}
groupName = {}
groupImage = {}
kuciyose = {}
protectname = []
wbanlist = []
protectinvite = []
protectkick = []
protectjoin = []
protectqr = []
protectantijs = []
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
token = json.load(tokenOpen)
premium = json.load(premiumOpen)
responsename = khie.getProfile().displayName
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']

kimak= {
    "Addaudio": False,
    "Audio": {},
    "Audios": {
     },
}

hoho = {
    "savefile": False,
    "namefile": "",
}

itil = {
    "blacklist": {},
}

peler = { 
    "receivercount": 0,
    "sendcount": 0
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

read = { 
    "readMember": {},
    "readPoint": {}
}
#=====================================================================
#=====================================================================
settings["myProfile"]["displayName"] = khieProfile.displayName
settings["myProfile"]["statusMessage"] = khieProfile.statusMessage
settings["myProfile"]["pictureStatus"] = khieProfile.pictureStatus
cont = khie.getContact(khieMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = khie.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
#=====================================================================
#=====================================================================
with open("temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = khie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = khie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output KhieBot.mp3 {}'.format(link))
    try:
        khie.sendAudio(to, 'KhieBot.mp3')
        time.sleep(2)
        os.remove('KhieBot.mp3')
    except Exception as e:
        khie.sendMessage(to, "Error")
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output KhieBot.mp4 {}'.format(link))
    try:
        khie.sendVideo(to, "KhieBot.mp4")
        time.sleep(2)
        os.remove('KhieBot.mp4')
    except Exception as e:
        khie.sendMessage(to, "Error")

def debug():
    get_profile_time_start = time.time()
    get_profile = khie.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = khie.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = khie.getContact(get_profile.mid)
    get_contact_time = time.time() - get_contact_time_start
    elapsed_time = time.time() - get_profile_time_start
    return " 「 Debug 」\n - Send Message\n   %.5f\n - Get Profile\n   %.5f\n - Get Contact\n   %.5f\n - Get Group\n   %.5f" % (elapsed_time,get_profile_time,get_contact_time,get_group_time)
#=====================================================================
def headers():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "CHROMEOS\t5.5.1\tRat-Login\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers2():
    Headers = {
    'User-Agent': "Line/8.11.0",
    'X-Line-Application': "IOSIPAD\t6.9\tRat-Login\t6.9",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers3():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "WIN10\t5.5.5\tRat-Login\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers4():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "DESKTOPMAC\t5.5.1\tRat-Login\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers

def headers5():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "DESKTOPWIN\t5.8.0\tRat-Login\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers6():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "WIN10\t5.5.5\tRat-Login\tV1.5\11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
#def Template(to):
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    khie.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    khie.sendMessage(to, '', annda, 13)

def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            khie.sendMessage(to, text, {'MSG_SENDER_NAME': khie.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + khie.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            khie.sendMessage(to, text, {'MSG_SENDER_NAME': khie.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + khie.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@KhieGans  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    khie.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(khie.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + khie.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = khie.genOBSParams({'oid': khieMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = khie.server.postContent('{}/talk/vp/upload.nhn'.format(str(khie.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        khie.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("KhieWasHere.mp4")
    
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = client.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)
#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================

def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def change(url):
	import base64
	return base64.b64encode(url.encode()).decode()
	
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@MentionOrang "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        khie.sendMessage(to, textx, {'MSG_SENDER_NAME': client.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + khie.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================
def logError(text):
    khie.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#=====================================================================
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        f = codecs.open('user.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = khie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output KhieBot.mp3 {}'.format(link))
    try:
        khie.sendAudio(to, 'KhieBot.mp3')
        time.sleep(2)
        os.remove('KhieBot.mp3')
    except Exception as e:
        khie.sendMessage(to, "Error")
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output KhieBot.mp4 {}'.format(link))
    try:
        khie.sendVideo(to, "KhieBot.mp4")
        time.sleep(2)
        os.remove('KhieBot.mp4')
    except Exception as e:
        khie.sendMessage(to, "Error")
#=====================================================================
async def khieBot(op):
    try:
        if settings["restartPoint"] != None:
            khie.sendMessage(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return
                        
        if op.type in [22,24]:
            client.leaveRoom(op.param1)
#=====================================================================
        if op.type == 13:
            if khie.getProfile().mid in op.param3:
                G = khie.getCompactGroup(op.param1)
                if settings["autoJoin"] == True:
                    khie.acceptGroupInvitation(op.param1)

        if op.type in [25, 26]:
            if op.type == 25: print ("[ 25 ] SEND MESSAGE")
            else: print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message               
            text = msg.text
            msg_id = msg.id
            receiver = msg.to             
            sender = msg._from
            s = khie.getProfile().mid
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False:
               setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:                    	
                    if sender != khie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if sender != s:
                	        peler["receivercount"] += 1
                        if sender == s:
                	        peler["sendcount"] += 1

#=====================================================================
#==========================================
#==========================================
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != khieMID: to = sender
                else: to = receiver
                if msg.contentType == 6:
                    try:
                        contact = khie.getContact(sender)
                        if msg.toType == 2:
                            anu = khie.getGroup(to)
                            if msg.contentMetadata['GC_EVT_TYPE'] == 'S' and msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                anu = msg.contentMetadata={'GC_EVT_TYPE': 'S', 'GC_CHAT_MID': to, 'RESULT': 'INFO', 'SKIP_BADGE_COUNT': 'false', 'GC_IGNORE_ON_FAILBACK': 'false', 'TYPE': 'G', 'DURATION': '0', 'GC_MEDIA_TYPE': 'VIDEO', 'VERSION': 'X', 'CAUSE': '16'}
                    except Exception as e:
                        khie.sendMessage(to, str(e))
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != khieMID: to = sender
                else: to = receiver
                if msg.contentType == 14:
                    if hoho["savefile"] == True:
                        try:
                             namafile = hoho["namafile"]
                             khie.downloadObjectMsg(msg_id,saveAs=namafile)
                             hoho["savefile"] = False
                             khie.sendMessage(to, "Successful, the file has been uploaded")
                        except Exception as e:
                         	khie.sendMessage(to, str(e))
                if msg.contentType == 1: 
                    if settings["changeCoverProfile"] == True:
                        path = khie.downloadObjectMsg(msg_id)
                        settings["changeCoverProfile"] = False
                        khie.updateProfileCover(path)
                        khie.sendMessage(to,"Cover Image Updated.")                                           
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    if msg.toType == 0:
                        if settings["autoRead"] == True:
                            khie.sendChatChecked(to, msg_id)
                    if msg.toType == 2:
                        if settings["autoRead1"] == True:
                            khie.sendChatChecked(to, msg_id)
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if settings["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = khie.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    khie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    khie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    khie.leaveGroup(group.id)
#==========================================
#==========================================
                    elif cmd.startswith("#savefile"):
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            text = removeCmd("#savefile", text)
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ", text)
                            if " " in key:
                                khie.sendMessage(to, "Failed !")
                            else:
                                hoho["namafile"] = str(key).lower()
                                hoho["savefile"] = True
                                khie.sendMessage(to, "Send file to save to be「 {} 」".format(str(key).lower()))
#                    elif cmd == "help":
#                        khie.sendMessage(to, "Type #help", {'QUICK_REPLY': '{"items": [{"type": "action","useTintColor": False,"imageUrl": "https://boteater.co/jpg-t8vyjfvq.jpg","action": {"type": "message","label": "Help","text": "#help"}},{"type": "action","useTintColor": False,"imageUrl": "https://boteater.co/jpg-t8vyjfvq.jpg","action": {"type": "message","label": "Mention","text": "#mention"}}]}'}, 0)
                    elif cmd == "#change cover":
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            settings["changeCoverProfile"] = True
                            khie.sendMessage(to,"Send a Image to change cover.")
#==========================================
                    elif cmd.startswith("infogithub "):
                        users = removeCmd("infogithub", text)
                        path = requests.get('https://api.github.com/users/{}'.format(users))
                        data = path.text
                        data = json.loads(data)
                        data = {
                            "type": "template",
                            "altText": "information",
                            "template": {
                                "type": "buttons",
                                "thumbnailImageUrl": "{}".format(str(data["avatar_url"])),
                                "imageSize": "contain",
                                "imageAspectRatio": "square",
                                "title": '{}'.format(str(data["name"])),
                                "text": 'Followers: {}\nFollowing: {}\nRepositories: {}'.format(str(data["followers"]), (data["following"]), (data["public_repos"])),
                                "actions": [{
                                    "type": "uri",
                                    "label": "Repositories",
                                    "uri": "https://github.com/{}?tab=repositories".format(str(users))
                                },
                                {
                                    "type": "uri",
                                    "label": "Go Page",
                                    "uri": "https://github.com/{}".format(str(users))
                                }]
                            }
                        }
                        sendTemplate(to, data)
#==========================================
                    elif cmd.startswith("#down "):
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                           number = removeCmd("#down", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 5000:                                             
                                       khie.sendMessage(to,"invalid >_< ! Max: 5000.")
                                   else:
                                       for i in range(0,number):
                                           khie.sendMessage(to,str(number))
                                           number -= 1
                                           time.sleep(0.008)
                               else:
                                  khie.sendMessage(to,"Please specify a valid number.")

                    elif cmd == "example login":
                        ret = "How to Login SelfBots\n\n"
                        ret += "Example :\n"
                        ret += "1. Addfree <your name>\n"
                        ret += "2. Login Free\n"
                        ret += "3. Click Link QR\n"
                        ret += "4. Click Link Liff\n"
                        ret += "5. Type Help to see your cmd"
                        hello = "{}".format(str(ret))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret)),
                            "sentBy": {
                                "label": "</> Noob Coder",
                                "iconUrl": "https://obs.line-scdn.net/{}".format(khie.getContact(khieMID).pictureStatus),
                                "linkUrl": "line://nv/profilePopup/mid=u79a6284e9ef959e88784874c6b662c9a"
                            }
                        }
                        sendTemplate(to, data)
#==========================================
                    if cmd == "kiss me":
                        khie.generateReplyMessage(msg.id)
                        khie.sendReplyMessage(msg.id, to,"。。・゜゜・❤ "+khie.getContact(sender).displayName+" ❤ \n(づ￣ ³￣)づ")
#==========================================
                    elif cmd == "(help)":
                        data = {
                            "type": "flex",
                            "altText": "help message",
                            "contents": {
                                "type": "carousel",
                                "contents": [
                                     {
                                        "type": "bubble",
                                        "styles": {
                                            "header": {"backgroundColor": "#000000"},
                                            "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                                        },
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "md",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=u79a6284e9ef959e88784874c6b662c9a",
                                                },
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "Free Command :",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "color": "#000000"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "1. Example Login",
                                                    "size": "xxs",
                                                    "align": "center",
                                                    "color": "#000000"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "2. Addfree <name>",
                                                    "size": "xxs",
                                                    "align": "center",
                                                    "color": "#000000"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "3. Login Free",
                                                    "size": "xxs",
                                                    "align": "center",
                                                    "color": "#000000"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "4. Logout Free",
                                                    "size": "xxs",
                                                    "align": "center",
                                                    "color": "#000000"
                                                }
                                           ]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "contents": [
                                                        {
                                                            "type": "icon",
                                                            "url": "https://boteater.co/jpg-2rzb4yuq.jpg",
                                                            "size": "md"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "Noob </> Coder",
                                                            "align": "center",
                                                            "color": "#FFFFFF",
                                                            "size": "md"
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm",
                                                        }
                                                    ]
                                                }
                                            ]
                                       }
                                    }
                                ]
                            }
                        }
                        sendTemplate(to, data)

                    elif cmd == "help":
                        data = {
                            "type": "flex",
                            "altText": "help message",
                            "contents": {
                                "type": "carousel",
                                "contents": [
                                     {
                                        "type": "bubble",
                                        "styles": {
                                            "header": {"backgroundColor": "#000000"},
                                            "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                                        },
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "md",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=u79a6284e9ef959e88784874c6b662c9a",
                                                },
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "Premium Command :",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "color": "#000000"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "1. Login Sb",
                                                    "size": "xxs",
                                                    "align": "center",
                                                    "color": "#000000"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "2. Logout Sb",
                                                    "size": "xxs",
                                                    "align": "center",
                                                    "color": "#000000"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "3. Restart Sb",
                                                    "size": "xxs",
                                                    "align": "center",
                                                    "color": "#000000"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "4. Help Login",
                                                    "size": "xxs",
                                                    "align": "center",
                                                    "color": "#000000"
                                                }
                                           ]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "contents": [
                                                        {
                                                            "type": "icon",
                                                            "url": "https://boteater.co/jpg-2rzb4yuq.jpg",
                                                            "size": "md"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "Noob </> Coder",
                                                            "align": "center",
                                                            "color": "#FFFFFF",
                                                            "size": "md"
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "sm",
                                                        }
                                                    ]
                                                }
                                            ]
                                       }
                                    }
                                ]
                            }
                        }
                        sendTemplate(to, data)
                    elif cmd == "cmd":
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            ret = "Help Message\n\n"
                            ret += "  • #glist\n"
                            ret += "  • #skill\n"
                            ret += "  • #slain\n"
                            ret += "  • #cvp\n"
                            ret += "  • #debug\n"
                            ret += "  • #speed\n"
                            ret += "  • #bcast\n"
                            ret += "  • #leave"
                            hello = "{}".format(str(ret))
                            data = {
                                "type": "text",
                                "text": "{}".format(str(ret)),
                                "sentBy": {
                                    "label": "</> Noob Coder",
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(khie.getContact(khieMID).pictureStatus),
                                    "linkUrl": "line://nv/profilePopup/mid=u79a6284e9ef959e88784874c6b662c9a"
                                }
                            }
                        sendTemplate(to, data)
#==========================================
#=========================================
#==========================================
#==========================================
                    elif cmd.startswith("#leave "):
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            number = removeCmd("#leave", text)
                            groups = khie.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = khie.getGroup(group)
                                try:
                                    khie.leaveGroup(G.id)
                                except:
                                    khie.leaveGroup(G.id)
                                khie.sendMessage(to, "「Leave 」\n\nGroup : " + G.name)
                            except Exception as error:
                                khie.sendMessage(to, str(error))
#==========================================
                    if cmd == "chat maker":
                        khie.sendMention(msg.to, 'Hallo @! if u want chat my creator\nType : Chatmaker [text]\nExample : Chatmaker hi khie',' ', [msg._from])
                    elif cmd.startswith("chatmaker "):
                        sep = text.split(" ")
                        txt = text.replace(sep[0] + " ","")
                        contact = khie.getContact(sender)
                        owner = "u79a6284e9ef959e88784874c6b662c9a"
                        mat_ = "Sender: @!"
                        mat_ += "\nMessage: {}".format(txt)
                        mat = {
                            'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,
                            'MSG_SENDER_NAME':  contact.displayName,
                            'mid': sender,
                        }
                        mid = khie.getContact(sender).displayName
                        mentions(owner, mat_, [sender])
                        khie.sendMessage(owner, mid, contentMetadata=mat, contentType=13)
                        khie.sendMention(to, "Hi @!\nYour message has been send ^_^","",[msg._from])
#==========================================
                    elif text.lower() == "list user" and msg._from not in myAdmin and to not in chatbot["botMute"]:
                        khie.sendMention(msg.to, 'Type : List user selfbot\n\nHai @! Sorry you are not Owner',' ', [msg._from])
                    elif text.lower() == "restart sb" and msg._from not in premium["myService"]:
                        khie.sendMention(msg.to, 'Type : Restart selfbot\n\nHai @! Sorry You are not listed In List Premium',' ', [msg._from])
                    elif text.lower() == "login sb" and msg._from not in premium["myService"]:
                        khie.sendMention(msg.to, 'Type : Login selfbot\n\nHai @! Sorry You are not listed In List Premium',' ', [msg._from])
                    elif text.lower() == "help login" and msg._from not in premium["myService"]:
                        khie.sendMention(msg.to, 'Type : Help login selfbot\n\nHai @! Sorry You are not listed In List Premium',' ', [msg._from])
                    elif text.lower() == "logout sb" and msg._from not in premium["myService"]:
                        khie.sendMention(msg.to, 'Type : LogOut selfbot\n\nHai @! Sorry You are not listed In List Premium',' ', [msg._from])
#==========================================
 #                   elif text.lower() == "free restart" and msg._from not in free["freeSb"]:
#                        khie.sendMention(msg.to, 'Type : Restart selfbot\n\nHai @! Sorry You are not listed In List Free',' ', [msg._from])
#                    elif text.lower() == "login free" and msg._from not in free["freeSb"]:
#                        khie.sendMention(msg.to, 'Type : Help login selfbot\n\nHai @! Sorry You are not listed In List Free',' ', [msg._from])
#                    elif text.lower() == "logout free" and msg._from not in free["freeSb"]:
#                        khie.sendMention(msg.to, 'Type : LogOut selfbot\n\nHai @! Sorry You are not listed In List Free',' ', [msg._from])
#==========================================
                    elif cmd.startswith("#name "):
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            string = removeCmd("#name", text)
                            if len(string) <= 10000000000:
                                pname = khie.getContact(sender).displayName
                                profile = khie.getProfile()
                                profile.displayName = string
                                khie.updateProfile(profile)
                                khie.sendMessage(to, "「 Update Name 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                    elif cmd.startswith("#status "):
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            string = removeCmd("#status", text)
                            if len(string) <= 10000000000:
                                pname = khie.getContact(sender).statusMessage
                                profile = khie.getProfile()
                                profile.statusMessage = string
                                khie.updateProfile(profile)
                                khie.sendMessage(to, "「 Update Status 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
#==========================================
#==========================================
                    elif cmd == "ping":
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            khie.sendMention(to, "PONG ! @!","",[msg._from])
#==========================================
#==========================================
#==========================================
#==========================================
                    elif cmd == "#join on":
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            if settings["autoJoin"] == True:
                                msgs=" 「 Join 」\nJoin already Enable♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to Enable♪"
                                settings["autoJoin"] = True
                            khie.sendMessage(to, msgs)
                    elif cmd == "#join off":
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            if settings["autoJoin"] == False:
                                msgs=" 「 Join 」\nJoin already DISABLED♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to DISABLED♪"
                                settings["autoJoin"] = False
                            khie.sendMessage(to, msgs)
#==========================================
#==========================================
#==========================================
#==========================================
                    elif cmd == "#mention":
                        group = khie.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(khie.getProfile().mid)
                        khie.datamention(to,'Mention',nama)
                    elif cmd== '#bye':
                        data = {
                            "type": "template",
                            "altText": "byebye",
                            "template": {
                                "type": "image_carousel",
                                "columns": [
                                    {
                                        "imageUrl":"https://stickershop.line-scdn.net/stickershop/v1/sticker/9173596/IOS/sticker@2x.png",
                                        "size": "full",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://nv/profilePopup/mid=u79a6284e9ef959e88784874c6b662c9a"
                                        }
                                    }
                                ]
                            }
                        }
                        sendTemplate(to, data)
                        khie.leaveGroup(to)
#==========================================
#==========================================
                    elif cmd.startswith("#skill "):
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = khie.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           for x in members:
                               contact = khie.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return khie.sendMessage(to,"not found name "+midn)
                           for target in targets:
                               khie.kickoutFromGroup(msg.to,[target])
                    elif cmd.startswith("#slain "):
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = khie.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           for x in members:
                               contact = khie.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return khie.sendMessage(to,"not found name "+midn)
                           for target in targets:
                               khie.kickoutFromGroup(msg.to,[target])
                               khie.findAndAddContactsByMid(target)
                               khie.inviteIntoGroup(msg.to, [target])
                               khie.cancelGroupInvitation(msg.to, [target])
                               time.sleep(5)
                               khie.inviteIntoGroup(msg.to, [target])
#==========================================
#==========================================
                    elif cmd.startswith("#cvp"):
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            link = removeCmd("helper:cvp", text)
                            contact = khie.getContact(sender)
                            khie.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = khie.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            time.sleep(2)
                            changeVideoAndPictureProfile(pict, vids)
                            khie.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("TeamAnuBot.mp4")                            
#==========================================
#==========================================
                    elif cmd == "about":
                        try:
                            arr = []
                            today = datetime.today()
                            thn = 2018 
                            bln = 8    #isi bulannya yg sewa
                            hr = 9   #isi tanggalnya yg sewa
                            future = datetime(thn, bln, hr)
                            days = (str(future - today))
                            comma = days.find(",")
                            days = days[:comma]
                            h = khie.getContact(khieMID)
                            groups = khie.getGroupIdsJoined()
                            contactlist = khie.getAllContactIds()
                            khietag = "u79a6284e9ef959e88784874c6b662c9a"
                            pedopil = "u21d04f683a70ee8776c4c58a0358c204"
                            kontak = khie.getContacts(contactlist)
                            favorite = khie.getFavoriteMids()
                            fil = khie.getSettings().privacyReceiveMessagesFromNotFriend
                            seal = khie.getSettings().e2eeEnable
                            blockedlist = khie.getBlockedContactIds()
                            src = khie.getSettings().privacySearchByUserid
                            kontak2 = khie.getContacts(blockedlist)
                            status = {"kick": "", "invite": ""}
                            try:khie.kickoutFromGroup(to, [khieMID]);status["kick"] = "Normal"
                            except:status["kick"] = "Limit"
                            try:khie.inviteIntoGroup(to, [khieMID]);status["invite"] = "Normal"
                            except:status["invite"] = "Limit"
                            if src == True:alid = "Add From LineID : True"
                            else:alid = "Add From LineID : False"                            
                            if seal == True:letsel = "Letter Sealing : True"
                            if seal == False:letsel = "Letter Sealing : False"
                            if fil == True:fpes = "Filter Message : False"
                            if fil == False:fpes = "Filter Message : True"
                            ret_ = "About Bots :\n"
                            ret_ += "\nBots : {}".format(h.displayName)
                            ret_ += "\nGroup : {}".format(str(len(groups)))
                            ret_ += "\nFriend : {}".format(str(len(kontak)))
                            ret_ += "\nFavorite: {}".format(str(len(favorite)))
                            ret_ += "\nBlocked : {}".format(str(len(kontak2)))
                            ret_ += "\nChat send : {}".format(str(peler["sendcount"]))
                            ret_ += "\nChat received : {}".format(str(peler["receivercount"]))
                            ret_ += "\n{}".format(alid)
                            ret_ += "\n{}".format(letsel)
                            ret_ += "\n{}".format(fpes)
                            ret_ += "\nKick : %s" % status["kick"]
                            ret_ += "\nInvite : %s" % status["invite"]
                            ret_ += "\n\nType : Bot Login"
                            ret_ += "\nVersion : V.08"
                            ret_ += "\nMaker :\n"
                            ret_ += "- @!                  "
                            ret_ += "\n- @!                  "
                            ret_ += "\nPowered :"
                            ret_ += "\nNoob </> Coder"
                            mentions(to, str(ret_),[khietag,pedopil])
                        except Exception as e:
                            khie.sendMessage(to, str(e))
#==========================================
#==========================================
                    elif cmd == "#debug":
                       if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            khie.sendMessage(to, debug())
                    elif cmd == "speed":
                        start = time.time()
                        khie.sendMessage("u79a6284e9ef959e88784874c6b662c9a", '</>')
                        elapsed_time = time.time() - start
                        khie.sendMessage(to,"Time:\n%s"%str(round(elapsed_time,5)))
#==========================================
#==========================================
                    elif cmd == "#glist":
                       if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = khie.getGroupIdsJoined()
                            sd = khie.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups\n".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                khie.generateReplyMessage(msg.id)
                                khie.sendReplyMessage(msg.id, to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                    elif cmd.startswith("#bcast"):
                      if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                        tod = text.split(" ")
                        hey = text.replace(tod[0] + " ", "")
                        text = "{}".format(hey)
                        groups = khie.getGroupIdsJoined()
                        friends = khie.getAllContactIds()
                        for gr in groups:
                            data = {
                                "type": "text",
                                "text": "「 Group Broadcast 」\n\n{}".format(text),
                                "sentBy": {
                                    "label": "Group Broadcast",
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(khie.getContact(khieMID).pictureStatus),
                                    "linkUrl": "line://nv/profilePopup/mid=u79a6284e9ef959e88784874c6b662c9a"
                                }
                            }
                            bcTemplate(gr, data)
                            time.sleep(1)
                        khie.sendMessage(to, "Succes Group cast to {} group ".format(str(len(groups))))
                    elif cmd.startswith("#openqr "):
                      if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            number = removeCmd("#openqr", text)
                            groups = khie.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = khie.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    khie.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(khie.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    khie.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(khie.reissueGroupTicket(G.id)))
                                khie.sendMessage(to, "「 Open Qr 」\n\nGroup : " + G.name + "\nLink: " + gurl)
                            except Exception as error:
                                khie.sendMessage(to, str(error))
#==========================================
#==========================================
                    elif text.lower() == "login sb" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            try:
                                a = headers6()
                                a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                qr = client.getAuthQrcode(keepLoggedIn=1, systemName='Rat-Login')
                                link = "line://au/q/" + qr.verifier
                                if msg.toType == 2:khie.sendMention(msg.to, '「 Request Login 」\nCheck your PM @!',' ', [msg._from])
                                else:pass
                                khie.sendMention(msg._from, '「 Request Login 」\nClick link @!, only 2 minutes\n{}'.format(link),"",[msg._from])
                                a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                a.update({'x-lpqs' : '/api/v4p/rs'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                req = LoginRequest()
                                req.type = 1
                                req.verifier = qr.verifier
                                req.e2eeVersion = 1
                                res = client.loginZ(req)
                                if msg._from not in premium['listLogin']:
                                    premium['listLogin'][msg._from] =  '%s' % user
                                    isi = "{}".format(res.authToken)
                                    os.system('cp -r login {}'.format(user))
                                    os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                    os.system('screen -dmS {}'.format(user))
                                    os.system('screen -r {} -X stuff "cd {} && python3 staff.py \n"'.format(user, user))
                                    khie.sendMention(msg.to, '「 Login Succes 」\n> @!\n> User name : {}\n> Click link liff for access temp :\nline://app/1602687308-GXq4Vvk9?type=text&text=FC_SAMURAI'.format(user),' ', [msg._from])
                                else:
                                    khie.sendMention(msg.to, '「 Request Login 」\n@!\nLink QR Expired -_-',' ', [msg._from])
                            except:
                                khie.sendMention(msg.to, '「  ERROR 」\n@!\nPlease Nonactive Filter Chat Or Letter Sealing -_-',' ', [msg._from])
                    elif text.lower() == "login sb" and msg._from in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            khie.sendMention(msg.to, '「 Login SelfBot 」\nHello @!Sorry Please Logout First Log In With Type  < LogoutSb >\nBecause You Are Still Login',' ', [msg._from])
                    elif text.lower().startswith("addme ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                        if msg._from not in premium['myService']:
                            nama = str(text.split(' ')[1])
                            premium['myService'][msg._from] =  '%s' % nama
                            khie.sendMention(msg.to, "「 Add Me  」 \nAdd @! to Login..","",[msg._from])
                        else:
                            khie.sendMention(msg.to, "「Add Me 」\nOwner @! already in List..","",[msg._from])
                    elif text.lower().startswith("adduser ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 not in premium['myService']:
                                    nama = str(text.split(' ')[1])
                                    premium['myService'][key1] =  '%s' % nama
                                    khie.sendMention(msg.to, '「 Add Service  」\nAdded @! to service','', [key1])
                                else:
                                    khie.sendMention(msg.to, '「 Add Service  」\nUser @! already in service','', [key1])
                    elif text.lower().startswith("deluser ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 in premium['myService']:
                                    del premium['myService'][key1]
                                    khie.sendMention(msg.to, '「 Del Service  」\nDeleted @! from service','', [key1])
                                else:
                                    khie.sendMention(msg.to, '「 Del Service  」\n\nUser @! not in service','', [key1])
                    elif text.lower() == "list user" and msg._from in myAdmin and to not in chatbot["botMute"]:
                        h = [a for a in premium['myService']]
                        k = len(h)//20
                        for aa in range(k+1):
                            msgas = '「 List Service 」\n'
                            no=0
                            for a in h:
                                no+=1
                                if premium['myService'][a] == "":cd = "None."
                                else:cd = premium['myService'][a]
                                if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                            khie.sendMention(msg.to, msgas,'', h)
                    elif text.lower() == "help login" and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            khie.sendMention(msg.to, 'Hai @!\n\n1. Type : Login Sb\n2. Check Personal Chat\n3. Press the Link Qr\n4. Type "Help" To see your command',' ', [msg._from])
                    elif text.lower() == "logout sb" and msg._from in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            del premium['listLogin'][msg._from]
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('rm -rf {}'.format(str(user)))
                            time.sleep(2)
                            khie.sendMention(msg.to, '「  Logout Sb  」\n> @! LogOut From Selfbot',' ', [msg._from])
                    elif text.lower() == "logout sb" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            khie.sendMention(msg.to, '「  Logout Sb  」\nHai @!Sorry Please You Login First By Type < Login Sb > Or Type < Help Login >',' ', [msg._from])
                    elif text.lower() == "restart sb" and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('screen -dmS {}'.format(user))
                            os.system('screen -r {} -X stuff "cd {} && python3 staff.py \n"'.format(user, user))
                            time.sleep(3)
                            khie.sendMention(msg.to, '「  Restart Sb  」\n> @! Succes Restart selfbot',' ', [msg._from])
                    elif text.lower().startswith("remove") and msg._from in myAdmin and to not in chatbot["botMute"]:
                        sep = text.split(" ")
                        anu = text.replace(sep[0] + " ","")
                        os.system("screen -S {} -X quit".format(str(anu)))
                        os.system('rm -rf {}'.format(str(anu)))
                        time.sleep(2)
                        khie.sendMention(msg.to, '「 Remove 」\n> @!\nSucces remove file : {}'.format(str(anu)),' ', [msg._from])
#==========================================
# FREE SELFBOT
#==========================================
                    elif text.lower() == "/login free" and msg._from not in free['listFree'] and to not in chatbot["botMute"]:
                        if msg._from in free["freeSb"]:
                            user = free["freeSb"][msg._from]
                            try:
                                a = headers6()
                                a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                qr = client.getAuthQrcode(keepLoggedIn=1, systemName='Rat-Login')
                                link = "line://au/q/" + qr.verifier
                                if msg.toType == 2:khie.sendMention(msg.to, '「 Request Login 」\nกดลิ้งได้ที่แชทส่วนตัว @!',' ', [msg._from])
                                else:pass
                                khie.sendMention(msg._from, '「 Request Login 」\nกดลิ้ง @!, ภายใน2นาที\n{}'.format(link),"",[msg._from])
                                a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                a.update({'x-lpqs' : '/api/v4p/rs'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                transport.setCustomHeaders(a)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = LineService.Client(protocol)
                                req = LoginRequest()
                                req.type = 1
                                req.verifier = qr.verifier
                                req.e2eeVersion = 1
                                res = client.loginZ(req)
                                if msg._from not in free['listFree']:
                                    free['listFree'][msg._from] =  '%s' % user
                                    isi = "{}".format(res.authToken)
                                    os.system('cp -r free {}'.format(user))
                                    os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                    os.system('screen -dmS {}'.format(user))
                                    os.system('screen -r {} -X stuff "cd {} && python3 free.py \n"'.format(user, user))
                                    khie.sendMention(msg.to, '「 Login Succes 」\n> @!\n> User name : {}\n> Click link liff for access temp :\nline://app/1602687308-GXq4Vvk9?type=text&text=Free%20Self%20Bots'.format(user),' ', [msg._from])
                                else:
                                    khie.sendMention(msg.to, '「 Request Login 」\n@!\nLink QR Expired -_-',' ', [msg._from])
                            except:
                                khie.sendMention(msg.to, '「  ERROR 」\n@!\nกรุณากดปิดการเข้ารหัสขั้นสูง Letter Sealing ด้วย -_-',' ', [msg._from])

                    elif text.lower() == "/login free" and msg._from in free['listFree'] and to not in chatbot["botMute"]:
                        if msg._from in free["freeSb"]:
                            khie.sendMention(msg.to, '「 Login SelfBot 」\nสวัสดีคับ @!ต้องขออภัย คุณต้องทำการ ลอคเอาท์ก่อน ถึงจะลอคอินใหม่อีดครั้งได้ \n คำสังในการลอคเอาท์คือ < /Logout free >\nแล้วค่อยสั่งลอคอินอีกครั้งด้วยคำสั่ง\n< /Login free >',' ', [msg._from])
                    elif text.lower().startswith("/addfree "):
                        if msg._from not in free['freeSb']:
                            nama = str(text.split(' ')[1])
                            free['freeSb'][msg._from] =  '%s' % nama
                            khie.sendMention(msg.to, "「 Add Me  」 \nAdd @! to Login..","",[msg._from])
                        else:
                            khie.sendMention(msg.to, "「Add Me 」\nYou @! already in List..","",[msg._from])
                    elif text.lower().startswith("free adduser ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 not in free['freeSb']:
                                    nama = str(text.split(' ')[1])
                                    free['myService'][key1] =  '%s' % nama
                                    khie.sendMention(msg.to, '「 Add Service  」\nAdded @! to service','', [key1])
                                else:
                                    khie.sendMention(msg.to, '「 Add Service  」\nUser @! already in service','', [key1])
                    elif text.lower().startswith("free deluser ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 in free['freeSb']:
                                    del free['freeSb'][key1]
                                    khie.sendMention(msg.to, '「 Del Service  」\nDeleted @! from service','', [key1])
                                else:
                                    khie.sendMention(msg.to, '「 Del Service  」\n\nUser @! not in service','', [key1])
                    elif text.lower() == "/free list" and msg._from in myAdmin and to not in chatbot["botMute"]:
                        h = [a for a in free['freeSb']]
                        k = len(h)//20
                        for aa in range(k+1):
                            msgas = '「 List Free 」\n'
                            no=0
                            for a in h:
                                no+=1
                                if free['freeSb'][a] == "":cd = "None."
                                else:cd = free['freeSb'][a]
                                if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                            khie.sendMention(msg.to, msgas,'', h)
                    elif text.lower() == "/logout free" and msg._from in free['listFree'] and to not in chatbot["botMute"]:
                        if msg._from in free["freeSb"]:
                            del free['listFree'][msg._from]
                            user = free["freeSb"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('rm -rf {}'.format(str(user)))
                            time.sleep(2)
                            khie.sendMention(msg.to, '「  Logout Sb  」\n> @! LogOut From Selfbot',' ', [msg._from])
                    elif text.lower() == "/logout free" and msg._from not in free['listFree'] and to not in chatbot["botMute"]:
                        if msg._from in free["freeSb"]:
                            khie.sendMention(msg.to, '「  Logout Sb  」\nHai @!Sorry Please You Login First By Type < Login Free >',' ', [msg._from])
                    elif text.lower() == "/restart free" and to not in chatbot["botMute"]:
                        if msg._from in free["freeSb"]:
                            user = free["freeSb"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('screen -dmS {}'.format(user))
                            os.system('screen -r {} -X stuff "cd {} && python3 free.py \n"'.format(user, user))
                            time.sleep(3)
                            khie.sendMention(msg.to, '「  Restart Sb  」\n> @! Succes Restart selfbot',' ', [msg._from])
#==========================================
#==========================================
                    elif text.lower() == "#reboot":
                        if msg._from in "u79a6284e9ef959e88784874c6b662c9a":
                            khie.sendMention(to, "@! Brb , going to pee",' ', [msg._from])
                            restartBot()
                        else:pass
#==========================================
#==========================================
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoin"] == True or settings["autoJoin"] == False:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = khie.findGroupByTicket(ticket_id)
                                khie.acceptGroupInvitationByTicket(group.id,ticket_id)
        if op.type == 55:
            print("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in wait['readPoint']:
                    if op.param2 in wait['ROM1'][op.param1]:
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                    else:
                        wait['ROM1'][op.param1][op.param2] = op.param2
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                        try:
                            if wait['lurkauto'] == True:
                                if len(wait['setTime'][op.param1]) % 5 == 0:
                                    anulurk(op.param1,wait)
                        except:pass
                elif op.param2 in wait['readPoints']:
                    wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                    wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
                else:pass
            except:
                pass
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
    
def run():
    while True:
        try:
            ops = khiePoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(khieBot(op))
                   #clientBot(op)
                   khiePoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()