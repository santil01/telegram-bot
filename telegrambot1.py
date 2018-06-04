import time
import requests
import datetime
D = True 
pull = {"Hello":"Hello Billionaire", "Hi":"hey","Time":time.strftime("%M")}
datep = 0
def getupdates():
    s = requests.get("https://api.telegram.org/bot506337865:AAELIzsWuRF2Vw7HgcsHjATQd1SvH31Hr30/getupdates", proxies=dict(http='socks5://telegram:telegram@hvmas.tgproxy.me:1080', https='socks5://telegram:telegram@hvmas.tgproxy.me:1080'))
    s = s.json()
    date = s['result'][len(s['result'])-1]['message']['date']
    chat_id = s['result'][len(s['result'])-1]['message']['chat']['id']
    first_name = s['result'][len(s['result'])-1]['message']['from']['first_name']
    s = s['result'][len(s['result'])-1]['message']['text']
    return s, chat_id, date, first_name
def sendm():
    m = requests.get("https://api.telegram.org/bot506337865:AAELIzsWuRF2Vw7HgcsHjATQd1SvH31Hr30/sendMessage?chat_id=" + str(chat_id) + "&" + "text=" + str(textm), proxies=dict(http='socks5://telegram:telegram@hvmas.tgproxy.me:1080', https='socks5://telegram:telegram@hvmas.tgproxy.me:1080'))
    
while D:
    
    s, chat_id, date, first_name = getupdates()
    min = time.strftime("%M")
    if min=="00":
        textm = "new hour!"
        sendm()
        time.sleep(60)
    if date!=datep:     

        if s=="Btc":
            b = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=USD-BTC")
            b = b.json()
            b = b['result'][0]['Last']
            textm = b
            sendm()
        for i in pull: 
            if s==i:
                textm = pull[i]
                sendm()
        datep = date
        
    
    time.sleep(1)
    
