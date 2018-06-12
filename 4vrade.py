# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:17:35 2018

@author: d3jvd
"""
y = 1
x = 3
SIRKA = 1250
VYSKA = 703

PRUMER = 100
SKOK = 110
FONT = 42
ODSAZENI = 30
start = 0
import pyglet
from pyglet.window import key
window = pyglet.window.Window(width=SIRKA, height=VYSKA)
batch = pyglet.graphics.Batch() 

'''
Menu:
'''

menu = pyglet.image.load('menu.png')
menu.anchor_x = 0
menu.anchor_y = 0
menu.sprite = pyglet.sprite.Sprite(menu, batch=batch)
start = pyglet.image.load('start_1.png')
start.anchor_x = -300
start.anchor_y = -300
start.sprite = pyglet.sprite.Sprite(start, batch=batch)
pravidla = pyglet.image.load('pravidla_0.png')
pravidla.anchor_x = -300
pravidla.anchor_y = -150
pravidla.sprite = pyglet.sprite.Sprite(pravidla, batch=batch)
konec = pyglet.image.load('konec_0.png')
konec.anchor_x = -300
konec.anchor_y = 0
konec.sprite = pyglet.sprite.Sprite(konec, batch=batch)

def tiktak(t):
    global start
    global pravidla
    global konec
    global menu
    print (x)
    if x % 3 == 0:
        start = pyglet.image.load('start_1.png')
        if y == 2:
            menu = pyglet.image.load('hra.png')
            menu.anchor_x = 0
            menu.anchor_y = 0
            menu.sprite = pyglet.sprite.Sprite(menu, batch=batch)
        elif y == 0:
            pass
    else:
        start = pyglet.image.load('start_0.png')
    start.anchor_x = -300
    start.anchor_y = -300
    start.sprite = pyglet.sprite.Sprite(start, batch=batch)
    if x % 3 == 1:
         pravidla = pyglet.image.load('pravidla_1.png')
         if y == 2:
            menu = pyglet.image.load('pravidla.png')
            menu.anchor_x = 0
            menu.anchor_y = 0
            menu.sprite = pyglet.sprite.Sprite(menu, batch=batch)
         elif y == 0:
            pass
    else:
        pravidla = pyglet.image.load('pravidla_0.png')
    pravidla.anchor_x = -300
    pravidla.anchor_y = -150
    pravidla.sprite = pyglet.sprite.Sprite(pravidla, batch=batch)
    if x % 3 == 2:
        konec = pyglet.image.load('konec_1.png')
    else:
        konec = pyglet.image.load('konec_0.png')
    konec.anchor_x = -300
    konec.anchor_y = 0
    konec.sprite = pyglet.sprite.Sprite(konec, batch=batch)
@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    global x
    global y
    if symbol == key.DOWN:
        x = x + 1
    if symbol == key.UP:
        x = x - 1
    if symbol == key.ENTER:
        y = 2
    if symbol == key.ESCAPE:
        y = 0

pyglet.clock.schedule_interval(tiktak, 1/30)    

pyglet.app.run()
print('Hotovo!')