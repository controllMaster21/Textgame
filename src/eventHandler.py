from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, KEYDOWN, KEYUP
import pygame as pg

class Events:

    mousePos = (0, 0)
    mouseRel = (0, 0)
    mousePressed = False

    keyPressed = 0
    keyReleased = 0

    windows = []

    def __init__(this, events):
        for e in events:
            if e.type == QUIT:
                exit()

            if e.type == MOUSEBUTTONDOWN:
                Events.mousePressed = True

            if e.type == MOUSEBUTTONUP:
                Events.mousePressed = False

            if e.type == KEYDOWN:
                Events.keyPressed = e.key
            
            if e.type == KEYUP:
                Events.keyReleased = e.key
                if Events.keyPressed == Events.keyReleased:
                    Events.keyPressed = 0
            
        Events.mousePos = pg.mouse.get_pos()
        Events.mouseRel = pg.mouse.get_rel()
            