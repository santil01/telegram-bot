
# coding: utf-8

# In[38]:
from os import environ
from retrying import retry
import time
import requests
import datetime
import json
token = "506337865:AAELIzsWuRF2Vw7HgcsHjATQd1SvH31Hr30"

def Time():
    return time.strftime("%M")
@retry
def Btc():
    b = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=USD-BTC")
    b = b.json()
    b = b['result'][0]['Last']
    return b
pull = {"Hello":"Hello Billionaire", "Hi":"hey", "Btc":Btc()}
datep = 0
@retry
def getupdates():
    s = requests.get("https://api.telegram.org/bot" + token +"/getupdates", proxies=dict(http='socks5://telegram:telegram@hvmas.tgproxy.me:1080', https='socks5://telegram:telegram@hvmas.tgproxy.me:1080'))
    s = s.json()
    s = s['result'][-1]['message']
    date = s['date']
    chat_id = s['chat']['id']
    first_name = s['from']['first_name']
    s = s['text']
    return s, chat_id, date, first_name
@retry
def sendm():
    m = requests.get("https://api.telegram.org/bot" + token +"/sendMessage?chat_id=" + str(chat_id) + "&" + "text=" + str(textm), proxies=dict(http='socks5://telegram:telegram@hvmas.tgproxy.me:1080', https='socks5://telegram:telegram@hvmas.tgproxy.me:1080'))

while True:
    application.listen(environ["PORT"])
    s, chat_id, date, first_name = getupdates()
    min = time.strftime("%M")

    if min=="00":
        textm = "new hour!"
        sendm()
        time.sleep(60)
    if date!=datep:          
        if s=="Btc":
            textm = Btc()                
            
        elif s=="Time":
            textm = Time()                
            
        elif s=="Hello":
            textm = "Hi, Billionaire!"                
        elif s=="Text":
            textm = "sent"
            Text()
#         for i in pull: 
#             if s==i:
#                 textm = pull[i]                
#                 sendm()
        else:
             textm = "Hi, " + first_name + ". Press the command. I knew following commands: Btc, Time, Hello"
        sendm()
        datep = date
        
    
    time.sleep(1)
    

