from display import *

#d0 is pixel to the up-right
#d1 if pixel to the right

# octants 1 and 5 : 0 < m < 1
# octants 2 and 6 : 1 < m < undefined
# octants 3 and 7 : undefined < m < -1
# octants 4 and 8 : -1 < m < 0

def draw_line( x0, y0, x1, y1, screen, color ):
    slope = (y0-y1) / (x0-x1)

    #mx - y + b = 0
    #deltay x - dealtax y + deltax b = 0
    #Ax + By + C = 0
    a = y0 - y1
    b = -1 * (x0 - x1)
    c = b * ((a / b) * (0 - x0) + y0)

    #OCTANT 1 AND 5
    if (0 <= slope and slope <= 1):
        if (min(x0,x1) == x0):
            currentx = x0
            currenty = y0
            sx, sy = x1,y1
        else:
            currentx = x1
            currenty = y1
            sx, sy = x0,y0
        #midpoint times 2
        d2 = 2 * a + b
        #loop to make line
        while currentx <= sx:
            plot(screen,color,currentx,currenty)
            d0 = 2*a*(currentx+1) + 2*b*(currenty+1) + c
            if abs(d0) < abs(d2):
                currenty += 1
                d2 += (2*b)
            currentx += 1
            d2 += (2*a)

    #OCTANT 2 AND 6
    elif (1 <= slope):
        if (min(x0,x1) == x0):
            currentx = x0
            currenty = y0
            sx,sy = x1,y1
        else:
            currentx = x1
            currenty = y1
            sx,sy = x0,y0
        #midpoint times 2
        d2 = 2 * b + a
        #loop to make line
        while currenty <= sy:
            plot(screen,color,currentx,currenty)
            d0 = 2*a*(currentx+1) + 2*b*(currenty+1) + c
            if abs(d0) < abs(d2):
                currentx += 1
                d2 += (2*a)
            currenty += 1
            d2 += (2*b)

    #OCTANT 3 AND 7
    elif (slope <= -1):
        #midpoint times 2
        d2 = 2 * b - a
        #loop to make line
        while currenty >= y1:
            plot(screen,color,currentx,currenty)
            d0 = 2*a*(currentx+1) + 2*b*(currenty-1) + c
            if abs(d0) > abs(d2):
                currentx += 1
                d2 += (2*a)
            currenty -= 1
            d2 -= (2*b)
