from PIL import Image
import numpy as np
from scipy.optimize import curve_fit
import pickle as pkl
import pygame
import Settings
from fitting_costs import rect_cost, mean_cost


# ================================INITIALISING========================================
pygame.init()


im = Image.open('sunset edit 4.png')
im = im.resize((Settings.xsize,Settings.ysize))
im = im.convert('RGB')
arr = np.array(im)
arf = arr.flatten()
yvals = arf
xvals = np.arange(len(yvals))
pygame.display.set_caption("Geometrize")
clock = pygame.time.Clock()

currentshapes = []


# ================================PROGRAM LOOP========================================
done = False

while not done:

    Settings.screen.fill((255,255,255))

    for cs in currentshapes:
        print(cs[1])
        pygame.draw.rect(Settings.screen, cs[1], cs[0])

    q,r = curve_fit(mean_cost,xvals,yvals)

    # l,t,w,h = int(q[0]),round(q[1]),round(q[2]),round(q[3])
    # cRed,cGreen,cBlue = round(q[4]),round(q[5]),round(q[6])
    #
    # currentshapes.append((pygame.Rect(l,t,w,h),(cRed,cGreen,cBlue)))

    cRed,cGreen,cBlue = round(q[0]),round(q[1]),round(q[2])

    currentshapes.append((pygame.Rect(0,0,Settings.xsize,Settings.ysize),(cRed,cGreen,cBlue)))

    clock.tick(60)
    pygame.display.flip()