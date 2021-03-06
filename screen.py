import pygame, sys
from pygame.locals import *
import math

pSize = 10
height = 400
width = 300

def init():
    pygame.init()

    # set up the window
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((height, width), 0, 32)
    pygame.display.set_caption('Drawing')

    # set up the colors
    global BLACK
    BLACK = (0, 0, 0)
    global WHITE
    WHITE = (255, 255, 255)
    global RED
    RED = (255, 0, 0)
    global GREEN
    GREEN = (0, 255, 0)
    global BLUE
    BLUE = (0, 0, 255)

def draw(r=0, g=0, b=0, C=[], T=30):
#    print("Red: " + str(r) + " Green: " + str(g) + " Blue: " + str(b))
    global DISPLAYSURF
    DISPLAYSURF.fill((r*255, g*255, b*255))

    length = math.floor(math.sqrt(len(C)))
    startX = math.floor((width-(length*pSize))/2)
    startY = math.floor((height-((len(C)/length)*pSize))/2)
    y=0
    while True:
        x = 0
        while x < length:
            p = C[(y*length)+x]
            px = startX + (x*pSize)
            py = startY + (y*pSize)
#            pygame.draw.rect(DISPLAYSURF, p>=T if (p*(255/T), 0, 0) else (0, p*(255/T), 0), (px, px + pSize, py + pSize))
            pygame.draw.rect(DISPLAYSURF, (((p/T)%1)*255, 0, 255) if p>=T else (0, ((p/T)%1)*255, 0), (px, py, pSize, pSize))
            x+=1
            if (y*length)+x >= len(C):
                paint()
                return
        y+=1

def test():
    global DISPLAYSURF
    # draw on the surface object
    DISPLAYSURF.fill(WHITE)
    pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
    pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
    pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
    pygame.draw.ellipse(DISPLAYSURF, RED, (300, 200, 40, 80), 1)
    pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

    pixObj = pygame.PixelArray(DISPLAYSURF)
    pixObj[380][280] = BLACK
    pixObj[382][282] = BLACK
    pixObj[384][284] = BLACK
    pixObj[386][286] = BLACK
    pixObj[388][288] = BLACK
    del pixObj

    # run the game loop
    while True:
        paint()

def paint():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

if __name__ == '__main__':
    init()
    test()