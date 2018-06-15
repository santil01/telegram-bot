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
    with open('last_update_id.txt', 'r') as f:
        date_old = f.read()
        
    return date_old
  
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
def sendm():
    requests.get("https://api.telegram.org/bot" + token +"/sendMessage?chat_id=" + str(chat_id) + "&" + "text=" + str(textm), proxies=dict(http=proxyt, https=proxyt))
@retry
def sendme():
    requests.get("https://api.telegram.org/bot" + token +"/sendMessage?chat_id=" + str(my_chat_id) + "&" + "text=" + str(textm), proxies=dict(http=proxyt, https=proxyt))

date_old = int(date_initial()) 

while True:
    s = requests.get("https://api.telegram.org/bot" + token +"/getupdates", proxies=dict(http=proxyt, https=proxyt)).json()
    s = s['result']
    length = len(s)
    min = time.strftime("%M")
    if min=="00":
        textm = "new hour!"
        
        sendme()
        time.sleep(60)
    for i in reversed(range(length)):
        
   
        if s[i]['update_id']==date_old:

            if i!=(length-1):
                
                s = s[i+1]                
                update_id = s['update_id']
                s = s['message']
                chat_id = s['chat']['id']
                first_name = s['from']['first_name']
                m = s['text']
                
                if chat_id!=my_chat_id:
                    textm = first_name + " " + ' wrote: ' + m
                    sendme()    
                if m=="Btc":
                    textm = Btc()                
                elif m=="Weather":
                    textm = Weather()
                elif m=="Time":
                    textm = Time()
                elif m=="Movie":
                    textm = first_name + ', what the fuck, dude? Go hard or Go home!'                 


                elif m=="Hello":
                    textm = "Hi, Billionaire!"                


                else:
                    textm = "Hi, " + first_name + ". \nPress the command.\nI know following commands: Btc, Time, Hello, Weather, Movie. \nBot version: 2.0"
                sendm()
                with open('last_update_id.txt', 'w') as f:
                    f.write(str(update_id))
                date_old = update_id 
            break
    time.sleep(1)
