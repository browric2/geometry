from PIL import Image as Im
import time
import pygame
import random
import cost_fun

pygame.init()

sizex, sizey = 50,50
size = (sizex,sizey)

im = Im.open("sunset edit 4.png")
#im.save("smiley.png")
#im = Im.open("smiley.png")
im_r = im.resize(size)#, Im.ANTIALIAS)
pix = im_r.load()
size = im_r.size
im_r.show()

Attempt = [[(0,0,0) for x in range(size[0])] for y in range(size[1])]


screen = pygame.display.set_mode(size)#,pygame.FULLSCREEN)
pygame.display.set_caption("Geometrize")
clock = pygame.time.Clock()


nshapes = 10
iterations = 200
learningrate = 2
currentshapes = []

totalcostmain = 0

done = False
while not done:
    #0left,1top,2width,3height,4red,5green,6blue,7alpha

    shape_params = [[0,0,0,0,0,0,0,0] for x in range(nshapes)]
    costlist = [0 for x in range(nshapes)]
    shapelist = [0 for x in range(nshapes)]


    shapeno = 0
    for shape in shape_params:
        shapecost_prev = 0
        shapecost_aft = 0
        shape[0] = left = random.randint(0,size[0]-1) #left
        shape[1] = top = random.randint(0,size[1]-1) #top
        shape[2] = width = random.randint(1,(size[0]-shape[0])) #width
        shape[3] = height = random.randint(1,(size[1]-shape[1])) #height
        shape[4] = red = random.randint(0,255) #red
        shape[5] = green = random.randint(0,255) #green
        shape[6] = blue = random.randint(0,255) #blue
        shape[7] = alpha = random.randint(0,255) #alpha

        screen.fill((255,255,255))

        for cs in currentshapes:
            pygame.draw.rect(screen,cs[1],cs[0])

        thisrect = shapelist[shapeno] = pygame.Rect(left,top,width,height)
        itcost_list = [0 for x in range(iterations)]

        itercost_prev = cost_fun.screen_cost(sizex,sizey,thisrect,pix,screen)
        shapemax = [sizex-width,sizey-height,sizex-left,sizey-top,255,255,255,255]
        shapemin = [0,0,1,1,0,0,0,0]
        newrect = 0

        for it in range(iterations):

            if it != 0:
                gradlist = [0 for x in range(len(shape))]
                it_prev = cost_fun.screen_cost(sizex,sizey,newrect,pix,screen)
                itercost_aft = cost_fun.shape_cost(shapemax[0],shapemax[1],shapemax[2],shapemax[3],screen,newrect,pix,shape[4],shape[5],shape[6])
                for p in range(len(shape)):

                    if shape[p]!= shapemax[p]:
                        shape[p] += 1
                        newrect = pygame.Rect(shape[0],shape[1],shape[2],shape[3])
                        itercost_grad = cost_fun.shape_cost(shapemax[0],shapemax[1],shapemax[2],shapemax[3],screen,newrect,pix,shape[4],shape[5],shape[6])
                        shape[p] -= 1
                        gradsign = -1
                    else:
                        shape[p] -= 1
                        newrect = pygame.Rect(shape[0],shape[1],shape[2],shape[3])
                        itercost_grad = cost_fun.shape_cost(shapemax[0],shapemax[1],shapemax[2],shapemax[3],screen,newrect,pix,shape[4],shape[5],shape[6])
                        shape[p] += 1
                        gradsign = 1

                    gradlist[p] = grad = itercost_grad-itercost_aft
                    # if p == 0:
                    #     print "1 = ", shape[p]
                    #     print itercost_grad, itercost_aft
                    shape[p] += learningrate*(gradsign*grad)
                    # if p == 0:
                    #     print grad
                    #     print "2 = ", shape[p]
                    if shape[p] > shapemax[p]:
                        shape[p] = shapemax[p]
                    if shape[p] < shapemin[p]:
                        shape[p] = shapemin[p]
                    newrect = pygame.Rect(shape[0],shape[1],shape[2],shape[3])

            #print shape[0]
            #print itcost_list
            newrect = pygame.Rect(shape[0],shape[1],shape[2],shape[3])
            itercost_aft = itcost_list[it] = cost_fun.shape_cost(shapemax[0],shapemax[1],shapemax[2],shapemax[3],screen,newrect,pix,shape[4],shape[5],shape[6])
            # screen.fill((255,255,255))
            # pygame.draw.rect(screen,(shape[4],shape[5],shape[6]),newrect)
            # clock.tick(15)
            # pygame.display.flip()


            itercost = itercost_aft - itercost_prev
            #print itcost_list

        print(it,itercost_aft)
        cost =  itercost_aft - itercost_prev
        costlist[shapeno] = cost
        shapeno += 1

    bestshape = costlist.index(min(costlist))
    print(costlist[bestshape])
    if costlist[bestshape] < 0:

        #print costlist[bestshape]
        params = shape_params[bestshape]
        col = (shape_params[bestshape][4],shape_params[bestshape][5],shape_params[bestshape][6])
        currentshapes.append((shapelist[bestshape],col))


    screen.fill((255,255,255))

    for cs in currentshapes:
        pygame.draw.rect(screen,cs[1],cs[0])

    # totalcost = 0
    # for x in range(sizex):
    #         for y in range(sizey):
    #             px,py = x, y
    #             impix = pix[px,py]
    #             attpix = screen.get_at((px, py))
    #             impix = (impix[0],impix[1],impix[2])
    #             attpix = (attpix[0],attpix[1],attpix[2])
    #             diff = numpy.subtract(attpix,impix)
    #             totalcost = totalcost + sum(abs(diff))
    #
    # print totalcost

    clock.tick(60)
    pygame.display.flip()



