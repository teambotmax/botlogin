import humanize,requests,traceback
from random import randint
from bs4 import BeautifulSoup
def instagramku(msg,wait,tksop,ss):
        data = {
                                    "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "INSTAGRAM",
                                            "contents": {
                                                "type": "bubble",
                                                "header": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "{}".format(ss['full_name']),
                                                            "weight": "bold",
                                                            "color": "#262423",
                                                            "size": "sm"
                                                        }
                                                    ]
                                                },
                                                "hero": {
                                                    "type": "image",
                                                    "url": "{}".format(ss['profile_pic_url_hd']),
                                                    "size": "full",
                                                    "aspectRatio": "1:1",
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "INSTAGRAM PROFILE",
                                                            "weight": "bold",
                                                            "size": "md",
                                                            "margin": "md"
                                                        },
                                                        {
                                                            "type": "separator",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "margin": "lg",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Nama",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 3
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(ss['full_name']),
                                                                            "color": "#262423",
                                                                            "size": "sm",
                                                                            "wrap": True,
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Username",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 3
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(tksop),
                                                                            "color": "#262423",
                                                                            "size": "sm",
                                                                            "wrap": True,
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Bio",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 3
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(ss['biography']),
                                                                            "color": "#262423",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Private",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 3
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(ss['is_private']),
                                                                            "color": "#262423",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Followers",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 3
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(humanize.intcomma(ss['edge_followed_by']['count'])),
                                                                            "color": "#262423",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Following",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 3
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(humanize.intcomma(ss['edge_follow']['count'])),
                                                                            "color": "#262423",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Post",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 3
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(humanize.intcomma(ss['edge_owner_to_timeline_media']['count'])),
                                                                            "color": "#262423",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [{
                                                            "type": "button",
                                                            "flex": 2,
                                                            "style": "primary",
                                                            "color": "#FF2B00",
                                                            "height": "sm",
                                                            "action": {
                                                                "type": "uri",
                                                                "label": "POST",
                                                                "uri": "{}instagram%20post%20{}".format(wait['ttt'],tksop)
                                                            }
                                                        }, {
                                                            "flex": 3,
                                                            "type": "button",
                                                            "margin": "sm",
                                                            "style": "primary",
                                                            "color": "#097500",
                                                            "height": "sm",
                                                            "action": {
                                                                "type": "uri",
                                                                "label": "STORY",
                                                                "uri": '{}instagram%20story%20{}'.format(wait['ttt'],tksop)
                                                            }
                                                            }]
                                                        }, {
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#0874DE",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "GO TO PAGE",
                                                            "uri": 'https://www.instagram.com/{}'.format(tksop)
                                                        }
                                                    }]
                                                }
                                            }
                                        }
                                    ]
                                }
        return data
def gimagesa(a,ret_):
        for i in a:
            if '.gif' in i['img']:
                links = 'line://app/1602687308-GXq4Vvk9?type=image&img='
            else:
                links = 'line://app/1602687308-GXq4Vvk9?type=image&img='
            ret_.append({
                                                "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": i['img'],
                                                    "size": "full",
                                                    "aspectRatio": "1:1",
                                                    "aspectMode": "fit",
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "button",
                                                            "style": "link",
                                                            "height": "sm",
                                                            "action": {
                                                                "type": "uri",
                                                                "label": "Send Image",
                                                                "uri": "{}{}".format(links,i['img'])
                                                            }                                                   
                                                        },
                                                    ],
                                                }})
        return ret_
