import pygame as pg
from renderFunctions import *
from eventHandler import Events

# setup window
pg.init()
display = pg.display
screen = display.set_mode(size=(1920, 1080))
apps = []

# setup gameloop
clock = pg.time.Clock()
running = True

def render():
    #if fullscreen:
    global dt
    dt = iconRender(screen, {"name":"terminal","path":"src/img.png"})
    for n in Events.windows:
        n.update()
    #else:
    #    renderText("Please enter Fullscreen", 1920 / 2, 1080 / 2, 64, (150, 150, 150), screen)


# gameloop
while running:
    # poll for events
    Events(pg.event.get())

    # refresh Screen
    screen.fill(pg.Color("black"))

    render() #rendering

    pg.display.flip() # draw

    clock.tick(60)  # limits FPS to 60

pg.quit()