from colorama import Fore, Back
from os import system
import os
import requests , uuid , time 



req = requests.session()
uid = uuid.uuid4()
system("title " + "t.me/undecryptable")
os.system('cls||clear')


print(Back.BLACK + Fore.YELLOW + '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"')
print('')

user = input(Back.BLACK + Fore.WHITE + "Enter @")

os.system('cls||clear')
print(Back.BLACK + Fore.YELLOW + '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"')
print('')

sid = input(Back.BLACK + Fore.WHITE + "Session id: ")

def swapper():
    def swapping():
        while True:
            headers = {
				'Host': 'api16-normal-c-alisg.tiktokv.com',
				'Content-Length': '25',
				'Connection': 'close',
				'Cookie': f'sessionid={sid}',
				'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
				"x-tt-passport-csrf-token": sid,
				'Content-Type': 'application/x-www-form-urlencoded',
				'sdk-version': '2',
                'passport-sdk-version': '5.12.1'}
            data = {
				'login_name': user}
            url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=CZ&device_id=6926456821994505733&iid=6933716544179652353&app_name=musical_ly'                
            dt = req.post(url,headers=headers,data=data)
            if '"message":"success"' in dt.text:
                    print(Back.BLACK + Fore.GREEN + f'\nSuccesfully swapped @{user}')
                    print('\n\t By reverse @undecryptable')
                    exit()
            elif '"login_name"' in dt.text:
                    print(Back.BLACK + Fore.YELLOW + f'\nGetting @{user} swapped!')
                    print('\n\t By reverse @undecryptable')
                    exit()
            elif '"message":"error"' in dt.text:
                    print(Back.BLACK + Fore.RED + f'ERROR @{user} wasn´t swapped')
            else:
                print(Back.BLACK + Fore.BLUE + 'Something went wrong!')
    def tt():       
        count = 1
        while True:
            url1 = f'https://www.tiktok.com/@{user}?'
            hed = {
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cache-control': 'max - age = 0',
				'sec-ch-ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"',
				'sec-ch-ua-mobile': '?0',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'none',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': 'Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25'}
            st = req.get(url1,headers=hed)
            if st.status_code == 404:
                print(Back.BLACK + Fore.GREEN + f'\n@{user} is available')
                swapping()
            elif st.status_code == 200:
                print(Back.BLACK + Fore.YELLOW + '['+ Fore.WHITE + f'{count}' + Fore.YELLOW + ']' + Fore.YELLOW + 'Swapping ' + Back.BLACK + Fore.WHITE + f'@{user}...')	
            else:
                print(Back.BLACK + Fore.RED + 'IP BLOCKED!')
            count += 1
    tt()
swapper()