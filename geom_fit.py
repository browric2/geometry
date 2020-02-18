from PIL import Image
import numpy as np
from scipy.optimize import curve_fit
import pickle as pkl
import pygame

xsize = 50
ysize = 50
size = (xsize,ysize)

pygame.init()


im = Image.open('sunset edit 4.png')
im = im.resize((xsize,ysize))
im = im.convert('RGB')

arr = np.array(im)
arf = arr.flatten()

yvals = arf
xvals = np.arange(len(yvals))


screen = pygame.display.set_mode(size)#,pygame.FULLSCREEN)
pygame.display.set_caption("Geometrize")
clock = pygame.time.Clock()

currentshapes = []

def f(x,left,top,width,height,R,G,B):

    npix = int(len(x)/3)
    x_rs = x.reshape(ysize,xsize,3)
    y = [0] * npix

    for i in range(npix):
        xpos = (i % xsize)
        ypos = int(np.floor(i % ysize))

        if left <= xpos < (left+width) and top <= ypos < (top+height):
            y[i] = np.array([R,G,B])
        else:
            y[i] = np.array(screen.get_at((xpos,ypos))[:3])


    return np.array(y).flatten()

done = False

j = 1
while not done:
    print(j)
    j += 1

    screen.fill((255,255,255))

    for cs in currentshapes:
        print(cs[1])
        pygame.draw.rect(screen, cs[1], cs[0])

    q,r = curve_fit(f,xvals,yvals)

    l,t,w,h = int(q[0]),int(q[1]),int(q[2]),int(q[3])
    cRed,cGreen,cBlue = int(q[4]),int(q[5]),int(q[6])

    currentshapes.append((pygame.Rect(l,t,w,h),(cRed,cGreen,cBlue)))

    clock.tick(60)
    pygame.display.flip()



q,r = curve_fit(f,xvals,yvals)

pkl.dump((q,r),open('qr.pkl','wb'))