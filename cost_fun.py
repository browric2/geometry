import numpy

def screen_cost(sizex,sizey,thisrect,pix,screen):
    cost = 0
    for x in range(sizex):
        for y in range(sizey):
            if thisrect.collidepoint(x, y):

                px, py = x, y
                impix = pix[px, py]
                attpix = screen.get_at((px, py))
                impix = (impix[0], impix[1], impix[2])
                attpix = (attpix[0], attpix[1], attpix[2])
                diff = numpy.subtract(attpix, impix)
                cost += float(sum(abs(diff)))
    return cost


def shape_cost(xmin,xmax,ymin,ymax,screen,thisrect,pix,red,green,blue):
    cost = 0

    for px in range(xmin,xmax+1):
        for py in range(ymin,ymax+1):
            impix = pix[px, py]
            impix = (impix[0], impix[1], impix[2])

            if thisrect.collidepoint(px,py):
                spix = (red,green,blue)
            else:
                spix = screen.get_at((px, py))
                spix = (spix[0],spix[1],spix[2])

            diff = numpy.subtract(spix, impix)
            cost += float(sum(abs(diff)))

    return cost
