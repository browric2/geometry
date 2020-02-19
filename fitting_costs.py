import Settings
import numpy as np


def rect_cost(x,left,top,width,height,R,G,B):

    npix = int(len(x)/3)
    y = [0] * npix

    for i in range(npix):
        xpos = (i % Settings.xsize)
        ypos = int(np.floor(i / Settings.ysize))

        if left <= xpos < (left+width) and top <= ypos < (top+height):
            y[i] = np.array([R,G,B])
        else:
            y[i] = np.array(Settings.screen.get_at((xpos,ypos))[:3])

    return np.array(y).flatten()

def minim_cost(imar,left,top,width,height,x,R,G,B):


    npix = int(len(x)/3)
    #x_rs = x.reshape(Settings.ysize,Settings.xsize,3)
    y = [0] * npix

    for i in range(npix):
        xpos = (i % Settings.xsize)
        ypos = int(np.floor(i / Settings.ysize))

        if left <= xpos < (left+width) and top <= ypos < (top+height):
            y[i] = np.array([R,G,B])
        else:
            y[i] = np.array(Settings.screen.get_at((xpos,ypos))[:3])
    return (np.array(y).flatten()-imar)**2

def moving_squares(size):
    scale = int(size*Settings.xsize)
    w = scale
    h = scale
    print(w,h)
    return lambda x,l,t,R,G,B : rect_cost(x,l,t,w,h,R,G,B)


def fixed_squares(size):
    scale = int(size*Settings.xsize)
    l = (Settings.xsize-scale)/2
    t = (Settings.ysize-scale)/2
    w = scale
    h = scale
    print(l,t,w,h)
    return lambda x,R,G,B : rect_cost(x,l,t,w,h,R,G,B)


def minim_fixed_squares(size,y):
    scale = int(size*Settings.xsize)
    l = (Settings.xsize-scale)/2
    t = (Settings.ysize-scale)/2
    w = scale
    h = scale
    print(l,t,w,h)
    return lambda *args: minim_cost(y,l,t,w,h,*args[0],*args[1],*args[2])


def mean_cost(x,R,G,B):

    npix = int(len(x)/3)
    y = [0] * npix

    for i in range(npix):
        y[i] = np.array([R,G,B])

    return np.array(y).flatten()
