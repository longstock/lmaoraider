import requests
import threading
import time

# open source, if you bought this from someone you got scammed lmao
# the ghost ping function trash dont use

print('created by withstock (github.com/longstock)')

print('hi :3, wanna try this shit?')
choice = input('Y/n: ')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        # u think there are malware actually?
if choice == 'Y':
    cid = input('enter channel id: ')
    url = f'https://discord.com/api/v9/channels/{cid}/messages'
    msg = input('message to the world: ')
    file = input('enter token file name: ')
    userid = input('enter user id u want to ping (only for ghost ping): ')
    

    def spamming(token):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        json = {
            "content": msg
        }
        while True:
            response = requests.post(url, headers=headers, json=json)
            print(response.json())

    def ghost(token, userid):
        
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        json = {
            "content": f'<@{userid}> {msg}'
        }
        while True:
            response = requests.post(url, headers=headers, json=json)
            print(response.json())
            if response.status_code == 429:
                nowdata = response.json()
                time.sleep(float(nowdata['retry_after']))
            
                response = requests.post(url, headers=headers, json=json)
                
                data = response.json()
                msgid = data['id']
                killurl = f'{url}/{msgid}'
                kl = requests.delete(killurl, headers=headers)
                if kl.status_code == 429:
                    kldata = kl.json()
                    time.sleep(float(kldata['retry_after']))
                    kl = requests.delete(killurl, headers=headers)
                    
            else:
                data = response.json()
                msgid = data['id']
                killurl = f'{url}/{msgid}'
                kl = requests.delete(killurl, headers=headers)

            
            

    def shit():
        lmao = input('ghost ping or not? Y/n: ')
        if lmao == 'Y':
            with open(file, "r") as f:
                tokens = [line.strip() for line in f if line.strip()]
            
            threads = []
            for token in tokens:
                t = threading.Thread(target=ghost, args=(token, userid))
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        elif lmao == 'n':
            with open(file, "r") as f:
                tokens = [line.strip() for line in f if line.strip()]
            
            threads = []
            for token in tokens:
                t = threading.Thread(target=spamming, args=(token,))
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        else:
            print('get the fuck out rn')

            
        
            

        
    if __name__ == "__main__":
        shit()
    
    

    
    

        
    
    







































































































































else:
    print('fuck off')
    