def DramaEnak(drama,text,to,deff,wait):
        if drama in ['drama','fantasi','comedy','sol','romance','thriller','horror']:
            if drama == 'drama':drama = 0
            if drama == 'fantasi':drama = 1
            if drama == 'comedy':drama = 2
            if drama == 'sol':drama = 3
            if drama == 'romance':drama = 4
            if drama == 'thriller':drama = 5
            if drama == 'horror':drama = 6
            data = deff
            ss = []
            h = []
            if len(text.split(' ')) == 6:
                try:
                    if text.split(' ')[3].lower() != 'page':return
                    b = requests.get(data[drama].find_all('a')[int(text.split(' ')[2])-1].get('href'))
                    soup1 = BeautifulSoup(b.text,'html5lib')
                    data2 = soup1.find_all(id='_listUl')
                    data3 = data2[0].find_all('a')
                    b = requests.get(data3[int(text.split(' ')[5])-1].get('href'))
                    soup1 = BeautifulSoup(b.text,'html5lib')
                    print(soup1)
                    date = soup1.select('img._images')
                    for b in range(0,len(date)):
                        url = date[b]['data-url']
                        #print(url)
                        ss.append({
                                                        "type": "bubble",
                                                        "hero": {
                                                            "type": "image",
                                                            "url": url,
                                                            "size": "full",
                                                            "aspectRatio": "1:1",
                                                            "aspectMode": "fit",
                                                        }})
                    k = len(ss)//10
                    h = []
                    for aa in range(k+1):
                        h.append({
                                            "messages": [
                                                {
                                                    "type": "flex",
                                                    "altText": "Webtoon",
                                                    "contents": {
                                                        "type": "carousel",
                                                        "contents": ss[aa*10 : (aa+1)*10]
                                                    }
                                                }
                                            ]
                                        })
                    return h
                except:e = traceback.format_exc();open('w','w').write(str(e))
            if len(text.split(' ')) == 2:
                    date = data[drama].find_all('img')
                    datea = data[drama].find_all(class_='info')
                    for b in range(0,len(date)):
                        url = date[b]['src']
                        ss.append({
                                                        "type": "bubble",
                                                        "hero": {
                                                            "type": "image",
                                                            "url": url,
                                                            "size": "full",
                                                            "aspectRatio": "1:1",
                                                            "aspectMode": "fit",
                                                            "action": {
                                                                "type": "uri",
                                                                "uri": "{}webtoon%20{}%201%20page%20{}".format(wait['ttt'],text.split(' ')[1],1)
                                                                }
                                                        },
                                                        "body": {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "vertical",
                                                                    "margin": "lg",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "baseline",
                                                                            "spacing": "sm",
                                                                            "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "Title",
                                                                                    "color": "#aaaaaa",
                                                                                    "size": "sm",
                                                                                    "flex": 1
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "{}".format(datea[b].find_all('p')[0].text),
                                                                                    "color": "#262423",
                                                                                    "wrap": True,
                                                                                    "size": "sm",
                                                                                    "flex": 4
                                                                                },
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "baseline",
                                                                            "spacing": "sm",
                                                                            "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": 'Author:',
                                                                                    "color": "#aaaaaa",
                                                                                    "size": "sm",
                                                                                    "flex": 1
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": '{}'.format(datea[b].find_all('p')[1].text),
                                                                                    "color": "#262423",
                                                                                    "wrap": True,
                                                                                    "size": "sm",
                                                                                    "flex": 4
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "baseline",
                                                                            "spacing": "sm",
                                                                            "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": 'Likes:',
                                                                                    "color": "#aaaaaa",
                                                                                    "size": "sm",
                                                                                    "flex": 1
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": '{}'.format(datea[b].find_all('p')[2].find_all('em')[0].text),
                                                                                    "color": "#262423",
                                                                                    "wrap": True,
                                                                                    "size": "sm",
                                                                                    "flex": 4
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "type": "separator",
                                                                    "color": "#000000",
                                                                },
                                                                {
                                                                    "type": "box",
                                                                    "layout": "vertical",
                                                                    "margin": "lg",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": 'Click The Image For Cek Episode',
                                                                            "color": "#262423",
                                                                            "wrap": True,
                                                                            "size": "md",
                                                                            "weight": "bold",
                                                                        }
                                                                    ]
                                                                },
                                                            ]
                                                        }})
                    k = len(ss)//10
                    h = []
                    for aa in range(k+1):
                        h.append({
                                            "messages": [
                                                {
                                                    "type": "flex",
                                                    "altText": "Webtoon",
                                                    "contents": {
                                                        "type": "carousel",
                                                        "contents": ss[aa*10 : (aa+1)*10]
                                                    }
                                                }
                                            ]
                                        })
                    return h
            if len(text.split(' ')) == 5:
                    if text.split(' ')[3].lower() != 'page':return
                    b = requests.get(data[drama].find_all('a')[int(text.split(' ')[2])-1].get('href')+'&page='+str(int(text.split(' ')[4])))
                    soup1 = BeautifulSoup(b.text,'html5lib')
                    data11 = soup1.find_all(class_='subj')
                    data2 = soup1.find_all(id='_listUl')
                    data3 = data2[0].find_all('a')
                    data4 = data2[0].find_all('img')
                    if len(data4) == 10:jumlah = 10
                    else:jumlah = len(data4)
                    for c in range(0,jumlah):
                        url = data4[c]['src']
                        ss.append({
                                                    "type": "bubble",
                                                    "hero": {
                                                        "type": "image",
                                                        "url": url,
                                                        "size": "full",
                                                        "aspectRatio": "1:1",
                                                        "aspectMode": "fit",
                                                    },
                                                    "body": {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "margin": "lg",
                                                                "spacing": "sm",
                                                                "contents": [
                                                                    {
                                                                        "type": "box",
                                                                        "layout": "baseline",
                                                                        "spacing": "sm",
                                                                        "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "Title",
                                                                                "color": "#aaaaaa",
                                                                                "size": "sm",
                                                                                "flex": 1
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": "{}".format(data11[c+1].text),
                                                                                "color": "#262423",
                                                                                "wrap": True,
                                                                                "size": "sm",
                                                                                "flex": 5
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    "footer": {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "button",
                                                                "style": "link",
                                                                "action": {
                                                                    "type": "uri",
                                                                    "label": "Go Page",
                                                                    "uri": data3[c].get('href')
                                                                }                                                   
                                                            },
                                                            {
                                                                "type": "button",
                                                                "style": "link",
                                                                "action": {
                                                                    "type": "uri",
                                                                    "label": "Read Online",
                                                                    "uri": "{}webtoon%20{}%20{}%20page%20{}%201".format(wait['ttt'],text.split(' ')[1],text.split(' ')[2],c+1)
                                                                }
                                                            }
                                                        ],
                                                    }})
                    data = {
                                        "messages": [
                                            {
                                                "type": "flex",
                                                "altText": "Webtoon",
                                                "contents": {
                                                    "type": "carousel",
                                                    "contents": ss
                                                }
                                            }
                                        ]
                                    }
                    return [data]
def Anloki(msg,kamui,chatingan):
        if msg.text.lower() == 'announ clear':
            a = kamui.getChatRoomAnnouncements(msg.to)
            try:
                for b in a:
                    kamui.removeChatRoomAnnouncement(msg.to,b.announcementSeq)
                kamui.sendMessage(msg.to, 'Done')
            except Exception as e:
                ee = traceback.format_exc()
                kamui.sendMessage(msg.to, '{}'.format(e))
        else:
                adit = chatingan
                adit.text = kamui.adityasplittext(msg.text,'ss')
                adit.link= 'line://nv/chatMsg?chatId={}&messageId={}'.format(msg.to,msg.id)
                adit.displayFields = 1
                try:
                    adit.thumbnail = "http://dl.profile.line-cdn.net/"+ kamui.getGroup(msg.to).pictureStatus
                except:
                    adit.thumbnail = 'https://aditnugraha98.herokuapp.com/static/lang-logo.png'
                if msg.text.lower().startswith('announ create unlock '):kamui.createChatRoomAnnouncement(msg.to,0,adit)
                if msg.text.lower().startswith('announ create all '):
                    a = kamui.getGroupIdsJoined()
                    for i in a:
                        try:
                            aas = kamui.talk.getRecentMessagesV2(i, 1)
                            adit.link = 'line://nv/chatMsg?chatId={}&messageId={}'.format(i,aas[0].id)
                            G = kamui.getGroup(i).pictureStatus
                            adit.thumbnail = "http://dl.profile.line-cdn.net/"+ G
                            kamui.createChatRoomAnnouncement(i,0,adit)
                        except:
                            e = traceback.format_exc()
                            open('w','w').write(str(e))
                kamui.sendMessage(msg.to,' 「 Announcements 」\nStatus: Success Announcement')
def Anlokiss(to,pesan,msg,chatingan):
        if pesan == 'announ clear':
            a = client.getChatRoomAnnouncements(to)
            try:
                for b in a:
                    client.removeChatRoomAnnouncement(to,b.announcementSeq)
                client.sendMessage(msg.to, 'Done')
            except Exception as e:
                ee = traceback.format_exc()
                client.sendMessage(to, '{}'.format(e))
        else:
                adit = chatingan
                adit.text = client.adityasplittext(pesan,'ss')
                adit.link= 'line://nv/chatMsg?chatId={}&messageId={}'.format(to,msg.id)
                adit.displayFields = 1
                try:
                    adit.thumbnail = "http://dl.profile.line-cdn.net/"+ kamui.getGroup(msg.to).pictureStatus
                except:
                    adit.thumbnail = 'https://aditnugraha98.herokuapp.com/static/lang-logo.png'
                if pesan.startswith('announ create unlock '):kamui.createChatRoomAnnouncement(msg.to,0,adit)
                if pesan.startswith('announ create all '):
                    a = client.getGroupIdsJoined()
                    for i in a:
                        try:
                            aas = client.getRecentMessagesV2(i, 1)
                            adit.link = 'line://nv/chatMsg?chatId={}&messageId={}'.format(i,aas[0].id)
                            G = kamui.getGroup(i).pictureStatus
                            adit.thumbnail = "http://dl.profile.line-cdn.net/"+ G
                            client.createChatRoomAnnouncement(i,0,adit)
                        except:
                            e = traceback.format_exc()
                            open('w','w').write(str(e))
                client.sendMessage(msg.to,' 「 Announcements 」\nStatus: Success Announcement')
def profilesku(a,b,c,d,e,link,wait,to):
        data = {
                                    "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "Me",
                                            "contents": {
                                                "type": "bubble",
                                                'styles': {
                                                    "header": {
                                                        "backgroundColor": '#42f4b9'
                                                    },
                                                    "body": {
                                                        "backgroundColor": '#42f4b9'
                                                    },
                                                    "footer": {
                                                        "backgroundColor": '#42f4b9'
                                                    },
                                                },
                                                "header": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "{}".format(a),
                                                            "weight": "bold",
                                                            "color": "#262423",
                                                            "size": "sm"
                                                        }
                                                    ]
                                                },
                                                "hero": {
                                                    "type": "image",
                                                    "url": "https://obs.line-scdn.net/{}".format(b),
                                                    "size": "full",
                                                    "aspectRatio": "1:1",
                                                    "aspectMode": "fit",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://ti/p/~"+str(c)
                                                    }
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "PROFILE",
                                                            "weight": "bold",
                                                            "size": "md",
                                                            "margin": "md"
                                                        },
                                                        {
                                                            "type": "separator",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "margin": "lg",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Nama",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 1
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(a),
                                                                            "color": "#262423",
                                                                            "size": "sm",
                                                                            "wrap": True,
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Mid",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 1
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(d),
                                                                            "color": "#262423",
                                                                            "size": "sm",
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "sm",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": "Bio",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 1
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "{}".format(e),
                                                                            "color": "#262423",
                                                                            "wrap": True,
                                                                            "size": "sm",
                                                                            "flex": 5
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "button",
                                                            "style": "link",
                                                            "height": "sm",
                                                            "action": {
                                                                "type": "uri",
                                                                "label": "My Profile",
                                                                "uri": link
                                                            }                                                   
                                                        },
                                                        {
                                                          "type": "spacer",
                                                            "size": "sm",
                                                        }
                                                    ],
                                                    "flex": 0
                                                }
                                            }
                                        }
                                    ]
                                }
        return data
