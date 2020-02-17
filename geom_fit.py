from PIL import Image
import numpy as np
from scipy.optimize import curve_fit
import pickle as pkl


xsize = 50
ysize = 50



im = Image.open('sunset edit 4.png')
im = im.resize((xsize,ysize))
im = im.convert('RGB')

arr = np.array(im)
arf = arr.flatten()

yvals = arf
xvals = np.arange(len(yvals))



def f(x,screen,left,top,width,height,R,G,B):

    x.reshape(ysize,xsize,3)

    y = [0] * int(len(x)/3)
    for i in range(int(len(x)/3)):
        y[i] = np.array([R,G,B])

    return np.array(y).flatten()




q,r = curve_fit(f,xvals,yvals)

pkl.dump((q,r),open('qr.pkl','wb'))