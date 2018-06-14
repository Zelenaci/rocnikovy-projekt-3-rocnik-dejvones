# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:17:35 2018

@author: d3jvd
"""
y = 1
SIRKA = 800
VYSKA = 600

'''
Menu:
'''
while y == 1:

    a = 0
    print ('\n---4 in row---')
    a = input ('Start hry -> [S]\nPravidla -> [P]\nKonec -> [K]\n >>> ')
    if a == 'S':
        p1 = input ('\nJméno 1. hráče >>> ')
        p2 = input ('Jméno 2. hráče >>> ')
        print ('Zapínám hru...')
    if a == 'P':
        print ('\nPravidla:\n\
 - Hra je na principu typické hry "4 v řadě".\n\
 - Velikost herního pole je 8x8 políček.\n\
 - Výhra nastává poze v případě 4 kuliček v řadě \n\
   (vodorovně nebo svisle, nikoliv úhlopříčně).\n\
 - Při zaplnění hracího pole nastává remíza\n\
Ovládání:\n\
 - Místo položení kuličky volíme levým tlačitkem myší\n\
 - Hráči hrají vždy střídavě (jméno hráče na tahu je vždy napsané)')
        a = input ('Zpět do menu -> [M]\n >>> ')
        if a == 'M':
            pass
        

print('Vypínání ...')