def webtoonk(msg,wait):
        data = {
                                    "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "Me",
                                            "contents": {
                                                "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": "https://webtoons-static.pstatic.net/image/pc/home/og_en.jpg?dt=2016110702",
                                                    "size": "full",
                                                    "aspectRatio": "1:1",
                                                    "aspectMode": "fit",
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "md",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "WEBTOON",
                                                            "weight": "bold",
                                                            "size": "md",
                                                            "margin": "md"
                                                        },
                                                        {
                                                            "type": "separator",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "margin": "md",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": " ",
                                                                    "flex": 1,
                                                                    "size": "md",
                                                                    "margin": "md"
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "| TYPE |",
                                                                    "weight": "bold",
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                    "flex": 2,
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "margin": "md",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "1.DRAMA",
                                                                    "flex": 1,
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                    "action":   {
                                                                                    "type": "uri",
                                                                                    "uri": "{}webtoon%20drama".format(wait['ttt'])
                                                                                }
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "4.FANTASI",
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                    "flex": 1,
                                                                    "action":   {
                                                                                    "type": "uri",
                                                                                    "uri": "{}webtoon%20fantasi".format(wait['ttt'])
                                                                                }
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "margin": "md",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "2.COMEDY",
                                                                    "flex": 1,
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                    "action":   {
                                                                                    "type": "uri",
                                                                                    "uri": "{}webtoon%20comedy".format(wait['ttt'])
                                                                                }
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "5.ROMANCE",
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                    "flex": 1,
                                                                    "action":   {
                                                                                    "type": "uri",
                                                                                    "uri": "{}webtoon%20romance".format(wait['ttt'])
                                                                                }
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "margin": "md",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "3.THRILLER",
                                                                    "flex": 1,
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                    "action":   {
                                                                                    "type": "uri",
                                                                                    "uri": "{}webtoon%20thriller".format(wait['ttt'])
                                                                                }
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "6.HORROR",
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                    "flex": 1,
                                                                    "action":   {
                                                                                    "type": "uri",
                                                                                    "uri": "{}webtoon%20horror".format(wait['ttt'])
                                                                                }
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "separator",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "margin": "md",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": " ",
                                                                    "flex": 1,
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "| COMMAND |",
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                    "flex": 3,
                                                                    "weight": "bold"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "separator",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "margin": "md",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "rname webtoon [type]",
                                                                    "flex": 0,
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                },
                                                            ]
                                                        },
                                                        {
                                                            "type": "separator",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "margin": "md",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "IMPORTANT CLICK TYPE FOR FAST COMMAND",
                                                                    "flex": 0,
                                                                    "size": "md",
                                                                    "margin": "md",
                                                                    "weight": "bold",
                                                                    "wrap": True,
                                                                },
                                                            ]
                                                        },
                                                    ]
                                                },
                                            }
                                        }
                                    ]
                                }
        return data
