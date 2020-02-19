from PIL import Image
import numpy as np
from scipy.optimize import curve_fit
import pickle as pkl
import pygame
import Settings
from fitting_costs import rect_cost, mean_cost, fixed_squares, moving_squares


# ================================INITIALISING========================================
pygame.init()


im = Image.open('smiley.jpg')
im = im.resize((Settings.xsize,Settings.ysize))
im = im.convert('RGB')
im.show()
arr = np.array(im)
arf = arr.flatten()
yvals = arf
xvals = np.arange(len(yvals))
pygame.display.set_caption("Geometrize")
clock = pygame.time.Clock()

currentshapes = []

#pp=[Settings.xsize/4,Settings.ysize/4,Settings.xsize/2,Settings.ysize/2,100,100,100]
pp=[20,20,20,20,100,100,100]


# ================================PROGRAM LOOP========================================
done = False

nsquares = 20
scales = [1-i for i in np.linspace(0,1,nsquares)[:-1]]

s_ind = 0
while not done:

    s = scales[s_ind % nsquares-1]
    Settings.screen.fill((255,255,255))
    pygame.event.get()

    for cs in currentshapes:
        print(cs[1],cs[0])
        pygame.draw.rect(Settings.screen, cs[1], cs[0])


    # scale = int(s*Settings.xsize)
    # q,r = curve_fit(moving_squares(s),xvals,yvals,p0=[100,100,100,(Settings.xsize-scale)/2,(Settings.ysize-scale)/2],)
    # l,t = int(q[0]),round(q[1])
    # w = scale
    # h = scale
    # cRed,cGreen,cBlue = round(q[2]),round(q[3]),round(q[4])
    # currentshapes.append((pygame.Rect(l,t,w,h),(cRed,cGreen,cBlue)))


    q,r = curve_fit(fixed_squares(s),xvals,yvals,p0=[100,100,100])
    scale = int(s*Settings.xsize)
    l = (Settings.xsize-scale)/2
    t = (Settings.ysize-scale)/2
    w = scale
    h = scale
    cRed,cGreen,cBlue = round(q[0]),round(q[1]),round(q[2])
    currentshapes.append((pygame.Rect(l,t,w,h),(cRed,cGreen,cBlue)))

    # q,r = curve_fit(rect_cost,xvals,yvals,p0=pp)
    # l,t,w,h = int(q[0]),round(q[1]),round(q[2]),round(q[3])
    # cRed,cGreen,cBlue = round(q[4]),round(q[5]),round(q[6])
    # currentshapes.append((pygame.Rect(l,t,w,h),(cRed,cGreen,cBlue)))

    # q,r = curve_fit(mean_cost,xvals,yvals)
    # cRed,cGreen,cBlue = round(q[0]),round(q[1]),round(q[2])
    # currentshapes.append((pygame.Rect(0,0,Settings.xsize,Settings.ysize),(cRed,cGreen,cBlue)))

    s_ind += 1
    clock.tick(5)
    pygame.display.flip()