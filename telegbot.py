from my_functions import *
def main():
    date_old = int(date_initial()) 

    while True:

        s = get_update()
        
        length = len(s)
        min = time.strftime("%M")
        if min=="00":
            textm = "new hour!"

            sendme(textm)
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
                        sendme(textm)    
                    if m=="/btc":
                        textm = Btc()                
                    elif m=="/weather":
                        textm = 'In Moscow now' + str(Weather())

                    elif m=="/time":
                        textm = Time()

                    else:
                        textm = "Hi, " + first_name + ". \nPress the command.\nI know following commands: Btc, Time, Weather, \nBot version: 2.3"
                    sendm(chat_id, textm)
                    with open('last_update_id.txt', 'w') as f:
                        f.write(str(update_id))
                    date_old = update_id 
                break
        time.sleep(1)
if __name__ == "__main__":
    main()
