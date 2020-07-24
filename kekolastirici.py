#!/bin/python3

#########################################################
# a script by https://discord.gg/b3c5qar @ Homo Erectus #
#########################################################

import os,time,sys,random

class intro:
    welcome = "Keko yazı stili erken erişim sürümüne hoşgeldiniz."
    eula = "Eula -SON KULLANICI SÖZLEŞMESİ- Programın herhangi bir kekoya herhangi bir kötü etkisi bulunması durumunda yazılım ve dağıtıcı herhangi bir sorumluluk kabul etmemektedir.\n\n-\nKabul etmek için \"return\" \n-\nÇıkmak için \"Ctrl + C\"\n\n "
def check():
    if not(os.path.isfile('eulaconfirm')):
        input(intro.welcome)
        input(intro.eula)
        eulafile = open("eulaconfirm", "w")
check()
while True:
    def randomupperfactor(c):
        if random.random() > 0.5:
            return c.upper()
        else:
            return c.lower()
    
    StringToRandomize = str(input("Keko Font İnput > " ))
    StringToRandomize =''.join(map(randomupperfactor, StringToRandomize))
    print("Keko Font Output : " + StringToRandomize + "\n")