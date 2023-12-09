import pygame as pg
from eventHandler import Events

class Input():

    active:bool = False
    text:str = ""

    def __init__(this):
        this.text = ""
        this.lastKey = 0
    
    def checkActive(this, focus, mousePos, shape) -> bool:
        if focus and Events.mousePressed and shape.collidepoint(mousePos):
            this.active = True
        if focus and Events.keyPressed == pg.K_RETURN:
            this.active = False
        return this.active
    
    def update(this, surface:pg.Surface, x:int, y:int, width:int, height:int, color:tuple[int], aColor:tuple[int], mousePos:tuple[int], focus:bool):
        hitBox = pg.Rect(x, y, width, height)
        active = this.checkActive(focus, mousePos, hitBox)

        if active:
            color = aColor

            if this.lastKey == Events.keyReleased:
                this.lastKey = 0

            if this.lastKey != Events.keyPressed:
                if Events.keyPressed == pg.K_BACKSPACE:
                    this.text = this.text[:-1]

                elif Events.keyPressed == pg.K_RETURN:
                    pass

                else:
                    this.text += pg.key.name(Events.keyPressed)
                    this.lastKey = Events.keyPressed
        else:
            color = color
            if this.text != "":
                print(this.text)
            this.text = ""

        shape = pg.draw.rect(surface, color, (x, y, width, height))
        textDisplay = surface.subsurface(shape)
        Text(this.text, x, y, height - 5, (0, 255, 0), textDisplay, "left")

    def getValue(this):
        if text := this.text != "":
            this.text = ""
            return text
        else:
            return None


class Text():
    def __init__(this, text:str, posX:int, posY:int, size:int, color:tuple, surface:pg.Surface, alignment:str):
        f = pg.font.Font(None, size).render(text, True, color)
        if alignment == "left":
            textpos = f.get_rect(x=posX, y=posY)
        elif alignment == "center":
            textpos = f.get_rect(centerx=posX, y=posY)
        elif alignment == "right":
            textpos = f.get_rect(x=posX * size * len(text), y=posY)
        surface.blit(f, textpos)