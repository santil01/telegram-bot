import time
import requests, bs4
import datetime
import json
from retrying import retry
from my_token import *
from my_proxy import *
from my_chat_id import *
def main():
    pass
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
    return time.strftime("%a, %d %b %Y %H:%M:%S")
@retry
def Btc():
    b = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=USD-BTC")
    b = b.json()
    b = b['result'][0]['Last']
    return b
@retry
def sendm(chat_id, textm):
    requests.get("https://api.telegram.org/bot" + token +"/sendMessage?chat_id=" + str(chat_id) + "&" + "text=" + str(textm), proxies=dict(http=proxyt, https=proxyt))
@retry
def sendme(textm):
    requests.get("https://api.telegram.org/bot" + token +"/sendMessage?chat_id=" + str(my_chat_id) + "&" + "text=" + str(textm), proxies=dict(http=proxyt, https=proxyt))

@retry
def get_update():
    s = requests.get("https://api.telegram.org/bot" + token +"/getupdates", proxies=dict(http=proxyt, https=proxyt)).json()
    s = s['result']
    return s
if __name__ == "__main__":
    main()
