
# coding: utf-8

# In[38]:

from retrying import retry
import time
import requests, bs4
import datetime
import json
token = "506337865:AAELIzsWuRF2Vw7HgcsHjATQd1SvH31Hr30"
proxyt = 'socks5://swcbbabh:aYEbh6q5gQ@c3po.vivalaresistance.info:3306'
my_chat_id = 210787766
@retry
def date_initial():
    date_old = requests.get("https://api.telegram.org/bot" + token +"/getupdates", proxies=dict(http=proxyt, https=proxyt)).json()
    date_old = date_old['result'][-1]['message']['date']
    return date_old
date_old = date_initial()   
@retry
def Weather():
    w = requests.get('https://yandex.ru/pogoda/moscow').text 
    w = bs4.BeautifulSoup(w, 'html.parser') 
    w = w.find('span', class_="temp__value").next_element
    return w
@retry
def Time():
    return time.strftime("%M")
@retry
def Btc():
    b = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=USD-BTC")
    b = b.json()
    b = b['result'][0]['Last']
    return b


@retry
def getupdates():
    s = requests.get("https://api.telegram.org/bot" + token +"/getupdates", proxies=dict(http=proxyt, https=proxyt)).json()
    s = s['result'][-1]['message']
    date = s['date']
    chat_id = s['chat']['id']
    first_name = s['from']['first_name']
    s = s['text']
    return s, chat_id, date, first_name
@retry
def sendm():
    requests.get("https://api.telegram.org/bot" + token +"/sendMessage?chat_id=" + str(chat_id) + "&" + "text=" + str(textm), proxies=dict(http=proxyt, https=proxyt))
@retry
def sendme():
    requests.get("https://api.telegram.org/bot" + token +"/sendMessage?chat_id=" + str(my_chat_id) + "&" + "text=" + str(textm), proxies=dict(http=proxyt, https=proxyt))


while True:
    
    s, chat_id, date, first_name = getupdates()
    min = time.strftime("%M")

    if min=="00":
        textm = "new hour!"
        
        sendme()
        time.sleep(60)
    if date!=date_old:
        if chat_id!=my_chat_id:
            textm = first_name + " " + ' wrote: ' + s
            sendme()    
        if s=="Btc":
            textm = Btc()                
        elif s=="Weather":
            textm = Weather()
        elif s=="Time":
            textm = Time()
        elif s=="Movie":
            textm = first_name + ', what the fuck, dude? Go hard or Go home!'                 
            

        elif s=="Hello":
            textm = "Hi, Billionaire!"                
        

        else:
            textm = "Hi, " + first_name + ". \nPress the command.\nI know following commands: Btc, Time, Hello, Weather, Movie. \nBot version: 1.9"
        sendm()
        date_old = date
        
    
    time.sleep(1)
