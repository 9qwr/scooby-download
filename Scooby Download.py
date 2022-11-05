from requests import get
import os
from time import sleep
from random import choice
import urllib3
from colorama import Fore
from alive_progress import alive_bar

Banner = f''''


░░░░░░░░░░░░░▄█▀▀░░░░░░░▀█░░░░░░
░░░░░░░░░░░▄▀░░░░░░░░░░░░░█░░░░░
░░░░░░░░░▄█░░░░░░░░░░░░░░░█░░░░░
░░░░░░░██▀░░░░░░░▄▄▄░░▄░█▄█▄░░░░
░░░░░▄▀░░░░░░░░░░████░█▄██░▀▄░░░
░░░░█▀░░░░░░░░▄▄██▀░░█████░██░░░
░░░█▀░░░░░░░░░▀█░▀█▀█▀▀▄██▄█▀░░░
░░░██░░░░░░░░░░█░░█░█░░▀▀▄█▀░░░░
░░░░█░░░░░█░░░▀█░░░░▄░░░░░▄█░░░░
░░░░▀█░░░░███▄░█░░░░░░▄▄▄▄█▀█▄░░
░░░░░▀██░░█▄▀▀██░░░░░░░░▄▄█░░▀▄░
░░░░░░▀▀█▄░▀▄▄░▄░░░░░░░███▀░░▄██
░░░░░░░░░▀▀▀███▀█▄░░░░░█▀░▀░░░▀█
░░░░░░░░░░░░▄▀░░░▀█▄░░░░░▄▄░░▄█▀
░░░▄▄▄▀▀▀▀▀█▀░░░░░█▄▀▄▄▄▄▄▄█▀▀░░
░▄█░░░▄██▀░░░░░░░░░█▄░░░░░░░░░░░
█▀▀░▄█░░░░░░░░░░░░░░▀▀█▄░░░░░░░░
█░░░█░░░░░░░░░░░░░░░░░░█▄░░░░░░░

Scooby Donwload v0.1

{Fore.LIGHTMAGENTA_EX} IG : j4s_8 & Sc : j4s_8 {Fore.RESET}
'''
print(Banner)
class KAITO():
    def __init__(self):
        self.dn=0
        self.list = 'qwertyuiopasdfghjklzxcvbnm7894521-'
        urllib3.disable_warnings()
        path_folder = 'DownloadMIX'
        try:
            os.mkdir(path_folder)
        except FileExistsError:
            print(f"{Fore.LIGHTYELLOW_EX}You Have a folder same {Fore.RED}{path_folder} ✅.{Fore.RESET}")
        os.chdir(path_folder)
        self.ask = input(Fore.LIGHTCYAN_EX+" Link :")
        self.download_all()
    
    def download_all(self):
        
        headers={'Accept': '*/*','Cookie': 'PHPSESSID=848fe4d03c2307dcb562741f02b79dde','User-Agent': 'Hero/7 (com.abdor14026.video; build:2; iOS 14.1.0) Alamofire/5.6.0','Accept-Language': 'ar-DE;q=1.0, de-DE;q=0.9','Accept-Encoding': 'gzip, deflate','Connection': 'close'}
        try:
            random = str(''.join((choice(self.list) for i in range(int(2)))))
            ABC = get(f'https://haniapp.me/wordpress/wp-json/aio-dl/api/?url={self.ask}',headers=headers,verify=False)
            kaitoo = ABC.json()
            video = kaitoo['urls'][0]['id']
            if ABC.ok:
                print("Downloading .. as {}.mp4".format(random))
                with alive_bar(100,title='Loding ..') as bar:
                    for i in range(100):
                        sleep(0.03)
                        bar()
                # download video
                print('Done :) ..')
                with open("{}.mp4".format(random), "wb") as f_out:
                    f_out.write(get(video,verify=False).content)
            else:
                print(Fore.RED+' link not working ..'+Fore.RESET)
        except KeyError:
            print(Fore.RED+' link not working ..'+Fore.RESET)
KAITO()