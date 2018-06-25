from retrying import retry
import time
import requests, bs4
import datetime
import json
token = "506337865:AAELIzsWuRF2Vw7HgcsHjATQd1SvH31Hr30"
#token = "617205115:AAEQU4mIOxR336eM-8G23upstvSVUXoogpQ"
proxyt = 'socks5://swcbbabh:aYEbh6q5gQ@ley.vivalaresistance.info:3306'
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
def joke():
    j = requests.get('https://www.anekdot.ru/random/anekdot/').text 
    j = bs4.BeautifulSoup(j, 'html.parser') 
    j = j.find('div', class_="btn2")
    j = j.find('div', class_="text").next_element
    return j
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
@retry
def get_update():
    s = requests.get("https://api.telegram.org/bot" + token +"/getupdates", proxies=dict(http=proxyt, https=proxyt)).json()
    s = s['result']
    return s

date_old = int(date_initial()) 

while True:
    
    s = get_update()
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
                if m=="/btc":
                    textm = Btc()                
                elif m=="/weather":
                    textm = 'In Moscow now' + str(Weather())
                    
                elif m=="/time":
                    textm = Time()
#                elif m=="Joke":
#                    print("1")
#                    textm = joke()
                elif m=="/movie":
                    textm = first_name + ', what the fuck, dude? Go hard or Go home!'                 


                elif m=="/hello":
                    textm = "Hi, Billionaire!"                


                else:
                    textm = "Hi, " + first_name + ". \nPress the command.\nI know following commands: Btc, Time, Hello, Weather, Movie, Joke. \nBot version: 2.2"
                sendm()
                with open('last_update_id.txt', 'w') as f:
                    f.write(str(update_id))
                date_old = update_id 
            break
    time.sleep(1)