def helpers(to,wait):
    ab = wait['ttt']
    ret_ = []
    ret_.append(
        {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "Commands",
                        "weight": "bold",
                        "color": "#666666",
                        "size": "sm"
                    }
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "? khie:me",
                                        "color": "#666666",
                                        'flex': 1,
                                    },
                                    {
                                         "type": "text",
                                         "text": "? Khie:ytsearch ",
                                         "color": "#666666",
                                         'flex': 1,
                                     }
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "spacing": "sm",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": "- Mention",
                                         "color": "#666666",
                                         'flex': 1,
                                     },
                                     {
                                         "type": "text",
                                         "text": "- Group",
                                         "color": "#666666",
                                         'flex': 1,
                                     }
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "spacing": "sm",
                                     "contents": [
                                          {
                                              "type": "text",
                                              "text": "- Broadcast",
                                              "color": "#666666",
                                              'flex': 1,
                                          },
                                          {
                                              "type": "text",
                                              "text": "- Friend",
                                              "color": "#666666",
                                              'flex': 1,
                                          }
                                      ]
                                  },
                                  {
                                      "type": "box",
                                      "layout": "baseline",
                                      "spacing": "sm",
                                      "contents": [
                                          {
                                              "type": "text",
                                              "text": "- Lurk",
                                              "color": "#666666",
                                              'flex': 1,
                                          },
                                          {
                                              "type": "text",
                                              "text": "- Clone",
                                              "color": "#666666",
                                              'flex': 1,
                                          }
                                      ]
                                  },
                                  {
                                      "type": "box",
                                      "layout": "baseline",
                                      "spacing": "sm",
                                      "contents": [
                                          {
                                              "type": "text",
                                              "text": "- Timeline",
                                              "color": "#666666",
                                              'flex': 1,
                                          },
                                          {
                                              "type": "text",
                                              "text": "- Profile",
                                              "color": "#666666",
                                              'flex': 1,
                                          }
                                      ]
                                  },
                              ]
                          }
                      ]
                  },
              }
          )
    ret_.append(
          {
              "type": "bubble",
              "header": {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                      {
                          "type": "text",
                          "text": "Commands",
                          "weight": "bold",
                          "color": "#666666",
                          "size": "sm"
                      }
                  ]
              },
              "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                      {
                          "type": "box",
                          "layout": "vertical",
                          "spacing": "sm",
                          "contents": [
                              {
                                  "type": "box",
                                  "layout": "baseline",
                                  "spacing": "sm",
                                  "contents": [
                                      {
                                          "type": "text",
                                          "text": "- Steal",
                                          "color": "#666666",
                                          'flex': 1,
                                      },
                                      {
                                          "type": "text",
                                          "text": "- Autojoin",
                                          "color": "#666666",
                                          'flex': 1,
                                      }
                                  ]
                              },
                              {
                                  "type": "box",
                                  "layout": "baseline",
                                  "spacing": "sm",
                                  "contents": [
                                      {
                                          "type": "text",
                                          "text": "- Autoadd",
                                          "color": "#666666",
                                          'flex': 1,
                                      },
                                      {
                                          "type": "text",
                                          "text": "- Gcall",
                                          "color": "#666666",
                                          'flex': 1,
                                      }
                                  ]
                              },
                              {
                                  "type": "box",
                                  "layout": "baseline",
                                  "spacing": "sm",
                                  "contents": [
                                      {
                                          "type": "text",
                                          "text": "- Spam",
                                          "color": "#666666",
                                          'flex': 1,
                                      },
                                      {
                                          "type": "text",
                                          "text": "- Media",
                                          "color": "#666666",
                                          'flex': 1,
                                      }
                                  ]
                              },
                              {
                                  "type": "box",
                                  "layout": "baseline",
                                  "spacing": "sm",
                                  "contents": [
                                      {
                                          "type": "text",
                                          "text": "- Note",
                                          "color": "#666666",
                                          'flex': 1,
                                      },
                                      {
                                          "type": "text",
                                          "text": "- Settings",
                                          "color": "#666666",
                                          'flex': 1,
                                      }
                                  ]
                              },
                          ]
                      }
                  ]
              },
          }
      )
    return ret_