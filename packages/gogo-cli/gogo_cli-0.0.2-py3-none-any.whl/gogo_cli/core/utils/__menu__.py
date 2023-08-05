from .__player__ import play as pl
from .__downloader__ import download as dl

import os

def menu(url, referrer, anime, episode):
    while True:
        os.system('clear')
        print("\n1. Play\n2. Download\n3. Replay episode\n4. Play next episode\n5. Quit\n")
        e = int(input(": "))
        if e == 1:
            pl(url, referrer, anime, episode)
        elif e == 2:
            dl(anime, url, referrer, episode)
        elif e == 3:
            pl(url, referrer, anime, episode)
        elif e == 4:
            from ..__gogo_cli__ import play
            playNext = 1
            play(anime, episode, playNext)
        elif e == 5:
            exit(0)
        else:
            print("[!] Invalid option")
            exit(1)


