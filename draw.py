from display import *

#d0 is pixel to the up-right
#d1 if pixel to the right

def draw_line( x0, y0, x1, y1, screen, color ):
    currentx = x0
    currenty = y0
    slope = (y1-y0) / (x1-x0)

    #Ax + By + C = 0
    a = y1 - y0
    b = -1 * (x1 - x0)
    c = b * ((a / b) * (0 - x0) + y0)

    d2 = 2 * a + b

    while currentx <= x1:
        plot(screen,color,currentx,currenty)
        d0 = 2*a*(currentx+1) + 2*b*(currenty+1) + c
        if abs(d0) < abs(d2): #possible error
            currenty += 1
            d2 += (2*b)
        currentx += 1
        d2 += (2*a)


def formula(slope,x0,y0,x):
    return slope * (x - x0) + y0
