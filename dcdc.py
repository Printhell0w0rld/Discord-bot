import urllib.request
import json


def get_id(dataLink,name):
    tank_dict = []
    with urllib.request.urlopen(dataLink) as url:
        tank_dict = json.loads(url.read().decode())
    if tank_dict['data']!=0:
        for tank in tank_dict['data']:
            if tank["nickname"]==name:
                return(tank["account_id"])
        return -1
    elif tank_dict['data']==0:
        return -1

def fetch_data(dataLink):
    tank_dict = []
    with urllib.request.urlopen(dataLink) as url:
        tank_dict = json.loads(url.read().decode())
    
    #print(user_dict)
    return(str(tank_dict['overallStats']['overallWN8']))
    
def fetch_data30(dataLink):
    tank_dict = []
    with urllib.request.urlopen(dataLink) as url:
        tank_dict = json.loads(url.read().decode())
    
    #print(user_dict)
    return(str(tank_dict["recents"]["recent30days"]["overallWN8"]))

def fetch_data24(dataLink):
    tank_dict = []
    with urllib.request.urlopen(dataLink) as url:
        tank_dict = json.loads(url.read().decode())
    
    #print(user_dict)
    return(str(tank_dict["recents"]["recent24hr"]["overallWN8"]))

def winrate30d(dataLink):
    tank_dict = []
    with urllib.request.urlopen(dataLink) as url:
        tank_dict = json.loads(url.read().decode())
    
    #print(user_dict)
    return(str(tank_dict["recents"]["recent30days"]["winrate"]))

def winrate24hr(dataLink):
    tank_dict = []
    with urllib.request.urlopen(dataLink) as url:
        tank_dict = json.loads(url.read().decode())
    
    #print(user_dict)
    return(str(tank_dict["recents"]["recent24hr"]["winrate"]))


#導入 Discord.py
import discord
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

import asyncio
#for sleep

import webbrowser

#調用 event 函式庫



@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

#def a():
#    print(132)
#a()

"""
@client.event
#改名
async def on_member_update(before, after): 
    n = after.nick 
    if n: # Check if they updated their username
        if n.count("kris") > 0: # If username contains tim
            last = before.nick
            if last: # If they had a username before change it back to that
                await after.edit(nick=last)
            else: # Otherwise set it to "NO STOP THAT"
                await after.edit(nick="NO STOP THAT")
"""



@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return

    if message.content[0] == '!' and message.content[1] == 'w' and message.content[2] == 'n' and message.content[3] == '8': 
        arr=message.content
        arr=arr.split('-')
        if arr[1]=='30d':
            string1=arr[2]
            userid=get_id("https://api.worldoftanks.com/wot/account/list/?language=en&application_id=4a07de52c30503b07af4bc6714dd7a7b&search="+string1,string1)
            if userid!=-1:
                wn8=str(fetch_data30("https://tomatobackend.herokuapp.com/api/player/com/"+str(userid)+"?cache=false"))
                await message.channel.send(string1+"'s "+'Recent 30 day Wn8= '+wn8)
            else:
                await message.channel.send("User not found")
        elif arr[1]=='24hr':
            string1=arr[2]
            userid=get_id("https://api.worldoftanks.com/wot/account/list/?language=en&application_id=4a07de52c30503b07af4bc6714dd7a7b&search="+string1,string1)
            if userid!=-1:
                wn8=str(fetch_data24("https://tomatobackend.herokuapp.com/api/player/com/"+str(userid)+"?cache=false"))
                await message.channel.send(string1+"'s "+'Recent 24hr Wn8= '+wn8)
            else:
                await message.channel.send("User not found")
        else:
            string1=arr[1]
            userid=get_id("https://api.worldoftanks.com/wot/account/list/?language=en&application_id=4a07de52c30503b07af4bc6714dd7a7b&search="+string1,string1)
            if userid!=-1:
                wn8=str(fetch_data("https://tomatobackend.herokuapp.com/api/player/com/"+str(userid)+"?cache=false"))
                await message.channel.send(string1+"'s "+'Wn8= '+wn8)
            else:
                await message.channel.send("User not found")

    if message.content[0] == '!' and message.content[1] == 'w' and message.content[2] == 'i' and message.content[3] == 'n' and message.content[4] == 'r': 
        arr=message.content
        arr=arr.split('-')
        if arr[1]=='30d':
            string1=arr[2]
            userid=get_id("https://api.worldoftanks.com/wot/account/list/?language=en&application_id=4a07de52c30503b07af4bc6714dd7a7b&search="+string1,string1)
            if userid!=-1:
                winrate=str(winrate30d("https://tomatobackend.herokuapp.com/api/player/com/"+str(userid)+"?cache=false"))
                await message.channel.send(string1+"'s "+'Recent 30 day winrate= '+winrate+"%")
            else:
                await message.channel.send("User not found")
        elif arr[1]=='24hr':
            string1=arr[2]
            userid=get_id("https://api.worldoftanks.com/wot/account/list/?language=en&application_id=4a07de52c30503b07af4bc6714dd7a7b&search="+string1,string1)
            if userid!=-1:
                winrate=str(winrate24hr("https://tomatobackend.herokuapp.com/api/player/com/"+str(userid)+"?cache=false"))
                await message.channel.send(string1+"'s "+'Recent 24hr winrate= '+winrate+"%")
            else:
                await message.channel.send("User not found")




    if message.content == 'クレア' or message.content == 'くれあ': 
        mes = await message.channel.send('クソガキ')
        mess = await message.channel.send('くさい')
        #await asyncio.sleep(5)
        #await mes.delete()
        #await mess.delete()

    if message.content == '我好帥':
        await message.delete()
        mess = await message.channel.send('不好意思，不要騙人啦')
        await asyncio.sleep(5)
        await mess.delete()

    if message.content == 'jason' or message.content == 'Jason':
        mess = await message.channel.send('傻逼')
        

    if message.content == 'Thomas' or message.content == 'thomas': 
        mess = await message.channel.send('好帥,一定有女友')
        await asyncio.sleep(5)
        await mess.delete()

    if message.content == '笑死':
        mess = await message.channel.send('笑死根本笑不死,去死Jasimpon')
        await asyncio.sleep(5)
        await mess.delete()
    if message.content == '好喔':
        mess = await message.channel.send('渣杰閉嘴')
        await asyncio.sleep(5)
        await mess.delete()
    #if message.content.startswith('!gogo'):
        #webbrowser.open('www.google.com')

    #if message.author.id == 584846501013094421:
        #kris's id
        #mess = await message.channel.send('喔 很酷喔喔喔')
        

    if message.author.id == 596618117422120961:
        #await message.delete()
        mess = await message.channel.send('@烤羊')
        
        #Jason's ID
        #836738582021406731

    if message.content == 'sstop!': 
        await message.delete()
        await client.close()



client.run('') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面







    