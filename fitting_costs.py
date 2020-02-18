import Settings
import numpy as np


def rect_cost(x,left,top,width,height,R,G,B):

    npix = int(len(x)/3)
    x_rs = x.reshape(Settings.ysize,Settings.xsize,3)
    y = [0] * npix

    for i in range(npix):
        xpos = (i % Settings.xsize)
        ypos = int(np.floor(i % Settings.ysize))

        if left <= xpos < (left+width) and top <= ypos < (top+height):
            y[i] = np.array([R,G,B])
        else:
            y[i] = np.array(Settings.screen.get_at((xpos,ypos))[:3])


    return np.array(y).flatten()


def mean_cost(x,R,G,B):

    npix = int(len(x)/3)
    y = [0] * npix

    for i in range(npix):
        y[i] = np.array([R,G,B])

    return np.array(y).flatten()
