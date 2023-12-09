import pygame as pg
from eventHandler import Events
from render import objects

class Window():
    CLIP = 2000
    TOPBARHEIGHT = 20
    SCALESIZE = 6
    BORDERWIDTH = 2

    type = ""
    __windowPosX = 300
    __windowPosY = 300
    __windowWidth = 500
    __windowHeight= 300

    __hitboxHeight = 20
    __hitboxWidth = __windowWidth - 20

    __leftWidth = SCALESIZE
    __leftHeight = __windowHeight

    __bottomWidth = __windowWidth
    __bottomHeight = SCALESIZE

    __rightWidth = SCALESIZE
    __rightHeight = __windowHeight

    def __init__(this, type, desktop):

        this.APP = {"terminal":Terminal()}

        this.app = this.APP[type]

        this.type = type
        this.topBar = pg.Rect(this.__windowPosX - (this.__hitboxWidth - this.__windowWidth) / 2, this.__windowPosY - (this.__hitboxHeight - this.TOPBARHEIGHT) / 2, this.__hitboxWidth, this.__hitboxHeight)
        this.left = pg.Rect(this.__windowPosX - this.__leftWidth / 2, this.__windowPosY, this.__leftWidth, this.__leftHeight)
        this.bottom = pg.Rect(this.__windowPosX, this.__windowPosY + this.__windowHeight - this.__bottomHeight / 2, this.__bottomWidth, this.__bottomHeight)
        this.right = pg.Rect(this.__windowPosX + this.__windowWidth - this.__rightWidth / 2, this.__windowPosY, this.__rightWidth, this.__rightHeight)
        this.desktop = desktop

    def update(this):
        mousePos = pg.mouse.get_pos()
        mouseMov = Events.mouseRel

        mousePressed = Events.mousePressed

        relMouseX = max(0, mousePos[0] - this.__windowPosX)
        relMouseY = max(0, mousePos[1] - this.__windowPosY - this.TOPBARHEIGHT)
        relMousePos = (min(relMouseX, this.__windowWidth), min(relMouseY, this.__windowHeight))

        if mousePressed and this.topBar.collidepoint(mousePos):
            this.__hitboxHeight = this.CLIP
            this.__hitboxWidth = this.CLIP

            this.__windowPosX += mouseMov[0]
            this.__windowPosY += mouseMov[1]
        else:
            this.__hitboxWidth = this.__windowWidth - 20
            this.__hitboxHeight = this.TOPBARHEIGHT
            
        if mousePressed and this.left.collidepoint(mousePos):
            this.__leftWidth = this.CLIP
            this.__leftHeight = this.CLIP

            this.__windowWidth -= mouseMov[0]
            this.__windowPosX += mouseMov[0]
        else:
            this.__leftWidth = this.SCALESIZE
            this.__leftHeight = this.__windowHeight
            
        if mousePressed and this.right.collidepoint(mousePos):
            this.__rightWidth = this.CLIP
            this.__rightHeight = this.CLIP

            this.__windowWidth += mouseMov[0]
        else:
            this.__rightWidth = this.SCALESIZE
            this.__rightHeight = this.__windowHeight
            
        if mousePressed and this.bottom.collidepoint(mousePos):
            this.__bottomWidth = this.CLIP
            this.__bottomHeight = this.CLIP

            this.__windowHeight += mouseMov[1]
        else:
            this.__bottomWidth = this.__windowWidth
            this.__bottomHeight = this.SCALESIZE

        this.topBar = pg.Rect(this.__windowPosX - (this.__hitboxWidth - this.__windowWidth) / 2, this.__windowPosY - (this.__hitboxHeight - this.TOPBARHEIGHT) / 2, this.__hitboxWidth, this.__hitboxHeight)
        this.left = pg.Rect(this.__windowPosX - this.__leftWidth / 2, this.__windowPosY + this.TOPBARHEIGHT, this.__leftWidth, this.__leftHeight)
        this.bottom = pg.Rect(this.__windowPosX, this.__windowPosY + this.__windowHeight + this.TOPBARHEIGHT - this.__bottomHeight / 2, this.__bottomWidth, this.__bottomHeight)
        this.right = pg.Rect(this.__windowPosX + this.__windowWidth - this.__rightWidth / 2, this.__windowPosY + this.TOPBARHEIGHT, this.__rightWidth, this.__rightHeight)
    
        this.border = pg.draw.rect(this.desktop, (200, 200, 200), (this.__windowPosX, this.__windowPosY, this.__windowWidth + this.BORDERWIDTH * 2, this.__windowHeight + this.TOPBARHEIGHT))
        this.panel = pg.draw.rect(this.desktop, (0, 0, 0), (this.__windowPosX + this.BORDERWIDTH, this.__windowPosY + this.TOPBARHEIGHT - this.BORDERWIDTH, this.__windowWidth, this.__windowHeight))
        this.drawPanel = this.desktop.subsurface(this.panel)

        focus =  this.panel.collidepoint(mousePos)

        this.app.update(this.drawPanel, relMousePos, focus)


class Terminal():
    window = None
    mousePos = ()

    def __init__(this):
        this.commandInput = objects.Input()
    
    def update(this, window, mousePos, focus):
        this.commandInput.update(window, 10, 10, 200, 30, (150, 150, 150), (0, 0, 0), mousePos, focus)