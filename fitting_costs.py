import Settings
import numpy as np


def rect_cost(x, left, top, width, height, R, G, B):
    npix = int(len(x) / 3)
    y = [0] * npix

    for i in range(npix):
        xpos = (i % Settings.xsize)
        ypos = int(np.floor(i / Settings.ysize))

        if left <= xpos < (left + width) and top <= ypos < (top + height):
            y[i] = np.array([R, G, B])
        else:
            y[i] = np.array(Settings.screen.get_at((xpos, ypos))[:3])
    return np.array(y).flatten()


def av_colour(y, left, top, width, height):
    npix = int(len(y) / 3)
    R, G, B = 0, 0, 0
    sum = 0
    for i in range(npix):
        xpos = (i % Settings.xsize)
        ypos = int(np.floor(i / Settings.ysize))

        if left <= xpos < (left + width) and top <= ypos < (top + height):
            a = np.array(y[i:i + 3])
            R += a[0]
            G += a[1]
            B += a[2]
            sum += 1
    R = int(np.round(R / sum))
    G = int(np.round(G / sum))
    B = int(np.round(B / sum))
    return R, G, B


def rect_cost_av_colour(x, y, left, top, width, height):
    npix = int(len(x) / 3)
    y_ = [0] * npix

    R, G, B = av_colour(y, left, top, width, height)

    for i in range(npix):
        xpos = (i % Settings.xsize)
        ypos = int(np.floor(i / Settings.ysize))

        if left <= xpos < (left + width) and top <= ypos < (top + height):
            y_[i] = np.array([R, G, B])
        else:
            y_[i] = np.array(Settings.screen.get_at((xpos, ypos))[:3])

    return np.array(y_).flatten()


def minim_cost(imar, left, top, width, height, x, R, G, B):
    npix = int(len(x) / 3)
    # x_rs = x.reshape(Settings.ysize,Settings.xsize,3)
    y = [0] * npix

    for i in range(npix):
        xpos = (i % Settings.xsize)
        ypos = int(np.floor(i / Settings.ysize))

        if left <= xpos < (left + width) and top <= ypos < (top + height):
            y[i] = np.array([R, G, B])
        else:
            y[i] = np.array(Settings.screen.get_at((xpos, ypos))[:3])
    return (np.array(y).flatten() - imar) ** 2


def moving_squares(size):
    scale = int(size * Settings.xsize)
    w = scale
    h = scale
    print(w, h, "_")
    return lambda x, l, t, R, G, B: rect_cost(x, l, t, w, h, R, G, B)


def moving_squares_av_colour(sizey):
    size, y = sizey
    scale = int(size * Settings.xsize)
    w = scale
    h = scale
    print(w, h, "_")
    return lambda x, l, t: rect_cost_av_colour(x, y, l, t, w, h)


def fixed_squares(size):
    scale = int(size * Settings.xsize)
    l = (Settings.xsize - scale) / 2
    t = (Settings.ysize - scale) / 2
    w = scale
    h = scale
    print(l, t, w, h)
    return lambda x, R, G, B: rect_cost(x, l, t, w, h, R, G, B)


def minim_fixed_squares(size, y):
    scale = int(size * Settings.xsize)
    l = (Settings.xsize - scale) / 2
    t = (Settings.ysize - scale) / 2
    w = scale
    h = scale
    print(l, t, w, h)
    return lambda *args: minim_cost(y, l, t, w, h, *args[0], *args[1], *args[2])


def mean_cost(x, R, G, B):
    npix = int(len(x) / 3)
    y = [0] * npix

    for i in range(npix):
        y[i] = np.array([R, G, B])

    return np.array(y).flatten()
