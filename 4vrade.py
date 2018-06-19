# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:17:35 2018
@author: d3jvd
"""
import pyglet as py
pr = '\nPravidla:\n\
 - Hra je na principu typické hry "4 v řadě".\n\
 - Velikost herního pole je 8x8 políček.\n\
 - Výhra nastává poze v případě 4 kuliček v řadě \n\
   (vodorovně, svisle nebo úhlopříčně).\n\
 - Při zaplnění hracího pole nastává remíza\n\
Ovládání:\n\
 - Místo položení kuličky volíme levým tlačitkem myší\n\
 - Hráči hrají vždy střídavě (jméno hráče na tahu je vždy napsané)'
'''
Menu:
'''
menu = 1
while menu:
    a = 0
    print ('\n---4 in row---')
    a = input ('Start hry -> [S]\nPravidla -> [P]\nKonec -> [K]\n >>> ')
    if a == 'S' or a == 's':
        p1 = input ('\nJméno 1. hráče >>> ')
        p2 = input ('Jméno 2. hráče >>> ')
        print ('Zapínám hru...')
        print ('\nNyní hraje: ',p1)
        menu = 0 
    elif a == 'P' or a == 'p':
        print (pr)
        a = input ('Zpět do menu -> [M]\n >>> ')
        if a == 'M' or a == 'm':
            pass
    elif a == 'K' or a =='k':
        quit()
    else:
        print ('Neznámý znak!')
'''
HRA:
'''
PLAYER = 1
SIRKA = 800
VYSKA = 600
POLE = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

KULE = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
 
window = py.window.Window(SIRKA,VYSKA)

@window.event
def on_draw():
    global menu
    pozadi = py.image.load('tabulka.png')
    sprite = py.sprite.Sprite(pozadi)
    sprite.draw()
    for x in range (0,8):
        for y in range (0,8):
            if POLE [x][y] == 0:
                pass
            elif POLE [x][y] == 1:
                KULE[x][y] =py.image.load('kule1.png')
                sprite = py.sprite.Sprite(KULE[x][y])
                sprite.x = x*100+15
                sprite.y = ((7-y)*74.59)+3
                sprite.draw()
            elif POLE [x][y] == 2:
                KULE[x][y] =py.image.load('kule2.png')
                sprite = py.sprite.Sprite(KULE[x][y])
                sprite.x = x*100+15
                sprite.y = ((7-y)*74.59)+3
                sprite.draw()

@window.event
def on_mouse_press(x, y, button, mod):
    global uhel
    if button == 1:
        if x in range (0,100):
            tah (0)
        elif x in range (100,200):
            tah (1)
        elif x in range (200,300):
            tah (2)
        elif x in range (300,400):
            tah (3)
        elif x in range (400,500):
            tah (4)
        elif x in range (500,600):
            tah (5)
        elif x in range (600,700):
            tah (6)
        elif x in range (700,800):
            tah (7)

def tah (grid_x):
    global p1
    global p2
    global PLAYER
    global POLE
    global KULE
    global menu
    global KONEC
    for y in range (0,8):
        try:
            if POLE [grid_x][0] != 0 and POLE [grid_x][1] != 0 and POLE [grid_x][2] != 0 and POLE [grid_x][3] != 0 and POLE [grid_x][4] != 0 and POLE [grid_x][5] != 0 and POLE [grid_x][6] != 0 and POLE [grid_x][7] != 0 :
                print ('\nKlikni jinam Nožko!')
                if PLAYER == 1:
                    PLAYER = 2
                elif PLAYER == 2:
                    PLAYER = 1
                break
            if POLE [grid_x][y+1] == 0:
                pass
            else:
                POLE [grid_x][y] = PLAYER
                break
        except:
            POLE [grid_x][7] = PLAYER
    WIN = False
    REM = 0
    for x in range (0,8):
        for y in range (0,8):
            try:
                if POLE [x][y] == 0:
                    REM += 1
                elif POLE [x][y] == POLE [x][y+1] == POLE [x][y+2] == POLE [x][y+3]:
                    WIN = True             
            except:
                pass
            try:
                if POLE [x][y] == 0:
                    REM += 1
                elif POLE [x][y] == POLE [x+1][y] == POLE [x+2][y] == POLE [x+3][y]:
                    WIN = True             
            except:
                pass
            try:
                if POLE [x][y] == 0:
                    REM += 1
                elif POLE [x][y] == POLE [x+1][y-1] == POLE [x+2][y-2] == POLE [x+3][y-3]:
                    WIN = True       
            except:
                pass
            try:
                if POLE [x][y] == 0:
                    REM += 1
                elif POLE [x][y] == POLE [x+1][y+1] == POLE [x+2][y+2] == POLE [x+3][y+3]:
                    WIN = True       
            except:
                pass
    if not WIN and REM == 0:
        print('\nRemíza, nikdo nevyhrál!')
    elif WIN == True:
        if PLAYER == 1:
            print ('\nVyhrál: ',p1)
        elif PLAYER == 2:
            print ('\nVyhrál: ',p2)
    if not WIN and REM != 0:   
        if PLAYER == 1:
            PLAYER = 2
            print ('\nNyní hraje: ',p2)
        elif PLAYER == 2:
            PLAYER = 1
            print ('\nNyní hraje: ',p1) 

py.app.run()
    