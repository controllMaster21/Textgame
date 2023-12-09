import pygame as pg
from eventHandler import Events
from render import window

def iconRender(desktop, *icons:dict):
    SPACING = 10
    SIZE = 32
    icons = list(icons)
    x = SPACING
    idx = 0
    
    for idx, item in enumerate(icons):
        img = pg.image.load(item["path"]).convert_alpha()
        imgRect = img.get_rect(topleft = (x, SPACING))
        desktop.blit(img, imgRect)
        icons[idx]["rect"] = imgRect
        x = idx * (SIZE + SPACING)

        if Events.mousePressed and imgRect.collidepoint(Events.mousePos):
            Events.windows.append(window.Window(item["name"], desktop))

    return icons