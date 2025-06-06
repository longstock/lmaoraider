import requests
import threading
import time

# open source, if you bought this from someone you got scammed lmao

print('created by withstock (github.com/longstock)')

print('hi :3, wanna try this shit?')
choice = input('Y/n: ')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        # u think there are malware actually?
if choice == 'Y':
    cid = input('enter channel id: ')
    url = f'https://discord.com/api/v9/channels/{cid}/messages'
    msg = input('message to the world: ')
    file = input('enter token file name: ')
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

    def shit():
        with open(file, "r") as f:
            tokens = [line.strip() for line in f if line.strip()]
        threads = []
        for token in tokens:
            t = threading.Thread(target=spamming, args=(token,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    if __name__ == "__main__":
        shit()
    
    

    
    

        
    
    







































































































































else:
    print('fuck off')
    
